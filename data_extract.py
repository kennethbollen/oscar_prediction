import bs4
import requests

film_sites = []
film_names = []
num_pages = int(round(4809/50)) + 1

for i in range(num_pages):
	i += 1
	print('\ngathering data from page %s' %i)
	url = 'http://www.imdb.com/search/title?groups=oscar_nominee&page=%s&ref_=adv_nxt' % num_pages
	req = requests.get(url)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text)
	#get film sites
	for link in soup.find_all('h3'):
	  try:
	    x = 'http://imdb.com' + link.a['href']
	    x.strip(' ')
	    film_sites.append(x)
	  except TypeError:
	    continue

#clean the url list
for i in range(len(film_names[i])):
	if len(film_names[i]) > 40:
		del(film_names[i])
	else:
		continue

for site in film_sites:
    req = requests.get(site)
    req.raise_for_status()
    soup = bs4.BeautifulSoup(req.text)
    #runtime
    for line in soup.find_all('time'):
    	print(line.text[:3].strip())
		
