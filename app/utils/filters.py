# Returns a date object in the following format "mm/dd/yy"
def format_date(date):
  return date.strftime('%m/%d/%y')

# Returns a URL with only the domain name
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Returns a pluralized version of the word depending on the amount provided
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word