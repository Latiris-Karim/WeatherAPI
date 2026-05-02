# WeatherAPI

A small FastAPI weather service deployed on Google Cloud Run. The weather 
logic is minimal — the project was about building the deployment pipeline.

## Stack

- **FastAPI** — HTTP API
- **Redis** (Cloud Memorystore in prod, container locally) — caching
- **Cloud Run** — serverless hosting
- **Cloud Build** — CI/CD on push to `main`
- **Artifact Registry** — container images
- **Secret Manager** — API keys and runtime secrets

## Deploy

Push to `main` → Cloud Build → Artifact Registry → new Cloud Run revision. 
Pipeline defined in `cloudbuild.yaml`.

## What I learned

- Containerizing FastAPI for Cloud Run
- Wiring Cloud Build → Artifact Registry → Cloud Run end to end
- Redis caching to cut latency and external API calls
