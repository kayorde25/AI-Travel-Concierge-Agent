"""
Travel App - Customer Service Tools
====================================
Mock API functions for the four travel service domains:
  - Flights
  - Hotels
  - Car Rentals
  - eVisa
"""

import random


# ---------------------------------------------------------------------------
# ✈️  FLIGHTS
# ---------------------------------------------------------------------------

def search_flights(origin: str, destination: str, date: str) -> str:
    """Search for available flights between two cities on a given date.

    Args:
        origin: Departure airport or city (e.g. 'New York', 'LHR').
        destination: Arrival airport or city (e.g. 'Tokyo', 'CDG').
        date: Travel date in YYYY-MM-DD format.

    Returns:
        A formatted list of available flights with times and prices.
    """
    seeds = [random.randint(100, 999) for _ in range(3)]
    options = [
        (f"FL-{seeds[0]}", "08:00 AM", "11:30 AM", "$350"),
        (f"FL-{seeds[1]}", "02:15 PM", "05:45 PM", "$420"),
        (f"FL-{seeds[2]}", "08:30 PM", "11:59 PM", "$290"),
    ]
    lines = [
        f"  • Flight {fid} | Departs {origin} at {dep} | Arrives {destination} at {arr} | {price}"
        for fid, dep, arr, price in options
    ]
    return (
        f"🛫 Available flights from {origin} to {destination} on {date}:\n"
        + "\n".join(lines)
        + "\n\nReply with the Flight ID (e.g. FL-123) and passenger name to book."
    )


def book_flight(flight_id: str, passenger_name: str) -> str:
    """Book a specific flight for a passenger.

    Args:
        flight_id: The flight identifier returned from search_flights (e.g. 'FL-452').
        passenger_name: Full name of the passenger as it appears on the passport.

    Returns:
        Booking confirmation with reference number.
    """
    ref = f"TX-{random.randint(10000, 99999)}"
    return (
        f"✅ Flight booked successfully!\n"
        f"   Flight:     {flight_id}\n"
        f"   Passenger:  {passenger_name}\n"
        f"   Booking Ref: {ref}\n\n"
        "Please save your booking reference for check-in and future queries."
    )


# ---------------------------------------------------------------------------
# 🏨  HOTELS
# ---------------------------------------------------------------------------

def search_hotels(city: str, checkin: str, checkout: str) -> str:
    """Search for hotel accommodations in a city.

    Args:
        city: Destination city name (e.g. 'Paris', 'Bangkok').
        checkin: Check-in date in YYYY-MM-DD format.
        checkout: Check-out date in YYYY-MM-DD format.

    Returns:
        A formatted list of available hotels with ratings, prices, and amenities.
    """
    hotels = [
        (f"HTL-{random.randint(10,99)}", f"Grand Plaza {city}", "4.5★", "$180/night", "Pool, Free WiFi, Gym"),
        (f"HTL-{random.randint(10,99)}", f"Cozy Stay Inn {city}", "4.0★", "$110/night", "Breakfast Included, Free WiFi"),
        (f"HTL-{random.randint(10,99)}", f"Luxury Palace {city}", "4.9★", "$350/night", "Spa, Ocean View, Butler Service"),
    ]
    lines = [
        f"  • [{hid}] {name} | {rating} | {price} | Amenities: {amenities}"
        for hid, name, rating, price, amenities in hotels
    ]
    return (
        f"🏨 Available hotels in {city} ({checkin} → {checkout}):\n"
        + "\n".join(lines)
        + "\n\nReply with the Hotel ID (e.g. HTL-42) and guest name to book."
    )


def book_hotel(hotel_id: str, guest_name: str) -> str:
    """Book a hotel room for a guest.

    Args:
        hotel_id: The hotel identifier returned from search_hotels (e.g. 'HTL-42').
        guest_name: Full name of the primary guest.

    Returns:
        Reservation confirmation with reference code.
    """
    code = f"RES-{random.randint(10000, 99999)}"
    return (
        f"✅ Hotel booked successfully!\n"
        f"   Hotel ID:   {hotel_id}\n"
        f"   Guest:      {guest_name}\n"
        f"   Reservation: {code}\n\n"
        "Your reservation confirmation will be emailed to you shortly."
    )


# ---------------------------------------------------------------------------
# 🚗  CAR RENTALS
# ---------------------------------------------------------------------------

def search_cars(location: str, pickup_date: str, dropoff_date: str) -> str:
    """Search for available rental cars at a location.

    Args:
        location: City or airport code (e.g. 'Los Angeles', 'CDG').
        pickup_date: Pick-up date in YYYY-MM-DD format.
        dropoff_date: Drop-off date in YYYY-MM-DD format.

    Returns:
        A formatted list of available vehicles with pricing and rental agency.
    """
    vehicles = [
        (f"CAR-{random.randint(10,99)}", "Economy Hatchback", "$45/day", "Hertz"),
        (f"CAR-{random.randint(10,99)}", "Midsize SUV",       "$75/day", "Enterprise"),
        (f"CAR-{random.randint(10,99)}", "Luxury Convertible","$120/day","Avis"),
    ]
    lines = [
        f"  • [{vid}] {vtype} | {price} | Agency: {agency}"
        for vid, vtype, price, agency in vehicles
    ]
    return (
        f"🚗 Available rental cars in {location} ({pickup_date} → {dropoff_date}):\n"
        + "\n".join(lines)
        + "\n\nReply with the Car ID (e.g. CAR-12) and driver name to book."
    )


def book_car(car_id: str, driver_name: str) -> str:
    """Book a rental car for a driver.

    Args:
        car_id: The vehicle identifier returned from search_cars (e.g. 'CAR-12').
        driver_name: Full name of the primary driver.

    Returns:
        Rental agreement confirmation with reference number.
    """
    ref = f"CR-{random.randint(10000, 99999)}"
    return (
        f"✅ Car rental booked successfully!\n"
        f"   Vehicle ID:  {car_id}\n"
        f"   Driver:      {driver_name}\n"
        f"   Agreement:   {ref}\n\n"
        "Please bring your driver's license and credit card at pickup."
    )


# ---------------------------------------------------------------------------
# 🛂  eVISA
# ---------------------------------------------------------------------------

def check_visa_requirements(citizenship: str, destination: str) -> str:
    """Check whether an eVisa is required for a traveler based on citizenship and destination.

    Args:
        citizenship: Country of citizenship (e.g. 'United States', 'Germany').
        destination: Country of travel destination (e.g. 'India', 'Turkey').

    Returns:
        Visa requirement details for the given citizenship/destination combination.
    """
    if citizenship.strip().lower() == destination.strip().lower():
        return f"No visa required — you are a citizen of {destination}."

    evisa_required = {
        "india":      "eVisa required. Fee: $25. Processing: 72 hours.",
        "turkey":     "eVisa required. Fee: $50. Processing: 24 hours.",
        "vietnam":    "eVisa required. Fee: $25. Processing: 3 business days.",
        "egypt":      "Visa on Arrival available OR eVisa. Fee: $25.",
        "kenya":      "eVisa required. Fee: $50. Processing: 3 business days.",
        "sri lanka":  "eVisa required. Fee: $20. Processing: 24 hours.",
        "ethiopia":   "eVisa required. Fee: $82. Processing: 3 business days.",
        "cambodia":   "eVisa available. Fee: $30. Processing: 3 business days.",
    }

    dest_lower = destination.strip().lower()
    if dest_lower in evisa_required:
        return (
            f"📋 Visa requirement for {citizenship} → {destination}:\n"
            f"   {evisa_required[dest_lower]}\n\n"
            "I can process your eVisa application right here. "
            "Please provide your passport number and nationality to proceed."
        )

    return (
        f"✅ Good news! Citizens of {citizenship} do not require a pre-arranged visa "
        f"for travel to {destination} for stays up to 30 days (visa-free or visa-on-arrival). "
        "We recommend verifying with the destination country's official embassy website before travel."
    )


def apply_evisa(passport_number: str, nationality: str, destination: str) -> str:
    """Submit an eVisa application for a traveler.

    Args:
        passport_number: Traveler's passport number.
        nationality: Country of nationality (e.g. 'United States').
        destination: Destination country requiring the eVisa (e.g. 'India').

    Returns:
        eVisa application confirmation with tracking ID and expected timeline.
    """
    app_id = f"EV-{random.randint(100000, 999999)}"
    return (
        f"📨 eVisa Application Submitted!\n"
        f"   Application ID: {app_id}\n"
        f"   Passport:       {passport_number}\n"
        f"   Nationality:    {nationality}\n"
        f"   Destination:    {destination}\n"
        f"   Status:         PENDING ⏳\n\n"
        "Expected approval within 24–72 hours. You will receive a notification "
        "once your eVisa is approved. Please keep your Application ID for tracking."
    )
