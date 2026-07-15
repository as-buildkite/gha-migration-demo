# gha-migration-demo

A small, realistic sample app used to demo the **Buildkite GitHub Actions migration converter**.

It intentionally has a full-featured GitHub Actions workflow so the converter
(`bk pipeline convert`) has real work to do — matrix builds, caching, `needs:`
dependencies, secrets, and artifact uploads.

## What's in here

| Part | Tech | Location |
| --- | --- | --- |
| Backend API | Python 3.11+ / FastAPI | [`app/`](app/) |
| API tests | pytest | [`tests/`](tests/) |
| Frontend utils | TypeScript | [`frontend/src/`](frontend/src/) |
| Frontend tests | jest | [`frontend/src/*.test.ts`](frontend/src/) |
| Container | Docker | [`Dockerfile`](Dockerfile) |
| CI | GitHub Actions | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) |

## Local development

### Python

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
ruff check .
pytest
uvicorn app.main:app --reload   # http://localhost:8000/health
```

### Node / TypeScript

```bash
npm install
npm run lint
npm test
```

### Docker

```bash
docker build -t gha-migration-demo .
docker run -p 8000:8000 gha-migration-demo
```

## Migrating CI to Buildkite

This repo deliberately does **not** contain a `.buildkite/` directory. To generate
a Buildkite pipeline from the existing GitHub Actions workflow, run:

```bash
bk pipeline convert --file .github/workflows/ci.yml --vendor github
```

Then review the output and commit it as `.buildkite/pipeline.yml` (or paste it into
the pipeline's settings in the Buildkite UI).
