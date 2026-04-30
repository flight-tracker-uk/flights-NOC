"""Ireland West / Knock Airport (NOC) destinations — April 2026."""

DESTINATIONS = {
    "NOC": {
        "name": "Ireland West (Knock)",
        "routes": {
            # UK
            "BHX": "Birmingham",
            "BRS": "Bristol",
            "EDI": "Edinburgh",
            "EMA": "East Midlands",
            "LHR": "London Heathrow",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "STN": "London Stansted",
            # Spain (Mainland)
            "AGP": "Malaga",
            "ALC": "Alicante",
            "BCN": "Barcelona",
            "XRY": "Jerez (Cadiz)",
            # Balearic Islands
            "PMI": "Palma de Mallorca",
            # Canary Islands
            "ACE": "Lanzarote",
            "TFS": "Tenerife South",
            # Italy
            "BGY": "Milan Bergamo",
            "FCO": "Rome Fiumicino",
            # France
            "LDE": "Lourdes",
            # Germany
            "CGN": "Cologne",
            # Portugal
            "FAO": "Faro",
            # Bosnia & Herzegovina
            "OMO": "Mostar (Medjugorje)",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
