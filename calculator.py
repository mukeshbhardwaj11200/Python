from tkinter import *
tk1=Tk()
tk1.title("Calculator")
def btn_Click(number):
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+str(number))
def btn_Delete():
        current=entrytext1.get()
        leng=len(str(current))
        entrytext1.delete(leng-1,END)
def btn_Clear():
       entrytext1.delete(0,END)
def btn_Add():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'+')
        global math
        math="addition"
def btn_Sub():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'-')
        global math
        math="subtraction"
def btn_div():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'/')
        global math
        math="division"
def btn_mul():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'x')
        global math
        math="multiplication"
def btn_square():
        entrytext1.insert(0,'Sq ')
        global math
        math="square"
def btn_mode():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'%')
        global math
        math="mode"
def btn_dot():
        current=entrytext1.get()
        entrytext1.delete(0,END)
        entrytext1.insert(0,str(current)+'.')
        current=current+"."
      
       
def btn_Equal():
        q=str(entrytext1.get())
        if(math=="addition"):
            l=q.split('+')
            sum1=0
            for e in l:
                sum1=sum1+float(e)
            entrytext1.delete(0,END)
            entrytext1.insert(0,str(sum1))
        if(math=="subtraction"):
            l=q.split('-')
            if(l[0]==''):
                sum2=0
                for i in range(1,len(l)):
                    sum2=sum2+float(l[i])
                entrytext1.delete(0,END)
                entrytext1.insert(0,"-"+str(sum2))
            else:
                sum2=float(l[0])
                for i in range(1,len(l)):
                    sum2=sum2-float(l[i])
                entrytext1.delete(0,END)
                entrytext1.insert(0,str(sum2))
        if(math=="division"):
            l=q.split('/')
            division_res=float(l[0])/float(l[1])
            entrytext1.delete(0,END)
            entrytext1.insert(0,division_res)
        if(math=="multiplication"):
            l=q.split('x')
            multi_res=float(l[0])*float(l[1])
            entrytext1.delete(0,END)
            entrytext1.insert(0,multi_res)
        if(math=="mode"):
            l=q.split('%')
            mode_res=float(l[0])%float(l[1])
            entrytext1.delete(0,END)
            entrytext1.insert(0,mode_res)
        if(math=="square"):
            l=q.split('Sq ')
            sq=float(l[1])**2
            entrytext1.delete(0,END)
            entrytext1.insert(0,sq)

vartext1=IntVar()

entrytext1=Entry(tk1,borderwidth=5,width=65)
entrytext1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

btn7=Button(tk1,text="7",font=3,padx=40,pady=10,command=lambda: btn_Click(7))
btn8=Button(tk1,text="8",font=3,padx=40,pady=10,command=lambda: btn_Click(8))
btn9=Button(tk1,text="9",font=3,padx=40,pady=10,command=lambda: btn_Click(9))
btndiv=Button(tk1,text="/",font=3,padx=40,pady=10,command=btn_div)
btn4=Button(tk1,text="4",font=3,padx=40,pady=10,command=lambda: btn_Click(4))
btn5=Button(tk1,text="5",font=3,padx=40,pady=10,command=lambda: btn_Click(5))
btn6=Button(tk1,text="6",font=3,padx=40,pady=10,command=lambda: btn_Click(6))
btnmul=Button(tk1,text="x",font=3,padx=40,pady=10,command=btn_mul)

btn1=Button(tk1,text="1",font=3,padx=40,pady=10,command=lambda: btn_Click(1))
btn2=Button(tk1,text="2",font=3,padx=40,pady=10,command=lambda: btn_Click(2))
btn3=Button(tk1,text="3",font=3,padx=40,pady=10,command=lambda: btn_Click(3))
btnsub=Button(tk1,text="- ",font=3,padx=40,pady=10,command=btn_Sub)

btndot=Button(tk1,text=". ",font=3,padx=40,pady=10,command=btn_dot)
btn0=Button(tk1,text="0",font=3,padx=40,pady=10,command=lambda: btn_Click(0))
btnequal=Button(tk1,text="=",font=3,padx=40,pady=10,command=btn_Equal)
btnadd=Button(tk1,text="+",font=3,padx=40,pady=10,command=btn_Add)

btnclear=Button(tk1,text="C",font=2,padx=38,pady=10,command=btn_Clear)
btnmode=Button(tk1,text="%",font=2,padx=37.5,pady=10,command=btn_mode)
btnsquare=Button(tk1,text="Sq",font=1,padx=34.2,pady=10,command=btn_square)
btndelete=Button(tk1,text="Del",font=1,padx=32.6,pady=10,command=btn_Delete)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)  
btn9.grid(row=1,column=2)
btndiv.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)  
btn6.grid(row=2,column=2)
btnmul.grid(row=2,column=3)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)  
btn3.grid(row=3,column=2)
btnsub.grid(row=3,column=3)

btndot.grid(row=4,column=0)
btn0.grid(row=4,column=1)  
btnequal.grid(row=4,column=2)
btnadd.grid(row=4,column=3)

btnclear.grid(row=5,column=0)
btnmode.grid(row=5,column=1)  
btnsquare.grid(row=5,column=2)
btndelete.grid(row=5,column=3)

tk1.mainloop()
