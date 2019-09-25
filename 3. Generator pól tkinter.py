from tkinter import *



m = Tk()
quantity = 0
def generator_few(number, inp):
    quantity_now = number
    quantity_new =quantity_now + int(inp.get())
    counter = 0
    while counter < (quantity_new):
        label_2 = quantity_now
        entry_2 = quantity_now
        entry_counter = entry_2 + counter
        label_counter = label_2 +counter
        label_2 = Label(m, text="tekst")
        entry_2 = Entry(m,)
        label_2.grid(row =3+entry_counter, column=0)
        entry_2.grid(row=3+label_counter, column=1)
        counter = counter +1
    global quantity
    quantity = quantity_new

def generator_singly():
    global quantity
    quantity = quantity+1
    label = Label(m, text="tekst")
    entry_2 = Entry(m, )
    label.grid(row=3 + quantity, column=0)
    entry_2.grid(row=3 + quantity, column=1)

entry = Entry(m, width=3)
inp = entry
button = Button(m, text="Pokaż", command= lambda: generator_few(quantity, inp))
button_2 = Button(m, text="Dodaj", command= generator_singly)
entry.grid(row = 0, column = 0)
button.grid(row=1, column=0)
button_2.grid(row = 2, column = 0)
m.mainloop()
