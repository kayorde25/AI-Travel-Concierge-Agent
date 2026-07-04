from pathlib import Path
import importlib.util

TOOLS_PATH = Path(__file__).resolve().parents[2] / "app" / "tools.py"
spec = importlib.util.spec_from_file_location("travel_tools", TOOLS_PATH)
travel_tools = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(travel_tools)


def test_search_flights_returns_relevant_route() -> None:
    result = travel_tools.search_flights("Lagos", "London", "2026-08-15")
    assert "Available flights" in result
    assert "Lagos" in result
    assert "London" in result
    assert "FL-" in result


def test_book_flight_returns_booking_reference() -> None:
    result = travel_tools.book_flight("FL-123", "Abiola Olaleye")
    assert "Flight booked successfully" in result
    assert "Abiola Olaleye" in result
    assert "Booking Ref" in result


def test_search_hotels_returns_city_and_hotel_ids() -> None:
    result = travel_tools.search_hotels("Dubai", "2026-09-10", "2026-09-15")
    assert "Available hotels in Dubai" in result
    assert "HTL-" in result


def test_book_hotel_returns_reservation_code() -> None:
    result = travel_tools.book_hotel("HTL-42", "Abiola Olaleye")
    assert "Hotel booked successfully" in result
    assert "Reservation" in result


def test_search_cars_returns_location_and_car_ids() -> None:
    result = travel_tools.search_cars("Paris", "2026-09-10", "2026-09-12")
    assert "Available rental cars in Paris" in result
    assert "CAR-" in result


def test_book_car_returns_agreement_number() -> None:
    result = travel_tools.book_car("CAR-12", "Abiola Olaleye")
    assert "Car rental booked successfully" in result
    assert "Agreement" in result


def test_check_visa_requirements_for_kenya() -> None:
    result = travel_tools.check_visa_requirements("Nigeria", "Kenya")
    assert "Visa requirement" in result
    assert "Kenya" in result
    assert "eVisa" in result


def test_apply_evisa_returns_application_id() -> None:
    result = travel_tools.apply_evisa("A12345678", "Nigeria", "Kenya")
    assert "eVisa Application Submitted" in result
    assert "Application ID" in result
    assert "Kenya" in result
