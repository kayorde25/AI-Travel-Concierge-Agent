# AI-Travel-Concierge-Agent
A generic Google ADK multi-agent travel concierge for flights, hotels, car rentals, and eVisa support.

Repository Structure
ai-travel-concierge-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── tools.py
│   └── fast_api_app.py
│
├── tests/
│   ├── unit/
│   │   ├── test_dummy.py
│   │   └── test_travel_tools.py
│   └── integration/
│       ├── test_agent.py
│       └── test_server_e2e.py
│
├── docs/
│   ├── DESIGN.md
│   ├── TESTING.md
│   └── SAFETY_AND_LIMITATIONS.md
│
├── frontend/
│   └── ...
│
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── README.md
├── .env.example
├── .gitignore
└── LICENSE


AI Travel Concierge Agent is a generic multi-agent travel assistant built with Google Agent Development Kit. It helps users complete common travel-planning tasks through one conversational interface, including flight search, hotel search, car rental support, and eVisa guidance.

The project was developed as a capstone-style AI agent prototype. It is intentionally generic and is not tied to any specific travel brand. The same design could be adapted by online travel agencies, travel marketplaces, airline support teams, hotel booking platforms, or concierge-service providers.

---

## Problem

Travel planning is often fragmented. A user may need to:

- Search for flights
- Find hotels
- Arrange car rentals
- Check visa requirements
- Ask booking-related questions
- Compare options across several services

Most travel platforms split these tasks across different pages, forms, and support channels. This creates friction for users and repetitive work for customer-support teams.

A multi-agent travel assistant can simplify this process by understanding the user’s request, routing it to the correct specialist agent, calling the appropriate tool, and returning a helpful response.

---

## Solution

AI Travel Concierge Agent provides a single conversational interface for travel assistance.

The user can ask:

```text
Find me a flight from Lagos to London on 2026-08-15.
Find hotels in Dubai from 2026-09-10 to 2026-09-15.
Do I need a visa to visit Kenya as a Nigerian citizen?
I need a rental car in Paris from 2026-09-10 to 2026-09-12.

The root coordinator agent receives the request and delegates it to the most relevant specialist agent.

Key Features
Multi-agent travel assistant
Root coordinator agent
Specialist agents for flights, hotels, cars, and eVisa support
Tool calling for travel workflows
Mock travel APIs for safe testing
Google ADK Web interface
Unit tests for travel tools
Traceable agent routing through ADK events
Generic design that can be adapted to real travel platforms
Agent Architecture

The system uses a coordinator-specialist architecture.

User Request
     ↓
Travel Coordinator Agent
     ↓
Specialist Agent
     ↓
Travel Tool
     ↓
Response to User


Example:

User asks: "Find me a flight from Lagos to London on 2026-08-15."

Travel Coordinator Agent
     ↓
Transfers to flights_agent
     ↓
flights_agent calls search_flights
     ↓
Flight options are returned to the user

Agents
1. Travel Coordinator Agent

The root agent receives the user’s request and decides which specialist agent should handle it.

Responsibilities:

Understand user intent
Route flight requests to the flights agent
Route hotel requests to the hotels agent
Route car rental requests to the cars agent
Route visa questions to the eVisa agent
Provide a smooth conversational experience

2. Flights Agent

Handles flight-related requests.

Supported tasks:

Search for flights
Book mock flight options
Explain available flight options

Tools:
search_flights
book_flight

3. Hotels Agent

Handles accommodation-related requests.

Supported tasks:

Search for hotels
Book mock hotel options
Provide destination-based accommodation assistance

Tools:
search_hotels
book_hotel

4. Cars Agent
Handles car rental and ground transport requests.
Supported tasks:
Search for car rentals
Book mock car options
Provide destination-based car rental support
Tools:
search_cars
book_car

5. eVisa Agent
Handles visa and travel-entry questions.
Supported tasks:
Check visa requirements
Support mock eVisa application guidance
Tools:
check_visa_requirements
apply_evisa

Tools
The current version uses mock tools. This keeps the prototype safe and prevents accidental real bookings, real payments, or exposure of sensitive user data.

Implemented tools include:
search_flights(origin, destination, date)
book_flight(flight_id, passenger_name)

search_hotels(destination, check_in_date, check_out_date)
book_hotel(hotel_id, guest_name)

search_cars(location, pickup_date, return_date)
book_car(car_id, driver_name)

check_visa_requirements(nationality, destination)
apply_evisa(destination, applicant_name)

Technology Stack
Python
Google Agent Development Kit
Gemini API
ADK Web
FastAPI
Pytest
uv

Repository Structure
app/
  agent.py              Agent definitions and multi-agent routing
  tools.py              Mock travel tools
  fast_api_app.py       Optional FastAPI app wrapper

tests/
  unit/                 Unit tests for travel tools
  integration/          Integration and server tests

docs/
  DESIGN.md             System design and architecture
  TESTING.md            Testing approach and evidence

 SAFETY_AND_LIMITATIONS.md
                        Safety design, limitations, and future work

README.md               Project overview
.env.example            Example environment variables
pyproject.toml          Python project configuration
Dockerfile              Container build file

Installation
Clone the repository:
git clone https://github.com/kayorde25/ai-travel-concierge-agent.git
cd ai-travel-concierge-agent

Install dependencies:
uv sync

Create a local environment file:
cp .env.example app/.env

Add your local API key inside app/.env:
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here

Running the Agent
Start ADK Web:
uv run adk web --port 8000 .

Open:
http://127.0.0.1:8000

Select the app/agent and start chatting with the assistant.

Testing

Run unit tests:
uv run pytest tests/unit
Manual integration testing was also performed through ADK Web. The ADK event trace confirmed that the coordinator agent transferred requests to the correct specialist agents and called the appropriate travel tools.
Safety Notes

This project does not make real bookings or process payments. All travel tools are mock tools for demonstration and testing.

This avoids:

Accidental flight bookings
Accidental hotel reservations
Real payment processing
Exposure of customer data
Uncontrolled calls to production travel APIs

A production version would require stronger guardrails, authentication, payment confirmation, audit logging, personal data protection, and human support escalation.

Limitations

The current version is a capstone prototype.

Limitations include:

Uses mock travel data
Does not connect to live flight APIs
Does not connect to live hotel APIs
Does not connect to live car rental APIs
Does not process payments
Does not make real bookings
Does not store long-term user memory
Runs locally through ADK Web
Integration tests may require live credentials and a configured runtime environment
Future Work

Planned improvements include:

Live flight API integration
Live hotel API integration
Live car rental or airport transfer integration
Real visa information integration
Persistent user memory
User authentication
Booking confirmation guardrails
Human support handoff
Payment-safe workflow design
Itinerary generation
Email and SMS notifications
Cloud deployment
Monitoring and logging
More extensive evaluation datasets
