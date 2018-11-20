from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

imdb = "https://www.imdb.com/showtimes/location?ref_=sh_lc" # "Movies near you" on IMDB

imdbhtml = uReq(imdb) # Requests the given url (imdb)
page_html = imdbhtml.read() # Reads html
imdbhtml.close() # Closes html (so your computer doesn't crash)
page_soup = soup(page_html, "html.parser") # Sets parsing method and parses the html

movie_containers = page_soup.findAll("div", {"class" : "title"}) # Goes through all of the html from that specific imdb page and finds the container for each movie

for movie_container in movie_containers: # Loops through every container and finds the title of each movie
    movie_title = movie_container.a.text # The location of the title
    print(movie_title)

#https://www.imdb.com/showtimes/location?ref_=sh_lc   
    
    



