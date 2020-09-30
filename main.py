from selenium import webdriver
from bs4 import BeautifulSoup
import re

browser = webdriver.Firefox()

# Ask the user for url
print('Website URL: ')
URL = input()

# Grab secure site
try:
    if URL[0:8] == 'https://':
        browser.get(URL)
    elif URL[0:7] == 'http://':
        NewURL = 'https://' + URL[7:]
        browser.get(NewURL)
    else:
        NewURL = 'https://' + URL
        browser.get(NewURL)
except:
    print("Could not find " + URL)
    browser.quit()
    quit()

# Get the page source and beautify the output
PageSRC = browser.page_source
soup = BeautifulSoup(PageSRC, 'html.parser')

# Write the links to a txt file using regular expression
links = re.findall("((\w+:\/\/)[-a-zA-Z0-9:@;?&=\/%\+\.\*!'\(\),\$_\{\}\^~\[\]`#|]+)", soup.prettify())
file = open(URL + ' Links.txt', 'w+')
file.write('Links taken from ' + URL + '\n\n')
for link in links:
    file.write(link[0] + '\n')

# Close the file
file.close()

# Close the browser
browser.quit()
