# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:49:40 2020

@author: Jagseer Singh
"""
import pandas as pd
import numpy as np
from fuzzywuzzy import process


def search_exer(s,easy,medium,hard):
    x=s.split(",")
    inputs=[]
    eqp=['mat','bench','dumbbell','chair','barbell','ladder','kettlebell','box','rod','cable','bar','ball']
    for i in range(len(x)):
        if(x[i]==''):
            continue
        inputs.append(x[i].split()[0])
    
    for i in range(len(inputs)):
        if (inputs[i]==''):
            continue
        highest=process.extractOne(inputs[i],eqp)
        if(highest[1]<75):
            inputs[i]=''
        else:
            inputs[i]=highest[0]
        
    df= pd.read_excel('datasheet_exer.xlsx')
    df.head()
    df = df.replace(np.nan, '', regex=True)
    df=df[['ID','EQUIPMENTS','DIFFICULTY']]
    dt=df.values.tolist()
    for i in range(len(dt)):
        dt[i][1]=dt[i][1].split(',')
        for j in range(len(dt[i][1])):
            dt[i][1][j]=dt[i][1][j].strip()

    search_list=[]
    for i in range(len(dt)):
        passing=True
        if(dt[i][2]==1 and easy==False):
            passing=False
        if(dt[i][2]==2 and medium==False):
            passing=False
        if(dt[i][2]==3 and hard==False):
            passing=False
        
        for j in range(len(dt[i][1])):
            failing=True
            for k in range(len(inputs)):
                if(dt[i][1][j].lower() == inputs[k].lower()):
                    failing=False
            if(dt[i][1][0]==""):
                failing=False
            if(failing==True):
                passing=False
        if(passing==True):
            search_list.append(dt[i][0])
    result=[]
    df1=pd.read_excel('datasheet_exer.xlsx')
    for i in range(len(search_list)):
        dic={}
        temp=(df1[df1['ID']==int(search_list[i])]).values.tolist()
        dic['ID']=temp[0][0]
        dic['Exercise_Name']=temp[0][1]
        dic['Body_Part']=temp[0][2]
        dic['Equipments']=temp[0][3]
        dic['Difficulty']=temp[0][4]
        dic['Procedure']=temp[0][5]
        result.append(dic)
    return result

#print(search_exer("ball",False,False,True))
