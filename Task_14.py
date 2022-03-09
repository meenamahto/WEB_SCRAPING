##out put shoud be:-

# {
#   "nm0004435": {
# "name": "Rajesh Khanna",
# "frequent_co_actors": [
#   {
# "imdb_id": "nm0000821",
# "name": "Amitabh Bachan"
# "num_movies": 2
#   }
# ]
#   },
#   "nm0000821": {
# "name": "Amitabh Bachan",
# "frequent_co_actors": [
#   {}, {}, {}
# ]
#   }
# }


import json,requests
from bs4 import BeautifulSoup
def analyse_co_actors():
    dict={}
    url="https://www.rottentomatoes.com/m/avengers_endgame"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    d=soup.find("div",class_="castSection")
    d1=d.find_all("div",class_="cast-item media inlineBlock")
    dict1={}
    list=[]
    movie_id=''
    for id in url[33:]:
        movie_id+=id
    list1=[]
    for i in d1:
        a=i.find("a",class_="unstyled articleLink").get_text().strip()
        list1.append(a)
    dict1["lead actor"]=list1[0]
    list1.pop(0)
    list3=["name"]
    for name in range(len(list1)):
        dict2={}
        for key in range(len(list3)):
            dict2.update({list3[0]:list1[name]})
        list.append(dict2)
    dict1["frequent_co_actors"]=list
    dict[movie_id]=dict1
    print(dict)
    with open("co_actors14.json","w") as file:
        json.dump(dict,file,indent=4)
analyse_co_actors()






# main_list=[{"abc":{"lead":"srk","co":[{"name":"amit"},{"name":"amir"}]},
# "xyz":{"lead":"srk","co":[{"name":"aks"},{"name":"amit"}]},
# "por":{"lead":"sal","co":[{"name":"amir"},{"name":"ritik"},
# {"name":"srk"},{"name":"amit"}]}
# }]
# res=[]
# for i in range(len(main_list)):
#     for j in main_list[i]:
#         ma=main_list[i][j]["lead"]
#         for k in range(len(main_list[i][j]["co"])):
#             ca=main_list[i][j]["co"][k]["name"]
#             for l in res:
#                 for m in l:
#                     if m in l:
#                         if ma in m and ca in m:
#                             l[m]=l[m]+1
#                             break
#             dict={}
#             dict[ma,ca]=1
#             res.append(dict)   
# print(res)
