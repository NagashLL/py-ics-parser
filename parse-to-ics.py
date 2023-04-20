import icalendar

# imports
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pathlib import Path
import os
import pytz
 
import csv
from icalendar import Calendar, Event

# Create a new iCalendar object
cal = Calendar()

# Construct the full path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'events.csv')

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(reader)

    # Loop over the rows in the CSV file
    for row in reader:
        # Create a new event
        event = Event()

        # Set the event properties from the CSV data
        event.add('summary', row[0])
        event.add('description', row[1])
        event.add('dtstart', row[2])
        event.add('dtend', row[3])

        # Add the event to the calendar
        cal.add_component(event)

# Write the calendar to a file
with open('events.ics', 'wb') as f:
    f.write(cal.to_ical())