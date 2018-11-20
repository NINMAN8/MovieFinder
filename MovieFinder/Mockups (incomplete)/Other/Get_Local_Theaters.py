from bs4 import BeautifulSoup as soup # imports the Beautiful Soup 4 module
from urllib.request import urlopen as uReq # imports the urllib.request module so that the program can request urls

theaterPageURL = "https://www.imdb.com/showtimes/?ref_=shlc_tny_th" # Page I want to scrape

theaterPage = uReq(theaterPageURL) # Requests the given url
theaterPage_html = theaterPage.read() # Reads and downloads the page's html
theaterPage.close() # Closes the page (so your computer doesn't crash)
theaterPage_soup = soup(theaterPage_html, "html.parser") # Defines the parsing method and parses the page

theater_containers = theaterPage_soup.findAll("div",{"class":"fav_box"})
withins = theaterPage_soup.find("h4", {"class":"li_group"})

strip1 = withins.span.text.strip("(")
strip2 = int(strip1.strip(")"))
numberWithin5 = strip2 - 1

for theater_container in theater_containers: # Loops over every theater and gets only the name

    within5 = [] # keeps track of all of the movie theaters within 5 miles
    within10 = [] # Keeps track of all of the movie theaters within 10 miles
    within20 = [] # Keeps track of all of the movie theaters within 20 miles
    within30 = [] # Keeps track of all of the movie theaters within 30 miles
    
    theaterName = theater_container.a.text # Location of all of the names of all of the movie theaters
    #print(theaterName) # for testing purposes only

    if theater_container <= numberWithin5:
        within5.append(theaterName)
    

    

    

    












