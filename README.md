# WASHAPP - Smart Carwash Reservation System

A beginner-friendly Python Tkinter carwash reservation system designed for a school project and GitHub defense.

## Features

- Vehicle selection
- Customer login
- Customer registration
- Demo account
- Customer dashboard
- Carwash service selection
- MM/DD/YYYY date format
- Time-slot selection
- Bay availability checking
- Reservation confirmation
- Automatic reservation IDs
- View all reservations for the logged-in customer
- Scrollable reservation history
- No database required

## Demo Account

Username:
`demo`

Password:
`demo123`

## Project Structure

```text
WASHAPP_GitHub_Project/
│
├── main.py
├── frontend.py
├── backend.py
├── config.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── ui/
    ├── __init__.py
    ├── buttons.py
    ├── frames.py
    ├── inputs.py
    ├── labels.py
    ├── text.py
    ├── textgrid.py
    └── window.py
```

## What each file does

### `main.py`
Starts the application.

### `frontend.py`
Contains the screens and connects the user interface to the backend.

Examples:
- Login screen
- Registration screen
- Dashboard
- Reservation form
- Confirmation page
- Reservation history

### `backend.py`
Contains the system's logic.

Examples:
- Login validation
- Registration
- Date validation
- Price calculation
- Bay availability
- Creating reservations
- Getting customer reservations

### `config.py`
Contains fixed system settings:
- colors
- vehicle types
- services
- prices
- bays
- time slots

### `ui/buttons.py`
Reusable button designs.

### `ui/frames.py`
Reusable Frame designs.

### `ui/inputs.py`
Reusable Entry, Password Entry, Combobox, and StringVar helpers.

### `ui/labels.py`
Reusable Label designs.

### `ui/text.py`
Reusable text/label helpers.

### `ui/textgrid.py`
Grid helpers used for time slots and bay selections.

### `ui/window.py`
Creates, centers, clears, and runs the main Tkinter window.

## How the system works

The basic flow is:

```text
main.py
   ↓
frontend.py
   ↓
backend.py
   ↓
reservation data
```

The frontend should handle what the user sees.

The backend should handle what the system does.

The reusable files inside `ui/` handle common GUI components.

## Run the program

Open the project folder in VS Code.

Run:

```bash
python main.py
```

No external Python packages are required because Tkinter is part of the standard Python installation on Windows.

## Important limitation

This version intentionally does NOT use a database.

Users and reservations are stored in memory while the program is running.

When the program closes, the temporary data is lost.

For a future version, a database such as SQLite or MySQL can be added to the backend.
