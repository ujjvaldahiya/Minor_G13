# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:33:16 2020

@author: Jagseer Singh
"""

import pandas as pd
import numpy as np
from fuzzywuzzy import process
from RecommendationSystemExercise import find_recommendations

def search_exer_byname(s):
    df= pd.read_excel('datasheet_exer.xlsx')
    df.head()
    df = df.replace(np.nan, '', regex=True)
    table_values=df.values.tolist()
    df1=df[['ID','EXERCISE_NAME']]
    dt=df1.values.tolist()
    exercises_name=[]
    for i in range(len(dt)):
        exercises_name.append(dt[i][1])
    closest=process.extractOne(s,exercises_name)
    result=[]
    if closest[1]<75:
        return result
    for i in range(len(table_values)):
        if(table_values[i][1]==closest[0]):
            dic={}
            dic['ID']=table_values[i][0]
            dic['Exercise_Name']=table_values[i][1]
            dic['Body_Part']=table_values[i][2]
            dic['Equipments']=table_values[i][3]
            dic['Difficulty']=table_values[i][4]
            dic['Procedure']=table_values[i][5]
            result.append(dic)
    his=[]
    his.append(str(result[0]['ID']))
    return result,find_recommendations(his)
    
#print(search_exer_byname("jump"))
