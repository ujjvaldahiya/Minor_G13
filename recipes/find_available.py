import pandas as pd
import numpy as np
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def search_available(s):
    df=pd.read_excel('datasheet_recipe.xlsx')
    df = df.replace(np.nan, '', regex=True)
    dt=df.values.tolist()
    major_ingridients=[]
    ingridients_set=set([])
    for i in range(len(dt)):
        ing = dt[i][2]   #ing is string
        ing=ing.split(',')# list of strings
        for j in range(len(ing)):
            ing[j]=ing[j].strip()
            ingridients_set.add(ing[j])
        major_ingridients.append(ing)
   
    #print(major_ingridients)
    available=s.split(',')
    for i in range(len(available)):
        available[i]=available[i].strip()
    for i in range(len(available)):
        if (available[i]==''):
            continue
        highest=process.extractOne(available[i],ingridients_set,scorer=fuzz.token_sort_ratio)
        if(highest[1]<70):
            available[i]=''
        else:
            available[i]=highest[0]
    return available