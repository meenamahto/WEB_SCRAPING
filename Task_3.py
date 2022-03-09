import json
from bs4 import BeautifulSoup
import requests
with open("top_movie1.json","r") as file:
    data=json.load(file)
def decades_by_years(movies):
    years=[]
    for i in range(len(movies)):
        rem=movies[i]["year"]%10
        decades=movies[i]["year"]-rem
        if decades not in years:
            years.append(decades)
    years.sort()
    movies_dict={i:[]for i in years}
    for i in range(len(movies)):
        for x,y in movies_dict.items():
            if x==1920:
                if movies[i]["year"]>=1920 and movies[i]["year"]<1930:
                    y.append(movies[i])
                    # print(y)
                    break
            elif x==1930:
                if movies[i]["year"]>=1930 and movies[i]["year"]<1940:
                    y.append(movies[i])
                    break
            elif x==1940:
                if movies[i]["year"]>=1940 and movies[i]["year"]<1950:
                    y.append(movies[i])
            elif x==1950:
                if movies[i]["year"]>=1950 and movies[i]["year"]<1960:
                    y.append(movies[i])
            elif x==1960:
                if movies[i]["year"]>=1960 and movies[i]["year"]<1970:
                    y.append(movies[i])
            elif x==1970:
                if movies[i]["year"]>=1970 and movies[i]["year"]<1980:
                    y.append(movies[i])
            elif x==1980:
                if movies[i]["year"]>=1980 and movies[i]["year"]<1990:
                    y.append(movies[i])
            elif x==1990:
                if movies[i]["year"]>=1990 and movies[i]["year"]<2000:
                    y.append(movies[i])
            elif x==2000:
                if movies[i]["year"]>=2000 and movies[i]["year"]<2010:
                    y.append(movies[i])
            elif x==2010:
                if movies[i]["year"]>=2010 and movies[i]["year"]<2020:
                    y.append(movies[i])
            elif x==2020:
                if movies[i]["year"]>=2020 and movies[i]["year"]<2030:
                    y.append(movies[i])
    print(movies_dict)
    with open("decades_by_years3.json","w") as file:
        json.dump(movies_dict,file,indent=4)
decades_by_years(data)
