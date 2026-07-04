# Kaggle Writeup Draft: TripSmooth AI Travel Concierge Agent

## Title
TripSmooth AI Travel Concierge Agent

## Track
Concierge Agents / Agents for Business

## Problem Statement
Travel platforms often require customers to move across separate workflows for flight search, hotel reservations, car rentals, visa requirements, and booking support. This creates friction, especially for customers who need quick answers and coordinated itinerary support.

## Solution
TripSmooth AI Travel Concierge Agent is a multi-agent travel assistant that welcomes the customer, identifies the request type, and delegates to the correct specialist agent. It supports flight search and booking, hotel search and booking, car rental search and booking, and eVisa requirement/application workflows.

## Technical Implementation
The project uses Google ADK/agents-cli with a FastAPI backend. The root `travel_coordinator` agent delegates to four domain-specific sub-agents: `flights_agent`, `hotels_agent`, `cars_agent`, and `evisa_agent`. Each specialist has its own tools for domain-specific actions.

## Agent Architecture
- Root coordinator agent: understands the user request and routes it.
- Flights agent: calls `search_flights` and `book_flight`.
- Hotels agent: calls `search_hotels` and `book_hotel`.
- Cars agent: calls `search_cars` and `book_car`.
- eVisa agent: calls `check_visa_requirements` and `apply_evisa`.

## Tools Used
The prototype uses mock Python tools to simulate travel supplier APIs. This keeps the demo safe and reproducible without exposing production API keys, passenger data, payment credentials, or booking supplier secrets.

## Evaluation
The project includes travel-specific evaluation cases for greetings, flight search, flight booking, hotel search, car rental search, visa requirement checks, multi-domain itinerary handling, and sensitive-data guardrails. Unit tests validate that the travel tools return the expected route, booking, reservation, vehicle, and eVisa outputs.

## Safety and Privacy
The prototype avoids real payment processing and avoids storing live personal information. The eVisa flow is simplified and includes a recommendation to verify travel rules with official government sources. In production, identity-sensitive and payment-sensitive workflows would require authentication, audit logging, encryption, and human escalation.

## Demo
The demo shows a customer asking for flights, hotels, rental cars, and visa support. It demonstrates agent routing, tool calls, booking references, and safe handling of mock travel workflows.

## Limitations
The prototype uses mock travel data rather than live supplier APIs. It does not process real payments or issue real travel documents. The frontend scaffold may require endpoint alignment depending on whether the project is run through ADK playground or custom FastAPI routes.

## Future Work
Future versions would connect to live travel APIs, add user preference memory, add itinerary storage, support cancellations and refunds, integrate human escalation, and deploy a production-safe version on Cloud Run.
