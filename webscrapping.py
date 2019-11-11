import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
from lxml import html
from lxml.html import fromstring
import urllib.request
from urllib.request import urlopen
import random
import re
import scrapy

def webScraper(url):
    res = requests.get(url)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

# Top 100 Comedy Movies
    
url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/'

soup = webScraper(url)

comedylist = []
comedyraw = soup.find_all('a',{"class": "unstyled articleLink"})
for movie in comedyraw:
    movie = movie.text
    movie = re.findall(r'\n.+\)', movie)
    comedylist.append(movie)

prefinalcomedylist = [item for sublist in comedylist for item in sublist]

top100comedymovies = []
for movie in prefinalcomedylist:
    movie = re.sub("\n", "", movie)
    movie = re.sub("\(\d+\)", "", movie)
    movie = movie.strip()
    top100comedymovies.append(movie)

# Top 100 Drama Movies

url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/'

soup = webScraper(url)

dramalist = []
dramaraw = soup.find_all('a',{"class": "unstyled articleLink"})
for movie in dramaraw:
    movie = movie.text
    movie = re.findall(r'\n.+\)', movie)
    dramalist.append(movie)

prefinaldramalist = [item for sublist in dramalist for item in sublist]

top100dramamovies = []
for movie in prefinaldramalist:
    movie = re.sub("\n", "", movie)
    movie = re.sub("\(\d+\)", "", movie)
    movie = movie.strip()
    top100dramamovies.append(movie)

# Top 100 Horror Movies

url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/'

soup = webScraper(url)

horrorlist = []
horrorraw = soup.find_all('a',{"class": "unstyled articleLink"})
for movie in horrorraw:
    movie = movie.text
    movie = re.findall(r'\n.+\)', movie)
    horrorlist.append(movie)

prefinalhorrorlist = [item for sublist in horrorlist for item in sublist]

top100horrormovies = []
for movie in prefinalhorrorlist:
    movie = re.sub("\n", "", movie)
    movie = re.sub("\(\d+\)", "", movie)
    movie = movie.strip()
    top100horrormovies.append(movie)

# Top 100 Romance Movies

url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/'

soup = webScraper(url)

romancelist = []
romanceraw = soup.find_all('a',{"class": "unstyled articleLink"})
for movie in romanceraw:
    movie = movie.text
    movie = re.findall(r'\n.+\)', movie)
    romancelist.append(movie)

prefinalromancelist = [item for sublist in romancelist for item in sublist]

top100romancemovies = []
for movie in prefinalromancelist:
    movie = re.sub("\n", "", movie)
    movie = re.sub("\(\d+\)", "", movie)
    movie = movie.strip()
    top100romancemovies.append(movie)

# Top 100 Thriller Movies

url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/'

soup = webScraper(url)

thrillerlist = []
thrillerraw = soup.find_all('a',{"class": "unstyled articleLink"})
for movie in thrillerraw:
    movie = movie.text
    movie = re.findall(r'\n.+\)', movie)
    thrillerlist.append(movie)

prefinalthrillerlist = [item for sublist in thrillerlist for item in sublist]

top100thrillermovies = []
for movie in prefinalthrillerlist:
    movie = re.sub("\n", "", movie)
    movie = re.sub("\(\d+\)", "", movie)
    movie = movie.strip()
    top100thrillermovies.append(movie)

d = {'comedy':top100comedymovies,'drama':top100dramamovies, 'horror':top100horrormovies , 'thriller': top100thrillermovies, 'romance':top100romancemovies}

dfTomatoe = pd.DataFrame(d)

dfTomatoe.to_csv('./output/dfTomatoe.csv')




