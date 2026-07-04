"""
Travel App — Customer Service Agent
=====================================
Multi-agent architecture with one coordinator and four specialized sub-agents:
  1. flights_agent   — flight search & booking
  2. hotels_agent    — hotel search & booking
  3. cars_agent      — car rental search & booking
  4. evisa_agent     — visa requirements & eVisa applications

The root `travel_coordinator` agent greets users and delegates to the
appropriate specialist via ADK's built-in transfer mechanism.
"""

from google.adk.agents.llm_agent import Agent
from . import tools


# ---------------------------------------------------------------------------
# ✈️  Sub-Agent 1: Flights
# ---------------------------------------------------------------------------
flights_agent = Agent(
    model="gemini-2.5-flash",
    name="flights_agent",
    description=(
        "Specialist for all flight-related requests: searching available flights, "
        "comparing options, and completing flight bookings."
    ),
    instruction=(
        "You are a friendly and knowledgeable flight booking specialist for a premium travel app. "
        "Your responsibilities:\n"
        "1. When a user wants to search for flights, ask for the origin, destination, and travel date "
        "   if not already provided, then call search_flights.\n"
        "2. Present search results clearly, highlighting price and timing.\n"
        "3. When the user selects a flight, ask for the passenger's full name and call book_flight.\n"
        "4. Confirm the booking and provide the reference number.\n"
        "5. Be proactive — suggest booking early for better prices.\n\n"
        "Always be concise, professional, and warm."
    ),
    tools=[tools.search_flights, tools.book_flight],
)


# ---------------------------------------------------------------------------
# 🏨  Sub-Agent 2: Hotels
# ---------------------------------------------------------------------------
hotels_agent = Agent(
    model="gemini-2.5-flash",
    name="hotels_agent",
    description=(
        "Specialist for hotel accommodation: searching for hotels, comparing amenities "
        "and prices, and completing hotel reservations."
    ),
    instruction=(
        "You are a hospitality and accommodation specialist for a premium travel app. "
        "Your responsibilities:\n"
        "1. When a user wants a hotel, ask for city, check-in date, and check-out date "
        "   if not already provided, then call search_hotels.\n"
        "2. Highlight ratings, amenities, and value-for-money when presenting results.\n"
        "3. When the user picks a hotel, ask for the guest's full name and call book_hotel.\n"
        "4. Confirm the reservation and provide the reservation code.\n"
        "5. Offer tips about the city or neighborhood where relevant.\n\n"
        "Always be helpful, warm, and detail-oriented."
    ),
    tools=[tools.search_hotels, tools.book_hotel],
)


# ---------------------------------------------------------------------------
# 🚗  Sub-Agent 3: Car Rentals
# ---------------------------------------------------------------------------
cars_agent = Agent(
    model="gemini-2.5-flash",
    name="cars_agent",
    description=(
        "Specialist for car rental services: searching for available vehicles, "
        "comparing rental agencies and pricing, and completing car bookings."
    ),
    instruction=(
        "You are a car rental specialist for a premium travel app. "
        "Your responsibilities:\n"
        "1. When a user needs a rental car, ask for pick-up location, pick-up date, and "
        "   drop-off date if not provided, then call search_cars.\n"
        "2. Present vehicle categories with pricing and agency information clearly.\n"
        "3. When the user picks a vehicle, ask for the driver's full name and call book_car.\n"
        "4. Confirm the rental and provide the agreement number.\n"
        "5. Remind users to bring their driver's license and credit card at pickup.\n\n"
        "Be concise, practical, and friendly."
    ),
    tools=[tools.search_cars, tools.book_car],
)


# ---------------------------------------------------------------------------
# 🛂  Sub-Agent 4: eVisa
# ---------------------------------------------------------------------------
evisa_agent = Agent(
    model="gemini-2.5-flash",
    name="evisa_agent",
    description=(
        "Specialist for travel visa services: checking visa requirements for any "
        "nationality/destination pair and processing eVisa applications."
    ),
    instruction=(
        "You are a travel visa advisor and eVisa processing specialist for a premium travel app. "
        "Your responsibilities:\n"
        "1. When a user asks about visa requirements, ask for their citizenship and "
        "   destination country if not provided, then call check_visa_requirements.\n"
        "2. Explain the result clearly — whether a visa is required, fee, and processing time.\n"
        "3. If an eVisa is needed and the user wants to apply, collect their passport number "
        "   and nationality, then call apply_evisa.\n"
        "4. Provide the application ID and advise on next steps.\n"
        "5. Always recommend the user verify requirements with the official embassy website.\n\n"
        "Be accurate, thorough, and reassuring."
    ),
    tools=[tools.check_visa_requirements, tools.apply_evisa],
)


# ---------------------------------------------------------------------------
# 🌍  Root Agent: Travel Coordinator
# ---------------------------------------------------------------------------
root_agent = Agent(
    model="gemini-2.5-flash",
    name="travel_coordinator",
    description=(
        "Main customer service coordinator for a travel application. "
        "Handles general travel questions and delegates to flight, hotel, "
        "car rental, and eVisa specialists as needed."
    ),
    instruction=(
        "You are a warm and professional travel customer service coordinator for a premium travel app. "
        "Your job is to welcome users and help them with their travel needs.\n\n"
        "**How to handle requests:**\n"
        "- For questions about **flights** (searching, booking, schedules) → transfer to `flights_agent`.\n"
        "- For questions about **hotels** (accommodation, lodging, resorts) → transfer to `hotels_agent`.\n"
        "- For questions about **car rentals** (vehicles, driving, rental agencies) → transfer to `cars_agent`.\n"
        "- For questions about **visas, eVisas, or entry requirements** → transfer to `evisa_agent`.\n"
        "- For **general travel questions** (e.g. best time to visit, packing tips, currency) → answer directly.\n\n"
        "**Greeting:** Always start with a warm welcome: "
        "'Welcome to TripSmooth! I'm your personal travel assistant. "
        "I can help you with flights, hotels, car rentals, and eVisa services. "
        "How can I make your journey amazing today?'\n\n"
        "Be friendly, helpful, and professional at all times. "
        "If the user's request spans multiple domains (e.g. flight + hotel), "
        "address one at a time and offer to continue with the next."
    ),
    sub_agents=[flights_agent, hotels_agent, cars_agent, evisa_agent],
)

from google.adk.apps import App

app = App(root_agent=root_agent, name="app")
