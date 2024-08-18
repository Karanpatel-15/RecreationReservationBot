# Reservation Automation Script

A Python script that automates booking an activity through a web-based reservation system using Selenium.

## Features

- Automatically refreshes the reservation page at a specified time.
- Continually checks and books a specific activity for a given date and time.
- Fills in personal details and confirms the reservation.

## Prerequisites

- Python 3.x
- Selenium (`pip install selenium`)
- Chrome WebDriver

## Setup

1. **Configure the script:**

   - Set `link`, `date`, `actTime`, `actName`, and `numberOfPeople` for your reservation.
   - Set your `number`, `email`, and `name` for the booking.

2. **Run the script:**
   - The script starts refreshing the page at 6:00 PM EST until it finds and books the desired slot.
   ```bash
   python reservation_script.py
   ```
