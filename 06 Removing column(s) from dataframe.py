columns = ['Col1', 'Col2', ...]
df.drop(columns, inplace=True, axis=1)

# This will delete one or more columns in-place. 
#Note that inplace=True was added in pandas v0.13 and won't work on older versions, 
#do you'd have to do assign the result back in that case:

df = df.drop(columns, axis=1)
