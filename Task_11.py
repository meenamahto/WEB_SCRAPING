import json
import requests
with open("movie_list9.json","r") as file:
    data=json.load(file)
# print(data)
def analyse_movie_genre(movie_list):
    director_list=[]
    list=[]
    for i in range(len(movie_list)):
        for j in range(len(movie_list[i]["Genre"])):
            director_name=movie_list[i]["Genre"][j]
        if director_name not in director_list:
            director_list.append(director_name)
        list.append(director_name)
    director_dict={i:""for i in director_list}
    for x,y in director_dict.items():
        count=0
        for i in range(len(list)):
            if x==list[i]:
                count+=1
                director_dict[x]=count
    print(director_dict)
    with open("analyse_movie_genre11.json","w") as file:
        json.dump(director_dict,file,indent=4)
analyse_movie_genre(data)