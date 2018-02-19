import bs4
import requests
url = 'http://www.imdb.com/search/title?groups=top_1000'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req)

film_sites = []
film_names = []

#get film names
for link in soup.find_all('h3'):
	print(link.text)

for i in range(len(film_names)):


#get film sites
for link in soup.find_all('h3'):
  try:
    x = 'imdb.com' + link.a['href'])
	  film_site.append(x)
  except TypeError:
    continue
    
#get the next page
for link in soup.find_all('a', href=True):
  try:
	  if re.search('Next', link.text) is not None:
		  print(link['href'])
  except:
    break 
