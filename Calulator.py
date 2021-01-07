#PROJECT NAME: CALCULATOR USING TKINTER
#COMPLETED BY: NAYAN MANDLIK
#SUBMITION DATE: 4/6/2020

from tkinter import *
root= Tk()


#backend coading
val= StringVar()
data=StringVar()
val=""
operator=""

def clickButton(event):#for printing numbers
    text=event.widget.cget('text')
    global val
    val=val+str(text)
    print(val)
    data.set(val)

def clickOperator(event):#for printing operators
    text = event.widget.cget('text')
    global operator
    operator=text #store operators in operator variable
    global val
    val = val + str(text)
    print(val)
    data.set(val)

def clear(event):#to clear screen
    global val
    val=""
    data.set("")

def result(event):#to calculate & display result
    global val
    global operator

    if operator=="/":#for division
        list = val.split("/")
        res = float(list[0]) / float(list[1])
        res=round(res,2)
        data.set(res)
        val=str(res)
    elif operator=="*":#for multiplication
        list = val.split("*")
        res = float(list[0]) * float(list[1])
        res = round(res, 2)
        data.set(res)
        val = str(res)
    elif operator=="-":#for substraction
        list = val.split("-")
        res = float(list[0]) - float(list[1])
        res = round(res, 2)
        data.set(res)
        val = str(res)
    elif operator=="+":#for addition
        list = val.split("+")
        res = float(list[0]) + float(list[1])
        res = round(res, 2)
        data.set(res)
        val = str(res)
    elif operator=="%":#for reminder
        list = val.split("%")
        print(list)
        res = float(list[0]) % float(list[1])
        res = round(res, 2)
        data.set(res)
        val = str(res)
    else:
        print("else")

#GUI coading
root.geometry('300x480')
root.title('CALCULATOR')

f= Frame(root, bg='grey', width=300, height=480)
f.place(x=0, y=0)

#frame 1
f1= Frame(root,)
l1= Entry(f1, textvariable=data, bg="white", font='lucida 30 bold')
l1.pack(fill=X)
f1.pack(fill=X,padx=10,pady=10)

#frame 2
f2= Frame(root,)
b1= Button(f2, text='C', font='lucida 20 bold')
b1.pack(fill=X)
b1.bind("<Button-1>", clear)
f2.pack(fill=X, padx=10, pady=5)

#frame 3
f3= Frame(root)
b2= Button(f3,text='7', font='lucida 20 bold', padx=16)
b2.bind("<Button-1>",clickButton)
b2.pack(side='left')

b3= Button(f3,text='8', font='lucida 20 bold', padx=16)
b3.pack(side='left')
b3.bind("<Button-1>",clickButton)

b4= Button(f3,text='9', font='lucida 20 bold', padx=16)
b4.pack(side='left')
b4.bind("<Button-1>",clickButton)

b5= Button(f3,text='/', font='lucida 20 bold', padx=18)
b5.pack(side='left')
b5.bind("<Button-1>",clickOperator)

f3.pack(fill=X, padx=10, pady=5)

#frame 4
f4= Frame(root)
b6= Button(f4,text='4', font='lucida 20 bold', padx=16)
b6.bind("<Button-1>",clickButton)
b6.pack(side='left')

b7= Button(f4,text='5', font='lucida 20 bold', padx=16)
b7.pack(side='left')
b7.bind("<Button-1>",clickButton)

b8= Button(f4,text='6', font='lucida 20 bold', padx=16)
b8.pack(side='left')
b8.bind("<Button-1>",clickButton)

b9= Button(f4,text='*', font='lucida 20 bold', padx=18)
b9.pack(side='left')
b9.bind("<Button-1>",clickOperator)

f4.pack(fill=X, padx=10, pady=5)

#frame 5
f5= Frame(root)
b10= Button(f5,text='3', font='lucida 20 bold', padx=16)
b10.bind("<Button-1>",clickButton)
b10.pack(side='left')

b11= Button(f5,text='2', font='lucida 20 bold', padx=16)
b11.pack(side='left')
b11.bind("<Button-1>",clickButton)

b12= Button(f5,text='1', font='lucida 20 bold', padx=16)
b12.pack(side='left')
b12.bind("<Button-1>",clickButton)

b13= Button(f5,text='-', font='lucida 20 bold', padx=18)
b13.pack(side='left')
b13.bind("<Button-1>",clickOperator)

f5.pack(fill=X, padx=10, pady=5)


#frame 6
f6= Frame(root)
b14= Button(f6,text='0', font='lucida 20 bold', padx=16)
b14.bind("<Button-1>",clickButton)
b14.pack(side='left')

b15= Button(f6,text='.', font='lucida 20 bold', padx=16)
b15.pack(side='left')
b15.bind("<Button-1>",clickButton)

b16= Button(f6,text='%', font='lucida 20 bold', padx=16)
b16.pack(side='left')
b16.bind("<Button-1>",clickOperator)

b17= Button(f6,text='+', font='lucida 20 bold', padx=18)
b17.pack(side='left')
b17.bind("<Button-1>",clickOperator)

f6.pack(fill=X, padx=10, pady=5)

#frame 7
f7= Frame(root)
b18= Button(f7,text='=', font='lucida 20 bold')
b18.pack(fill=X)
b18.bind("<Button-1>",result)
f7.pack(fill=X, padx=10, pady=5)


root.mainloop()