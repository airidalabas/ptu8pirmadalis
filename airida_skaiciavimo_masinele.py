from tkinter import *
langas = Tk()
langas.title("calculatoPRIMITTIVO")

e_juosta = Entry(langas, width=45, borderwidth=7)
e_juosta.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

def spausti_myg(numeris):
    e_juosta.insert(END, numeris)

def lygu ():
    pasirinktas_sk = eval(e_juosta.get())
    e_juosta.delete(0, END)
    e_juosta.insert(0, pasirinktas_sk)

def myg_istrinti():
    e_juosta.delete(0, END)

myg_1 = Button(langas, text='1', padx=40, pady=20, command=lambda: spausti_myg(1))
myg_2 = Button(langas, text='2', padx=40, pady=20, command=lambda: spausti_myg(2))
myg_3 = Button(langas, text='3', padx=40, pady=20, command=lambda: spausti_myg(3))
myg_4 = Button(langas, text='4', padx=40, pady=20, command=lambda: spausti_myg(4))
myg_5 = Button(langas, text='5', padx=40, pady=20, command=lambda: spausti_myg(5))
myg_6 = Button(langas, text='6', padx=40, pady=20, command=lambda: spausti_myg(6))
myg_7 = Button(langas, text='7', padx=40, pady=20, command=lambda: spausti_myg(7))
myg_8 = Button(langas, text='8', padx=40, pady=20, command=lambda: spausti_myg(8))
myg_9 = Button(langas, text='9', padx=40, pady=20, command=lambda: spausti_myg(9))
myg_0 = Button(langas, text='0', padx=40, pady=20, command=lambda: spausti_myg(0))
myg_sudetis = Button(langas, text='+', padx=40, pady=20, command=lambda: spausti_myg("+"))
myg_atimtis = Button(langas, text='-', padx=40, pady=20, command=lambda: spausti_myg("-"))
myg_daugyba = Button(langas, text='*', padx=40, pady=20, command=lambda: spausti_myg("*"))
myg_dalyba = Button(langas, text='/', padx=40, pady=20, command=lambda: spausti_myg("/"))
myg_lygu = Button(langas, text='=', padx=40, pady=20, command=lygu)
myg_c = Button(langas, text='c', padx=40, pady=20, command=myg_istrinti)

myg_7.grid(row=1, column=0)
myg_8.grid(row=1, column=1)
myg_9.grid(row=1, column=2)
myg_sudetis.grid(row=1, column=3)
myg_4.grid(row=2, column=0)
myg_5.grid(row=2, column=1)
myg_6.grid(row=2, column=2)
myg_atimtis.grid(row=2, column=3)
myg_1.grid(row=3, column=0)
myg_2.grid(row=3, column=1)
myg_3.grid(row=3, column=2)
myg_daugyba.grid(row=3, column=3)
myg_0.grid(row=4, column=0)
myg_c.grid(row=4, column=1)
myg_lygu.grid(row=4, column=2)
myg_dalyba.grid(row=4, column=3)

langas.mainloop()




