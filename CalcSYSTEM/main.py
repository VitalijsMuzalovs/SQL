from tkinter import *
from datetime import datetime
from click import command
import psycopg2

def cmdRESET():
    txtOrdNr.delete(0,END)
    txtItem1.delete(0,END)
    txtItem2.delete(0,END)
    txtItem3.delete(0,END)
    txtItem4.delete(0,END)
    txt_costs.delete(0,END)
    txt_tips.delete(0,END)
    txt_tax.delete(0,END)
    txt_subtotal.delete(0,END)
    txt_total.delete(0,END)



win=Tk()
win.title('ORDERING System')
win.geometry('1000x400')



#TOP FRAME
frame_top = Frame(win,width=1000,height=20)
frame_top.pack(side=TOP,fill=BOTH)


lbTitle=Label(frame_top,text='ORDERING SYSTEM')
lbTitle.pack()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")
fm_dt = timestampStr
lbDate=Label(frame_top,text=fm_dt)
lbDate.pack()


#LEFT FRAME
frame_left = Frame(win,width=700,height=500)
frame_left.pack(side=LEFT,fill=BOTH)

# LEFT 0.th COLUMN
lb_OrdNr=Label(frame_left,text='Order No.:')
lb_OrdNr.grid(sticky='w',row=0,column=0)
lb_Item_1=Label(frame_left,text='Item 1:')
lb_Item_1.grid(sticky='w' ,row=1,column=0)
lb_Item_2=Label(frame_left,text='Item 2:')
lb_Item_2.grid(sticky='w' ,row=2,column=0)
lb_Item_3=Label(frame_left,text='Item 3:')
lb_Item_3.grid(sticky='w' ,row=3,column=0)
lb_Item_4=Label(frame_left,text='Item 4:')
lb_Item_4.grid(sticky='w' ,row=4,column=0)

# LEFT 1.st COLUMN
txtOrdNr = Entry(frame_left,width=30,border=1)
txtOrdNr.grid(sticky='w',row=0,column=1)
txtItem1 = Entry(frame_left,width=30,border=1)
txtItem1.grid(sticky='w',row=1,column=1)
txtItem2 = Entry(frame_left,width=30,border=1)
txtItem2.grid(sticky='w',row=2,column=1)
txtItem3 = Entry(frame_left,width=30,border=1)
txtItem3.grid(sticky='w',row=3,column=1)
txtItem4 = Entry(frame_left,width=30,border=1)
txtItem4.grid(sticky='w',row=4,column=1)

# LEFT 2.nd COLUMN
lb_cost=Label(frame_left,text='Costs:')
lb_cost.grid(sticky='w' ,row=0,column=2)
lb_tips=Label(frame_left,text='Tips:')
lb_tips.grid(sticky='w' ,row=1,column=2)
lb_tax=Label(frame_left,text='Tax:')
lb_tax.grid(sticky='w',row=2,column=2)
lb_subtotal=Label(frame_left,text='SubTotal:')
lb_subtotal.grid(sticky='w' ,row=3,column=2)
lb_total=Label(frame_left,text='TOTAL:')
lb_total.grid(sticky='w' ,row=4,column=2)

# LEFT 3.rd COLUMN
txt_costs = Entry(frame_left,width=30,border=1)
txt_costs.grid(sticky='w',row=0,column=3)
txt_tips = Entry(frame_left,width=30,border=1)
txt_tips.grid(sticky='w',row=1,column=3)
txt_tax = Entry(frame_left,width=30,border=1)
txt_tax.grid(sticky='w',row=2,column=3)
txt_subtotal = Entry(frame_left,width=30,border=1)
txt_subtotal.grid(sticky='w',row=3,column=3)
txt_total = Entry(frame_left,width=30,border=1)
txt_total.grid(sticky='w',row=4,column=3)

#Buttons
btPrice=Button(frame_left,text='PRICE',command=None)
btPrice.grid(row=5,column=0)
btTOTAL=Button(frame_left,text='TOTAL',command=None)
btTOTAL.grid(row=5,column=1)
btRESET=Button(frame_left,text='RESET',command=cmdRESET)
btRESET.grid(row=5,column=2)
btFIND=Button(frame_left,text='FIND',command=None)
btFIND.grid(row=5,column=3)
btEXIT=Button(frame_left,text='EXIT',command=None)
btEXIT.grid(row=5,column=4)


#RIGHT FRAME
frame_right = Frame(win,width=300,height=500)
frame_right.pack(side=RIGHT,fill=BOTH)

#CALCULATOR
btX = "40"
pdY="20"

def btClick(number):
        current=e.get()
        e.delete(0,END)
        newVal = str(current)+str(number)
        e.insert(0,newVal)

def pressClear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def calculate(sign):
    global mathOp
    global num1
    try:
        mathOp = sign
        num1 = int(e.get())
        e.delete(0,END)
    except ValueError:
        e.insert(0,'Not number!')
    return 0
    
def pressEqual():
    try:
        num2 = int(e.get())
        if mathOp=="+":
            rez = num1+num2
        elif mathOp=="-":
            rez = num1-num2
        elif mathOp=="/":
            rez = num1/num2
        elif mathOp=="*":
            rez = num1*num2
        else:
            rez=0
        e.delete(0,END)
        e.insert(0,str(rez))
    except:
        e.delete(0,END)
        e.insert('ERROR!')
    return 0

e = Entry(frame_right,width=15,font=("Arial Black",22) )

for i in range(10):
    myExpr = "bt"+str(i)+"=Button(frame_right,text="+str(i)+",padx=btX,pady=pdY,command=lambda:btClick("+str(i)+"))"
    exec(myExpr)

btEq=Button(frame_right,text="=",padx=btX,pady=pdY,command=lambda:pressEqual())
btClear=Button(frame_right,text="C",padx=btX,pady=pdY,command=lambda:pressClear())

myDict={"myPlus":'+',"myMinus":"-","myMult":"*","myDevide":"/"}

for myKey,v in myDict.items():
    myExpr = myKey+"=Button(frame_right,text='"+v+"',padx=btX,pady=pdY,command=lambda:calculate('"+v+"'))"
    exec(myExpr)

e.grid(row=1,column=1,columnspan=5)

m=0
for i in range(5,1,-1):
    for j in range(1,4):
        if not(i==5 and j!=2):
            myExpr2="bt"+str(m)+".grid(row="+str(i)+",column="+str(j)+")"
            exec(myExpr2)
            m+=1

myMinus.grid(row=2,column=4)
myPlus.grid(row=3,column=4)
myMult.grid(row=4,column=4)
myDevide.grid(row=5,column=4)

btEq.grid(row=5,column=3)
btClear.grid(row=5,column=1)

# DB FUNCTIONS
def connectDB(myFunc):
    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='aphfgqzl'
    DB_USER='aphfgqzl'
    DB_PASS='E-XRiqulSIwntxQurDLibzk8EAeyalBZ'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # myFunc()
    # cur.execute('''CREATE TABLE IF NOT EXISTS orders(id SERIAL,ordNr TEXT PRIMARY KEY,Item_1 TEXT,Item_2 TEXT,Item_3 TEXT,Item_4 TEXT,Costs FLOAT(2),Tips FLOAT(2),Tax FLOAT(2),SubTotal FLOAT(2),Total FLOAT(2));
    # ''')
    # cur.execute('''INSERT INTO  pols (name,surname) VALUES (%s,%s);''',(f_name.get(),uzv_surname.get()))

    conn.commit()
    conn.close()


win.mainloop()