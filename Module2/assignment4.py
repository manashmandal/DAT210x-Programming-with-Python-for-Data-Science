import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
df.columns = df.loc[1]
df = df[2:]



# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df.dropna(axis=0, thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
print(df.head())

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
del df['RK']

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
print(df.shape[0])


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

df = df[df.PLAYER != 'PP']
df = df[df.PLAYER != 'PLAYER']

print(df.shape[0])
len(pd.Series.unique(df['PCT']))
print(int(df['GP'][16]) + int(df['GP'][17]))