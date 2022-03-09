import os
import requests
import json
from bs4 import BeautifulSoup
def scrape_movie_details(movie_url):
    movie_id=''
    for id in movie_url[33:]:
        if "/" not in id:
            movie_id+=id
        else:
            break  
    file_name=movie_id+".json"
    text=None
    if text is None: 
        url=requests.get(movie_url)
        htmlcontect=url.content
        soup=BeautifulSoup(htmlcontect,"html.parser")
        ul=soup.find("ul",class_="content-meta info")
        li=ul.find_all('li',class_='meta-row clearfix')
        dict={}
        h1=soup.find('h1',class_='scoreboard__title').get_text()
        dict.update({"movie name":h1})
        for i in li:
            key=i.find("div",class_="meta-label subtle").get_text().strip().replace(":","")
            value=i.find("div",class_="meta-value").get_text().strip().replace("\n","").replace(" ","")
            dict.update({key:value})
        with open(file_name,'w') as file:
            json.dump(dict,file,indent=4)
    print(dict)
scrape_movie_details("https://www.rottentomatoes.com/m/avengers_endgame")
