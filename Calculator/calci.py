#evaluating all the required modules

from tkinter import *
b=''
c=0

#evaluating all kinds of operator and button and errors

def evaluate(a):
    global b,c
    if a=='=':
        l1['text']=b
        try:
            c=eval(b)
            l1['text']=' '
            label['text']=c
        except:
            label['text']="Infinity"
    elif a=='<-':
        print("In the <- statement")
        d=label['text']
        print("label text =",d)
        b=''
        if d==' ' or d=="Infinity":
            return evaluate("clear")
        else:
            print("in else")
            d = str(d)
            n = len(d)
            b+=d[0:n-1]
            print(b)
            label['text']=b

        
        
    elif a=='clear':
        b=''
        label['text']=b
        l1['text']=' '
    else:
        try:
            b+=str(a)
            label['text']=b
        except:
            pass
        
root=Tk()
root.geometry("300x500")
root.configure(background='orange')
l1=Label(root,text='',bg='orange',fg='black',font='Arial 32 bold italic')
l1.grid(row=0,column=3)
label=Label(root,text='',bg='orange',fg='black',font='Arial 32 bold italic')
label.grid(row=0,columnspan=1,column=0)

#calculator button structure

button=Button(root,text='9',font='Arial 32 bold italic',command=lambda:evaluate(9),bg='red',width=3,height=1)
button.grid(row=1,column=0)
button1=Button(root,text='8',font='Arial 32 bold italic',command=lambda:evaluate(8),bg='red',width=3,height=1)
button1.grid(row=1,column=1)
button2=Button(root,text='7',font='Arial 32 bold italic',command=lambda:evaluate(7),bg='red',width=3,height=1)
button2.grid(row=1,column=2)
button3=Button(root,text='+',font='Arial 32 bold italic',command=lambda:evaluate('+'),bg='red',width=3,height=2)
button3.grid(row=5,column=0)
button4=Button(root,text='-',font='Arial 32 bold italic',command=lambda:evaluate('-'),bg='red',width=3,height=2)
button4.grid(row=5,column=1)
button5=Button(root,text='6',font='Arial 32 bold italic',command=lambda:evaluate(6),bg='red',width=3,height=1)
button5.grid(row=2,column=0)
button6=Button(root,text='5',font='Arial 32 bold italic',command=lambda:evaluate(5),bg='red',width=3,height=1)
button6.grid(row=2,column=1)
button7=Button(root,text='4',font='Arial 32 bold italic',command=lambda:evaluate(4),bg='red',width=3,height=1)
button7.grid(row=2,column=2)
button8=Button(root,text='3',font='Arial 32 bold italic',command=lambda:evaluate(3),bg='red',width=3,height=1)
button8.grid(row=3,column=0)
button9=Button(root,text='2',font='Arial 32 bold italic',command=lambda:evaluate(2),bg='red',width=3,height=1)
button9.grid(row=3,column=1)
button10=Button(root,text='1',font='Arial 32 bold italic',command=lambda:evaluate(1),bg='red',width=3,height=1)
button10.grid(row=3,column=2)
button11=Button(root,text='0',font='Arial 32 bold italic',command=lambda:evaluate(0),bg='red',width=3,height=1)
button11.grid(row=4,column=0)
button12=Button(root,text='.',font='Arial 32 bold italic',command=lambda:evaluate('.'),bg='red',width=3,height=1)
button12.grid(row=4,column=1)
button13=Button(root,text='=',font='Arial 32 bold italic',command=lambda:evaluate('='),bg='red',width=3,height=1)
button13.grid(row=4,column=2)
button14=Button(root,text='clear',font='Arial 32 bold italic',command=lambda:evaluate('clear'),bg='red',width=3,height=2)
button14.grid(row=5,column=2,rowspan=1)
button15=Button(root,text='*',font='Arial 32 bold italic',command=lambda:evaluate('*'),bg='red',width=3,height=2)
button15.grid(row=6,column=0)
button16=Button(root,text='/',font='Arial 32 bold italic',command=lambda:evaluate('/'),bg='red',width=3,height=2)
button16.grid(row=6,column=1)
button17=Button(root,text='<-',font='Arial 32 bold italic',command=lambda:evaluate('<-'),bg='red',width=3,height=2)
button17.grid(row=6,column=2)

#holding screen

root.mainloop()

