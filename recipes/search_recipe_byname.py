import pandas as pd
import numpy as np
from fuzzywuzzy import process
#from RecommendationSystemRecipe import find_recommendations

def search_recipe_byname(s):
    df= pd.read_excel('datasheet_recipe.xlsx')
    df = df.replace(np.nan, '', regex=True)
    table_values=df.values.tolist()
    print(df.head())
    df1=df[['recipe_id','recipe_name']]
    dt=df1.values.tolist()
    recipe_name=[]
    for i in range(len(dt)):
        recipe_name.append(dt[i][1])
    closest=process.extract(s,recipe_name)
    result=[]
    for i in range(len(table_values)):
        for j in range(len(closest)):
            if(table_values[i][1]==closest[j][0]):
                dic={}
                dic['ID']=table_values[i][0]
                dic['Name']=table_values[i][1]
                dic['Ingridients']=table_values[i][3]
                dic['Procedure']=table_values[i][4]
                dic['Time']=table_values[i][5]
                dic['Yield']=table_values[i][6]
                result.append(dic)
    return result, None