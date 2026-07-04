# TripSmooth AI Travel Concierge Agent

A multi-agent AI travel assistant built for the Kaggle Vibe Coding Agents Capstone Project. The project demonstrates a practical customer-support and travel-planning agent for flights, hotels, car rentals, and eVisa support.

## Track

**Concierge Agents** / **Agents for Business**

## Problem

Travel customers often struggle with fragmented support across flight search, hotel booking, airport transfers, car rentals, visa requirements, and post-booking questions. A travel platform needs an assistant that can understand the customer’s intent, route the request to the right specialist, call the right tool, and provide safe, clear support.

## Solution

TripSmooth AI Travel Concierge Agent is a coordinator-led multi-agent assistant. The root coordinator welcomes the customer, understands the travel request, and delegates to one of four specialist sub-agents:

- **Flights Agent** — flight search and booking support
- **Hotels Agent** — hotel search and reservation support
- **Cars Agent** — rental car search and booking support
- **eVisa Agent** — visa requirement checks and eVisa application support

The current prototype uses mock travel tools so it can be safely demonstrated without exposing production travel APIs or payment credentials.

## Key Features

- Multi-agent routing through a root travel coordinator
- Domain-specific sub-agents for flights, hotels, cars, and eVisa support
- Tool-calling functions for search and booking workflows
- FastAPI backend generated with Google ADK/agents-cli
- React chat frontend scaffold
- Unit, integration, and evaluation test structure
- Cloud Run-ready deployment scaffold through Docker and Terraform assets
- Privacy-conscious demo design using mock services instead of real passenger/payment data

## Architecture

```text
User
  ↓
React / ADK Playground UI
  ↓
FastAPI backend
  ↓
Root Agent: travel_coordinator
  ↓
Specialist sub-agents
  ├── flights_agent → search_flights(), book_flight()
  ├── hotels_agent  → search_hotels(), book_hotel()
  ├── cars_agent    → search_cars(), book_car()
  └── evisa_agent   → check_visa_requirements(), apply_evisa()
```

## Agent Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Tool use | Python functions for flight, hotel, car, and visa workflows |
| Multi-agent design | Root coordinator plus four specialist sub-agents |
| Delegation/routing | Coordinator transfers requests to the relevant specialist |
| Safety/privacy | Mock tools; no real payment or passport processing in demo |
| Evaluation | Travel-specific eval cases and unit tests |
| Deployment readiness | FastAPI, Dockerfile, and Cloud Run scaffold |

## Project Structure

```text
app/
  agent.py              # Multi-agent definition
  tools.py              # Mock travel tools
  fast_api_app.py       # FastAPI backend
frontend/
  src/App.jsx           # React chat UI scaffold
tests/
  unit/                 # Tool-level tests
  integration/          # ADK/A2A integration tests
  eval/                 # Agent evaluation cases
Dockerfile
pyproject.toml
agents-cli-manifest.yaml
```

## Local Setup

### 1. Install dependencies

```bash
uvx google-agents-cli setup
agents-cli install
```

Alternative Python setup:

```bash
uv sync
```

### 2. Configure environment variables

Copy the example file:

```bash
cp .env.example app/.env
```

Then set either Vertex AI configuration or a Gemini API key. Do not commit `app/.env` to GitHub.

### 3. Run the agent locally

```bash
agents-cli playground
```

This is the easiest way to demonstrate the agent for the Kaggle video.

### 4. Run tests

```bash
uv run pytest tests/unit
```

For integration tests:

```bash
uv run pytest tests/integration
```

## Demo Script

Recommended demo flow:

1. Ask: “Find me a flight from Lagos to London on 2026-08-15.”
2. Show the coordinator routing to the flights agent.
3. Ask to book one of the returned flight IDs.
4. Ask: “Find hotels in Dubai from 2026-09-10 to 2026-09-15.”
5. Ask: “Do I need a visa to visit Kenya as a Nigerian citizen?”
6. Ask: “I need a rental car in Paris from 2026-09-10 to 2026-09-12.”
7. Explain that mock tools are used for safety and demonstration.

## Evaluation Cases

The project includes travel-specific evaluation examples covering:

- Greeting and capability explanation
- Flight search
- Flight booking
- Hotel search
- Car rental search
- Visa requirement checks
- Multi-domain itinerary requests
- Safety-aware handling of sensitive visa/passport/payment data

## Limitations

- Mock APIs are used instead of live travel suppliers.
- The prototype does not process real payments.
- eVisa responses are simplified and should be verified against official government sources in production.
- The frontend may require endpoint alignment depending on whether the project is run through ADK playground or custom FastAPI routes.

## Future Improvements

- Connect to live flight, hotel, car, and visa APIs
- Add user preference memory
- Add price tracking and itinerary storage
- Add human escalation for payment, cancellation, and identity-sensitive issues
- Add production-grade authentication and audit logs
- Add full frontend integration with ADK streaming endpoints

## Author

Abiola Olaleye
