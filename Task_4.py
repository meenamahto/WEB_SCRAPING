import json
import requests
from bs4 import BeautifulSoup

def scrape_movies_details(movie_url):
    url=requests.get(movie_url)
    htmlcontect=url.content
    soup=BeautifulSoup(htmlcontect,"html.parser")
    ul=soup.find("ul",class_="content-meta info")
    li=ul.find_all('li',class_='meta-row clearfix')
    # print(li)
    dict={}
    h1=soup.find('h1',class_='scoreboard__title').get_text()
    # print(h1)
    dict.update({"movie name":h1})

    for i in li:
        key=i.find("div",class_="meta-label subtle").get_text().strip().replace(":","")
        
        value=i.find("div",class_="meta-value").get_text().strip().replace("\n","").replace(" ","")
        if key!="Genre" and key!="Original Language" and  key!="Director" and key!="Writer" and key!="Runtime":
            # print(key)
            dict.update({key:value})
        elif key=="Runtime":
            t=int(value[2:4])
            time=(int(value[0])*60)+t
            time_minutes=str(time)+value[-1]
            dict.update({key:time_minutes})
        else:
            new_value=value.replace(","," ")
            value_list=new_value.split()
            # print(value_list)
            dict.update({key:value_list})
        print(dict)
    with open("movie_details4.json","w") as file:
        json.dump(dict,file,indent=4)
scrape_movies_details("https://www.rottentomatoes.com/m/black_panther_2018")

