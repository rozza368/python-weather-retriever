import urllib.request
from bs4 import BeautifulSoup

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

def scrape():
    input_loc = input('Enter a location. ')
    w_loc = input_loc.strip() # in case the user put a space at the start or end
    display_loc = w_loc.title() # makes the letters title case
    w_loc = w_loc.replace(' ', '+') # if the location is more than one word, prepare it for link

    quote_page = 'https://www.google.com/search?client=firefox-b-d&q={}+weather'.format(w_loc)
    req = urllib.request.Request(quote_page, headers = headers)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('span', attrs={'id': 'wob_tm'}) # finds current temperature
    result = temperature.text.strip()

    message = 'The current temperature in {} is {}°C.'.format(display_loc, result)
    print(message + '\n')
    scrape()

try:
    scrape()
except AttributeError:
    print("That location is invalid. Please enter a valid location.\n")
    scrape()
