from bs4 import BeautifulSoup
from collections import Counter
import urllib2

url='http://olympics.usahockey.com/page/show/1067902-roster'
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


locations = []
cities = []
states = []

tables = soup.findAll("table", { "class" : "dataTable" })
for table in tables:
	rows = table.findAll("tr")
	for row in rows:
		entries = row.findAll("td")
		if len(entries) > 6:
			city,state = entries[6].get_text().encode('ascii').split(", ")
			cities.append(city)
			states.append(state)

print Counter(states)
print Counter(cities)







