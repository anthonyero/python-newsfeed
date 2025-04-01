def format_date(date):
  return date.strftime('%m/%d/%y')

# This is to test the `format_date(date)` function. Simply run the file to validate 
from datetime import datetime
print(format_date(datetime.now()))