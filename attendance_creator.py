#imports
import pandas as pd
import easygui
import openpyxl
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
easygui.msgbox('                      Welcome to atendance taker version-1.0',ok_button="Next")
#Colour function
def color_negative_red(val):
    color = 'red' if val =='A' else 'black'
    return 'color: %s' % color
#while loop
d=True
while (d==True):
    #inputting the files
    easygui.msgbox('                               SELECT CLASS LIST',ok_button="Click here to select the file")
    classlist=filedialog.askopenfilename()
    try:
        df=pd.read_excel(classlist)
    except:
        easygui.msgbox('An error occured-CLASS LIST MUST BE IN .xlsx FORMAT',ok_button="Exit")
        break
    try:
        df['names'] = df['names'].str.upper()
    except:
        easygui.msgbox('An error occured-Label the first row of the excel as names',ok_button="Exit")
        break
    easygui.msgbox('                               SELECT TODAYS LIST',ok_button="Click here to select the file")
    today=filedialog.askopenfilename()
    try:
        today=pd.read_csv(today)
    except:
        easygui.msgbox('An error occured-TODAYS LIST MUST BE IN .csv FORMAT',ok_button="Exit")
        break
    #list creation
    todayslist=str(datetime.today()).split()[0]
    dayto=list()
    try:
        dayto=today['Full Name']. tolist()
        for i in range(len(dayto)):
            dayto[i]=dayto[i].upper()
    except:
        easygui.msgbox('An error occured-Label the first row of the excel as Full Name',ok_button="Exit")
        break
    
    #Adding atendance
    df[todayslist]='Nil'
    for index, row in df.iterrows():
        if df.loc[index,'names'] in dayto:
            df.loc[index,todayslist]='P'
        else:
            df.loc[index,todayslist]='A'
    #Abscent, Present counter
    p=0
    a=-2
    for index, row in df.iterrows():
        if df.loc[index,todayslist]=='P':
            p=p+1
        elif df.loc[index,todayslist]=='A':
            a=a+1 
    for index, row in df.iterrows():
        if df.loc[index,'names']=='\PRESENT':
            df.loc[index,todayslist]=p
        elif df.loc[index,'names']=='\ABSENT':
            df.loc[index,todayslist]=a
    #returning csv
    df=df.sort_values(by='names')
    df=df.style.applymap(color_negative_red)
    g=easygui.ynbox('The excel has been updated', 'Title', ('save', 'save as'))
    
    
    if g==False:
        naneoffile=easygui.enterbox("Input name of the file: ")
        easygui.msgbox('                               SELECT LOCATION',ok_button="Browse")
        path = easygui.diropenbox()
        newexcel=path+'/'+naneoffile
        df.to_excel(newexcel+'.xlsx',index=False)
        easygui.msgbox('                            YOUR FILE HAS BEEN SAVED')
    else:
        df.to_excel(classlist,index=False)
        
        
    print("\n")
    #print("your excel has been updated")
    d=easygui.ynbox('Do you have another file? ', 'Title', ('Yes', 'No'))
easygui.msgbox('                         Thank you for using atendance taker',ok_button="Exit")

