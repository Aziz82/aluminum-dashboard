#!/usr/bin/env bash
# Cloud runner for the aluminium dashboard (no PC needed).
# Token: write the GitHub PAT to "$WORK/token" first (read it from Google Drive deploy.token).
# Usage: bash cloud_run.sh {setup|status|lock|build|publish|release}
set -uo pipefail
WORK=${WORK:-/tmp/alu}; ENG="$WORK/engine"; SITE="$WORK/site"
REPO="github.com/Aziz82/aluminum-dashboard.git"
TOKEN=$(grep -oE 'github_pat_[A-Za-z0-9_]+' "$WORK/token" | head -1)
[ -n "$TOKEN" ] || { echo "NO TOKEN in $WORK/token"; exit 2; }
AUTH="https://x-access-token:${TOKEN}@${REPO}"
TODAY=$(date -u +%F)
m(){ sed "s/${TOKEN}/[TOKEN]/g"; }
g(){ git -c user.email=a@m.local -c user.name=Bot "$@" 2>&1 | m; return ${PIPESTATUS[0]}; }
case "${1:-}" in
 setup)
  rm -rf "$ENG" "$SITE"
  g clone --depth 30 --branch engine "$AUTH" "$ENG" || exit 1
  g clone --depth 3 --branch main "$AUTH" "$SITE" || exit 1
  echo "engine HEAD: $(git -C "$ENG" log --oneline -1)"; echo "site HEAD: $(git -C "$SITE" log --oneline -1)";;
 status)
  echo "TODAY(UTC)=$TODAY"
  python3 -c "import json;print('live as_of =',json.load(open('$SITE/data.json'))['meta']['as_of'])"
  echo "lock: $(cat "$ENG/.run_lock.json")";;
 lock)
  python3 - "$ENG/.run_lock.json" "$TODAY" <<'PY' || exit 3
import json,sys,datetime
p,t=sys.argv[1],sys.argv[2]
try: L=json.load(open(p))
except Exception: L={}
if L.get('date')==t and L.get('state')=='running':
    s=datetime.datetime.fromisoformat(L['started'])
    age=(datetime.datetime.now(datetime.timezone.utc)-s).total_seconds()/60
    if age<45: print(f'LOCK HELD by another run ({age:.0f} min old)'); sys.exit(1)
json.dump({'date':t,'state':'running','started':datetime.datetime.now(datetime.timezone.utc).isoformat(),'by':'cloud'},open(p,'w'))
PY
  git -C "$ENG" add .run_lock.json; g -C "$ENG" commit -qm "lock $TODAY" >/dev/null
  if g -C "$ENG" push origin engine; then echo "LOCK ACQUIRED"; else echo "LOCK PUSH REJECTED - another run is active"; exit 3; fi;;
 build)
  python3 "$ENG/build_data_json.py" "$ENG" "$SITE" || exit 1
  cp "$SITE/data.json" "$ENG/data.json"
  [ -d "$SITE/assets" ] && { echo "ASSETS DIR PRESENT - STOP"; exit 1; }
  EXPECT_DATE=$TODAY python3 "$ENG/validate_dashboard.py" "$ENG" "$SITE"; rc=$?; echo "VALIDATOR_EXIT=$rc"; exit $rc;;
 publish)
  EXPECT_DATE=$TODAY python3 "$ENG/validate_dashboard.py" "$ENG" "$SITE" >/dev/null || { echo "VALIDATION FAILED - NOT PUBLISHING"; exit 1; }
  CH=$(git -C "$SITE" status --porcelain)
  [ "$CH" = " M data.json" ] || { echo "UNEXPECTED SITE CHANGES: $CH"; exit 1; }
  git -C "$SITE" add data.json; g -C "$SITE" commit -qm "data refresh $TODAY"; g -C "$SITE" push origin main || exit 1
  echo "SITE PUSHED: $(git -C "$SITE" log --oneline -1)"
  python3 -c "import json,datetime;json.dump({'date':'$TODAY','state':'done','finished':datetime.datetime.now(datetime.timezone.utc).isoformat(),'by':'cloud'},open('$ENG/.run_lock.json','w'))"
  git -C "$ENG" add -A; g -C "$ENG" commit -qm "engine refresh $TODAY"; g -C "$ENG" push origin engine || exit 1
  echo "ENGINE PUSHED: $(git -C "$ENG" log --oneline -1)";;
 release)
  python3 -c "import json,datetime;json.dump({'date':'$TODAY','state':'done','finished':datetime.datetime.now(datetime.timezone.utc).isoformat(),'by':'cloud-abort'},open('$ENG/.run_lock.json','w'))"
  git -C "$ENG" add .run_lock.json; g -C "$ENG" commit -qm "release lock $TODAY" >/dev/null; g -C "$ENG" push origin engine;;
 *) echo "usage: setup|status|lock|build|publish|release"; exit 2;;
esac
