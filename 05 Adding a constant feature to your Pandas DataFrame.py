import pandas as pd
import re

column= ['symbols', 'sym_names', 'sr_no']
symbols= ['$','#','^', '*','@']
sym_names= ['dollar','pound', 'hat', 'star', 'at']
sr_no = [1,2,3,4,5]

test_df = pd.DataFrame({
                        'sr_no' : [1,2,3,4,5],
                         'symbols' : ['$','#','^', '*','@'],
                         'sym_names' : ['dollar','pound', 'hat', 'star', 'at']

    })
print("Before adding constant feature")
print(test_df)

print("*******************************************")
test_df_new= test_df.assign(dataset='training')
print("After adding constant feature")
print(test_df_new)


print("*******************************************")
df_col_merged =pd.concat([test_df, test_df_new], axis=0)
print("The merged datasframe columnwise: ")
print(df_col_merged)
