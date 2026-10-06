\
\
\
\
\
   

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from backend import Backend
from config import (
    APP_TITLE,
    TAGLINE,
    BG_MAIN,
    BG_CARD,
    TEXT_CYAN,
    TEXT_MUTED,
    VEHICLE_TYPES,
    SERVICES,
    BAYS,
    TIME_SLOTS,
)
from ui.window import Window
from ui.frames import (
    main_frame,
    card,
    header_frame,
    button_bar,
    row_frame,
)
from ui.buttons import button, selection_button
from ui.labels import (
    label,
    title,
    cyan_title,
    muted,
    header_brand,
)
from ui.inputs import entry, password_entry, combobox, text_variable
from ui.text import multiline_text
from ui.textgrid import create_grid, add_to_grid, grid_index


class Frontend:
    def __init__(self):
        self.window = Window()
        self.root = self.window.root
        self.backend = Backend()

        self.current_user = None
        self.selected_vehicle = ""
        self.selected_service = ""
        self.selected_date = ""
        self.selected_time = ""
        self.selected_bay = ""

        self.service_var = text_variable()
        self.time_var = text_variable()
        self.bay_var = text_variable()

        self.time_buttons = {}
        self.bay_buttons = {}

        self.setup_styles()
        self.show_vehicle_selection()
        self.window.center()

                                                              
                         
                                                              

    def setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground="#111d2e",
            background="#111d2e",
            foreground="white",
            arrowcolor=TEXT_CYAN,
            bordercolor="#2c4057",
            padding=8,
        )

    def clear(self):
        self.window.clear()

    def header(self, page_title, subtitle=""):
        frame = header_frame(self.root)

        frame.pack(
            fill="x",
            padx=35,
            pady=(20, 8),
        )

        header_brand(frame).pack(anchor="w")

        label(
            frame,
            page_title,
            size=18,
            bold=True,
            bg=BG_MAIN,
        ).pack(anchor="w")

        if subtitle:
            label(
                frame,
                subtitle,
                size=8,
                color="#d9f7ff",
                bg=BG_MAIN,
            ).pack(anchor="w")

    def reset_reservation(self):
        self.selected_service = ""
        self.selected_date = ""
        self.selected_time = ""
        self.selected_bay = ""

        self.service_var.set("")
        self.time_var.set("")
        self.bay_var.set("")

                                                              
                       
                                                              

    def show_vehicle_selection(self):
        self.clear()

        self.header(
            APP_TITLE,
            TAGLINE,
        )

        container = main_frame(self.root)
        container.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=15,
        )

        title(
            container,
            "SELECT YOUR VEHICLE",
            22,
        ).pack(pady=(20, 5))

        label(
            container,
            "Choose your vehicle type to continue.",
            color=TEXT_MUTED,
            bg=BG_MAIN,
        ).pack(pady=(0, 25))

        grid = main_frame(container)
        grid.pack()

        icons = {
            "Sedan": "🚗",
            "SUV": "🚙",
            "Van": "🚐",
            "Pick-up": "🛻",
            "Motorcycle": "🏍",
        }

        for i, vehicle in enumerate(VEHICLE_TYPES):
            vehicle_card = card(grid)
            vehicle_card.grid(
                row=0,
                column=i,
                padx=8,
                pady=10,
                ipadx=8,
                ipady=8,
            )

            label(
                vehicle_card,
                icons.get(vehicle, "🚗"),
                size=34,
                color=TEXT_CYAN,
            ).pack(padx=20, pady=(15, 5))

            label(
                vehicle_card,
                vehicle,
                size=12,
                bold=True,
            ).pack(pady=5)

            button(
                vehicle_card,
                "SELECT",
                lambda v=vehicle: self.select_vehicle(v),
                width=12,
            ).pack(padx=20, pady=(5, 15))

        info = card(container)
        info.pack(
            pady=35,
            padx=100,
            fill="x",
        )

        label(
            info,
            "Choose your vehicle first. Your selection will be remembered throughout the reservation process.",
            size=10,
            color="#a8bdd0",
        ).pack(pady=14)

    def select_vehicle(self, vehicle):
        self.selected_vehicle = vehicle
        self.show_access_page()

                                                              
                    
                                                              

    def show_access_page(self):
        self.clear()

        self.header(
            "Customer Access",
            f"Selected Vehicle: {self.selected_vehicle}",
        )

        container = main_frame(self.root)
        container.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=15,
        )

        login_card = card(container)
        login_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10),
            pady=10,
        )

        cyan_title(login_card, "LOGIN", 18).pack(pady=(25, 20))

        label(login_card, "Username").pack(
            anchor="w",
            padx=35,
        )

        username = entry(login_card)
        username.pack(
            fill="x",
            padx=35,
            pady=(5, 15),
            ipady=8,
        )

        label(login_card, "Password").pack(
            anchor="w",
            padx=35,
        )

        password = password_entry(login_card)
        password.pack(
            fill="x",
            padx=35,
            pady=(5, 20),
            ipady=8,
        )

        button(
            login_card,
            "LOGIN",
            lambda: self.login_user(
                username.get(),
                password.get(),
            ),
            width=20,
        ).pack(pady=10)

        register_card = card(container)
        register_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10,
        )

        cyan_title(register_card, "NEW CUSTOMER?", 18).pack(
            pady=(25, 10),
        )

        muted(
            register_card,
            "Create an account!",
        ).pack(pady=(0, 20))

        button(
            register_card,
            "SIGN UP / REGISTER",
            self.show_registration,
            width=22,
        ).pack(pady=30)

        label(
            register_card,
            "OR",
            bold=True,
            color="#71869a",
        ).pack(pady=10)

        button(
            register_card,
            "USE DEMO ACCOUNT",
            self.demo_login,
            width=22,
            primary=False,
        ).pack(pady=10)

        label(
            register_card,
            "Demo Account: demo / demo123",
            size=9,
            color="#8ea6bd",
        ).pack(pady=10)

        button(
            container,
            "← CHANGE VEHICLE",
            self.show_vehicle_selection,
            width=20,
            primary=False,
        ).pack(
            side="bottom",
            pady=15,
        )

    def login_user(self, username, password):
        success, message, user = self.backend.authenticate(
            username,
            password,
        )

        if not success:
            messagebox.showerror("Login Failed", message)
            return

        self.current_user = user
        self.reset_reservation()
        self.show_dashboard()

    def demo_login(self):
        self.current_user = self.backend.get_demo_user()
        self.reset_reservation()
        self.show_dashboard()

                                                              
                  
                                                              

    def show_registration(self):
        self.clear()

        self.header(
            "Customer Registration",
            f"Selected Vehicle: {self.selected_vehicle}",
        )

        container = main_frame(self.root)
        container.pack(
            fill="both",
            expand=True,
        )

        form = card(
            container,
            width=560,
            height=570,
        )
        form.pack(pady=10)

        cyan_title(form, "CREATE ACCOUNT", 19).pack(
            pady=(25, 20),
        )

        fields = {}

        definitions = [
            ("Full Name", False),
            ("Username", False),
            ("Password", True),
            ("Confirm Password", True),
            ("Contact Number", False),
        ]

        for field_name, secret in definitions:
            label(
                form,
                field_name,
            ).pack(
                anchor="w",
                padx=45,
                pady=(6, 3),
            )

            widget = password_entry(form) if secret else entry(form)

            widget.pack(
                fill="x",
                padx=45,
                ipady=7,
                pady=(0, 6),
            )

            fields[field_name] = widget

        def register():
            full_name = fields["Full Name"].get()
            username = fields["Username"].get()
            password = fields["Password"].get()
            confirm = fields["Confirm Password"].get()
            contact = fields["Contact Number"].get()

            if password != confirm:
                messagebox.showerror(
                    "Registration Failed",
                    "Password and Confirm Password do not match.",
                )
                return

            success, message = self.backend.register_user(
                full_name,
                username,
                password,
                contact,
            )

            if not success:
                messagebox.showerror(
                    "Registration Failed",
                    message,
                )
                return

            self.current_user = {
                "username": username.strip(),
                "full_name": full_name.strip(),
                "contact": contact.strip(),
            }

            messagebox.showinfo(
                "Registration Successful",
                message,
            )

            self.reset_reservation()
            self.show_dashboard()

        button(
            form,
            "CREATE ACCOUNT",
            register,
            width=25,
        ).pack(pady=(15, 8))

        button(
            form,
            "← BACK TO LOGIN",
            self.show_access_page,
            width=25,
            primary=False,
        ).pack(pady=(0, 20))

                                                              
               
                                                              

    def show_dashboard(self):
        self.clear()

        self.header(
            "Customer Dashboard",
            f"Welcome, {self.current_user['full_name']}!",
        )

        main = main_frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=10,
        )

        info = card(main)
        info.pack(
            fill="x",
            pady=(0, 12),
        )

        label(
            info,
            f"Customer: {self.current_user['full_name']}",
            size=11,
            bold=True,
        ).pack(
            side="left",
            padx=20,
            pady=15,
        )

        label(
            info,
            f"Vehicle: {self.selected_vehicle}",
            size=11,
            bold=True,
            color=TEXT_CYAN,
        ).pack(
            side="left",
            padx=20,
        )

        label(
            info,
            f"Contact: {self.current_user['contact']}",
            size=10,
            color=TEXT_MUTED,
        ).pack(
            side="right",
            padx=20,
        )

        grid = main_frame(main)
        grid.pack(
            fill="both",
            expand=True,
        )

        reservation_card = card(grid)
        reservation_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8),
            pady=5,
        )

        cyan_title(
            reservation_card,
            "CREATE RESERVATION",
        ).pack(pady=(25, 8))

        muted(
            reservation_card,
            "Select a service, date, time, and available bay.",
        ).pack(pady=5)

        button(
            reservation_card,
            "BOOK RESERVATION",
            self.show_reservation_page,
            width=25,
        ).pack(pady=25)

        services_card = card(grid)
        services_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8,
            pady=5,
        )

        cyan_title(
            services_card,
            "CARWASH SERVICES",
        ).pack(pady=(25, 12))

        for service in SERVICES:
            label(
                services_card,
                "• " + service,
            ).pack(
                anchor="w",
                padx=35,
                pady=4,
            )

        current_card = card(grid)
        current_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(8, 0),
            pady=5,
        )

        cyan_title(
            current_card,
            "CURRENT RESERVATIONS",
        ).pack(pady=(25, 12))

        reservations = self.backend.get_user_reservations(
            self.current_user["username"]
        )

        if not reservations:
            muted(
                current_card,
                "No reservation yet.",
            ).pack(pady=20)
        else:
            for reservation in reversed(reservations[-3:]):
                label(
                    current_card,
                    (
                        f"{reservation['reservation_id']} • "
                        f"{reservation['date']} • "
                        f"{reservation['time']}"
                    ),
                    size=9,
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=4,
                )

            button(
                current_card,
                "VIEW ALL RESERVATIONS",
                self.view_reservations,
                width=22,
                primary=False,
            ).pack(pady=15)

        for column in range(3):
            grid.columnconfigure(column, weight=1)

        grid.rowconfigure(0, weight=1)

        bottom = button_bar(main)
        bottom.pack(
            fill="x",
            pady=10,
        )

        button(
            bottom,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False,
        ).pack(
            side="right",
            padx=5,
        )

                                                              
                      
                                                              

    def show_reservation_page(self):
        self.clear()

        self.header(
            "Book Reservation",
            "Select your service, date, time, and available bay.",
        )

        nav = button_bar(self.root)
        nav.pack(
            fill="x",
            padx=35,
            pady=(0, 8),
        )

        button(
            nav,
            "← DASHBOARD",
            self.show_dashboard,
            width=18,
            primary=False,
        ).pack(side="left")

        main = main_frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5,
        )

        left = card(main)
        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8),
        )

        right = card(main)
        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 0),
        )

                 
        cyan_title(left, "1. VEHICLE", 13).pack(
            anchor="w",
            padx=25,
            pady=(20, 5),
        )

        label(
            left,
            self.selected_vehicle,
            size=12,
            bold=True,
        ).pack(
            anchor="w",
            padx=25,
            pady=5,
        )

                 
        cyan_title(left, "2. SELECT SERVICE", 13).pack(
            anchor="w",
            padx=25,
            pady=(20, 5),
        )

        self.service_var.set(self.selected_service)

        service_combo = combobox(
            left,
            self.service_var,
            SERVICES,
        )
        service_combo.pack(
            fill="x",
            padx=25,
            pady=5,
        )
        service_combo.bind(
            "<<ComboboxSelected>>",
            self.update_price,
        )

        self.price_label = label(
            left,
            "Price: --",
            size=15,
            bold=True,
            color=TEXT_CYAN,
        )
        self.price_label.pack(
            anchor="w",
            padx=25,
            pady=15,
        )

              
        cyan_title(left, "3. RESERVATION DATE", 13).pack(
            anchor="w",
            padx=25,
            pady=(10, 5),
        )

        self.date_entry = entry(left)
        self.date_entry.pack(
            fill="x",
            padx=25,
            ipady=8,
            pady=5,
        )

        if self.selected_date:
            self.date_entry.insert(
                0,
                self.selected_date,
            )

        self.date_entry.bind(
            "<KeyRelease>",
            self.on_date_changed,
        )

        label(
            left,
            "Format: MM/DD/YYYY (example: 09/15/2026)",
            size=9,
            color="#7f96aa",
        ).pack(
            anchor="w",
            padx=25,
        )

              
        cyan_title(left, "4. RESERVATION TIME", 13).pack(
            anchor="w",
            padx=25,
            pady=(18, 5),
        )

        self.time_var.set(self.selected_time)
        self.time_buttons = {}

        time_grid = create_grid(left, columns=4)
        time_grid.pack(
            fill="x",
            padx=25,
            pady=5,
        )

        for index, time_value in enumerate(TIME_SLOTS):
            row, column = grid_index(index, 4)

            btn = selection_button(
                time_grid,
                time_value,
                lambda t=time_value: self.select_time(t),
            )

            add_to_grid(
                btn,
                row,
                column,
                sticky="ew",
            )

            self.time_buttons[time_value] = btn

                          
        cyan_title(
            right,
            "5. SELECT CARWASH BAY",
            15,
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5),
        )

        muted(
            right,
            "Choose one available bay.",
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15),
        )

        self.bay_var.set(self.selected_bay)
        self.bay_buttons = {}

        bay_grid = create_grid(right, columns=2)
        bay_grid.pack(
            fill="x",
            padx=20,
        )

        for index, bay in enumerate(BAYS):
            row, column = grid_index(index, 2)

            btn = tk.Button(
                bay_grid,
                text=bay + "\nAvailable",
                command=lambda b=bay: self.select_bay(b),
                font=("Segoe UI", 11, "bold"),
                fg="white",
                bg="#173247",
                activebackground=TEXT_CYAN,
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                width=12,
                height=3,
            )

            add_to_grid(
                btn,
                row,
                column,
                padx=8,
                pady=8,
                sticky="ew",
            )

            self.bay_buttons[bay] = btn

        preview = tk.Frame(
            right,
            bg="#0b1624",
            highlightbackground="#263c54",
            highlightthickness=1,
        )
        preview.pack(
            fill="x",
            padx=25,
            pady=20,
        )

        label(
            preview,
            "RESERVATION PREVIEW",
            size=12,
            bold=True,
            color=TEXT_CYAN,
            bg="#0b1624",
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 8),
        )

        self.preview_label = multiline_text(
            preview,
            "Select a service, date, time, and bay.",
            size=9,
            color="#b7c7d5",
            bg="#0b1624",
        )
        self.preview_label.pack(
            anchor="w",
            padx=15,
            pady=(0, 12),
        )

        bottom = button_bar(self.root)
        bottom.pack(
            fill="x",
            padx=35,
            pady=(0, 15),
        )

        button(
            bottom,
            "CONTINUE TO SUMMARY →",
            self.validate_reservation,
            width=24,
        ).pack(side="right")

        self.update_bay_buttons()
        self.update_price()

    def on_date_changed(self, event=None):
        self.update_bay_buttons()
        self.update_price()

    def update_price(self, event=None):
        service = self.service_var.get()

        if not service:
            self.price_label.config(text="Price: --")
            return

        price = self.backend.get_price(
            self.selected_vehicle,
            service,
        )

        if price is None:
            self.price_label.config(text="Price: --")
            return

        self.price_label.config(
            text=f"Price: ₱{price:,.2f}",
        )

        date = self.date_entry.get().strip()
        time = self.time_var.get()
        bay = self.bay_var.get()

        preview = (
            f"Vehicle: {self.selected_vehicle}\n"
            f"Service: {service}\n"
            f"Date: {date if date else '--'}\n"
            f"Time: {time if time else '--'}\n"
            f"Bay: {bay if bay else '--'}\n"
            f"Total: ₱{price:,.2f}"
        )

        self.preview_label.config(text=preview)

    def select_time(self, time_value):
        self.time_var.set(time_value)
        self.selected_time = time_value

        self.update_bay_buttons()
        self.update_price()

    def select_bay(self, bay):
        self.bay_var.set(bay)
        self.selected_bay = bay

        self.update_bay_buttons()
        self.update_price()

                                                              
                 
                                                              

    def update_bay_buttons(self):
        if not self.bay_buttons:
            return

        date = self.date_entry.get().strip()
        time = self.time_var.get()

        for bay, btn in self.bay_buttons.items():
            available = True

            if date and time:
                available = self.backend.is_bay_available(
                    bay,
                    date,
                    time,
                )

            if not available:
                btn.config(
                    text=bay + "\nRESERVED",
                    bg="#5b2630",
                    fg="#ffb8c1",
                    state="disabled",
                )
            else:
                selected = self.bay_var.get() == bay

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
                    state="normal",
                )

                                                              
                
                                                              

    def validate_reservation(self):
        service = self.service_var.get().strip()
        date = self.date_entry.get().strip()
        time = self.time_var.get().strip()
        bay = self.bay_var.get().strip()

        if not service:
            messagebox.showwarning(
                "Missing Service",
                "Please select a carwash service.",
            )
            return

        if not date:
            messagebox.showwarning(
                "Missing Date",
                "Please enter a reservation date.",
            )
            return

        valid, message = self.backend.validate_date(date)

        if not valid:
            messagebox.showwarning(
                "Invalid Date",
                message,
            )
            return

        if not time:
            messagebox.showwarning(
                "Missing Time",
                "Please select a reservation time.",
            )
            return

        if not bay:
            messagebox.showwarning(
                "Missing Bay",
                "Please select a carwash bay.",
            )
            return

        if not self.backend.is_bay_available(
            bay,
            date,
            time,
        ):
            messagebox.showerror(
                "Bay Unavailable",
                f"{bay} is already reserved for {date} at {time}.",
            )
            self.update_bay_buttons()
            return

        self.selected_service = service
        self.selected_date = date
        self.selected_time = time
        self.selected_bay = bay

        self.show_confirmation()

                                                              
                  
                                                              

    def show_confirmation(self):
        self.clear()

        self.header(
            "Reservation Confirmation",
            "Review your reservation before final confirmation.",
        )

        main = main_frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=150,
            pady=15,
        )

        summary = card(main)
        summary.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=10,
        )

        cyan_title(
            summary,
            "RESERVATION SUMMARY",
            22,
        ).pack(pady=(30, 25))

        price = self.backend.get_price(
            self.selected_vehicle,
            self.selected_service,
        )

        details = [
            ("Customer Name", self.current_user["full_name"]),
            ("Contact Number", self.current_user["contact"]),
            ("Vehicle", self.selected_vehicle),
            ("Service", self.selected_service),
            ("Date", self.selected_date),
            ("Time", self.selected_time),
            ("Bay", self.selected_bay),
            ("Total Price", f"₱{price:,.2f}"),
        ]

        detail_frame = row_frame(summary)
        detail_frame.pack(
            fill="x",
            padx=80,
        )

        for field_name, value in details:
            row = row_frame(detail_frame)
            row.pack(
                fill="x",
                pady=6,
            )

            label(
                row,
                field_name + ":",
                size=11,
                bold=True,
                color="#8ea6bd",
                width=20,
                anchor="w",
            ).pack(side="left")

            label(
                row,
                value,
                size=11,
                bold=True,
                bg=BG_CARD,
                anchor="w",
            ).pack(side="left")

        muted(
            summary,
            "Please make sure all details are correct before confirming.",
        ).pack(pady=25)

        buttons = row_frame(summary)
        buttons.pack(pady=20)

        button(
            buttons,
            "EDIT RESERVATION",
            self.show_reservation_page,
            width=22,
            primary=False,
        ).pack(
            side="left",
            padx=8,
        )

        button(
            buttons,
            "CONFIRM RESERVATION",
            self.confirm_reservation,
            width=24,
        ).pack(
            side="left",
            padx=8,
        )

    def confirm_reservation(self):
        success, message, reservation = self.backend.create_reservation(
            self.current_user,
            self.selected_vehicle,
            self.selected_service,
            self.selected_date,
            self.selected_time,
            self.selected_bay,
        )

        if not success:
            messagebox.showerror(
                "Reservation Failed",
                message,
            )
            self.show_reservation_page()
            return

        self.show_success(reservation)

                                                              
             
                                                              

    def show_success(self, reservation):
        self.clear()

        self.header(
            "Reservation Successful",
            "Your carwash reservation has been confirmed.",
        )

        main = main_frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=150,
            pady=15,
        )

        success = card(main)
        success.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=10,
        )

        label(
            success,
            "✓",
            size=55,
            bold=True,
            color=TEXT_CYAN,
        ).pack(pady=(25, 0))

        label(
            success,
            "RESERVATION CONFIRMED!",
            size=23,
            bold=True,
        ).pack(pady=5)

        label(
            success,
            f"Reservation ID: {reservation['reservation_id']}",
            size=14,
            bold=True,
            color=TEXT_CYAN,
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

        multiline_text(
            success,
            details,
            size=11,
        ).pack(pady=10)

        muted(
            success,
            "Your reservation has been successfully confirmed.",
        ).pack(pady=10)

        buttons = row_frame(success)
        buttons.pack(pady=20)

        button(
            buttons,
            "VIEW ALL RESERVATIONS",
            self.view_reservations,
            width=22,
        ).pack(side="left", padx=5)

        button(
            buttons,
            "MAKE ANOTHER",
            self.make_another_reservation,
            width=20,
            primary=False,
        ).pack(side="left", padx=5)

        button(
            buttons,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False,
        ).pack(side="left", padx=5)

                                                              
                           
                                                              

    def view_reservations(self):
        reservations = self.backend.get_user_reservations(
            self.current_user["username"]
        )

        if not reservations:
            messagebox.showinfo(
                "No Reservation",
                "You do not have any confirmed reservations yet.",
            )
            return

        self.clear()

        self.header(
            "My Reservations",
            f"All reservations for {self.current_user['full_name']}",
        )

        main = main_frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=10,
        )

        title(
            main,
            f"TOTAL RESERVATIONS: {len(reservations)}",
            16,
        ).pack(
            anchor="w",
            pady=(5, 10),
        )

        container = main_frame(main)
        container.pack(
            fill="both",
            expand=True,
        )

        canvas = tk.Canvas(
            container,
            bg=BG_MAIN,
            highlightthickness=0,
        )

        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview,
        )

        scroll_frame = main_frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all"),
            ),
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=scroll_frame,
            anchor="nw",
        )

        def resize_scroll_frame(event):
            canvas.itemconfig(
                canvas_window,
                width=event.width,
            )

        canvas.bind(
            "<Configure>",
            resize_scroll_frame,
        )

        canvas.configure(
            yscrollcommand=scrollbar.set,
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True,
        )

        scrollbar.pack(
            side="right",
            fill="y",
        )

        for reservation in reversed(reservations):
            reservation_card = card(scroll_frame)
            reservation_card.pack(
                fill="x",
                padx=10,
                pady=8,
            )

            label(
                reservation_card,
                reservation["reservation_id"],
                size=18,
                bold=True,
                color=TEXT_CYAN,
            ).pack(
                anchor="w",
                padx=25,
                pady=(18, 10),
            )

            details = [
                ("Customer", reservation["customer"]),
                ("Contact", reservation["contact"]),
                ("Vehicle", reservation["vehicle"]),
                ("Service", reservation["service"]),
                ("Date", reservation["date"]),
                ("Time", reservation["time"]),
                ("Bay", reservation["bay"]),
                ("Total", f"₱{reservation['total']:,.2f}"),
            ]

            details_frame = row_frame(reservation_card)
            details_frame.pack(
                fill="x",
                padx=25,
                pady=5,
            )

            for field_name, value in details:
                row = row_frame(details_frame)
                row.pack(
                    fill="x",
                    pady=3,
                )

                label(
                    row,
                    field_name + ":",
                    size=10,
                    bold=True,
                    color="#8ea6bd",
                    width=18,
                    anchor="w",
                ).pack(side="left")

                label(
                    row,
                    value,
                    size=10,
                    bold=True,
                    anchor="w",
                ).pack(side="left")

            label(
                reservation_card,
                "✓ CONFIRMED",
                size=9,
                bold=True,
                color=TEXT_CYAN,
            ).pack(
                anchor="w",
                padx=25,
                pady=(8, 18),
            )

        bottom = button_bar(self.root)
        bottom.pack(
            fill="x",
            padx=50,
            pady=(5, 15),
        )

        button(
            bottom,
            "MAKE ANOTHER RESERVATION",
            self.make_another_reservation,
            width=25,
        ).pack(
            side="left",
            padx=5,
        )

        button(
            bottom,
            "BACK TO DASHBOARD",
            self.show_dashboard,
            width=20,
            primary=False,
        ).pack(
            side="left",
            padx=5,
        )

        button(
            bottom,
            "LOGOUT",
            self.logout,
            width=15,
            primary=False,
        ).pack(
            side="right",
            padx=5,
        )

                                                              
                      
                                                              

    def make_another_reservation(self):
        self.reset_reservation()
        self.show_reservation_page()

    def logout(self):
        if not messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?",
        ):
            return

        self.current_user = None
        self.selected_vehicle = ""
        self.reset_reservation()
        self.show_vehicle_selection()

    def run(self):
        self.window.run()
