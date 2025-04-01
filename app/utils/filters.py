def format_date(date):
  return date.strftime('%m/%d/%y')

# This is to test the `format_date(date)` function. Simply run the file to validate 
from datetime import datetime
print(format_date(datetime.now()))

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# This is to test the `format_url(url)` function
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))