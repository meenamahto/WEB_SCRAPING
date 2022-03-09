import json
import requests
with open("movie_list_details5.json","r") as file:
    data=json.load(file)
# print(data)
def analyse_movie_language_and_director(movie_lang):
    director_list=[]
    language_list=[]
    list=[]
    list1=[]
    for i in (movie_lang):
        for j in (i["Director"]):
            director_name=j
        for k in (i["Original Language"]):
            language_name=k
        if director_name not in director_list:
            director_list.append(director_name)
        if language_name not in language_list:
            language_list.append(language_name)
        list.append(director_name)
        list1.append(language_name)
    # print(list1)
    director_dict={i:{}for i in director_list}
    for x,y in director_dict.items():
        count=0
        for i in movie_lang:
            for j in (i["Original Language"]):
                lang=j
            for k in (i["Director"]):
                dir=k
                if x==k:
                    count+=1
                    y.update({lang:count})
    print(director_dict)
    with open("movie_language_and_director10.json","w") as file:
        json.dump(director_dict,file,indent=4)
analyse_movie_language_and_director(data)
