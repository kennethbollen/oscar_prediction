import bs4
import requests

film_sites = []
film_names = []
num_pages = int(round(4809/50)) + 1

for i in range(num_pages):
	i += 1
	url = 'http://www.imdb.com/search/title?groups=oscar_nominee&page=%s&ref_=adv_nxt' % num_pages
	req = requests.get(url)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text)
	#get film sites
	for link in soup.find_all('h3'):
	  try:
	    x = 'imdb.com' + link.a['href']
	    x.strip(' ')
	    film_sites.append(x)
	  except TypeError:
	    continue
	#get film names
	for link in soup.find_all('h3'):
		x = link.text
		x.strip(' ')
		film_names.append(link.text)

