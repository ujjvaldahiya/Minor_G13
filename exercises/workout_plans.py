import pandas as pd
def find_plan():
    df=pd.read_excel('workout_plans.xlsx')
    df=df.fillna(value=0)
    df2=pd.read_excel('datasheet_exer.xlsx')
    df2=df2[['ID','EXERCISE_NAME']]
    dt2=df2.values.tolist()
    dt=df.values.tolist()
    
    plans=[]
    
    for i in dt:
            dic={}
            dic['name']=i[0]
            dic['difficulty']=i[1]
            ex=[]
            for j in range(2,10):
                if i[j]!=0:
                    dic2={}
                    dic2['id']=int(i[j])
                    dic2['name']=dt2[int(i[j])-101][1]
                    ex.append(dic2)
            dic['exercises']=ex
            plans.append(dic)
    return plans