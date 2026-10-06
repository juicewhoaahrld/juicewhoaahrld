\
\
\
\
\
\
\
\
\
\
\
\
\
   

from datetime import datetime
from config import DEMO_USER, PRICES


class Backend:
    def __init__(self):
        self.users = {
            DEMO_USER["username"]: {
                "password": DEMO_USER["password"],
                "full_name": DEMO_USER["full_name"],
                "contact": DEMO_USER["contact"],
            }
        }

        self.reservations = []
        self.reservation_counter = 1

                                                              
           
                                                              

    def register_user(self, full_name, username, password, contact):
        full_name = full_name.strip()
        username = username.strip()
        contact = contact.strip()

        if not full_name or not username or not password or not contact:
            return False, "Please fill in all fields."

        if username in self.users:
            return False, "Username already exists. Please choose another username."

        self.users[username] = {
            "password": password,
            "full_name": full_name,
            "contact": contact,
        }

        return True, "Account created successfully."

    def authenticate(self, username, password):
        username = username.strip()

        if not username or not password:
            return False, "Please enter username and password.", None

        user = self.users.get(username)

        if user is None:
            return False, "Username does not exist.", None

        if user["password"] != password:
            return False, "Incorrect password.", None

        current_user = {
            "username": username,
            **user,
        }

        return True, "Login successful.", current_user

    def get_demo_user(self):
        return {
            "username": DEMO_USER["username"],
            "full_name": DEMO_USER["full_name"],
            "contact": DEMO_USER["contact"],
        }

                                                              
            
                                                              

    def get_price(self, vehicle, service):
        try:
            return PRICES[service][vehicle]
        except KeyError:
            return None

                                                              
          
                                                              

    def validate_date(self, date_text):
        try:
            selected_date = datetime.strptime(
                date_text.strip(),
                "%m/%d/%Y",
            ).date()
        except ValueError:
            return False, "Please use the format MM/DD/YYYY."

        if selected_date < datetime.now().date():
            return False, "The reservation date cannot be in the past."

        return True, "Valid date."

                                                              
                      
                                                              

    def is_bay_available(self, bay, date, time):
        for reservation in self.reservations:
            if (
                reservation["bay"] == bay
                and reservation["date"] == date
                and reservation["time"] == time
            ):
                return False

        return True

                                                              
                  
                                                              

    def create_reservation(
        self,
        current_user,
        vehicle,
        service,
        date,
        time,
        bay,
    ):
        if not current_user:
            return False, "Please log in first.", None

        if not vehicle:
            return False, "Please select a vehicle.", None

        if not service:
            return False, "Please select a carwash service.", None

        if not date:
            return False, "Please enter a reservation date.", None

        valid_date, date_message = self.validate_date(date)
        if not valid_date:
            return False, date_message, None

        if not time:
            return False, "Please select a reservation time.", None

        if not bay:
            return False, "Please select a carwash bay.", None

        if not self.is_bay_available(bay, date, time):
            return (
                False,
                f"{bay} is already reserved for {date} at {time}.",
                None,
            )

        price = self.get_price(vehicle, service)

        if price is None:
            return False, "Invalid vehicle or service.", None

        reservation_id = f"RES-{self.reservation_counter:04d}"
        self.reservation_counter += 1

        reservation = {
            "reservation_id": reservation_id,
            "username": current_user["username"],
            "customer": current_user["full_name"],
            "contact": current_user["contact"],
            "vehicle": vehicle,
            "service": service,
            "date": date,
            "time": time,
            "bay": bay,
            "total": price,
        }

        self.reservations.append(reservation)

        return True, "Reservation confirmed.", reservation

    def get_user_reservations(self, username):
        return [
            reservation
            for reservation in self.reservations
            if reservation["username"] == username
        ]

    def get_all_reservations(self):
        return list(self.reservations)
