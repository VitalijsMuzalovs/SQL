from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import Combobox
import psycopg2.extras
import psycopg2


def connectDB(myFunc):
    ''' DB connection.Argument - is a function with query to be executed '''

    DB_HOST='abul.db.elephantsql.com'
    DB_NAME='aphfgqzl'
    DB_USER='aphfgqzl'
    DB_PASS='E-XRiqulSIwntxQurDLibzk8EAeyalBZ'
    DB_PORT=5432

    conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('''CREATE TABLE IF NOT EXISTS orders(id SERIAL,ordNr TEXT PRIMARY KEY,Item_1 FLOAT(2),Item_2 FLOAT(2),Item_3 FLOAT(2),Item_4 FLOAT(2),Costs FLOAT(2),Tips FLOAT(2),Tax FLOAT(2),SubTotal FLOAT(2),Total FLOAT(2));
     ''')
    myFunc(cur)
        
    conn.commit()
    conn.close()
    cur.close


def getTotalRecs():
    ''' Function gets current record count'''
    def myFn(cur):
        global recCount
        cur.execute('''SELECT count(id) FROM orders ''')
        recCount = cur.fetchone()
        return recCount
    connectDB(myFn)
    return recCount

def lb_count_refresh():
    '''Label refresh.Label shows current record count'''
    lb_count['text']=f'Record count: {getTotalRecs()}'


def cmdRESET():
    '''RESET button - clear all fields'''
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

def btTotal():
    ''' TOTAL button - calculates total price
    Total price it is a costs (sum) of all items + tax 21% of all items + tips amount '''
    if len(txt_tips.get())==0 or float(txt_tips.get())==False: 
        txt_tips.delete(0,END)
        txt_tips.insert(0,0)
    if len(txtItem1.get())==0 or float(txtItem1.get())==False: 
        txtItem1.delete(0,END)
        txtItem1.insert(0,0)
    if len(txtItem2.get())==0 or float(txtItem2.get())==False: 
        txtItem2.delete(0,END)
        txtItem2.insert(0,0)
    if len(txtItem3.get())==0 or float(txtItem3.get())==False: 
        txtItem3.delete(0,END)
        txtItem3.insert(0,0)
    if len(txtItem4.get())==0 or float(txtItem4.get())==False: 
        txtItem4.delete(0,END)
        txtItem4.insert(0,0)


    costs=round(float(txtItem1.get())+float(txtItem2.get())+float(txtItem3.get())+float(txtItem4.get()),2)

    txt_costs.delete(0,END)
    txt_costs.insert(0,costs)

    tax=round(float(costs*0.21),2)
    txt_tax.delete(0,END)
    txt_tax.insert(0,tax)

    subtotal=round(costs+tax,2)
    txt_subtotal.delete(0,END)
    txt_subtotal.insert(0,subtotal)

    total=subtotal+float(txt_tips.get())
    txt_total.delete(0,END)
    txt_total.insert(0,round(total,2))


win=Tk()
win.title('ORDERING System')
win.geometry('1020x400')



#################
### TOP FRAME ###
#################
frame_top = Frame(win,width=1020,height=20)
frame_top.pack(side=TOP,fill=BOTH)


lbTitle=Label(frame_top,text='ORDERING SYSTEM')
lbTitle.pack()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")
fm_dt = timestampStr
lbDate=Label(frame_top,text=fm_dt)
lbDate.pack()


##################
### LEFT FRAME ###
##################
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
lb_count = Label(frame_left,text=f'Record count: {getTotalRecs()}')
lb_count.grid(sticky='sw',row=10,column=2)

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

# QUERY FUNCTIONS
def cmdCreate():
    '''CREATE button - creates a new order. If it's allready exists => error occurs!'''
    def myInsertNew(cur):
        cur.execute('''INSERT INTO  orders (ordNr,Item_1,Item_2,Item_3,Item_4,Costs,Tips,Tax,SubTotal,Total) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',(txtOrdNr.get(),txtItem1.get(),txtItem2.get(),txtItem3.get(),txtItem4.get(),txt_costs.get(),txt_tips.get(),txt_tax.get(),txt_subtotal.get(),txt_total.get()))
    try:
        connectDB(myInsertNew)
        lb_count_refresh()
        cmdRESET()
        renewOrderCmb()
        messagebox.showinfo(title="SAVED", message='Succesfully saved!')
    except:
        messagebox.showinfo(title="ERROR", message='Error!')

def cmdDeleteALL():
    '''DELETE ALL button - deletes all orders from DB'''
    def myDeleteAll(cur):
        cur.execute('''DELETE FROM orders;''')
    connectDB(myDeleteAll)
    lb_count_refresh()
    cmdRESET()

def cmdDelete():
    '''DELETE button - deletes current order (displayed in 'Order No' field)'''
    def myDeleteAll(cur):
        cur.execute(f'''DELETE FROM orders WHERE ordNr LIKE '{txtOrdNr.get()}';''')
    connectDB(myDeleteAll)
    cmdRESET()
    lb_count_refresh()


def renewOrderCmb():
    '''Refreshes comboboxe's content (existing order's list)'''
    def fetchOrders(cur):
        global output
        cur.execute('''SELECT ordNr FROM orders ORDER BY ordNr ASC;''')
        records=cur.fetchall()
        output=()
        for record in records:
            cmbText=f'{record[0]}'
            output+=(cmbText,)
    connectDB(fetchOrders)
    cmb['values']=output

def fetchRecord(*arg):
    '''Gets data of particular order'''
    def myFn(cur):
        global rs
        val = n.get()
        cur.execute(f'''SELECT * FROM orders WHERE ordNr LIKE '{val}';''')
        rs=cur.fetchall()
        return rs
    
    connectDB(myFn)

    txtOrdNr.delete(0,END)
    txtOrdNr.insert(0,rs[0][1])
    txtItem1.delete(0,END)
    txtItem1.insert(0,rs[0][2])
    txtItem2.delete(0,END)
    txtItem2.insert(0,rs[0][3])
    txtItem3.delete(0,END)
    txtItem3.insert(0,rs[0][4])
    txtItem4.delete(0,END)
    txtItem4.insert(0,rs[0][5])
    txt_costs.delete(0,END)
    txt_costs.insert(0,rs[0][6])
    txt_tips.delete(0,END)
    txt_tips.insert(0,rs[0][7])
    txt_tax.delete(0,END)
    txt_tax.insert(0,rs[0][8])
    txt_subtotal.delete(0,END)
    txt_subtotal.insert(0,rs[0][9])
    txt_total.delete(0,END)
    txt_total.insert(0,rs[0][10])

def cmdUpdate():
    '''UPDATE button - update record,if it's exists.'''
    def checkRec(cur):
        global ordExist
        cur.execute(f'''SELECT count(id) FROM orders WHERE ordNr LIKE '{txtOrdNr.get()}';''')
        ordExist = cur.fetchone()
        return ordExist
    connectDB(checkRec)

    # print(ordExist[0])
    if int(ordExist[0])>0:
        def myFn(cur):
            cur.execute(f'''UPDATE orders SET 
            ordNr='{txtOrdNr.get()}'
            ,Item_1={txtItem1.get()}
            ,Item_2={txtItem2.get()}
            ,Item_3={txtItem3.get()}
            ,Item_4={txtItem4.get()}
            ,Costs={txt_costs.get()}
            ,Tips={txt_tips.get()}
            ,Tax={txt_tax.get()}
            ,SubTotal={txt_subtotal.get()}
            ,Total={txt_total.get()}
            WHERE ordNr LIKE '{txtOrdNr.get()}';''')
        connectDB(myFn)
        messagebox.showinfo(title="UPDATED", message='Succesfully updated!')
    else:
        messagebox.showinfo(title="ERROR", message='This record doesnt exist!Please,create it first!')



#   BUTTONS
btTOTAL=Button(frame_left,text='TOTAL',width=8,command=lambda:btTotal())
btTOTAL.grid(row=5,column=0,pady=15)
btPrice=Button(frame_left,text='CREATE',width=8,command=lambda:cmdCreate())
btPrice.grid(row=5,column=1)
bdUpdate=Button(frame_left,text='UPDATE',width=8,command=lambda:cmdUpdate())
bdUpdate.grid(row=5,column=2)

btRESET=Button(frame_left,text='RESET',width=8,command=cmdRESET)
btRESET.grid(row=6,column=0)
btDelete=Button(frame_left,text='DELETE',width=8,command=cmdDelete)
btDelete.grid(row=6,column=1)
bdDelAll=Button(frame_left,text='DELETE ALL',width=8,command=lambda:cmdDeleteALL())
bdDelAll.grid(row=6,column=2)
btEXIT=Button(frame_left,text='EXIT',width=8,command=win.quit)
btEXIT.grid(row=6,column=3)


n=StringVar() 

cmb = Combobox(frame_left,textvariable=n)  
cmb.grid(row=7,column=2,pady=15)
renewOrderCmb()
n.trace('w',fetchRecord)

###################
### RIGHT FRAME ###
###################
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
lbDev=Label(frame_right,text='by Vitālijs Muzaļovs')
lbDev.grid(row=6,columnspan=5,pady=15,sticky='se')

win.mainloop()
