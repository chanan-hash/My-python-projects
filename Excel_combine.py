import pandas as pd
import glob
# before starting you also need "openpyxl" library because some functions in the background are reading from it
# this is what pycharm wrote for me, so do also 'pip install openpyxl' in the command kine or from pycharm itself (setting\interpreter, etc...)
# this means that 'openpyxl' it is more known library to python

# !!!!Important!!!!
# Before working and coding on your excel file, you need to understand your file whats wrinte in it and what do oyu want to do with it
# and to to work "on blind" becuase then you can do mistake or just create a mess with your file, and not to get your goal


location = ('C:\\Users\\חנן\\Desktop\\טפסים למחנה\\*.xlsx') # the location of the file + the format (xlsx - excel). we need double slash \\, or 'r' before the string of the file path
# if it is excel format we need to check if it saved as .xls (old version of excel) or .xlsx (newer version of excel) it is important for the file reading
excel_files = glob.glob(location) # creating a list of all the  differnt file path names - all the files the end with .xlsx, if the finish is not correct it will print an empty list

# print(excel_files)

pd.set_option('display.max_rows',91) # the number of the rows is according to what it is written

# we will create a data frame - like an empty excel file

df1 = pd.DataFrame() # like a spreadsheet to put inside it akk the excel files

for excel_file in excel_files: # we are iterating glob (the list of all the excel file) and put them in one spreadsheet
    df2 = pd.read_excel(excel_file) #each iteration we are
    df1 = pd.concat([df1,df2], ignore_index=True) # contact function combine the given data frames, and we are putting them in a list
                                #ignore index --> instead working with the  regular numbers, we are working with the index

# df1.fillna(value="",inplace="") if we want otchang all kind of names/arguments
df1.to_excel("C:\\Users\\חנן\\Desktop\\טפסים למחנה\\all_capm_data.xlsx", index= False)# we want to put the data frame into excel and to give the location
                # remember to put \\ and not one \ and in the end to give the name we want, and to avoid extra index
print(df1)

# based on https://www.youtube.com/watch?v=x_k1N1ZjJFM

