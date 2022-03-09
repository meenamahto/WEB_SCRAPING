import json
with open("movie_list_details5.json","r") as file:
    data=json.load(file)
def analyse_movie_language(movie_list):
    language_list=[]
    list=[]
    for i in range(len(movie_list)):
        for j in range(len(movie_list[i]["Original Language"])):
            if movie_list[i]["Original Language"][j] not in language_list:
                language_list.append(movie_list[i]["Original Language"][j])
            list.append(movie_list[i]["Original Language"][j])
    language_dict={i:""for i in language_list}
    for x,y in language_dict.items():
        count=0
        for i in range(len(list)):
            if x==list[i]:
                count+=1
                language_dict[x]=count
    print(language_dict)
    # print(language_list)
    # print(list)
    with open("analyse_movie_language6.json","w") as file:
        json.dump(language_dict,file,indent=4)
analyse_movie_language(data)

