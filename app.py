
from ast import Str
from bs4 import BeautifulSoup as soup
import bs4
import requests
import pandas as pd

from flask import Flask
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('HomePage.html')

@app.route("/products",methods=['POST'])
def products():
    if request.method=='POST':
        value=request.form.get('platform')
        if value=="1":
            url="https://www.imdb.com/search/title/?count=100&title_type=feature,tv_series"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Fan Fanvourites')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=='2':
            url="https://www.imdb.com/search/title/?companies=co0144901"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Popular On Netflix')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="3":
            url="https://www.imdb.com/search/title/?companies=co0476953"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Popular On Amazon-Prime')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="4":
            url="https://www.imdb.com/search/title/?companies=co0847080"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Popular On Disney+ Hotstar')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="5":
            url="https://www.imdb.com/search/title/?companies=co0603531"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Popular On VOOT')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="6":
            url="https://www.imdb.com/search/title/?companies=co0721599"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            i=0
            movies=[]
            movies.append('Popular On MX-Player')
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="7":
            url="https://www.imdb.com/list/ls048452188/"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all("h3",class_="lister-item-header")
            movies=[]
            movies.append('New and Upcoming SuperHero Movies/Series')
            i=0
            for movie in scraped_movies:
                if i<10:
                    movie=movie.get_text().replace("\n","")
                    movies.append(movie)
                i+=1
            return render_template('HomePage.html',movies=movies)
        elif value=="8":
            url="https://paytm.com/movies/belagavi"
            page=requests.get(url)
            Soup=soup(page.content,"html.parser")
            scraped_movies=Soup.find_all(class_="MobileRunningMovie_lineClamp__akkn9 MobileRunningMovie_clampTwo__eTC0p")
            movies=[]
            movies.append("Movies in BELGAUM Theatres RIGHT NOW..!!")
            for movie in scraped_movies:
                movie=movie.get_text().replace("\n","")
                movies.append(movie)
            return render_template('HomePage.html',movies=movies)


if __name__=="__main__":
    app.run(debug=True,port=8000)