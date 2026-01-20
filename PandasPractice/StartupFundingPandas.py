# Startups in 2021 end.csv
import pandas as pd 

df = pd.read_csv("PandasPractice/Startups in 2021 end.csv", delimiter=',', parse_dates=[3], date_format={'Date Joined': '%d/%m/%y'})
print(df)
print("df - datatypes", df.dtypes)
print("df.info() : ", df.info())

# Display the last three rows 
print("Last three rows:")
print(df.tail(3))

# Display the first three rows
print("First three rows:")
print(df.head(3))
print()

# Summary of statistics of DataFrame using describe() method
print("Summary of statistics of Dataframe using describe() method:", df.describe())

# Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape():", df.shape)
print()

# Access the Name Column 
Industry = df['Industry']
print("Access the Name column: df: ")
print(Industry)
print()

'''Access the Name column: df: 
0              Artificial intelligence
1                                Other
2                              Fintech
3                              Fintech
4         Internet software & services
                    ...
931       Internet software & services
932            Artificial Intelligence
933        Data management & analytics
934                      Cybersecurity
935    E-commerce & direct-to-consumer'''

# Access the Multiple Columns 
Industry_Company = df[['Industry', 'Company']]
print("Access the Multiple Columns: df :")
print(Industry_Company)
print()

'''Access the Multiple Columns: df :
                            Industry          Company
0            Artificial intelligence        Bytedance
1                              Other           SpaceX
2                            Fintech           Stripe
3                            Fintech           Klarna
4       Internet software & services            Canva
..                               ...              ...
931     Internet software & services        YipitData
932          Artificial Intelligence         Anyscale
933      Data management & analytics  Iodine Software
934                    Cybersecurity       ReliaQuest
935  E-commerce & direct-to-consumer       Pet Circle
'''

"""There are four primary ways to select rows with .loc. These include:
Selecting a single row
Selecting multiple rows
Selecting a slice of rows
Conditional row selection"""

# Case 1 : using .loc - default case - starts here
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['Industry'] == 'Select Investors']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'Industry']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['Industry','Company']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'Country':'Industry']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['Industry'] == 'Select Investor','Country':'Industry']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as ID
# Why Second cycle - Note Index - , index_col='ID'

# valuation = pd.char.replace(valuation, "$", "")
# valuation = valuation.astype(float)

# Q -> Can we add column name if there is missing Column name in the Dataset.  
df_index_col = pd.read_csv('PandasPractice/Startups in 2021 end.csv', delimiter="," ,parse_dates=[3], date_format={'Date Joined': '%d/%m/%Y'} , index_col='ID')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Second cycle - with index_col as ID 

print(df_index_col.index)
'''
Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
       ...
       926, 927, 928, 929, 930, 931, 932, 933, 934, 935],
'''

#Selecting a single row using .loc
second_row = df_index_col.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[1, 2]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[1 : 4]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['Industry'] == 'Select Investors']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:4,'Industry']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:4,['Industry','Company']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:4,'Country':'Industry']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['Industry'] == 'Select Investors','Country':'Industry']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")


""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame

# 0,Bytedance,$140,4/7/2017,China,Beijing,Artificial intelligence,"Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group"

df.loc[len(df.index)] = [0,'Bytedance', '$140', 4/7/2017,'China','Beijing','Artificial intelligence',"Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group"] 
print("Modified DataFrame - add a new row:")
print(df)
print()

# Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)


# delete Company column
df.drop('Company', axis=1, inplace=True)
# delete Industry column
df.drop(columns='Industry', inplace=True)
# delete City and Country columns
df.drop(['Country', 'City'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete Company , Industry , Country , City , column :")
print(df)

#Rename Labels in a DataFrame
# rename column City to City_Changed
df.rename(columns= {'City': 'City_Changed'}, inplace=True)
# rename columns 'Industry' and 'Country'
df.rename(mapper= {'Industry': 'Industry_Changed', 'Valuation ($B)':'Valuation_B'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)

#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)

print(df.columns)

# 1. Clean the string and 2. Convert safely to float
df['Valuation_B'] = pd.to_numeric(
    df['Valuation_B'].astype(str).str.replace(r'[$,]', '', regex=True), 
    errors='coerce'
).fillna(0)

print(df['Valuation_B'].head(100))



#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25
selected_rows = df.query('ID == \'Select Investors\'')

print(selected_rows.to_string())
print(len(selected_rows))



# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='Valuation_B')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Valuation_B', 'Date Joined'])

print("Sorting by 'Valuation_B' (ascending) and then by 'Date Joined' (ascending):\n")
print(df1.to_string(index=False))

#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped = df.groupby('Date Joined')['Valuation_B'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)



# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.


# to be continued....