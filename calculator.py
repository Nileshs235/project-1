from tkinter import*
calcy = Tk()

data=""
def get_data(value):
    global data
    data = data + str(value)
    var.set(data)
def equal_data():
    global data 
    total = str(eval(data))
    var.set(total)
def clear():
    global datad
    data = ""
    var.set(data)


calcy.title("calculator")
calcy.config(bg='gray')
calcy.geometry('500x550')
calcy.resizable(False,False)
Label_title=Label(calcy,text="Calculator",font=('Calibri',50, 'bold'),bg='gray')
Label_title.place(x=90, y=20, height=70, width=320)

var=StringVar()
output_box = Entry(calcy, relief='sunken', font=('Calibri',50, 'bold'),bd=4,textvariable=var)
output_box.place(x=20, y=110, height=60, width=460 )


key1= Button(calcy,text="7",font=('Calibri',50, 'bold'),command=lambda:get_data(7))
key1.place(x=20, y=190, height=70,width=115)
key2= Button(calcy,text="8",font=('Calibri',50, 'bold'),command=lambda:get_data(8))
key2.place(x=135, y=190, height=70,width=115)
key3= Button(calcy,text="9",font=('Calibri',50, 'bold'),command=lambda:get_data(9))
key3.place(x=250, y=190, height=70,width=115)
key4= Button(calcy,text="+",font=('Calibri',50, 'bold'),command=lambda:get_data("+"))
key4.place(x=365, y=190, height=70,width=115)



key5= Button(calcy,text="4",font=('Calibri',50, 'bold'),command=lambda:get_data(4))
key5.place(x=20, y=260, height=70,width=115)
key6= Button(calcy,text="5",font=('Calibri',50, 'bold'),command=lambda:get_data(5))
key6.place(x=135, y=260, height=70,width=115)
key7= Button(calcy,text="6",font=('Calibri',50, 'bold'),command=lambda:get_data(6))
key7.place(x=250, y=260, height=70,width=115)
key8= Button(calcy,text="-",font=('Calibri',50, 'bold'),command=lambda:get_data("-"))
key8.place(x=365, y=260, height=70,width=115)



key9= Button(calcy,text="1",font=('Calibri',50, 'bold'),command=lambda:get_data(1))
key9.place(x=20, y=330, height=70,width=115)
key10= Button(calcy,text="2",font=('Calibri',50, 'bold'),command=lambda:get_data(2))
key10.place(x=135, y=330, height=70,width=115)
key11= Button(calcy,text="3",font=('Calibri',50, 'bold'),command=lambda:get_data(3))
key11.place(x=250, y=330, height=70,width=115)
key12= Button(calcy,text="/",font=('Calibri',50, 'bold'),command=lambda:get_data("/"))
key12.place(x=365, y=330, height=70,width=115)


key13= Button(calcy,text=".",font=('Calibri',50, 'bold'),command=lambda:get_data("."))
key13.place(x=20, y=400, height=70,width=115)
key14= Button(calcy,text="0",font=('Calibri',50, 'bold'),command=lambda:get_data(0))
key14.place(x=135, y=400, height=70,width=115)
key15= Button(calcy,text="c",font=('Calibri',50, 'bold'),command=clear)
key15.place(x=250, y=400, height=70,width=115)
key16= Button(calcy,text="*",font=('Calibri',50, 'bold'),command=lambda:get_data("*"))
key16.place(x=365, y=400, height=70,width=115)

key17= Button(calcy,text="=",font=('Calibri',50, 'bold'),command=equal_data)
key17.place(x=140, y=470, height=70,width=225)

calcy.mainloop()