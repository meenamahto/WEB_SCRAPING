import json,requests
from bs4 import BeautifulSoup
with open("top_movie1.json","r") as file:
    data=json.load(file)
def analyse_co_actors(movie_data):
    name_list=[]
    actors_dict={}
    for i in range(len(data)):
        url=data[i]["movie_url"]
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        d=soup.find("div",class_="castSection")
        d1=d.find_all("div",class_="cast-item media inlineBlock")
        list=[]
        movie_id=''
        for id in url[33:]:
            movie_id+=id
        for i in d1:
            a=i.find("a",class_="unstyled articleLink").get_text().strip()
            list.append(a)
        name_list.append(list)
        actors_list=[]
        for name in range(len(name_list)):
            actors_list.append(name_list[name][0])
        for i in range(len(actors_list)):
            count=0
            dict1={}
            for j in range(len(actors_list)):
                if actors_list[i]==actors_list[j]:
                    count=count+1
                    dict1["name"]=actors_list[i]
                    dict1["num_movies"]=count
                else:
                    dict1["name"]=actors_list[i]
                    dict1["num_movies"]=1
                actors_dict.update({movie_id:dict1})
    print(actors_dict)
    with open("actors_movie15.json","w") as file:
        json.dump(actors_dict,file,indent=4)
analyse_co_actors(data)
