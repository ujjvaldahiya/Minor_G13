# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:47:04 2020

@author: Jagseer Singh
"""

import pandas as pd
import numpy as np
import pickle
import warnings;
warnings.filterwarnings('ignore')


model_name="model_r_recipe.pkl"
with open(model_name, 'rb') as file:  
    model = pickle.load(file)
def similar_products(v, n = 4):
    # extract most similar products for the input vector
    ms = model.similar_by_vector(v,topn=n+1 )[1:]
    # extract name and similarity score of the similar products
    result=[]
    for i in range(len(ms)):
        result.append(ms[i][0])
    return result

def aggregate_vectors(products):
    product_vec = []
    for i in products:
        try:
            product_vec.append(model[i])
        except KeyError:
            continue
        
    return np.mean(product_vec, axis=0)


#History is list of exercises
def find_recommendations(history):
    recommendations=similar_products(aggregate_vectors(history))
    df=pd.read_excel('datasheet_recipe.xlsx')
    data=df.values.tolist()
    result=[]
    for i in recommendations:
        j=data[int(i)-101]
        dic={}
        dic['ID']=j[0]
        dic['recipe_name']=j[1]
        dic['ingredients']=j[4]
        dic['procedure']=j[5]
        dic['time']=j[6]
        dic['servings']=j[7]
        result.append(dic)
    return result