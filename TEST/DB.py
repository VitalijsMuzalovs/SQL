from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import psycopg2
import psycopg2.extras

def cmdSubmit():
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('''CREATE TABLE IF NOT EXISTS pols(id SERIAL PRIMARY KEY,name TEXT,surname TEXT);
    ''')
    cur.execute('''INSERT INTO  pols (name,surname) VALUES (%s,%s);''',(f_name.get(),uzv_surname.get()))

    conn.commit()
    conn.close()
    cmdClear()

def cmdClear():
    f_name.delete(0,END)
    uzv_surname.delete(0,END)

def cmdDelete():
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('''DELETE FROM pols;''')

    conn.commit()
    conn.close()

def atjaunot():
    output_label.config(text='')
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('''SELECT * FROM pols;''')
    records=cur.fetchall()
    output=' '
    for record in records:
        output_label.config(text=f'{output}\n{record[1]} {record[2]}')
        output=output_label['text']
    cur.close()
    conn.close()
    cmdSelAll()
    
    
def cmdSel():
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('''SELECT * FROM pols WHERE name LIKE '%a%' or surname LIKE '%a%';''')
    records=cur.fetchall()
    output=' '
    for record in records:
        msgTxt=f'{output}\n{record[1]} - {record[2]}'
        output=msgTxt
    cur.close()
    conn.close()

    messagebox.showinfo(title="SELECT", message=output)

def cmdSelAll():
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('''SELECT * FROM pols;''')
    records=cur.fetchall()
    output=()
    for record in records:
        cmbText=f'{record[1]} {record[2]}'
        output+=(cmbText,)
    cmb['values']=output
    cur.close()
    conn.close()

def cmdSum():
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('''SELECT SUM(eur) FROM pols;''')
    records=cur.fetchall()
    messagebox.showinfo(title="SELECT", message=records)
    cur.close()
    conn.close()

def funkcija(*arg):
    aaa = str(n.get()).split(' ')[0]
    print(aaa)
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='gvgcmzwr'
    DB_USER='gvgcmzwr'
    DB_PASS='0peneraq77HDuDIVzplpqgqpE2oN1yid'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # cur.execute('DELETE FROM pols WHERE name LIKE \' ' + aaa + '\'')
    cur.execute('DELETE FROM pols WHERE name LIKE \'' + aaa + '\'')
    conn.commit()
    conn.close()
    atjaunot()


win=Tk()
win.title('TEST DB')
win.geometry('550x300')

my_frame=LabelFrame(win,text='DB test')
my_frame.pack(pady=20)

f_label=Label(my_frame,text='Name').grid(row=0,column=0,padx=10,pady=10)
f_name=Entry(my_frame)
f_name.grid(row=0,column=1,padx=10,pady=10)

uzv_label=Label(my_frame,text='Surname').grid(row=1,column=0,padx=10,pady=10)
uzv_surname=Entry(my_frame)
uzv_surname.grid(row=1,column=1,padx=10,pady=10)

myBt= Button(my_frame,text='Submit',command=cmdSubmit)
myBt.grid(row=2,column=1)

myBtClear= Button(my_frame,text='Clear',command=cmdClear)
myBtClear.grid(row=2,column=2)

myBtDel= Button(my_frame,text='Delete',command=cmdDelete)
myBtDel.grid(row=2,column=3)

myBtUpd= Button(my_frame,text='Update',command=atjaunot)
myBtUpd.grid(row=2,column=4)

myBtSel= Button(my_frame,text='SELECT A',command=cmdSel)
myBtSel.grid(row=2,column=5)

myBtSum= Button(my_frame,text='SUM',command=cmdSum)
myBtSum.grid(row=2,column=6)

output_label=Label(my_frame,text='')
output_label.grid(row=3,column=0)

n=StringVar() 

cmb = Combobox(win,height=50,textvariable=n)  
cmb.pack()
cmdSelAll()
n.trace('w',funkcija)

win.mainloop()