
	def sewp(request):
		r = requests.get("http://www.vladtv.com/")

		soup = BeautifulSoup(r.content, 'html.parser')

		content = soup.find_all("a")

		for link in soup.find_all("a"):
		    link = link.get("href")

		ella = "ella"
		context = {
		    "link": link,
		    "ella": ella,
		}
		print r
		return render(request, "posts/display_soup.html", context)