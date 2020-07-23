import numpy as np 
import pandas as pd 

#Before running this code, ensure that your missing values are all set to numpy not a number i.e (NaN)
#Use dataframename.replace('character representing missing value', np.nan, inplace=True)

#Function takes in the name of your dataset.

def errorReplacer(data):
    df = data
    x = pd.DataFrame(df.isnull().sum())
    x = x[x[0] > 0]

    for i in x.index:
        if df[i].dtypes == 'float':
            mean = df[i].mean()
            df[i].replace(np.nan, mean, inplace = True)
            if df[i].dtypes == 'int':
                df[i] = df[i].astype(int)
            elif df[i].dtypes == 'float':
                pass
        elif df[i].dtypes == 'object':
            mode = df[i].mode()
            df[i].replace(np.nan, mode, inplace = True)
    return df


