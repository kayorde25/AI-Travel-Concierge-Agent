# Submission Checklist

## Before GitHub Upload

- [ ] Delete `app/.env` if it exists.
- [ ] Delete `.venv/` if it exists.
- [ ] Delete `frontend/node_modules/` if it exists.
- [ ] Delete `app/.adk/` if it exists.
- [ ] Confirm `.env.example` remains.
- [ ] Confirm `.gitignore` excludes `.env`, `.venv`, `node_modules`, `.adk`, and private keys.
- [ ] Rotate/regenerate any API key that was previously saved inside `app/.env`.

## Local Test

```bash
uv sync
uv run pytest tests/unit
agents-cli playground
```

## GitHub

```bash
git init
git add .
git commit -m "feat: add TripSmooth AI Travel Concierge Agent"
git branch -M main
git remote add origin https://github.com/<your-username>/tripsmooth-ai-travel-concierge.git
git push -u origin main
```

## Demo Video

Record 2–5 minutes showing:

1. Project problem
2. Agent architecture
3. Flight search
4. Flight booking
5. Hotel search
6. Car rental or eVisa flow
7. Safety note: mock tools, no real payment/passport processing
8. GitHub repo and tests

## Kaggle Submission

- [ ] Project title: TripSmooth AI Travel Concierge Agent
- [ ] Track: Concierge Agents or Agents for Business
- [ ] GitHub link
- [ ] Demo video link
- [ ] Optional live app/playground link
- [ ] Writeup pasted from `KAGGLE_WRITEUP_DRAFT.md`
- [ ] Screenshot/logo uploaded
