from modules.opensky import get_opensky_data
from modules.wikipedia import get_wikipedia_data
from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data
from modules.aviation_safety import get_aviation_safety_data
from modules.airport_info import get_airport_info
from modules.models.aircraft import Aircraft

def osint_from_tail(tail_value):
    # 1. Get ICAO
    # 2. Get OpenSky
    # 3. Get Wikipedia
    # 4. Get Photos from Jet Photos
    # 5. Get Data from Flight Aware (TODO: ask for permission to use emulation)
    # 6. Get Airport Information
    aircraft = Aircraft()
    aircraft = get_opensky_data(aircraft, tail_value)
    aircraft = get_wikipedia_data(aircraft, tail_value)
    aircraft.photos = get_jetphotos_data(tail_value)
    flight_aware = get_flightaware_data(tail_value)
    aircraft.history = flight_aware["history"]
    aircraft.telemetry = flight_aware["telemetry"]
    aircraft.registration_details = flight_aware["registration"]
    aircraft.departure_airport = flight_aware["departure"]
    aircraft.arrival_airport = flight_aware["arrival"]
    aircraft.safety = get_aviation_safety_data(tail_value)
    # aircraft.airport = get_airport_info(aircraft.)
    # aircraft.airport = get_airport_info(aircraft.)
    aircraft.print()
    return

def osint_from_icao(icao_value):
    return