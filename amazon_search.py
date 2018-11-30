#! python3
import requests, bs4, webbrowser, sys

# Opens the first 5 links of the search term in Amazon in a webbrowser

# TODO Remove "Top Rated from Our Brands"

searchterm = "cables"

#req = requests.get("https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + " ".join(sys.argv[1:]))
req = requests.get("https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "".join(searchterm))

#webbrowser.open("https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "".join(searchterm))

#site = "https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + " ".join(sys.argv[1:])

soup = bs4.BeautifulSoup(req.text, "html.parser")

linkElems = soup.select("a.a-text-normal")
finder = soup.find_all("a", class_="a-text-normal")


hreflinks = []
hreflinks2 = []

for i in linkElems:
    if i.has_attr("href"):
        if i["href"] not in hreflinks:
            hreflinks.append(i["href"])

for t in hreflinks:
    if t.startswith("https:"):
        hreflinks2.append(t)

hreflinks = []

for g in hreflinks2:
    if g.endswith(("Reviews", "Promotions")) or "ref=" in g:
        hreflinks.append(g)

for h1 in hreflinks:
    if h1 in hreflinks2:
        hreflinks2.remove(h1)

# print(hreflinks)
print (hreflinks2)

sites = 5

for sites in range(sites):
    webbrowser.open(hreflinks2[sites])

# webbrowser.open(str(site))
