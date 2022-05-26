import pandas as pd
import numpy as np




def find_empty_row(DataFrame, stationary_Column_Name):
    
    column_list =  DataFrame.columns.values.tolist()
    column_list.remove(stationary_Column_Name)


    
    for col in column_list:
        empty_list = DataFrame[col].isnull().values.any()
        count_for_empty= DataFrame[col].isnull().sum()
        row_index_for_nan = DataFrame[col].isnull()
        
        if empty_list :
                # print ('Blank observed for Column : {}  '.format (col))
                # print ('Total number of blank row : {}'. format(count_for_empty))
                
                for row in row_index_for_nan:
                    _reqrd_col = DataFrame.loc[row_index_for_nan,[stationary_Column_Name]]
                print ( 'Column Name = {} :  Total Blank Row = {} : For Value = {}'.format(col, count_for_empty,_reqrd_col))
        else:
            print ('Column Name = {} :  Total Blank Row = {} '.format(col, count_for_empty))
            

# Invocation pattern 


df =  pd.read_csv('iris.csv')
df1 = df.mask(np.random.random(df.shape) < .1)
df2 =df1.copy()
df2['MyFirstCol'] = np.arange(len(df2))



find_empty_row (df2, 'MyFirstCol')


        
