import bs4
import requests
url = 'http://www.imdb.com/search/title?groups=top_1000'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req)

film_sites = []
film_names = []
num_pages = int(1000/50)


#get film names
for link in soup.find_all('h3'):
	print(link.text)

for i in range(num_pages):
	i += 1
	url = 'http://www.imdb.com/search/title?groups=top_1000&page=%s&ref_=adv_prv' % num_pages
	req = requests.get(url)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text)
	#get film sites
	for link in soup.find_all('h3'):
	  try:
	    x = 'imdb.com' + link.a['href']
	    film_site.append(x)
	  except TypeError:
	    continue
	#get film names
	for link in soup.find_all('h3'):
		print(link.text)

