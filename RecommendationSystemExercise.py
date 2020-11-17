import pandas as pd
import numpy as np
import pickle
import warnings;
warnings.filterwarnings('ignore')

df = pd.read_excel('datasheet_exer.xlsx')
model_name="model_r_ex.pkl"
with open(model_name, 'rb') as file:  
    model = pickle.load(file)
def similar_products(v, n = 4):
    # extract most similar products for the input vector
    ms = model.similar_by_vector(v,topn=n+1 )[1:]
    # extract name and similarity score of the similar products
    result=[]
    for i in range(len(ms)):
        dic={}
        temp=(df[df['ID']==int(ms[i][0])]).values.tolist()
        dic['ID']=temp[0][0]
        dic['Exercise_Name']=temp[0][1]
        dic['Body_Part']=temp[0][2]
        dic['Equipments']=temp[0][3]
        dic['Difficulty']=temp[0][4]
        dic['Procedure']=temp[0][5]
        result.append(dic)
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
    return similar_products(aggregate_vectors(history))

#print(find_recommendations(['120','110']))