#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This script compares two files row by row, and outputs the 'line' which is not existed 
# in the other file. In other words, This outputs the difference between the files you 
# inputs.

from tkinter import *
from tkinter import ttk
import pprint

def file_comparing():
    str_file1 = t1.get()
    str_file2 = t2.get()
    line1_list = []
    line2_list = []

    try:
        file1 = open(str_file1, encoding='utf-8')
        file2 = open(str_file2, encoding='utf-8')
    except FileNotFoundError:
        print("Sorry...Couldn't find the files which you inputs...\nPossible resons:")
        print(" Are files you just input truly 'utf-8'?\n Are files in same folder with this script?")

    line1 = file1.readline()
    line2 = file2.readline()

    while line1:
        line1 = file1.readline()
        line1_list.append(line1)

    while line2:
        line2 = file2.readline()
        line2_list.append(line2)

    line1_set = set(line1_list)
    line2_set = set(line2_list)
    matched_list = list(line1_set ^ line2_set)

    line1_consequence = [line for line in line1_list if line in matched_list]
    line2_consequence = [line for line in line2_list if line in matched_list]

    consequence = open("consequence.txt", "w", encoding="utf-8")
    consequence.write("---")
    consequence.write(str_file1)
    consequence.write("---\n\n")
    for n in range(len(line1_consequence)):
        consequence.write(line1_consequence[n])
    consequence.write("\n\n---")
    consequence.write(str_file2)
    consequence.write("---\n\n")
    for n in range(len(line2_consequence)):
        consequence.write(line2_consequence[n])
    consequence.close()
            

    pprint.pprint(matched_list)
    label1 = ttk.Label(
            frame1,
            text="---The differences between input files were saved in 'consequence.txt'.---",
            padding=(5,10))
    label1.grid(row=4,column=1)
    file1.close()
    file2.close()
    
root = Tk()
root.title('File Compare')
frame1 = ttk.Frame(root)
string_file1 = ttk.Label(frame1, text='Please input the file-name1 which you want to compare : ')
string_file2 = ttk.Label(frame1, text='Please input the file-name2 which you want to compare : ')

t1 = StringVar()
t2 = StringVar()

entry1 = ttk.Entry(frame1, textvariable=t1) 
entry2 = ttk.Entry(frame1, textvariable=t2) 
button1 = ttk.Button(frame1, text='Compare', command=file_comparing)
def button2_clicked(): root.quit()
button2 = ttk.Button(frame1, text='Exit', command=button2_clicked)


frame1.grid(row=0,column=0,sticky=(N,E,S,W))

icon = PhotoImage(file='file_image.png')
photo = ttk.Label(
    frame1,
    image=icon
    )
photo.grid(row=0,column=0)

message_string = ttk.Label(
    frame1,
    text='When files are input, two files row by row\n\n,and outputs the "line" which is not existed\n\nin the other file.\n\nThis only supports "utf-8"'
    )
message_string.grid(row=0,column=1)


string_file1.grid(row=1,column=0,sticky=E)
entry1.grid(row=1,column=1,sticky=W)

string_file2.grid(row=2,column=0,sticky=E)
entry2.grid(row=2,column=1,sticky=W)

button1.grid(row=3,column=0,sticky=W)
button2.grid(row=3,column=1,sticky=W)

for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
