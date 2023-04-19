

# imports
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pathlib import Path
import os
import pytz
 
# init the calendar
cal = Calendar()