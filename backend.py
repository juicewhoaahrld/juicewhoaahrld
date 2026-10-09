from datetime import datetime

PRICES = {
    "Basic Wash": {"Sedan": 130, "SUV": 180, "Van": 200, "Pick-up": 200, "Motorcycle": 100},
    "Wash + Vacuum": {"Sedan": 160, "SUV": 200, "Van": 230, "Pick-up": 230, "Motorcycle": 130},
    "Wash + Wax": {"Sedan": 250, "SUV": 300, "Van": 350, "Pick-up": 350, "Motorcycle": 180},
    "Premium Wash": {"Sedan": 350, "SUV": 400, "Van": 450, "Pick-up": 450, "Motorcycle": 250},
    "Engine Wash": {"Sedan": 450, "SUV": 500, "Van": 550, "Pick-up": 550, "Motorcycle": 300},
}


def validate_date(date_text):
    try:
        selected = datetime.strptime(date_text.strip(), "%m/%d/%Y").date()
    except ValueError:
        return False
    return selected >= datetime.now().date()


def calculate_price(vehicle, service):
    return PRICES.get(service, {}).get(vehicle)


def bay_available(reservations, bay, date, time):
    return not any(r.get("bay") == bay and r.get("date") == date and r.get("time") == time for r in reservations)


def reservations_for_user(reservations, username):
    return [r for r in reservations if r.get("username") == username]
