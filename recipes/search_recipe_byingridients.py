import pandas as pd
import numpy as np
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def search_recipe(available):
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
        
    result=[]
    for i in range(len(major_ingridients)):
        total_req=len(major_ingridients[i])
        total_available=0
        for j in major_ingridients[i]:
            for k in available:
                if j==k:
                    total_available+=1
        if(total_available>2 or (total_available>0 and total_req/total_available <=2.5)):
            dic={}
            dic['ID']=dt[i][0]
            dic['Name']=dt[i][1]
            dic['Ingredients']=dt[i][4]
            dic['Procedure']=dt[i][5]
            dic['Time']=dt[i][6]
            dic['Yield']=dt[i][7]
            result.append(dic)

    return result