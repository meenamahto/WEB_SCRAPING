import requests
import json
from bs4 import BeautifulSoup
def get_movies_list_details(movie_list):
    with open("top_movie1.json","r") as file:
        data=json.load(file)
    for i in range(80,100):
        url=requests.get(data[i]["movie_url"])
        htmlcontect=url.content
        soup=BeautifulSoup(htmlcontect,"html.parser")
        ul=soup.find("ul",class_="content-meta info")
        li=ul.find_all('li',class_='meta-row clearfix')
        dict={}
        h1=soup.find('h1',class_='scoreboard__title').get_text()
        # print(h1)
        dict.update({"movie name":h1})
        for i in li:
            key=i.find("div",class_="meta-label subtle").get_text().strip().replace(":","")
            value=i.find("div",class_="meta-value").get_text().strip().replace("\n","").replace(" ","")
            if key!="Genre" and key!="Original Language" and  key!="Director" and key!="Writer" :
                # print(key)
                dict.update({key:value})
            else:
                new_value=value.replace(","," ")
                value_list=new_value.split()
                dict.update({key:value_list})
        movie_list.append(dict)
    print(movie_list)
    with open("movie_list_details5.json","w") as file:
        json.dump(movie_list,file,indent=4)
get_movies_list_details([])
