# Aluminium dashboard engine (branch `engine`)
Data engine for https://aziz82.github.io/aluminum-dashboard/ . GitHub Pages serves `main` only; this branch is never served.
Daily cloud run: clone -> research -> edit market_data.json / price_history.json -> `cloud_run.sh build` (build + validate) -> `cloud_run.sh publish` (pushes data.json to main, engine state here).
Everything here is public-source market data only. Migrated from the Google Drive folder on 2026-10-06.
