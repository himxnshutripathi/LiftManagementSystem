from tkinter import *
import ultimate as ulti

root = Tk()
canvas = Canvas(root)
root.geometry("350x450")
root.title('Lift Management')
root.resizable(False,False)

title = Label(root,text='Lift Management System', font='20px')
title.grid(row=0, column=0, columnspan=3, padx='20px',pady='10px')

lb1 = Label(root,text='Current Fl -')
lb1.grid(row=2,column=0)
lb1 = Label(root,text='Destination Fl -')
lb1.grid(row=3,column=0)
lb1 = Label(root,text='State -')
lb1.grid(row=4,column=0)

el1 = Label(root, text='Lift A')
el1.grid(row=1, column=1, padx='10px', pady='10px')

lAe1 = IntVar()
el1ep1 = Entry(root, bd=1, width=5,textvariable=lAe1)
el1ep1.grid(row=2, column=1, padx='10px', pady='10px')
lAe2 = IntVar()
el1ep2= Entry(root, bd=1, width=5, textvariable=lAe2)
el1ep2.grid(row=3, column=1, padx='10px', pady='10px')
lAe3 = StringVar()
el1ep3= Entry(root, bd=1, width=10,textvariable=lAe3)
el1ep3.grid(row=4, column=1, padx='10px', pady='10px')

el2 = Label(root, text='Lift B')
el2.grid(row=1, column=2, padx='10px', pady='10px')

lBe1 = IntVar()
el2ep1= Entry(root, bd=1, width=5, textvariable=lBe1)
el2ep1.grid(row=2, column=2, padx='10px', pady='10px')
lBe2 = IntVar()
el2ep2= Entry(root, bd=1, width=5, textvariable=lBe2)
el2ep2.grid(row=3, column=2, padx='10px', pady='10px')
lBe3 = StringVar()
el2ep3= Entry(root, bd=1, width=10, textvariable=lBe3)
el2ep3.grid(row=4, column=2, padx='10px', pady='10px')

canvas.create_line(0,25,310,25,width=1)
canvas.place(x=15,y=210)

personCf = Label(root, text="Person's Current floor")
personCf.grid(row=5,column=1, padx='10px',pady='10')

pE1 = IntVar()
personEntry1 = Entry(root, bd=1, width=5, textvariable=pE1)
personEntry1.grid(row=5,column=2, padx='10px',pady='10')

personDf = Label(root, text="Person's Destination floor")
personDf.grid(row=6,column=1, padx='10px',pady='10')

pE2 = IntVar()
personEntry2 = Entry(root, bd=1, width=5, textvariable=pE2)
personEntry2.grid(row=6,column=2, padx='10px',pady='10')

def func():
    out.config(text=chosenL.name)

butt=Button(root, text='Get Lift', bg='grey', command=func, relief="groove")
butt.grid(row=7, column=2,padx='20px',pady="20px")

out = Label(root)
out.grid(row=7,column=1,rowspan=2,padx='10px',pady='10px')


p1 = ulti.Person(pE1.get(),pE2.get())
persDir = p1.getPersonDirect()
person_floor = p1.persFloor

lA = ulti.Lift('lA',lAe1.get(),lAe3.get(), lAe2.get())
lB = ulti.Lift('lB',lBe1.get(),lBe3.get(), lBe2.get())

chosenL = ulti.choose_lift(person_floor,persDir, lA, lB)

root.mainloop()