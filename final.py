import tkinter
import json
def submit():
    u=txt.get()
    p=txt1.get()
    with open('tk.json')as f:
        dct=json.load(f)
        if(u in dct and dct[u]==p):
            lbl.configure(text='The username is duplicate') 
        elif(len(p)<=3 or len(p)>=10):
            lbl.configure(text='wrong number of letter')
        elif(u.isalnum()!=True):
            lbl.configure(text='wrong!characters of numerical type or letters')
        else:
            dct[u]=p
            with open('tk.json','w')as f:
                json.dump(dct,f)
                lbl.configure(text='good luck')
def login():
    u=txt.get()
    p=txt1.get()
    with open('tk.json','r')as f:
        dct=json.load(f)
        if(u in dct and dct[u]==p):
            lbl.configure(text='wellcome')
        else:
            lbl.configure(text='wrong user') 

PTK=tkinter.Tk()
PTK.title('Project')
PTK.geometry('400x300')
lbl=tkinter.Label(PTK,font=('arial',14,'bold'),text=" ")
lbl.grid(column=30, row=4)
btn1=tkinter.Button(PTK,font=('arial',14),text='submit',bg='blue',fg='yellow',command=submit)
btn1.grid(column=8,row=40)
btn2=tkinter.Button(PTK,font=('arial',14),text='login',bg='blue',fg='yellow',command=login)
btn2.grid(column=17,row=40)
txt=tkinter.Entry(PTK,font=('arial',8,'bold'),bg='pink',width=10,fg='red')
txt.grid(column=6,row=4)
txt1=tkinter.Entry(PTK,font=('arial',8,'bold'),bg='pink',fg='red',width=10)
txt1.grid(column=15,row=4)
PTK.mainloop()
"""
Created on Fri Feb 25 10:51:15 2022

@author: sanaz-pc
"""

