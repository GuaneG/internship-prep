# In this script, you will learn how to create your own data, along with how to work with data that already exists.

# Print function for this script change parameter to see the only 1 output of the script. This is useful for debugging and for keeping the output clean.
def my_print(*args, isToBePrinted=False, **kwargs):
    if isToBePrinted:
        print(*args, **kwargs)

# Getting started

import pandas as pd

# Creating data
# There are two core objects in pandas: Series and DataFrame. 
# DataFrame is a table.It contains array of individual entries, each of which has a value.
# Each entry corresponds to a row(or record) and a column.

first_df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
my_print(first_df) 

# In this example the "0, No" entry has the value of 131. The "0, Yes" entry has the value of 50.And so on.
# DataFrame entries are not restricted to integers.

second_df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
my_print(second_df)

# We are using the pd.DataFrame() constructor to create to generate these DataFrame objects.
# The syntax for declaring a new one is a dictionary, where the keys are the column names(Bob and Sue in this example) 
# and the values are lists of entries for each column.This is the standart way to create a DataFrame.

# The dictionary-list constructor assigns values to the column labels, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the row labels. 
# Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.

# The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:

third_df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
my_print(third_df)

# You can also create CSV from a DataFrame using the to_csv() method. This is useful for exporting data to share with others, or for saving your work.

third_df.to_csv("C:\\Projects\\internship-prep\\example-data\\product_reviews.csv")



# Series 
# A Series, by contrast, is a sequence of data values. 
# If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

first_series = pd.Series([1, 2, 3, 4, 5])
my_print(first_series)

# A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. 
# However, a Series does not have a column name, it only has one overall name:

second_series = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
my_print(second_series)


# The Series and the DataFrame are intimately related.
# It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". 
# We'll see more of this in the next section of this tutorial.


# Reading data

# Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file. 
# When you open a CSV file you get something that looks like this:
#
# #   #   #   #   #   #   #   #  #  
# Product A,Product B,Product C, #
# 30,21,9,                       #
# 35,34,1,                       #
# 41,11,11                       #
# #   #   #   #   #   #   #   #  #  

# So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.
# Let's now set aside our toy datasets and see what a real dataset looks like when we read it into a DataFrame. 
# We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:

grades = pd.read_csv("C:\\Projects\\internship-prep\\example-data\\grades.csv")
my_print(grades)

# We can use the shape attribute to check how large the resulting DataFrame is:

my_print(grades.shape)

# The first number is the number of rows, and the second is the number of columns. So the grades dataset has 15 rows and 10 columns.


# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows of the DataFrame:

my_print(grades.head())

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
# For example, if this CSV file had a built-in index, we could have specified that with the index_col parameter. 
# To make pandas use a column for the index, we can specify an index_col.

grades = pd.read_csv("C:\\Projects\\internship-prep\\example-data\\grades.csv", index_col="student_id")
my_print(grades.head())

# In the result table our student_id column has been used as the index.


# Native Accessors
# Native Python objects provide good ways of indexing data. Pandas carries all of these over, which helps make it easy to start with.


# In Python, we can access the property of an object by accessing it as an attribute.
# A book object, for example, might have a title property, which we can access by calling book.title. 
# Columns in a pandas DataFrame work in much the same way.

my_print(grades.math.head())

# If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:

my_print(grades["math"].head())

# These are the two ways of selecting a specific Series out of a DataFrame. 
# Neither of them is more or less syntactically valid than the other, but the indexing operator []
# does have the advantage that it can handle column names with reserved characters in them 
# (e.g. if we had a country providence column, reviews.country providence wouldn't work).

# Doesn't a pandas Series look kind of like a fancy dictionary? 
# It pretty much is, so it's no surprise that, to drill down to a single specific value, we need only use the indexing operator [] again:

# Because of we created the grades DataFrame with student_id as the index, we must use the student_id to access specific values:
my_print(grades["math"][1001])

# If we had created the DataFrame without an index, we would have to use the default integer index to access specific values:
grades2 = pd.read_csv("C:\\Projects\\internship-prep\\example-data\\grades.csv")
my_print(grades2["math"][0])



# Indexing in pandas

# The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem.
# As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, loc and iloc. 
# For more advanced operations, these are the ones you're supposed to be using.

# Index-based selection
# Pandas indexing works in one of two paradigms. 
# The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm
# To select the first row of data in a DataFrame, we may use the following:

my_print(grades.iloc[0])

# Both loc and iloc are row-first, column-second. 
# This is the opposite of what we do in native Python, which is column-first, row-second.

# This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. 
# To get a column with iloc, we can do the following:

my_print(grades.iloc[:, 0]) # Bütün rowları seçmek için : kullanılır. 0 ise first_name columnunu seçer.

# On its own, the : operator, which also comes from native Python, means "everything".
# When combined with other selectors, however, it can be used to indicate a range of values. 
# For example, to select the first three rows and first two columns:

my_print(grades.iloc[0:3, 0:2]) # İlk üç row ve ilk iki columnu seçer. 0:3 ifadesi 0,1,2 rowlarını seçer. 0:2 ifadesi ise 0,1 columnlarını seçer.

my_print(grades.iloc[1:3, 0:2]) # İlk row dışında üç row ve ilk iki columnu seçer. 1:3 ifadesi 1,2 rowlarını seçer. 0:2 ifadesi ise 0,1 columnlarını seçer.

my_print(grades.iloc[[0, 1, 2], 0]) # 0, 1, ve 2 rowlarını ve 0. columnu seçer.

my_print(grades.iloc[-5:, :]) # Son 5 rowu seçer. -5 ifadesi son 5 rowu seçer. : ifadesi ise bütün columnları seçer.

# Label-based selection

# The second paradigm for attribute selection is the one followed by the loc operator: label-based selection.
# In this paradigm, it's the data index value, not its position, which matters.
# For example, to get the first entry in the math column, we can use the loc operator:

my_print(grades.loc[1001, "math"])

# iloc is conceptually simpler than loc because it ignores the dataset's indices.
# When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position.
# loc, by contrast, uses the information in the indices to do its work. 
# Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. 
# For example, here's one operation that's much easier using loc

my_print(grades.loc[1001:1005, "math":"english"]) # 1001'den 1005'e kadar olan rowları ve math'ten english'e kadar olan columnları seçer. 1001:1005 ifadesi 1001, 1002, 1003, 1004, 1005 rowlarını seçer. math:english ifadesi ise math, programming, database, english columnlarını seçer.

my_print(grades.loc[:, "math":"english"]) # Bütün rowları ve math'ten english'e kadar olan columnları seçer. : ifadesi bütün rowları seçer. math:english ifadesi ise math, programming, database, english columnlarını seçer.


# Manipulating the index
# Label-based selection derives its power from the labels in the index. 
# Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.
    
# The set_index() method can be used to do the job. Here is what happens when we set_index to the math field:
grades2.set_index("first_name")
my_print(grades2)
# Notice that the set_index() method does not modify the original DataFrame. It returns a new DataFrame with the modified index.
# To modify the original DataFrame, we can use the inplace parameter:
grades2.set_index("first_name", inplace=True)
my_print(grades2)



# Conditional selection

# So far we've been indexing various strides of data, using structural properties of the DataFrame itself. 
# To do interesting things with the data, however, we often need to ask questions based on conditions.
# For example, we might want to know how many students scored above 90 in math.

my_print(grades.math > 90)

# This operation produced a Series of True/False booleans based on the country of each record. 
# This result can then be used inside of loc to select the relevant data:

my_print(grades.loc[grades.math > 90, :]) # math'ten 90'dan büyük olan rowları ve bütün columnları seçer. grades.math > 90 ifadesi math'ten 90'dan büyük olan rowları seçer. : ifadesi ise bütün columnları seçer.

# We can use the ampersand (&) to bring the two questions together:

my_print(grades.loc[(grades.math > 90) | (grades.english > 80), :]) # math'ten 90'dan büyük olan veya english'ten 80'dan büyük olan rowları ve bütün columnları seçer. grades.math > 90 ifadesi math'ten 90'dan büyük olan rowları seçer. grades.english > 80 ifadesi ise english'ten 80'dan büyük olan rowları seçer. : ifadesi ise bütün columnları seçer.

my_print(grades.loc[(grades.math > 90) & (grades.english > 93), :]) # math'ten 90'dan büyük olan ve english'ten 93'den büyük olan rowları ve bütün columnları seçer. grades.math > 90 ifadesi math'ten 90'dan büyük olan rowları seçer. grades.english > 93 ifadesi ise english'ten 93'den büyük olan rowları seçer. : ifadesi ise bütün columnları seçer.

# Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

# The first is isin. isin is lets you select data whose value "is in" a list of values.
# For example, here's how we can use it to select students whose math score is either 90, 95, or 100:

my_print(grades.loc[grades.math.isin([90,91,92,95,100]), :]) # math'ten 90, 95, veya 100 olan rowları ve bütün columnları seçer. grades.math.isin([90, 95, 100]) ifadesi math'ten 90, 95, veya 100 olan rowları seçer. : ifadesi ise bütün columnları seçer.

# The second is isnull (and its companion notnull). 
# These methods let you highlight values which are (or are not) empty (NaN). 
# For example, to filter out students who do have a programming score, we can do the following:

my_print(grades.loc[grades.programming.notnull(), :]) # programming'ten null olmayan rowları ve bütün columnları seçer. grades.programming.notnull() ifadesi programming'ten null olmayan rowları seçer. : ifadesi ise bütün columnları seçer.


# Assigning data

# Going the other way, assigning data to a DataFrame is easy. You can assign either a constant value:

grades["passed_math"] = grades.math >= 70 
# Yeni column oluşturur, math'ten 70'e eşit veya büyük olan rowlara True, diğerlerine False atar.
my_print(grades)

# Another example of assigning data is to assign a Series to a column.
grades["reversed_index"] = range(len(grades),0,-1)
my_print(grades, isToBePrinted=True)




# Summary Functions and Maps

# In the last tutorial, we learned how to select relevant data out of a DataFrame or Series. 
# Plucking the right data out of our data representation is critical to getting work done, as we demonstrated in the exercises.

# However, the data does not always come out of memory in the format we want it in right out of the bat.
# Sometimes we have to do some more work ourselves to reformat it for the task at hand.
# This tutorial will cover different operations we can apply to our data to get the input "just right".


# Summary Functions

# Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way. 
# For example, consider the describe() method:

my_print(grades.year.describe())

# This method generates a high-level summary of the attributes of the given column. 
# It is type-aware, meaning that its output changes based on the data type of the input. 
# The output above only makes sense for numerical data; for string data here's what we get:

my_print(grades.department.describe())

# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series, there is usually a helpful pandas function that makes it happen.
# For example, to see the mean of the year column, we can use the mean() function:

my_print(grades.year.mean())

# To see a list of unique values we can use the unique() function:

my_print(grades.department.unique())

# To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:

my_print(grades.department.value_counts())


#27,28.05.2026 AWS Cloud Practitioner Essentials baktım.
#29.05.2026 günün ilk yarısı AWS Cloud da Database Services baktım. Günün ikinci yarısı ise map'lere başladım.
#29.05.2026 21:08 Gün bitti; pandas maps te kaldın mapsten devam et.


# Maps

# A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values.
# In data science we often have a need for creating new representations from existing data, or
# for transforming data from the format it is in now to the format that we want it to be in later. 
# Maps are what handle this work, making them extremely important for getting your work done!

# There are two mapping methods that you will use often.

# map() is the first, and slightly simpler one. 
# For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:



