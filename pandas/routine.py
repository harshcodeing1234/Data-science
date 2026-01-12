import pandas as pd #type:ignore

data = {
    'Date':['03/12/25','04/12/25','05/12/25','06/12/25','07/12/25','08/12/25'],
    '10:00 - 12:00':['DBMS','DBMS','DBMS','DBMS','DBMS','Feature Enginering'],
    '02:00 - 04:00':['Software Enginering','Software Enginering','Software Enginering','Software Enginering','Feature Enginering','Feature Enginering'],
    '05:00 - 07:00':['Java','Java','Java','Java','Java','Disaster manegment'],
    '9:00 - 11:00':['Web Technology','Web Technology','Web Technology','Web Technology','Web Technology','Disaster manegment']
}

df = pd.DataFrame(data)
print(df)

df = df.to_excel('studyplan.xlsx',index=False)





