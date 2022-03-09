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
    if os.path.exists("data/movie_details/"+file_name):   
        file=open(file_name,"w")
        text=file.read()
        return text
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
        cast_detail=scrape_movie_cast(movie_url)
        dict.update({"cast":cast_detail})
    with open("movie_details_with_cast13.json","w") as file:
        json.dump(dict,file,indent=4)
    print(dict)
dict_list=[]
def scrape_movie_cast(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    s=soup.find("section",class_="panel panel-rt panel-box")
    cast=soup.find("div",class_="castSection")
    s=cast.find_all("div",class_="cast-item media inlineBlock")
    link_list=[]
    name_list=[]
    for i in s:
        name=i.find("a",class_="unstyled articleLink").get_text().strip()
        a=i.find("a",class_="unstyled articleLink")
        c=a.get_text()
        b=a["href"]
        link_list.append(b)
        name_list.append(name)
    list=["name","link"]
    for i in range(len(name_list)):
        d={}
        for j in range(len(list)):
            d.update({list[0]:name_list[i]})
            d.update({list[1]:link_list[i]})
        dict_list.append(d)
    return dict_list
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")
