# The link to the video in learned from there (she explains very well, recommended with subtitles)
# https://www.youtube.com/watch?v=x_k1N1ZjJFM

# !!!!Important!!!!
# Before working and coding on your excel file, you need to understand your file whats wrinte in it and what do oyu want to do with it
# and to to work "on blind" becuase then you can do mistake or just create a mess with your file, and not to get your goal

import pandas as pd
import glob
import os # will help us to retrieve our file path names

# here we want to orgenize our new excel document from one sheet to multiple sheets

location = ('C:\\Users\\חנן\\Desktop\\טפסים למחנה\\*.xlsx') # the location of the file + the format (xlsx - excel). we need double slash \\, or 'r' before the string of the file path
excel_files = glob.glob(location)

writer = pd.ExcelWriter("C:\\Users\\חנן\\Desktop\\טפסים למחנה\\multiple_sheets.xlsx")
# ExcelWriter --> is a class to write data frames
# we're doing it in another new excel, and not in the one we have created, becuase working with sheets is something very praticular to excel
# and if we will do it the wat we have done it before it's gonna over write them, and not to create a multiple sheets

for excel_file in excel_files:
    #sheet = excel_file # the name of the sheet will be the name of the previous separate excel files
    # now we don't want the whole path name, only the endding that is the name we want for our sheet
    sheet = os.path.basename(excel_file) # the os library helping us to filtarte/screen out the name itself from the path name
    # now let get rid of the ".xlsx"
    sheet = sheet.split(".")[0] # sheet is a string name, so we want to split the string after the point/dot, and to take onlt the name in index 0 --> first index/first name
    print(sheet)
    df1 = pd.read_excel(excel_file) # creating a data frame that read an excel file, and it will read each sheet
    # read the list of all our excel files from glob
#    df1.fillna(value="N\A", inplace="True") # fill in all the ending that are going to turn into blanks
    df1.to_excel(writer,sheet_name=sheet, index=False) # we are going to send all our data we have organized to excel, an in the location/path and name we have chosen
    # and in the new excel file, we want also to put the sheets and they will be with the name we made them (sheet variable)
    # and with out the index column (only the default in excel it self)

writer.save() # if we want save it all, we will just have an empty excel file (0 kb) and it want be able to open and read it
# when we save it all in the excel file/document so the whole data will be there
