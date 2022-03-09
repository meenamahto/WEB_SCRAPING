import json
import requests
with open("movie_list_details5.json","r") as file:
    data=json.load(file)
# print(data)
def analyse_movie_director():
    director_list=[]
    list=[]
    for i in range(len(data)):
        for j in range(len(data[i]["Director"])):
            director_name=data[i]["Director"][j]
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
    # print(list)
    with open("analyse_movie_director7.json","w") as file:
        json.dump(director_dict,file,indent=4)
analyse_movie_director()       
