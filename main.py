from surf_data import get_data
import sqlite3 #Makes our data table
from text import send_text
from datetime import date
from database import database_commit

data = get_data()
textString = database_commit(data)

send_text(textString)

