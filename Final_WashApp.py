import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class CarwashApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("WASHAPP - Smart Carwash Reservation System")
        self.geometry("1100x720")
        self.minsize(950, 650)
        self.configure(bg="#08111f")

        
        self.users = {
            "demo": {
                "password": "demo123",
                "full_name": "Demo Customer",
                "contact": "09000000000"
            }
        }

        self.reservations = []
        self.reservation_counter = 1
        self.current_user = None

       
        self.selected_vehicle = ""
        self.selected_service = ""
        self.selected_date = ""
        self.selected_time = ""
        self.selected_bay = ""

        
        self.prices = {
            "Basic Wash": {
                "Sedan": 130,
                "SUV": 180,
                "Van": 200,
                "Pick-up": 200,
                "Motorcycle": 100
            },
            "Wash + Vacuum": {
                "Sedan": 160,
                "SUV": 200,
                "Van": 230,
                "Pick-up": 230,
                "Motorcycle": 130
            },
            "Wash + Wax": {
                "Sedan": 250,
                "SUV": 300,
                "Van": 350,
                "Pick-up": 350,
                "Motorcycle": 180
            },
            "Premium Wash": {
                "Sedan": 350,
                "SUV": 400,
                "Van": 450,
                "Pick-up": 450,
                "Motorcycle": 250
            },
            "Engine Wash": {
                "Sedan": 450,
                "SUV": 500,
                "Van": 550,
                "Pick-up": 550,
                "Motorcycle": 300
            }
        }

        self.services = list(self.prices.keys())
        self.vehicle_types = [
            "Sedan",
            "SUV",
            "Van",
            "Pick-up",
            "Motorcycle"
        ]
        self.bays = [
            "Bay 1",
            "Bay 2",
            "Bay 3",
            "Bay 4",
            "Bay 5"
        ]

        self.setup_styles()
        self.show_vehicle_selection()


    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground="#111d2e",
            background="#111d2e",
            foreground="white",
            arrowcolor="#29d9ff",
            bordercolor="#2c4057",
            padding=8
        )

       
        style.configure(
            "Black.TCombobox",
            fieldbackground="#ffffff",
            background="#ffffff",
            foreground="black",
            arrowcolor="#29d9ff",
            bordercolor="#2c4057",
            padding=8
        )

        style.configure(
            "TEntry",
            fieldbackground="#111d2e",
            foreground="white",
            insertcolor="white",
            bordercolor="#2c4057",
            padding=8
        )

        style.configure(
            "Horizontal.TProgressbar",
            troughcolor="#111d2e",
            background="#29d9ff"
        )

    def clear_page(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_header(self, title, subtitle=""):
        header = tk.Frame(self, bg="#08111f", height=120)
        header.pack(fill="x", padx=35, pady=(20, 8))
        header.pack_propagate(False)

        tk.Label(
            header,
            text="WASHAPP",
            font=("Segoe UI", 28, "bold"),
            fg="#29d9ff",
            bg="#08111f"
        ).pack(anchor="w")

        tk.Label(
            header,
            text=title,
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#08111f"
        ).pack(anchor="w")

        if subtitle:
            tk.Label(
                header,
                text=subtitle,
                font=("Segoe UI", 8),
                fg="#d9f7ff",
                bg="#08111f"
            ).pack(anchor="w")

    def card(self, parent, width=None, height=None):
        frame = tk.Frame(
            parent,
            bg="#101d2d",
            highlightbackground="#23374e",
            highlightthickness=1
        )

        if width is not None:
            frame.configure(width=width)

        if height is not None:
            frame.configure(height=height)
            frame.pack_propagate(False)

        return frame

    def button(self, parent, text, command, width=18, primary=True):
        bg = "#119bc1" if primary else "#17283b"
        active = "#29d9ff" if primary else "#263c54"

        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            font=("Segoe UI", 10, "bold"),
            fg="white",
            bg=bg,
            activebackground=active,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=10,
            pady=10
        )


    def show_vehicle_selection(self):
        self.clear_page()

        self.create_header(
            "Smart Carwash Reservation System",
            "Technology That Keeps Your Ride Shining."
        )

        container = tk.Frame(self, bg="#08111f")
        container.pack(fill="both", expand=True, padx=60, pady=15)

        tk.Label(
            container,
            text="SELECT YOUR VEHICLE",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#08111f"
        ).pack(pady=(20, 5))

        tk.Label(
            container,
            text="Choose your vehicle type to continue.",
            font=("Segoe UI", 11),
            fg="#8ea6bd",
            bg="#08111f"
        ).pack(pady=(0, 25))

        grid = tk.Frame(container, bg="#08111f")
        grid.pack()

        vehicle_icons = {
            "Sedan": "🚗",
            "SUV": "🚙",
            "Van": "🚐",
            "Pick-up": "🛻",
            "Motorcycle": "🏍"
        }

        for i, vehicle in enumerate(self.vehicle_types):
            card = self.card(grid)
            card.grid(
                row=0,
                column=i,
                padx=8,
                pady=10,
                ipadx=8,
                ipady=8
            )

            tk.Label(
                card,
                text=vehicle_icons.get(vehicle, "🚗"),
                font=("Segoe UI Emoji", 34),
                fg="#29d9ff",
                bg="#101d2d"
            ).pack(padx=20, pady=(15, 5))

            tk.Label(
                card,
                text=vehicle,
                font=("Segoe UI", 12, "bold"),
                fg="white",
                bg="#101d2d"
            ).pack(pady=5)

            tk.Button(
                card,
                text="SELECT",
                command=lambda v=vehicle: self.select_vehicle(v),
                font=("Segoe UI", 9, "bold"),
                fg="white",
                bg="#119bc1",
                activebackground="#29d9ff",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                padx=20,
                pady=8
            ).pack(padx=20, pady=(5, 15))

        info = self.card(container)
        info.pack(pady=35, padx=100, fill="x")

        tk.Label(
            info,
            text=(
                "Choose your vehicle first. Your selection will be remembered "
                "throughout the reservation process."
            ),
            font=("Segoe UI", 10),
            fg="#a8bdd0",
            bg="#101d2d",
            pady=14
        ).pack()

    def select_vehicle(self, vehicle):
        self.selected_vehicle = vehicle
        self.show_access_page()


    def show_access_page(self):
        self.clear_page()

        self.create_header(
            "Customer Access",
            f"Selected Vehicle: {self.selected_vehicle}"
        )

        container = tk.Frame(self, bg="#08111f")
        container.pack(fill="both", expand=True, padx=60, pady=15)

        login = self.card(container)
        login.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10),
            pady=10
        )

        tk.Label(
            login,
            text="LOGIN",
            font=("Segoe UI", 18, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 20))

        tk.Label(
            login,
            text="Username",
            fg="white",
            bg="#101d2d",
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=35)

        username_entry = tk.Entry(
            login,
            font=("Segoe UI", 11),
            bg="#edf1f5",
            fg="black",
            insertbackground="black",
            relief="flat"
        )
        username_entry.pack(
            fill="x",
            padx=35,
            pady=(5, 15),
            ipady=8
        )

        tk.Label(
            login,
            text="Password",
            fg="white",
            bg="#101d2d",
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=35)

        password_entry = tk.Entry(
            login,
            show="*",
            font=("Segoe UI", 11),
            bg="#edf1f5",
            fg="black",
            insertbackground="black",
            relief="flat"
        )
        password_entry.pack(
            fill="x",
            padx=35,
            pady=(5, 20),
            ipady=8
        )

        self.button(
            login,
            "LOGIN",
            lambda: self.login_user(
                username_entry.get(),
                password_entry.get()
            ),
            width=20
        ).pack(pady=10)

        register = self.card(container)
        register.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        tk.Label(
            register,
            text="NEW CUSTOMER?",
            font=("Segoe UI", 18, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 10))

        tk.Label(
            register,
            text="Create an account!",
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(pady=(0, 20))

        self.button(
            register,
            "SIGN UP / REGISTER",
            self.show_registration,
            width=22
        ).pack(pady=30)

        tk.Label(
            register,
            text="OR",
            font=("Segoe UI", 10, "bold"),
            fg="#71869a",
            bg="#101d2d"
        ).pack(pady=10)

        self.button(
            register,
            "USE DEMO ACCOUNT",
            self.demo_login,
            width=22,
            primary=False
        ).pack(pady=10)

        tk.Label(
            register,
            text="Demo Account: demo / demo123",
            font=("Segoe UI", 9),
            fg="#8ea6bd",
            bg="#101d2d"
        ).pack(pady=10)

        self.button(
            container,
            "← CHANGE VEHICLE",
            self.show_vehicle_selection,
            width=20,
            primary=False
        ).pack(side="bottom", pady=15)

    def login_user(self, username, password):
        username = username.strip()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        if username not in self.users:
            messagebox.showerror(
                "Login Failed",
                "Username does not exist."
            )
            return

        if self.users[username]["password"] != password:
            messagebox.showerror(
                "Login Failed",
                "Incorrect password."
            )
            return

        self.current_user = {
            "username": username,
            **self.users[username]
        }

        self.reset_reservation_selection()
        self.show_dashboard()

    def demo_login(self):
        self.current_user = {
            "username": "demo",
            **self.users["demo"]
        }

        self.reset_reservation_selection()
        self.show_dashboard()


    def show_registration(self):
        self.clear_page()

        self.create_header(
            "Customer Registration",
            f"Selected Vehicle: {self.selected_vehicle}"
        )

        container = tk.Frame(self, bg="#08111f")
        container.pack(fill="both", expand=True)

        form = self.card(container, width=560, height=570)
        form.pack(pady=10)

        tk.Label(
            form,
            text="CREATE ACCOUNT",
            font=("Segoe UI", 19, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 20))

        fields = {}

        field_names = [
            ("Full Name", False),
            ("Username", False),
            ("Password", True),
            ("Confirm Password", True),
            ("Contact Number", False)
        ]

        for name, secret in field_names:
            tk.Label(
                form,
                text=name,
                font=("Segoe UI", 10),
                fg="white",
                bg="#101d2d"
            ).pack(anchor="w", padx=45, pady=(6, 3))

            entry = tk.Entry(
                form,
                show="*" if secret else "",
                font=("Segoe UI", 11),
                bg="#eef0f3",
                fg="black",
                insertbackground="black",
                relief="flat"
            )
            entry.pack(
                fill="x",
                padx=45,
                ipady=7,
                pady=(0, 6)
            )

            fields[name] = entry

        def register():
            full_name = fields["Full Name"].get().strip()
            username = fields["Username"].get().strip()
            password = fields["Password"].get()
            confirm = fields["Confirm Password"].get()
            contact = fields["Contact Number"].get().strip()

            if not all([
                full_name,
                username,
                password,
                confirm,
                contact
            ]):
                messagebox.showwarning(
                    "Incomplete Registration",
                    "Please fill in all fields."
                )
                return

            if username in self.users:
                messagebox.showerror(
                    "Registration Failed",
                    "Username already exists. Please choose another username."
                )
                return

            if password != confirm:
                messagebox.showerror(
                    "Registration Failed",
                    "Password and Confirm Password do not match."
                )
                return

            self.users[username] = {
                "password": password,
                "full_name": full_name,
                "contact": contact
            }

            self.current_user = {
                "username": username,
                **self.users[username]
            }

            messagebox.showinfo(
                "Registration Successful",
                "Account created successfully!"
            )

            self.reset_reservation_selection()
            self.show_dashboard()

        self.button(
            form,
            "CREATE ACCOUNT",
            register,
            width=25
        ).pack(pady=(15, 8))

        self.button(
            form,
            "← BACK TO LOGIN",
            self.show_access_page,
            width=25,
            primary=False
        ).pack(pady=(0, 20))


    def show_dashboard(self):
        self.clear_page()

        self.create_header(
            "Customer Dashboard",
            f"Welcome, {self.current_user['full_name']}!"
        )

        main = tk.Frame(self, bg="#08111f")
        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=10
        )

        info = self.card(main)
        info.pack(fill="x", pady=(0, 12))

        tk.Label(
            info,
            text=f"Customer: {self.current_user['full_name']}",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg="#101d2d"
        ).pack(side="left", padx=20, pady=15)

        tk.Label(
            info,
            text=f"Vehicle: {self.selected_vehicle}",
            font=("Segoe UI", 11, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(side="left", padx=20)

        tk.Label(
            info,
            text=f"Contact: {self.current_user['contact']}",
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(side="right", padx=20)

        grid = tk.Frame(main, bg="#08111f")
        grid.pack(fill="both", expand=True)

        reservation_card = self.card(grid)
        reservation_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8),
            pady=5
        )

        tk.Label(
            reservation_card,
            text="CREATE RESERVATION",
            font=("Segoe UI", 16, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 8))

        tk.Label(
            reservation_card,
            text="Select a service, date, time, and available bay.",
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(pady=5)

        self.button(
            reservation_card,
            "BOOK RESERVATION",
            self.show_reservation_page,
            width=25
        ).pack(pady=25)

        services_card = self.card(grid)
        services_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8,
            pady=5
        )

        tk.Label(
            services_card,
            text="CARWASH SERVICES",
            font=("Segoe UI", 16, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 12))

        for service in self.services:
            tk.Label(
                services_card,
                text="• " + service,
                font=("Segoe UI", 10),
                fg="white",
                bg="#101d2d"
            ).pack(anchor="w", padx=35, pady=4)

        current_card = self.card(grid)
        current_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(8, 0),
            pady=5
        )

        tk.Label(
            current_card,
            text="CURRENT RESERVATIONS",
            font=("Segoe UI", 16, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 12))

        user_reservations = [
            r for r in self.reservations
            if r["username"] == self.current_user["username"]
        ]

        if not user_reservations:
            tk.Label(
                current_card,
                text="No reservation yet.",
                font=("Segoe UI", 10),
                fg="#8ea6bd",
                bg="#101d2d"
            ).pack(pady=20)
        else:
            
            for r in reversed(user_reservations[-3:]):
                tk.Label(
                    current_card,
                    text=(
                        f"{r['reservation_id']} • "
                        f"{r['date']} • {r['time']}"
                    ),
                    font=("Segoe UI", 9),
                    fg="white",
                    bg="#101d2d"
                ).pack(anchor="w", padx=20, pady=4)

            self.button(
                current_card,
                "VIEW ALL RESERVATIONS",
                self.view_reservation,
                width=22,
                primary=False
            ).pack(pady=15)

        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(2, weight=1)
        grid.rowconfigure(0, weight=1)

        bottom = tk.Frame(main, bg="#08111f")
        bottom.pack(fill="x", pady=10)

        self.button(
            bottom,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False
        ).pack(side="right", padx=5)


    def show_reservation_page(self):
        self.clear_page()

        header = tk.Frame(
            self,
            bg="#08111f",
            height=70
        )
        header.pack(
            fill="x",
            padx=35,
            pady=(20, 5)
        )
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Book Reservation",
            font=("Segoe UI", 24, "bold"),
            fg="white",
            bg="#08111f"
        ).pack(anchor="w")

        top_nav = tk.Frame(
            self,
            bg="#08111f"
        )
        top_nav.pack(
            fill="x",
            padx=35,
            pady=(0, 8)
        )

        self.button(
            top_nav,
            "← DASHBOARD",
            self.show_dashboard,
            width=18,
            primary=False
        ).pack(side="left")

        main = tk.Frame(
            self,
            bg="#08111f"
        )
        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )

        left = self.card(main)
        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        right = self.card(main)
        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

    
        tk.Label(
            left,
            text="1. VEHICLE",
            font=("Segoe UI", 13, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        
        self.vehicle_var = tk.StringVar(value=self.selected_vehicle)

        vehicle_combo = ttk.Combobox(
            left,
            textvariable=self.vehicle_var,
            values=self.vehicle_types,
            state="readonly",
            font=("Segoe UI", 10),
            style="Black.TCombobox"
        )
        vehicle_combo.pack(
            fill="x",
            padx=25,
            pady=5
        )
        vehicle_combo.bind(
            "<<ComboboxSelected>>",
            self.update_vehicle_selection
        )

        
        tk.Label(
            left,
            text="2. SELECT SERVICE",
            font=("Segoe UI", 13, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        self.service_var = tk.StringVar(
            value=self.selected_service
        )

        service_combo = ttk.Combobox(
            left,
            textvariable=self.service_var,
            values=self.services,
            state="readonly",
            font=("Segoe UI", 10),
            style="Black.TCombobox"
        )
        service_combo.pack(
            fill="x",
            padx=25,
            pady=5
        )
        service_combo.bind(
            "<<ComboboxSelected>>",
            self.update_price
        )

        self.price_label = tk.Label(
            left,
            text="Price: --",
            font=("Segoe UI", 15, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        )
        self.price_label.pack(
            anchor="w",
            padx=25,
            pady=15
        )

     
        tk.Label(
            left,
            text="3. RESERVATION DATE",
            font=("Segoe UI", 13, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(10, 5)
        )

        self.date_entry = tk.Entry(
            left,
            font=("Segoe UI", 11),
            bg="#eaedf1",
            fg="black",
            insertbackground="black",
            relief="flat"
        )
        self.date_entry.pack(
            fill="x",
            padx=25,
            ipady=8,
            pady=5
        )

        if self.selected_date:
            self.date_entry.insert(
                0,
                self.selected_date
            )

        self.date_entry.bind(
            "<KeyRelease>",
            lambda event: (
                self.update_bay_buttons(),
                self.update_price()
            )
        )

        tk.Label(
            left,
            text="Format: MM/DD/YYYY  (example: 09/15/2026)",
            font=("Segoe UI", 9),
            fg="#7f96aa",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25
        )

      
        tk.Label(
            left,
            text="4. RESERVATION TIME",
            font=("Segoe UI", 13, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(18, 5)
        )

        time_values = [
            "7:00 AM",
            "8:00 AM",
            "9:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "1:00 PM",
            "2:00 PM",
            "3:00 PM",
            "4:00 PM",
            "5:00 PM",
            "6:00 PM"
        ]

        self.time_var = tk.StringVar(
            value=self.selected_time
        )
        self.time_buttons = {}

        time_grid = tk.Frame(
            left,
            bg="#101d2d"
        )
        time_grid.pack(
            fill="x",
            padx=25,
            pady=5
        )

        for i, time_value in enumerate(time_values):
            btn = tk.Button(
                time_grid,
                text=time_value,
                command=lambda t=time_value: self.select_time(t),
                font=("Segoe UI", 10, "bold"),
                fg="white",
                bg="#173247",
                activebackground="#29d9ff",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                padx=8,
                pady=9
            )
            btn.grid(
                row=i // 4,
                column=i % 4,
                padx=4,
                pady=4,
                sticky="ew"
            )
            self.time_buttons[time_value] = btn

        for col in range(4):
            time_grid.columnconfigure(col, weight=1)

        
        tk.Label(
            right,
            text="5. SELECT CARWASH BAY",
            font=("Segoe UI", 15, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        tk.Label(
            right,
            text="Choose one available bay.",
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        self.bay_var = tk.StringVar(
            value=self.selected_bay
        )
        self.bay_buttons = {}

        bay_grid = tk.Frame(
            right,
            bg="#101d2d"
        )
        bay_grid.pack(
            fill="x",
            padx=20
        )

        for i, bay in enumerate(self.bays):
            btn = tk.Button(
                bay_grid,
                text=bay + "\nAvailable",
                command=lambda b=bay: self.select_bay(b),
                font=("Segoe UI", 11, "bold"),
                fg="white",
                bg="#173247",
                activebackground="#29d9ff",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                width=12,
                height=3
            )
            btn.grid(
                row=i // 2,
                column=i % 2,
                padx=8,
                pady=8,
                sticky="ew"
            )
            self.bay_buttons[bay] = btn

        bay_grid.columnconfigure(0, weight=1)
        bay_grid.columnconfigure(1, weight=1)

        preview = tk.Frame(
            right,
            bg="#0b1624",
            highlightbackground="#263c54",
            highlightthickness=1
        )
        preview.pack(
            fill="x",
            padx=25,
            pady=20
        )

        tk.Label(
            preview,
            text="RESERVATION PREVIEW",
            font=("Segoe UI", 12, "bold"),
            fg="#29d9ff",
            bg="#0b1624"
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 8)
        )

        self.preview_label = tk.Label(
            preview,
            text="Select a service, date, time, and bay.",
            font=("Segoe UI", 9),
            fg="#b7c7d5",
            bg="#0b1624",
            justify="left"
        )
        self.preview_label.pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

        bottom = tk.Frame(
            self,
            bg="#08111f"
        )
        bottom.pack(
            fill="x",
            padx=35,
            pady=(0, 15)
        )

        self.button(
            bottom,
            "CONTINUE TO SUMMARY →",
            self.validate_reservation,
            width=24
        ).pack(side="right")

        self.update_bay_buttons()
        self.update_price()

    def update_vehicle_selection(self, event=None):
        """Update the vehicle selected for the current reservation."""
        vehicle = self.vehicle_var.get().strip()
        if vehicle:
            self.selected_vehicle = vehicle
            self.update_price()
            self.update_bay_buttons()

    def update_price(self, event=None):
        service = self.service_var.get()

        if service and self.selected_vehicle:
            price = self.prices[
                service
            ][
                self.selected_vehicle
            ]

            self.price_label.config(
                text=f"Price: ₱{price:,.2f}"
            )

            date = self.date_entry.get().strip()
            time = self.time_var.get()
            bay = self.bay_var.get()

            preview_text = (
                f"Vehicle: {self.selected_vehicle}\n"
                f"Service: {service}\n"
                f"Date: {date if date else '--'}\n"
                f"Time: {time if time else '--'}\n"
                f"Bay: {bay if bay else '--'}\n"
                f"Total: ₱{price:,.2f}"
            )

            self.preview_label.config(
                text=preview_text
            )
        else:
            self.price_label.config(
                text="Price: --"
            )

    def select_time(self, time_value):
        self.time_var.set(time_value)
        self.selected_time = time_value

        for value, btn in self.time_buttons.items():
            btn.config(
                bg="#119bc1"
                if value == time_value
                else "#173247"
            )

        self.update_bay_buttons()
        self.update_price()

    def select_bay(self, bay):
        self.bay_var.set(bay)
        self.selected_bay = bay

        self.update_bay_buttons()
        self.update_price()


    def is_bay_available(self, bay, date, time):
        for reservation in self.reservations:
            if (
                reservation["bay"] == bay
                and reservation["date"] == date
                and reservation["time"] == time
            ):
                return False

        return True

    def update_bay_buttons(self):
        if not hasattr(self, "bay_buttons"):
            return

        date = (
            self.date_entry.get().strip()
            if hasattr(self, "date_entry")
            else ""
        )

        time = (
            self.time_var.get()
            if hasattr(self, "time_var")
            else ""
        )

        for bay, btn in self.bay_buttons.items():
            available = True

            if date and time:
                available = self.is_bay_available(
                    bay,
                    date,
                    time
                )

            if not available:
                btn.config(
                    text=bay + "\nRESERVED",
                    bg="#5b2630",
                    fg="#ffb8c1",
                    state="disabled"
                )
            else:
                selected = (
                    self.bay_var.get() == bay
                )

                btn.config(
                    text=(
                        bay +
                        ("\nSELECTED" if selected else "\nAvailable")
                    ),
                    bg=(
                        "#119bc1"
                        if selected
                        else "#173247"
                    ),
                    fg="white",
                    state="normal"
                )

    def validate_reservation(self):
        service = self.service_var.get().strip()
        date = self.date_entry.get().strip()
        time = self.time_var.get().strip()
        bay = self.bay_var.get().strip()

        if not service:
            messagebox.showwarning(
                "Missing Service",
                "Please select a carwash service."
            )
            return

        if not date:
            messagebox.showwarning(
                "Missing Date",
                "Please enter a reservation date."
            )
            return

        
        try:
            selected_date = datetime.strptime(
                date,
                "%m/%d/%Y"
            ).date()

            if selected_date < datetime.now().date():
                messagebox.showwarning(
                    "Invalid Date",
                    "The reservation date cannot be in the past."
                )
                return

        except ValueError:
            messagebox.showwarning(
                "Invalid Date",
                "Please use the format MM/DD/YYYY."
            )
            return

        if not time:
            messagebox.showwarning(
                "Missing Time",
                "Please select a reservation time."
            )
            return

        if not bay:
            messagebox.showwarning(
                "Missing Bay",
                "Please select a carwash bay."
            )
            return

        if not self.is_bay_available(
            bay,
            date,
            time
        ):
            messagebox.showerror(
                "Bay Unavailable",
                (
                    f"{bay} is already reserved for "
                    f"{date} at {time}.\n"
                    "Please choose another bay or time."
                )
            )
            self.update_bay_buttons()
            return

        self.selected_service = service
        self.selected_date = date
        self.selected_time = time
        self.selected_bay = bay

        self.show_confirmation()


    def show_confirmation(self):
        self.clear_page()

        self.create_header(
            "Reservation Confirmation",
            "Review your reservation before final confirmation."
        )

        main = tk.Frame(
            self,
            bg="#08111f"
        )
        main.pack(
            fill="both",
            expand=True,
            padx=150,
            pady=15
        )

        summary = self.card(main)
        summary.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=10
        )

        tk.Label(
            summary,
            text="RESERVATION SUMMARY",
            font=("Segoe UI", 22, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(
            pady=(30, 25)
        )

        price = self.prices[
            self.selected_service
        ][
            self.selected_vehicle
        ]

        details = [
            ("Customer Name", self.current_user["full_name"]),
            ("Contact Number", self.current_user["contact"]),
            ("Vehicle", self.selected_vehicle),
            ("Service", self.selected_service),
            ("Date", self.selected_date),
            ("Time", self.selected_time),
            ("Bay", self.selected_bay),
            ("Total Price", f"₱{price:,.2f}")
        ]

        detail_frame = tk.Frame(
            summary,
            bg="#101d2d"
        )
        detail_frame.pack(
            fill="x",
            padx=80
        )

        for label_text, value in details:
            row = tk.Frame(
                detail_frame,
                bg="#101d2d"
            )
            row.pack(
                fill="x",
                pady=6
            )

            tk.Label(
                row,
                text=label_text + ":",
                font=("Segoe UI", 11, "bold"),
                fg="#8ea6bd",
                bg="#101d2d",
                width=20,
                anchor="w"
            ).pack(side="left")

            tk.Label(
                row,
                text=value,
                font=("Segoe UI", 11, "bold"),
                fg="white",
                bg="#101d2d",
                anchor="w"
            ).pack(side="left")

        tk.Label(
            summary,
            text=(
                "Please make sure all details are correct "
                "before confirming."
            ),
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(pady=25)

        buttons = tk.Frame(
            summary,
            bg="#101d2d"
        )
        buttons.pack(pady=20)

        self.button(
            buttons,
            "EDIT RESERVATION",
            self.show_reservation_page,
            width=22,
            primary=False
        ).pack(
            side="left",
            padx=8
        )

        self.button(
            buttons,
            "CONFIRM RESERVATION",
            self.confirm_reservation,
            width=24
        ).pack(
            side="left",
            padx=8
        )


    def confirm_reservation(self):
        
        if not self.is_bay_available(
            self.selected_bay,
            self.selected_date,
            self.selected_time
        ):
            messagebox.showerror(
                "Bay No Longer Available",
                (
                    "The selected bay was reserved by another customer.\n"
                    "Please edit your reservation and choose another bay/time."
                )
            )
            self.show_reservation_page()
            return

        reservation_id = (
            f"RES-{self.reservation_counter:04d}"
        )
        self.reservation_counter += 1

        price = self.prices[
            self.selected_service
        ][
            self.selected_vehicle
        ]

        reservation = {
            "reservation_id": reservation_id,
            "username": self.current_user["username"],
            "customer": self.current_user["full_name"],
            "contact": self.current_user["contact"],
            "vehicle": self.selected_vehicle,
            "service": self.selected_service,
            "date": self.selected_date,
            "time": self.selected_time,
            "bay": self.selected_bay,
            "total": price
        }

        self.reservations.append(reservation)

        self.show_success(reservation)


    def show_success(self, reservation):
        self.clear_page()

        self.create_header(
            "Reservation Successful",
            "Your carwash reservation has been confirmed."
        )

        main = tk.Frame(
            self,
            bg="#08111f"
        )
        main.pack(
            fill="both",
            expand=True,
            padx=150,
            pady=15
        )

        success = self.card(main)
        success.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=10
        )

        tk.Label(
            success,
            text="✓",
            font=("Segoe UI", 55, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=(25, 0))

        tk.Label(
            success,
            text="RESERVATION CONFIRMED!",
            font=("Segoe UI", 23, "bold"),
            fg="white",
            bg="#101d2d"
        ).pack(pady=5)

        tk.Label(
            success,
            text=f"Reservation ID: {reservation['reservation_id']}",
            font=("Segoe UI", 14, "bold"),
            fg="#29d9ff",
            bg="#101d2d"
        ).pack(pady=15)

        details = (
            f"Customer: {reservation['customer']}\n"
            f"Vehicle: {reservation['vehicle']}\n"
            f"Service: {reservation['service']}\n"
            f"Date: {reservation['date']}\n"
            f"Time: {reservation['time']}\n"
            f"Bay: {reservation['bay']}\n"
            f"Total: ₱{reservation['total']:,.2f}"
        )

        tk.Label(
            success,
            text=details,
            font=("Segoe UI", 11),
            fg="#d9e6ef",
            bg="#101d2d",
            justify="left"
        ).pack(pady=10)

        tk.Label(
            success,
            text="Your reservation has been successfully confirmed.",
            font=("Segoe UI", 10),
            fg="#9bb0c2",
            bg="#101d2d"
        ).pack(pady=10)

        buttons = tk.Frame(
            success,
            bg="#101d2d"
        )
        buttons.pack(pady=20)

        self.button(
            buttons,
            "VIEW ALL RESERVATIONS",
            self.view_reservation,
            width=22
        ).pack(
            side="left",
            padx=5
        )

        self.button(
            buttons,
            "MAKE ANOTHER",
            self.make_another_reservation,
            width=20,
            primary=False
        ).pack(
            side="left",
            padx=5
        )

        self.button(
            buttons,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False
        ).pack(
            side="left",
            padx=5
        )


    def view_reservation(self):
        
        user_reservations = [
            r for r in self.reservations
            if r["username"] == self.current_user["username"]
        ]

        if not user_reservations:
            messagebox.showinfo(
                "No Reservation",
                "You do not have any confirmed reservations yet."
            )
            return

        self.clear_page()

        self.create_header(
            "My Reservations",
            f"All reservations for {self.current_user['full_name']}"
        )

        main = tk.Frame(
            self,
            bg="#08111f"
        )
        main.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=10
        )

        tk.Label(
            main,
            text=f"TOTAL RESERVATIONS: {len(user_reservations)}",
            font=("Segoe UI", 16, "bold"),
            fg="#29d9ff",
            bg="#08111f"
        ).pack(
            anchor="w",
            pady=(5, 10)
        )

        
        container = tk.Frame(
            main,
            bg="#08111f"
        )
        container.pack(
            fill="both",
            expand=True
        )

        canvas = tk.Canvas(
            container,
            bg="#08111f",
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tk.Frame(
            canvas,
            bg="#08111f"
        )

        scroll_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=scroll_frame,
            anchor="nw"
        )

        def resize_scroll_frame(event):
            canvas.itemconfig(
                canvas_window,
                width=event.width
            )

        canvas.bind(
            "<Configure>",
            resize_scroll_frame
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        
        for reservation in reversed(user_reservations):

            reservation_card = self.card(
                scroll_frame
            )

            reservation_card.pack(
                fill="x",
                padx=10,
                pady=8
            )

            
            tk.Label(
                reservation_card,
                text=reservation["reservation_id"],
                font=("Segoe UI", 18, "bold"),
                fg="#29d9ff",
                bg="#101d2d"
            ).pack(
                anchor="w",
                padx=25,
                pady=(18, 10)
            )

            details = [
                ("Customer", reservation["customer"]),
                ("Contact", reservation["contact"]),
                ("Vehicle", reservation["vehicle"]),
                ("Service", reservation["service"]),
                ("Date", reservation["date"]),
                ("Time", reservation["time"]),
                ("Bay", reservation["bay"]),
                (
                    "Total",
                    f"₱{reservation['total']:,.2f}"
                )
            ]

            details_frame = tk.Frame(
                reservation_card,
                bg="#101d2d"
            )

            details_frame.pack(
                fill="x",
                padx=25,
                pady=5
            )

            for label_text, value in details:

                row = tk.Frame(
                    details_frame,
                    bg="#101d2d"
                )

                row.pack(
                    fill="x",
                    pady=3
                )

                tk.Label(
                    row,
                    text=label_text + ":",
                    font=("Segoe UI", 10, "bold"),
                    fg="#8ea6bd",
                    bg="#101d2d",
                    width=18,
                    anchor="w"
                ).pack(
                    side="left"
                )

                tk.Label(
                    row,
                    text=value,
                    font=("Segoe UI", 10, "bold"),
                    fg="white",
                    bg="#101d2d",
                    anchor="w"
                ).pack(
                    side="left"
                )

            tk.Label(
                reservation_card,
                text="✓ CONFIRMED",
                font=("Segoe UI", 9, "bold"),
                fg="#29d9ff",
                bg="#101d2d"
            ).pack(
                anchor="w",
                padx=25,
                pady=(8, 18)
            )

        
        bottom = tk.Frame(
            self,
            bg="#08111f"
        )
        bottom.pack(
            fill="x",
            padx=50,
            pady=(5, 15)
        )

        self.button(
            bottom,
            "MAKE ANOTHER RESERVATION",
            self.make_another_reservation,
            width=25
        ).pack(
            side="left",
            padx=5
        )

        self.button(
            bottom,
            "BACK TO DASHBOARD",
            self.show_dashboard,
            width=20,
            primary=False
        ).pack(
            side="left",
            padx=5
        )

        self.button(
            bottom,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False
        ).pack(
            side="right",
            padx=5
        )


    def make_another_reservation(self):
        self.selected_service = ""
        self.selected_date = ""
        self.selected_time = ""
        self.selected_bay = ""

        self.show_reservation_page()

    def reset_reservation_selection(self):
        self.selected_service = ""
        self.selected_date = ""
        self.selected_time = ""
        self.selected_bay = ""


    def logout(self):
        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:
            self.current_user = None
            self.selected_vehicle = ""
            self.reset_reservation_selection()
            self.show_vehicle_selection()


if __name__ == "__main__":
    app = CarwashApp()
    app.mainloop()
