import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_csv('Datasets/servo.data', delimiter=',')

# print(df.describe())


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
df.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']


vgain_5_count = 0

for vgain_value in (df['vgain']):
    if vgain_value == 5:
        vgain_5_count += 1

print(vgain_5_count)

both_count = 0

for i in range(len(df['motor'])):
    if df['motor'][i] == 'E':
        if df['screw'][i] == 'E':
            both_count += 1

print(both_count)


accountable_vgain = []

for i in range(len(df['pgain'])):
    if (df['pgain'][i] == 4):
        accountable_vgain.append(df['vgain'][i])


print(sum(accountable_vgain) / len(accountable_vgain))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..



# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



