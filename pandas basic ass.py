# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:03:24 2023

@author: user
"""

'''Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
import pandas as pd
s=[4,8,15,16,23,42]
se=pd.Series(s)
print(se)

Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it.
import pandas as pd
Fruits=["apple","mango","pomogranate","chikoo","pear",'banana',"grapes",'strawberry','pineapple','peru']
s=pd.Series(Fruits)
print(s)

Q3. Create a Pandas DataFrame that contains the following data:
import pandas as pd
de={"Name":["Alice",'Bob','Claire'],
    "Age":[25,30,27],
    "Gender":["Female","Male","Female"]}
df=pd.DataFrame(de)
print(df)

Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
Ans: DataFrme make table and put data in it which we are give in variable, Series make data into series not in table like dataframe

Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
you give an example of when you might use one of these functions?
Ans:
    -height = it is use for fetch top 5 data or how much we want. for e.g.: while fetchting top 5 or specific data
    -tail= it is use for fetch last 5 data or how much we want. for e.g.: while fetching last 5 data.
    -type= to get what type of data type it is. for e.g.:to identifying whjich datatype we have given to follow its property.
    -read=to read the file by giving format of it. for e.g.: to reading csv file.
    
Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
Ans: Dataframe is mutable.

Q7. Create a DataFrame using multiple Series. Explain with an example.
import pandas as pd
Name=pd.Series(["Vinayak","Hitesh","Santosh","Sunita"])
Relation=pd.Series(["Myself","Brother","Father","Mother"])
Age=pd.Series([24,19,45,46])
df=pd.DataFrame({"Name":Name,"Relation":Relation,"Age":Age})
print(df)
'''