# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 04:38:23 2022

@author: Dell
"""
import pandas as pd
lst1=[1,2,3,4]
lst2=[7,8,9,10]

dict={"col1":lst1,"col2":lst2}
df=pd.DataFrame(dict)
df
#########################
#NOW to add 3 in single column
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
"""
    col1  col2
0     4    10
1     5    11
2     6    12
3     7    13
"""

#########################
#Now to apply on single column
df=df["col1"].apply(add_3)
df

"""
    col1  col2
0     4     7
1     5     8
2     6     9
3     7    10


"""

#######################################
lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=[9,10,11,12]
lst4=[13,14,15,16]
d={"A":lst1,"B":lst2,"C":lst3,"C":lst4,"D":lst4}
df=pd.DataFrame(d)
df
"""
   A  B   C   D
0  1  5  13  13
1  2  6  14  14
2  3  7  15  15
3  4  8  16  16
"""
df[['A','B']]=df[['A','B']].apply(add_3)
df
"""
   A   B   C   D
0  4   8  13  13
1  5   9  14  14
2  6  10  15  15
3  7  11  16  16

"""

#########################################
#Apply lambda function to single column
df['D']=df['D'].apply(lambda x:x+3)
df
"""
   A   B   C   D
0  4   8  13  16
1  5   9  14  17
2  6  10  15  18
3  7  11  16  19
"""

####################
#apply lambda function to multiple columns
df[['A','B']]=df[['A','B']].apply(lambda x:x-3)
df
"""
   A  B   C   D
0  1  5  13  16
1  2  6  14  17
2  3  7  15  18
3  4  8  16  19
"""

##############################################
import numpy as np
df['A']=df['A'].apply(np.square)
df
"""
    A  B   C   D
0   1  5  13  16
1   4  6  14  17
2   9  7  15  18
3  16  8  16  19
"""

############################
df["B"]=df["B"].transform(add_3)
df

"""
    A   B   C   D
0   1   8  13  16
1   4   9  14  17
2   9  10  15  18
3  16  11  16  19
"""

########################
#Using dataframe.map()
df["B"]=df["B"].map(lambda x:x-3)
df
"""
    A  B   C   D
0   1  5  13  16
1   4  6  14  17
2   9  7  15  18
3  16  8  16  19
"""
#####################
################################
#shuffling of rows
tech={'courses':['A','B','C','D'],
      'fees':[200,300,400,500],
      'duration':[2,3,4,5],
      'discount':['1%','2%','3%','4%']
            
      }
df=pd.DataFrame(tech)
df
"""
     courses  fees  duration discount
0       A   200         2       1%
1       B   300         3       2%
2       C   400         4       3%
3       D   500         5       4%
"""
######################
#shuffle dataframe rows and return all rows
df1=df.sample(frac=1)
df1
"""
    courses  fees  duration discount
0       A   200         2       1%
1       B   300         3       2%
3       D   500         5       4%
2       C   400         4       3%
"""

################################

df2=df.sample(frac=0.5)
df2
"""
     courses  fees  duration discount
3       D   500         5       4%
2       C   400         4       3%
"""
##############################
df1=df.sample(frac=1).reset_index()
df1

"""
     index courses  fees  duration discount
0      1       B   300         3       2%
1      3       D   500         5       4%
2      0       A   200         2       1%
3      2       C   400         4       3%
"""

####################
df1=df.sample(frac=1).reset_index(drop=True)
df1
"""
    courses  fees  duration discount
0       C   400         4       3%
1       A   200         2       1%
2       B   300         3       2%
3       D   500         5       4%
"""

#######################
df3=df.iloc[np.random.permutation(df.index)]
df3
"""
    courses  fees  duration discount
0       A   200         2       1%
2       C   400         4       3%
3       D   500         5       4%
1       B   300         3       2%
"""

########################
df3=df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
df3
"""
   courses  fees  duration discount
0       D   500         5       4%
1       C   400         4       3%
2       A   200         2       1%
3       B   300         3       2%
"""
##########################
df2=df.apply(lambda x:x.sample(frac=1).values)
df2
"""
    courses  fees  duration discount
0       C   500         3       4%
1       B   400         4       1%
2       A   300         2       2%
3       D   200         5       3%
"""
###################################
#shuffle data frame randomly by rows and columns
df2=df.sample(frac=1,axis=1).sample(frac=1,axis=0).reset_index(drop=True)
df2
"""
    fees courses  duration discount
0   400       C         4       3%
1   200       A         2       1%
2   500       D         5       4%
3   300       B         3       2%
"""
##############################################
#########################################
#covert Nan
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark",np.nan,"Hadoop","Python","pandas",np.nan,"Java"],
    'Fee' :[20000,25000, np.nan,22000,24000,np.nan,22000],
    'Duration':[np.nan,'40days','35days', np.nan,'60days','50days','55days'],
    'Discount':[1000,np.nan,1500,np.nan,2500,2100,np.nan]
              }
df = pd.DataFrame(technologies)
print(df)
###########################################
#Convert Nan to empty string
df2=df.replace(np.nan,"",regex=True)
df2
"""
   Courses      Fee Duration Discount
0   Spark  20000.0            1000.0
1          25000.0   40days         
2  Hadoop            35days   1500.0
3  Python  22000.0                  
4  pandas  24000.0   60days   2500.0
5                    50days   2100.0
6    Java  22000.0   55days  
"""
#########################################
#multiple columns replace the string
df4=df[["Courses","Fee"]].replace(np.nan,"",regex=True)
df4
"""
   Courses      Fee
0   Spark  20000.0
1          25000.0
2  Hadoop         
3  Python  22000.0
4  pandas  24000.0
5                 
6    Java  22000.0
"""
###################################
#Applying empty space for all data frame using fillna()
df5=df.fillna("")
df5
"""
   Courses      Fee Duration Discount
0   Spark  20000.0            1000.0
1          25000.0   40days         
2  Hadoop            35days   1500.0
3  Python  22000.0                  
4  pandas  24000.0   60days   2500.0
5                    50days   2100.0
6    Java  22000.0   55days 
"""   
#######################
##Applying empty space for single column useing fillna()
df6=df["Courses"].fillna("")
df6
"""
0     Spark
1          
2    Hadoop
3    Python
4    pandas
5          
6      Java
Name: Courses, dtype: object
"""
######################
df7=df.Courses.fillna("")
df7
"""
0     Spark
1          
2    Hadoop
3    Python
4    pandas
5          
6      Java
Name: Courses, dtype: object
"""
#############################
#Replace single column Nan with zeros
df8=df["Courses"].fillna(0)
df8
"""
0     Spark
1         0
2    Hadoop
3    Python
4    pandas
5         0
6      Java
Name: Courses, dtype: object
"""
##############################
#replace nan with some value
df9=df["Courses"].replace(np.nan,"value",regex=True)
df9
"""
0     Spark
1     value
2    Hadoop
3    Python
4    pandas
5     value
6      Java
Name: Courses, dtype: object
"""
##################################
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","male","Hadoop","Python","pandas","male","Java"],
    'Fee' :[20000,25000, np.nan,22000,24000,np.nan,22000],
    'Duration':[np.nan,'40days','35days', np.nan,'60days','50days','55days'],
    'Discount':[1000,np.nan,1500,np.nan,2500,2100,np.nan]
              }
df = pd.DataFrame(technologies)
print(df)
"""
   Courses      Fee Duration  Discount
0   Spark  20000.0      NaN    1000.0
1    male  25000.0   40days       NaN
2  Hadoop      NaN   35days    1500.0
3  Python  22000.0      NaN       NaN
4  pandas  24000.0   60days    2500.0
5    male      NaN   50days    2100.0
6    Java  22000.0   55days       NaN
"""
###########################################
#replace Courses column male with female
df10=df["Courses"].replace("male","female",regex=True)
df10
df11=df.apply(lambda x:x.replace("male","Hero",regex=True))
df11
"""
0     Spark
1    female
2    Hadoop
3    Python
4    pandas
5    female
6      Java
Name: Courses, dtype: object
"""
df11=df.iloc[:,2:4]
df11
"""

    Duration  Discount
0      NaN    1000.0
1   40days       NaN
2   35days    1500.0
3      NaN       NaN
4   60days    2500.0
5   50days    2100.0
6   55days       NaN
"""

#########################
################################
#change column data types
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration ':['30day','40days','35days', '40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)
"""

Courses       object
Fee            int64
Duration      object
Discount     float64
dtype: object
"""
#############################################3
#To covert object data types to string
df2=df.convert_dtypes()
df2.dtypes
"""

Courses       string
Fee            Int64
Duration      string
Discount     Float64
dtype: object
"""
##################
#covert data frame as object type
df3=df.astype(str)
df3.dtypes
"""

Courses      object
Fee          object
Duration     object
Discount     object
dtype: object
"""
df3=df3.convert_dtypes()
df3.dtypes
df3=df3.astype(str)
df3.dtypes
#################
#change type of one or multiple column data type
df4=df.astype({"Fee":int,"Discount":float})
df4.dtypes
"""

Courses       object
Fee            int32
Duration      object
Discount     float64
dtype: object
"""
################################
df5=df.astype({"Courses":int},errors='raise')
# ValueError: invalid literal for int() with base 10: 'Spark'
df5.dtypes
#####################
df6=df.astype(str)
df6.dtypes
"""
Courses      object
Fee          object
Duration     object
Discount     object
dtype: object
df6=df6.infer_objects()
df6.dtypes
"""
####################
#convert numeric types
df6['Fee']=pd.to_numeric(df6['Fee'])
df6.dtypes
"""
Courses      object
Fee           int64
Duration     object
Discount     object
dtype: object
"""
############################
#To apply to multiple coulumns
df6['Discount']=df6['Discount'].apply(pd.to_numeric)
df6.dtypes

df[['Fee','Discount']]=df[['Fee','Discount']].apply(pd.to_numeric)
df.dtypes
"""
Courses       object
Fee            int64
Duration      object
Discount     float64
dtype: object
"""
######################
####################
###iloc
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days',np.nan,None,'55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
index_labels=['r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=index_labels)
print(df)
"""
     Courses    Fee Duration  Discount
r1    Spark  20000   30days      1000
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
r4   Python  22000   40days      1200
r5   pandas  24000      NaN      2500
r6   Oracle  21000     None      2100
r7     Java  22000   55days      2000
"""
#################################
#Select single row
df.iloc[1]
"""
Courses     PySpark
Fee           25000
Duration     40days
Discount       2300
Name: r2, dtype: object
"""
#####################
#Select single column 
df.iloc[:,0]
"""
r1      Spark
r2    PySpark
r3     Hadoop
r4     Python
r5     pandas
r6     Oracle
r7       Java
Name: Courses, dtype: object
"""
########################
#To access multiple rows,u need to give double sqaure bracket
df.iloc[[1,2]]
"""
    Courses    Fee Duration  Discount
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
"""
###################
#Here you will get cell value
df.iloc[1,2]

#'40days'
####################
#To display 0,1,2 columns
df.iloc[:,[0,1,2]]
"""
    Courses    Fee Duration
r1    Spark  20000   30days
r2  PySpark  25000   40days
r3   Hadoop  26000   35days
r4   Python  22000   40days
r5   pandas  24000      NaN
r6   Oracle  21000     None
r7     Java  22000   55days
"""


#########################
#To select rows between 0,1,2,3 excluding 4,look to rows not to column
df.iloc[0:4]
"""
     Courses    Fee Duration  Discount
r1    Spark  20000   30days      1000
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
r4   Python  22000   40days      1200
"""
#####################
#to select columns from 0,1,2,3 excluding 4
df.iloc[:,1:4]
"""
     Fee Duration  Discount
r1  20000   30days      1000
r2  25000   40days      2300
r3  26000   35days      1500
r4  22000   40days      1200
r5  24000      NaN      2500
r6  21000     None      2100
r7  22000   55days      2000
"""
############################
#To select alternate rows in step of 2 ,here we will get r1 and r3
df.iloc[0:4:2]
"""
    Courses  Fee Duration  Discount
r1   Spark  20000   30days      1000
r3  Hadoop  26000   35days      1500
"""
#######################
#To select alternate columns in step of 2
df.iloc[:,1:4:2]
"""
     Fee  Discount
r1  20000      1000
r2  25000      2300
r3  26000      1500
r4  22000      1200
r5  24000      2500
r6  21000      2100
r7  22000      2000
"""


#########################
#accessing coulmns using conditions
df.iloc[list(df['Fee']>=24000)]

"""
    Courses    Fee Duration  Discount
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
r5   pandas  24000      NaN      2500
"""

################################
#############################
#loc

# if you want to access single row by label not an index then loc method is used

df.loc['r2']
"""
Courses     PySpark
Fee           25000
Duration     40days
Discount       2300
Name: r2, dtype: object
"""


#if you want to access multiple rows then use [[]] double square bracket
df.loc[['r2','r3']]
"""
    Courses    Fee Duration  Discount
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
"""

#######################
#select rows in range of r1 to r4,here r4 is getting displayed
df.loc['r1':'r4']
"""
     Courses    Fee Duration  Discount
r1    Spark  20000   30days      1000
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
r4   Python  22000   40days      1200
"""
#select alternate rows using label index
df.loc['r1':'r5':2]
#here you will get 
 #   Courses    Fee Duration  Discount
#r1   Spark  20000   30days      1000
#r3  Hadoop  26000   35days      1500
#r5  pandas  24000      NaN      2500
#####################################
df.iloc[1:5:2]

"""
  Courses    Fee Duration  Discount
r2  PySpark  25000   40days      2300
r4   Python  22000   40days      1200
"""

#To select multiple columns
df.loc[:,["Courses","Fee"]]
"""  Courses    Fee
r1    Spark  20000
r2  PySpark  25000
r3   Hadoop  26000
r4   Python  22000
r5   pandas  24000
r6   Oracle  21000
r7     Java  22000
"""
###########################
#To select range of columns
df.loc[:,'Fee':'Discount']

"""Fee    Duration  Discount
r1  20000   30days      1000
r2  25000   40days      2300
r3  26000   35days      1500
r4  22000   40days      1200
r5  24000      NaN      2500
r6  21000     None      2100
r7  22000   55days      2000
"""
#############################
#using condition,here no need to write list
df.loc[(df['Fee']>=24000)]
df.iloc[list(df['Fee']>=24000)]
"""
    Courses    Fee Duration  Discount
r2  PySpark  25000   40days      2300
r3   Hadoop  26000   35days      1500
r5   pandas  24000      NaN      2500

"""


##########################################
###########################################
#filters
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days',np.nan,None,'55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
#index_labels=['r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
##########################################
df2=df.filter(items=['Courses','Fee'])
df2
"""
    Courses    Fee
r1    Spark  20000
r2  PySpark  25000
r3   Hadoop  26000
r4   Python  22000
r5   pandas  24000
r6   Oracle  21000
r7     Java  22000
"""
#To filter column using like,here axis=1 for column
df2=df.filter(like='ration',axis=1)
df2
"""
    Duration
r1   30days
r2   40days
r3   35days
r4   40days
r5      NaN
r6     None
r7   55days
"""
#################################
#To filter column using regex param,The below example filters column that ends with e
df2=df.filter(regex='e$',axis=1)
df2
"""
      Fee
r1  20000
r2  25000
r3  26000
r4  22000
r5  24000
r6  21000
r7  22000
"""
###############################
#To filter rows
df2=df.filter(items=[3,4],axis=0)
df2
"""
 Courses    Fee Duration  Discount
3  Python  22000   40days      1200
4  pandas  24000      NaN      2500
"""
#######################################
df2=df.filter(items=['Courses'],axis=1)
df2

df2=df.filter(like='4',axis=0)
df2
"""
 Courses    Fee Duration  Discount
4  pandas  24000      NaN      2500
"""
###############################################
##############################################
#Query rows using DataFrame.query()
df2=df.query(" Courses=='Spark'")
df2
"""
Courses    Fee Duration  Discount
0   Spark  20000   30days      1000
"""
#######################################
df2=df.query("Courses !='Spark'")
df2
"""
 Courses    Fee Duration  Discount
1  PySpark  25000   40days      2300
2   Hadoop  26000   35days      1500
3   Python  22000   40days      1200
4   pandas  24000      NaN      2500
5   Oracle  21000     None      2100
6     Java  22000   55days      2000
"""
#######################################
df2=df.query("Courses in('Spark','PySpark') ")
df2
"""
 Courses    Fee Duration  Discount
0    Spark  20000   30days      1000
1  PySpark  25000   40days      2300
"""
############################################
###########################################
#Adding columns
#DataFrame.assign(**kwargs)
import pandas as pd
import numpy as np

technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1000,2300,1000,1200,2500]
          }

df = pd.DataFrame(technologies)
print(df)
tutors=['Ram','Sham','Ghansham','Radhesham','Radhakisan']
df2=df.assign(TutorsAssigned=tutors)
df2
"""
    Courses    Fee  Discount TutorsAssigned
0    Spark  22000      1000            Ram
1  PySpark  25000      2300           Sham
2   Hadoop  23000      1000       Ghansham
3   Python  24000      1200      Radhesham
4   Pandas  26000      2500     Radhakisan
"""
#####################################
#Adding multiple columns
schedule=['10am','12 am','1 pm','3 pm','6 pm']
doubt_session=['9am','11 am','12 pm','2pm','5 pm']
df2=df.assign(schedule=schedule,doubt_session=doubt_session)
df2
"""
    Courses    Fee  Discount schedule doubt_session
0    Spark  22000      1000     10am           9am
1  PySpark  25000      2300    12 am         11 am
2   Hadoop  23000      1000     1 pm         12 pm
3   Python  24000      1200     3 pm           2pm
4   Pandas  26000      2500     6 pm          5 pm
"""
##################################
#To derive column from existing two columns
df2=df.assign(discount_percentage=lambda x:(x.Discount/x.Fee)*100)
df2
"""
   Courses    Fee   Discount  discount_percentage
0    Spark  22000      1000             4.545455
1  PySpark  25000      2300             9.200000
2   Hadoop  23000      1000             4.347826
3   Python  24000      1200             5.000000
4   Pandas  26000      2500             9.615385
"""

###################################
#Insert column to desired location

# Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors', tutors )
print(df)
##############################
import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df.columns)
##################
###################
# Rename a Single Column 
df2=df.rename(columns = {'Courses':'Courses_List'})
print(df2.columns)
df2
"""
   Courses_List    Fee Duration
0        Spark  20000    30day
1      PySpark  25000   40days
2       Hadoop  26000   35days
3       Python  22000   40days
4       pandas  24000   60days
5       Oracle  21000   50days
6         Java  22000   55days
"""
##########################
df3=df.rename({'Courses':'Courses_List'},axis=1)
df3
"""
   Courses_List    Fee Duration
0        Spark  20000    30day
1      PySpark  25000   40days
2       Hadoop  26000   35days
3       Python  22000   40days
4       pandas  24000   60days
5       Oracle  21000   50days
6         Java  22000   55days
"""
##############################
df.rename(columns={'Courses':'Courses_List'},inplace=True)
df
"""
   Courses_List    Fee Duration
0        Spark  20000    30day
1      PySpark  25000   40days
2       Hadoop  26000   35days
3       Python  22000   40days
4       pandas  24000   60days
5       Oracle  21000   50days
6         Java  22000   55days
"""
######################
#To rename multiple columns
df.rename(columns={'Courses':'Courses_List','Fee':'Courses_Fee'},inplace=True)
df
"""
   Courses_List  Courses_Fee Duration
0        Spark        20000    30day
1      PySpark        25000   40days
2       Hadoop        26000   35days
3       Python        22000   40days
4       pandas        24000   60days
5       Oracle        21000   50days
6         Java        22000   55days
"""
##############################################
########################################
###Drop rows
import pandas as pd
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[20000,25000,26000,22000],
    'Duration':['30day','40days',np.nan, None],
    'Discount':[1000,2300,1500,1200]
               }

indexes=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=indexes)
print(df)
######################################
#Drop rows by index label
df1=df.drop(['r1','r2'])
df1
"""
Courses    Fee Duration  Discount
r3  Hadoop  26000      NaN      1500
r4  Python  22000     None      1200
"""
df=pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[[1,3]])
df1
"""
Courses    Fee Duration  Discount
r1   Spark  20000    30day      1000
r3  Hadoop  26000      NaN      1500
"""
###########################
#Delete rows by index range
df=pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[2:])
df1
"""
Courses    Fee Duration  Discount
r1    Spark  20000    30day      1000
r2  PySpark  25000   40days      2300
"""
##########################
#Delete rows when you have default index
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
"""
Courses    Fee Duration  Discount
1  PySpark  25000   40days      2300
2   Hadoop  26000      NaN      1500
3   Python  22000     None      1200
"""
#################################
df=pd.DataFrame(technologies)
df3=df.drop([1,3])
df3
"""
Courses    Fee Duration  Discount
0   Spark  20000    30day      1000
2  Hadoop  26000      NaN      1500
"""
######################################
df=pd.DataFrame(technologies)
df4=df.drop(range(0,2))
df4
"""
Courses    Fee Duration  Discount
2  Hadoop  26000      NaN      1500
3  Python  22000     None      1200

"""
##############################
# Delete Rows inplace
df = pd.DataFrame(technologies,index=indexes)
df.drop(['r1','r2'],inplace=True)
print(df)
######################################
# Delete rows with Nan, None & Null Values
df = pd.DataFrame(technologies,index=indexes)
df2=df.dropna()
print(df2)
"""
Courses    Fee Duration  Discount
r1    Spark  20000    30day      1000
r2  PySpark  25000   40days      2300
"""
#########################################################
############################################
#groupby().sum()
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','55days','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
                })
df = pd.DataFrame(technologies, columns=['Courses','Fee','Duration','Discount'])
print(df)
"""
    Courses    Fee Duration  Discount
0    Spark  22000   30days      1000
1  PySpark  25000   50days      2300
2   Hadoop  23000   55days      1000
3   Python  24000   40days      1200
4   Pandas  26000   60days      2500
5   Hadoop  25000   35days      1300
6    Spark  25000   55days      1400
7   Python  22000   50days      1600
"""


#######################################
df2=df.groupby('Courses').sum()
df2
"""
          Fee  Discount
Courses                 
Hadoop   48000      2300
Pandas   26000      2500
PySpark  25000      2300
Python   46000      2800
Spark    47000      2400
"""
#############################
# Use GroupBy() & compute sum on specific column
df2 = df.groupby('Courses')['Fee'].sum()
print(df2)
"""
Courses
Hadoop     48000
Pandas     26000
PySpark    25000
Python     46000
Spark      47000
Name: Fee, dtype: int64
"""
#######################################
# Using GroupBy multiple column
df2 = df.groupby(['Courses','Duration'])['Fee'].sum()
print(df2)
"""
Courses  Duration
Hadoop   35days      25000
         55days      23000
Pandas   60days      26000
PySpark  50days      25000
Python   40days      24000
         50days      22000
Spark    30days      22000
         55days      25000
Name: Fee, dtype: int64

"""
#####################################
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)
df1

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
df2
#############################################
# Using pandas.merge()
df3= pd.merge(df1,df2)
df3
# Using DataFrame.merge()
df3=df1.merge(df2)
df3
"""
Courses    Fee Duration  Discount
0   Spark  20000   30days      2000
1  Python  22000   35days      1200
"""
df4=pd.merge(df1,df2,on='Courses')
df4
"""
Courses    Fee Duration  Discount
0   Spark  20000   30days      2000
1  Python  22000   35days      1200
"""

# Merge by left Join
df3=pd.merge(df1,df2, on='Courses', how='left')
print(df3)
"""
    Courses    Fee Duration  Discount
0    Spark  20000   30days    2000.0
1  PySpark  25000   40days       NaN
2   Python  22000   35days    1200.0
3   pandas  30000   50days       NaN
"""
# Merge by right Join
df3=pd.merge(df1,df2, on='Courses', how='right')
print(df3)
"""
Courses      Fee Duration  Discount
0   Spark  20000.0   30days      2000
1    Java      NaN      NaN      2300
2  Python  22000.0   35days      1200
3      Go      NaN      NaN      2000
"""
############################################
#join
# pandas join 
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)
##############################
df2=df.drop(1,axis=0)
df2
df2=df.drop(columns=['Fee'],axis=0)
df2
df
df3=df.drop(['Fee'],axis=1)
df3
