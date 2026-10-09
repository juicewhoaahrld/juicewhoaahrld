# Final_WashApp_Github

Python Tkinter carwash reservation system prepared for GitHub and project defense.

## Run

```bash
python main.py
```

Demo account: `demo`  
Password: `demo123`

## Files

- `main.py`: application entry point.
- `frontend.py`: Tkinter screens and user interactions.
- `backend.py`: reusable date validation, price calculation, bay availability, and reservation filtering functions.
- `config.py`: application constants, vehicle types, services, bays, time slots, and colors.
- `ui/buttons.py`: reusable button component.
- `ui/frames.py`: reusable frame and card components.
- `ui/inputs.py`: entry fields, password fields, comboboxes, and variables.
- `ui/labels.py`: reusable labels and titles.
- `ui/textgrid.py`: grid layout helpers.
- `ui/text.py`: text label helpers.
- `ui/window.py` and `ui/center_window.py`: window creation and centering helpers.

The system uses no database. Data stored in the main application is temporary and is lost when the program closes.
