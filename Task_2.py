import json
with open("top_movie1.json","r") as file:
    data=json.load(file)
# print(a)
def group_by_year(movie):
    years=[]
    for i in movie:
        year=i["year"]
        if year not in years:
            years.append(year)
        movie_dict={i:[]for i in years}
        for i in movie:
            year=i["year"]
            for x,y in movie_dict.items():
                if x==year:
                    y.append(i)
    with open("group_by_year2.json","w") as file:
        json.dump(movie_dict,file,indent=4)
    return movie_dict
print(group_by_year(data))


