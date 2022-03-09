import json,requests
from bs4 import BeautifulSoup
with open("top_movie1.json","r") as file:
    data=json.load(file)
final_list=[]
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
    dict_list=[]
    for i in range(len(name_list)):
        d={}
        for j in range(len(list)):
            d.update({list[0]:name_list[i]})
            d.update({list[1]:link_list[i]})
        dict_list.append(d)
    final_list.append(dict_list)
    print(final_list)

    with open("movie_cast12.json","w") as file:
        json.dump(final_list,file,indent=4)
for i in range(10):
    scrape_movie_cast(data[i]["movie_url"])