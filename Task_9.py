import os
import requests
import json,time,random
from bs4 import BeautifulSoup
with open("top_movie1.json","r") as f:
    data=json.load(f)
list=[]
def scrape_movie_details(movie_url):
    random_sleep=random.randint(1,3)
    movie_id=''
    for id in movie_url[33:]:
        if "/" not in id:
            movie_id+=id
        else:
            break  
    file_name=movie_id+".json"
    text=None
    if text is None: 
        time.sleep(random_sleep)
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
            if key!="Genre":
                dict.update({key:value})
            else:
                n_value=value.replace(","," ")
                value1=n_value.split()
                dict.update({key:value1})
        list.append(dict)
    with open("movie_list9.json",'w') as file:
        json.dump(list,file,indent=4)
    print(list)
for i in range(len(data)):
    scrape_movie_details(data[i]["movie_url"])