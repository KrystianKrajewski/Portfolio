from tkinter import *
from tkinter import messagebox, filedialog
import pickle


def check(state_next):
    """Function that change button_next state if user choose required options"""
    if state_next == "0":
        button_next.configure(state=NORMAL)
    else: pass

def clear_alkohol(strength_a, quantity_a, target_a):
    """"Function that clear entry fileds in frame alkohol """
    strength_a.delete(0, END)
    quantity_a.delete(0, END)
    target_a.delete(0, END)

def calc_alkohol( frame, strength_a, quantity_a, target_a):
    """Function that make calculactions based on data enter by user"""

    strength = float(strength_a.get())
    quantity = float(quantity_a.get())
    docelowa = float(target_a.get())

    stezenie = (strength * quantity) / 100
    quantity_calk = stezenie * 100 / docelowa
    quantity_wody = quantity_calk - quantity

    label_wynik_water = Label(frame, text="{:.2f}".format(quantity_wody), font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_quantity_total = Label(frame, text="{:.2f}".format(quantity_calk), font=("Times New Roman", 11), relief=GROOVE)
    label_litr_water = Label(frame, text="L", justify=LEFT, font=("Times New Roman", 11))
    label_litr_quantity_total = Label(frame, text="L", justify=LEFT, font=("Times New Roman", 11))

    label_wynik_water.grid(row=3, column=2)
    label_wynik_quantity_total.grid(row=4, column=2)
    label_litr_water.grid(row=3, column=3, sticky=W)
    label_litr_quantity_total.grid(row=4, column=3, sticky=W)

def calc_sweetening(frame, tincture_quantity, variable_radio_sweetening, variable_radio_sweetening_sub):
    """Function that make calculactions based on data enter by user"""
    quantity_n = float(tincture_quantity.get())
    variable_radio_sweetening = int(variable_radio_sweetening)
    variable_radio_sweetening_sub = int(variable_radio_sweetening_sub)
    if variable_radio_sweetening_sub == 60:
        quantity_gram = quantity_n * variable_radio_sweetening
        quantity_ml = quantity_gram / 100 * variable_radio_sweetening_sub
        sub = 'cukru'
    elif variable_radio_sweetening_sub == 75:
        quantity_gram = quantity_n * (variable_radio_sweetening * 30 / 100)
        quantity_ml = quantity_gram * variable_radio_sweetening_sub
        sub = 'miodu'
    elif variable_radio_sweetening_sub == 0 or variable_radio_sweetening == 0:
        komunikat_calc_window = messagebox.showinfo(frame, text="Nim przejdziesz dalej musisz wybrać type nalewki i rodzaj substancji słodzącej")
    label_wynik_gram = Label(frame, text="Należy dodać: {:.2f} gram {}".format(quantity_gram, sub),
                             font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_ml = Label(frame,
                           text="Należy dodać: {:.2f} ml {}".format(quantity_ml, sub),
                           font=("Times New Roman", 11), relief=GROOVE)
    label_wynik_gram.grid(row=5, column=2, columnspan=2, sticky=W)
    label_wynik_ml.grid(row=6, column=2, columnspan=2, sticky=W)

def clear_sweetening(tincture_quantity, variable_radio_sweetening, variable_radio_sweetening_sub):
    """Function that clear field is sweetenin frame"""
    tincture_quantity.delete(0, END)
    variable_radio_sweetening_sub.set("0")
    variable_radio_sweetening.set("0")

def calc_window():
    """Function that creat calculator window with fields"""
    window_calc_window = Toplevel(padx=10, pady=10)
    
       
    frame_alkohol = LabelFrame(window_calc_window, text="Kalkulator rozcięczania:", padx=10, pady=10)
        
    frame_sweetening = LabelFrame(window_calc_window, text="Kalulator słodzenia:", padx=10, pady=10)
        
    label_strength_alko = Label(frame_alkohol, text="Moc rozcieńczanego alkoholu:", justify=LEFT,
                           font=("Times New Roman", 11))
    label_quantity_alko = Label(frame_alkohol, text="Ilość alkoholu:", font=("Times New Roman", 11))
    label_concentration = Label(frame_alkohol, text="Moc docelowa nalewki:", justify=LEFT, font=("Times New Roman", 11))
    label_water = Label(frame_alkohol, text="Ilość wody, którą należy dodać:", justify=LEFT,
                       font=("Times New Roman", 11))
    label_quantity_total = Label(frame_alkohol, text="Ilość otrzymanej mieszaniny:", justify=LEFT,
                             font=("Times New Roman", 11))
    label_litr_quantity_a = Label(frame_alkohol, text="L", justify=LEFT, font=("Times New Roman", 11))
    label_percentage_strength= Label(frame_alkohol, text="%",  justify=LEFT, font=("Times New Roman", 11))
    laabel_procent_concentration =Label(frame_alkohol, text="%", justify=LEFT, font=("Times New Roman", 11))

        
    label_label_choose_tincture_typee = Label(frame_sweetening, text="Wybierz rodzaj przygotowywanej\nprzez Ciebie nalewki:",
                                         font=("Times New Roman", 11), padx=20, justify=LEFT)
    label_choose_sweetening_sub = Label(frame_sweetening, text="Wybierz czym słodzisz nalewkę:", font=("Times New Roman", 11), padx=20)
    label_tincture_quantity = Label(frame_sweetening, text="Wprowadź ilość nalewki do osłodzenia", font=("Times New Roman", 11) )
    label_litr_tincture_quantity = Label(frame_sweetening, text="L", font=("Times New Roman", 11))
        
    entry_strength_alko = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_quantity_alko = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_total_strength = Entry(frame_alkohol, width=3, relief=GROOVE, font=("Times New Roman", 11))
    entry_tincture_quantity = Entry(frame_sweetening, width=3, relief=GROOVE, font=("Times New Roman", 11))

    strength_a = entry_strength_alko
    quantity_a = entry_quantity_alko
    target_a = entry_total_strength
    tincture_quantity = entry_tincture_quantity

        
    variable_radio_sweetening_sub = IntVar()
    variable_radio_sweetening_sub.set("0")
    variable_radio_sweetening = IntVar()
    variable_radio_sweetening.set("0")
    radio_dry = Radiobutton(frame_sweetening, text = "wytrawna", font = ("Times New Roman", 11),
                                 variable=variable_radio_sweetening, value=50)
    radio_semidry = Radiobutton(frame_sweetening, text = "półwytrawna", font = ("Times New Roman", 11),
                                    variable=variable_radio_sweetening, value=100)
    radio_semisweet = Radiobutton(frame_sweetening, text="półsłodka", font=("Times New Roman", 11),
                                    variable=variable_radio_sweetening, value=200)
    radio__sweet = Radiobutton(frame_sweetening, text="słodka", font=("Times New Roman", 11),
                                  variable=variable_radio_sweetening, value=300)
    radio_liqueur = Radiobutton(frame_sweetening, text="likier/krem", font=("Times New Roman", 11),
                                  variable=variable_radio_sweetening, value=400 )
    radio_sugar = Radiobutton(frame_sweetening, text="cukier",font=("Times New Roman", 11),
                               variable=variable_radio_sweetening_sub, value=60)
    radio_honey = Radiobutton(frame_sweetening, text="miód", font=("Times New Roman", 11),
                             variable=variable_radio_sweetening_sub, value=75)
        # Przyciski
    button_calc_alkohol = Button(frame_alkohol, text="OBLICZ",
                           command=lambda: calc_alkohol(frame_alkohol, strength_a, quantity_a, target_a),
                           font=("Times New Roman", 10), relief=GROOVE)
    button_clear_alkohol = Button(frame_alkohol, text="WYCZYŚĆ", command=lambda: clear_alkohol(strength_a, quantity_a, target_a),
                            font=("Times New Roman", 10), relief=GROOVE)
    button_calc_sweetening = Button(frame_sweetening, text="OBLICZ",
                                     command= lambda: calc_sweetening(frame_sweetening, tincture_quantity, variable_radio_sweetening.get(), variable_radio_sweetening_sub.get()),
                             font=("Times New Roman", 10), relief=GROOVE)
    button_clear_sweetening = Button(frame_sweetening, text="WYCZYŚĆ",
                                      command= lambda: clear_sweetening(tincture_quantity, variable_radio_sweetening, variable_radio_sweetening_sub),
                                      font=("Times New Roman", 10), relief=GROOVE)

    button_close_calc_window = Button(window_calc_window, text="ZAMKNIJ", command=window_calc_window.destroy, font=("Times New Roman", 10), relief=GROOVE)
    


    frame_alkohol.grid(row=1, column=0)

    frame_sweetening.grid(row=2, column=0)

    label_strength_alko.grid(row=0, column=1, sticky=W)
    label_quantity_alko.grid(row=1, column=1, sticky=W)
    label_concentration.grid(row=2, column=1, sticky=W)
    label_water.grid(row=3, column=1, sticky=W)
    label_quantity_total.grid(row=4, column=1, sticky=W)
    label_litr_quantity_a.grid(row=1, column=3, sticky=W)
    label_percentage_strength.grid(row=0, column=3, sticky=W)
    laabel_procent_concentration.grid(row=2, column=3, sticky=W)

    label_label_choose_tincture_typee.grid(row=1, column = 1, rowspan= 2, sticky= E)
    label_choose_sweetening_sub.grid(row=1, column=2, columnspan=3, sticky=NE)
    label_tincture_quantity.grid(row=4, column=2, sticky=E)
    label_litr_tincture_quantity.grid(row=4, column=4, sticky=W)

    entry_strength_alko.grid(row=0, column=2, padx=20)
    entry_quantity_alko.grid(row=1, column=2, padx=20)
    entry_total_strength.grid(row=2, column=2, padx=20)

    entry_tincture_quantity.grid(row=4, column=3)

    button_calc_alkohol.grid(row=5, column=4, sticky=E)
    button_clear_alkohol.grid(row=5, column=0, sticky=W)

    button_calc_sweetening.grid(row=8, column=5, sticky=E)
    button_clear_sweetening.grid(row=8, column=0, sticky=W)

    radio_dry.grid(row=3, column=1, sticky=W)
    radio_semidry.grid(row=4, column=1, sticky=W)
    radio_semisweet.grid(row=5, column=1, sticky=W)
    radio__sweet.grid(row=6, column=1, sticky=W)
    radio_liqueur.grid(row=7, column=1, sticky=W)

    radio_sugar.grid(row=2, column=2)
    radio_honey.grid(row=2, column=3)

    button_close_calc_window.grid(row=3, column=0, sticky=W, pady=5)

def clear_new(name, strength, quantity,type, sub,composition_1,composition_2,composition_3, composition_4,composition_5, s_quantity_1, s_quantity_2, s_quantity_3,
           s_quantity_4,s_quantity_5,unit_1, unit_2,unit_3, unit_4, unit_5 ):
    """Function that clear field in new project window"""
    name.delete(0, END)
    strength.delete(0, END)
    quantity.delete(0, END)
    type.set("wytrawna")
    sub.set("cukier")
    composition_1.delete(0, END)
    composition_2.delete(0, END)
    composition_3.delete(0, END)
    composition_4.delete(0, END)
    composition_5.delete(0, END)
    s_quantity_1.delete(0, END)
    s_quantity_2.delete(0, END)
    s_quantity_3.delete(0, END)
    s_quantity_4.delete(0, END)
    s_quantity_5.delete(0, END)
    unit_1.set("szt.")
    unit_2.set("szt.")
    unit_3.set("szt.")
    unit_4.set("szt.")
    unit_5.set("szt.")

def save(window, name, strength, quantity,type, sub,composition_1,composition_2,composition_3, composition_4,composition_5, s_quantity_1, s_quantity_2, s_quantity_3,
          s_quantity_4,s_quantity_5,unit_1, unit_2,unit_3, unit_4, unit_5 ):
    """Function that preparing data to save, and then saving them using pickling."""
    name = str(name.get())
    strength = str(strength.get())
    quantity = str(quantity.get())
    type = str(type.get())
    sub = str(sub.get())
    composition_1 = str(composition_1.get())
    composition_2 = str(composition_2.get())
    composition_3 = str(composition_3.get())
    composition_4 = str(composition_4.get())
    composition_5 = str(composition_5.get())
    s_quantity_1 = str(s_quantity_1.get())
    s_quantity_2 = str(s_quantity_2.get())
    s_quantity_3 = str(s_quantity_3.get())
    s_quantity_4 = str(s_quantity_4.get())
    s_quantity_5 = str(s_quantity_5.get())
    unit_1 = str(unit_1.get())
    unit_2 = str(unit_2.get())
    unit_3 = str(unit_3.get())
    unit_4 = str(unit_4.get())
    unit_5 = str(unit_5.get())
    store_ = { 1:name, 2:strength, 3:quantity, 4:type, 5:sub, 6:composition_1+" "+s_quantity_1+" "+unit_1, 7:composition_2+" "+s_quantity_2+" "+unit_2,
    8:composition_3+" "+s_quantity_3+" "+unit_3, 9:composition_4+" "+s_quantity_4+" "+unit_4, 10:composition_5+" "+s_quantity_5+" "+unit_5,}
    file_store_ = open(name+".txt", "ab")
    pickle.dump(store_, file_store_)
    file_store_.close()
    messagebox.showinfo(window, "Nalewka została zapisana!")

def new_project():
    """Function that create window allowing to choose tincture composition and save project"""
    #Definiowanie zmiennych z list:
    variable_type_tincture = StringVar()
    variable_type_tincture.set("wytrawna")
    type = variable_type_tincture
    variable_sub__sweetening = StringVar()
    variable_sub__sweetening.set("cukier")
    sub = variable_sub__sweetening
    variable_unit_1 = StringVar()
    variable_unit_1.set("")
    unit_1 = variable_unit_1
    variable_unit_2 = StringVar()
    variable_unit_2.set("")
    unit_2 = variable_unit_2
    variable_unit_3 = StringVar()
    variable_unit_3.set("")
    unit_3 = variable_unit_3
    variable_unit_4 = StringVar()
    variable_unit_4.set("")
    unit_4 = variable_unit_4
    variable_unit_5 = StringVar()
    variable_unit_5.set("")
    unit_5 = variable_unit_5

    window_new_project = Toplevel(padx=10, pady=10)

    #Pola w oknie
    label_name = Label(window_new_project, text="Nazwa nalewki:", font=("Times New Roman", 11))
    entry_name = Entry(window_new_project, relief=GROOVE, font=("Times New Roman", 11))
    label_strength = Label(window_new_project, text="Zawartość alkoholu(%):", font=("Times New Roman", 11))
    entry_strength = Entry(window_new_project, width=2, relief=GROOVE, font=("Times New Roman", 11))
    label_quantity = Label(window_new_project, text="Ilość(L):", font=("Times New Roman", 11))
    entry_quantity = Entry(window_new_project, width=2, relief=GROOVE, font=("Times New Roman", 11))
    label_type = Label(window_new_project, text="type nalewki:",  font=("Times New Roman", 11))
    optionm_type = OptionMenu(window_new_project, variable_type_tincture, "wytrawna", "półwytrawna", "półsłodka", "słodka",
                        "likier/krem" )
    label_sub__sweetening = Label(window_new_project, text="Sub. słodząca:", font=("Times New Roman", 11))
    optionm_sub__sweetening = OptionMenu(window_new_project, variable_sub__sweetening, "cukier", "miód")
    button_close_new = Button(window_new_project, text="ZAMKNIJ", command=window_new_project.destroy,
                                       font=("Times New Roman", 10), relief=GROOVE)
    button_clear_new = Button(window_new_project, text="WYCZYŚĆ", font=("Times New Roman", 10), relief=GROOVE,
                                command=lambda:clear_new(name, strength, quantity,type, sub,composition_1,composition_2,composition_3, composition_4,
                                                      composition_5, s_quantity_1, s_quantity_2, s_quantity_3,s_quantity_4,s_quantity_5,
                                                      unit_1, unit_2,unit_3, unit_4, unit_5 ))
    button_save_new = Button(window_new_project, text="ZAPISZ", font=("Times New Roman", 10), relief=GROOVE,
                                command=lambda:save(window_new_project,name, strength, quantity,type, sub,composition_1,composition_2,
                                                     composition_3, composition_4,composition_5, s_quantity_1, s_quantity_2, s_quantity_3,
                                                     s_quantity_4,s_quantity_5,unit_1, unit_2,unit_3, unit_4, unit_5 ))

    name = entry_name
    strength = entry_strength
    quantity= entry_quantity


    frame_components_list = LabelFrame(window_new_project, text="Dodatki", padx=10, pady=10)

    #Pola w ramce
        #1
    label_component_1 = Label(frame_components_list, text="1. Składnik:", font=("Times New Roman", 11))
    entry_component_1 = Entry(frame_components_list, relief=GROOVE, font=("Times New Roman", 11))
    label_component_1_quantity = Label(frame_components_list, text="Ilość:", font=("Times New Roman", 11))
    entry_component_1_quantity = Entry(frame_components_list, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_component_1 = OptionMenu(frame_components_list, variable_unit_1, "l", "ml", "kg", "dag", "g","szt.")
        #2
    label_component_2 = Label(frame_components_list, text="2. Składnik:", font=("Times New Roman", 11))
    entry_component_2 = Entry(frame_components_list, relief=GROOVE, font=("Times New Roman", 11))
    label_component_2_quantity = Label(frame_components_list, text="Ilość:", font=("Times New Roman", 11))
    entry_component_2_quantity = Entry(frame_components_list, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_component_2 = OptionMenu(frame_components_list, variable_unit_2, "l", "ml", "kg", "dag", "g","szt.")
        #3
    label_component_3 = Label(frame_components_list, text="3. Składnik:", font=("Times New Roman", 11))
    entry_component_3 = Entry(frame_components_list, relief=GROOVE, font=("Times New Roman", 11))
    label_component_3_quantity = Label(frame_components_list, text="Ilość:", font=("Times New Roman", 11))
    entry_component_3_quantity = Entry(frame_components_list, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_component_3 = OptionMenu(frame_components_list, variable_unit_3, "l", "ml", "kg", "dag", "g","szt.")
        #4
    label_component_4 = Label(frame_components_list, text="4. Składnik:", font=("Times New Roman", 11))
    entry_component_4 = Entry(frame_components_list, relief=GROOVE, font=("Times New Roman", 11))
    label_component_4_quantity = Label(frame_components_list, text="Ilość:", font=("Times New Roman", 11))
    entry_component_4_quantity = Entry(frame_components_list, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_component_4 = OptionMenu(frame_components_list, variable_unit_4, "l", "ml", "kg", "dag", "g","szt.")
        #5
    label_component_5 = Label(frame_components_list, text="5. Składnik:", font=("Times New Roman", 11))
    entry_component_5 = Entry(frame_components_list, relief=GROOVE, font=("Times New Roman", 11))
    label_component_5_quantity = Label(frame_components_list, text="Ilość:", font=("Times New Roman", 11))
    entry_component_5_quantity = Entry(frame_components_list, width=4, relief=GROOVE, font=("Times New Roman", 11))
    optionm_component_5 = OptionMenu(frame_components_list, variable_unit_5, "l", "ml", "kg", "dag", "g","szt.")


    composition_1 = entry_component_1
    s_quantity_1 = entry_component_1_quantity
    composition_2 = entry_component_2
    s_quantity_2 = entry_component_2_quantity
    composition_3 = entry_component_3
    s_quantity_3 = entry_component_3_quantity
    composition_4 = entry_component_4
    s_quantity_4 = entry_component_4_quantity
    composition_5 = entry_component_5
    s_quantity_5 = entry_component_5_quantity


    label_name.grid(row=0, column=1, pady=10)
    entry_name.grid(row=0, column = 2,pady=10, sticky = W)
    label_strength.grid(row=1, column= 1, pady=10)
    entry_strength.grid(row=1, column=2, pady=10, sticky=W)
    label_quantity.grid(row=1, column=3, pady=10)
    entry_quantity.grid(row=1, column=4, pady=10, sticky=W)
    label_type.grid(row=2, column=1, pady=10)
    optionm_type.grid(row=2, column=2,pady=10, sticky=W)
    label_sub__sweetening.grid(row=2, column=3, pady=10)
    optionm_sub__sweetening.grid(row=2, column=4,pady=10, sticky=W)
    button_close_new.grid(row = 8, column = 0, padx=5, pady=5)
    button_clear_new.grid(row = 8, column=3, padx=5, pady=5)
    button_save_new.grid(row = 8, column=5, padx=5, pady=5)

    frame_components_list.grid(row=3, column=1, columnspan = 4)
        #1
    label_component_1.grid(row=3, column=1, padx= 10, pady = 10)
    entry_component_1.grid(row=3, column=2,padx= 10, pady = 10)
    label_component_1_quantity.grid(row=3, column=3,padx= 10, pady = 10)
    entry_component_1_quantity.grid(row=3, column=4,padx= 10, pady = 10)
    optionm_component_1.grid(row=3, column=5,padx= 10, pady = 10)
        #2
    label_component_2.grid(row=4, column=1,padx= 10, pady = 10)
    entry_component_2.grid(row=4, column=2)
    label_component_2_quantity.grid(row=4, column=3,padx= 10, pady = 10)
    entry_component_2_quantity.grid(row=4, column=4,padx= 10, pady = 10)
    optionm_component_2.grid(row=4, column=5,padx= 10, pady = 10)
        #3
    label_component_3.grid(row=5, column=1,padx= 10, pady = 10)
    entry_component_3.grid(row=5, column=2,padx= 10, pady = 10)
    label_component_3_quantity.grid(row=5, column=3,padx= 10, pady = 10)
    entry_component_3_quantity.grid(row=5, column=4,padx= 10, pady = 10)
    optionm_component_3.grid(row=5, column=5,padx= 10, pady = 10)
        #4
    label_component_4.grid(row=6, column=1,padx= 10, pady = 10)
    entry_component_4.grid(row=6, column=2,padx= 10, pady = 10)
    label_component_4_quantity.grid(row=6, column=3,padx= 10, pady = 10)
    entry_component_4_quantity.grid(row=6, column=4,padx= 10, pady = 10)
    optionm_component_4.grid(row=6, column=5)
        #5
    label_component_5.grid(row=7, column=1,padx= 10, pady = 10)
    entry_component_5.grid(row=7, column=2,padx= 10, pady = 10)
    label_component_5_quantity.grid(row=7, column=3,padx= 10, pady = 10)
    entry_component_5_quantity.grid(row=7, column=4,padx= 10, pady = 10)
    optionm_component_5.grid(row=7, column=5,padx= 10, pady = 10)

def point_file(frame_loading):
    """Function that load project ang inster data in separate frame"""
    open = filedialog.askopenfilename(initialdir="*/", title="Wybierz projekt:",
                           filetypees=(("pliki txt", "*.txt"), ("wszystkie pliki", "*.*")))

    file_store_ = open(file=open, mode="rb")
    store_ = pickle.load(file_store_)


    label_name = Label(frame_loading, text=store_[1], font=("Times New Roman", 16, "bold italic"), justify=CENTER)
    label_strength_i_quantity = Label(frame_loading, text="Moc nalewki: "+store_[2]+"\t Ilość: "+store_[3],
                              font=("Times New Roman", 11))
    label_type_i_sub = Label(frame_loading, text="type : "+store_[4]+"\t Sub. słodząca: "+store_[5],
                              font=("Times New Roman", 11))
    label_componenti = Label(frame_loading, text="SKŁADNIKI:", font=("Times New Roman", 11, "bold"))
    label_composition_1 = Label(frame_loading, text=store_[6], font=("Times New Roman", 11), justify = LEFT)
    label_composition_2 = Label(frame_loading, text=store_[7], font=("Times New Roman", 11), justify = LEFT,)
    label_composition_3 = Label(frame_loading, text=store_[8], font=("Times New Roman", 11), justify = LEFT,)
    label_composition_4 = Label(frame_loading, text=store_[9], font=("Times New Roman", 11), justify = LEFT,)
    label_composition_5 = Label(frame_loading, text=store_[10], font=("Times New Roman", 11), justify = LEFT,)

    label_name.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
    label_strength_i_quantity.grid(row=1, column=0,columnspan=3,sticky=W)
    label_type_i_sub.grid(row=2, column= 0,columnspan=3,sticky=W)
    label_componenti.grid(row=3, column=0, sticky=W,pady=10)
    label_composition_1.grid(row=4, column=1,sticky=W)
    label_composition_2.grid(row=5, column=1,sticky=W)
    label_composition_3.grid(row=6, column=1,sticky=W)
    label_composition_4.grid(row=7, column=1,sticky=W)
    label_composition_5.grid(row=8, column=1,sticky=W)


def load_project():
    """window wczytywanie uprzednio przygotowanego projektu"""
    window_load_project = Toplevel(padx=10, pady=10)
    frame_point_file = LabelFrame(window_load_project, text="Wybierz projekt:")
    frame_loading = LabelFrame(window_load_project, text="Wczytany projekt:")
    button_close = Button(window_load_project, text="ZAMKNIJ", command=window_load_project.destroy,
                                       font=("Times New Roman", 10), relief=GROOVE)
    button_clear = Button(window_load_project, text="WYCZYŚ", font=("Times New Roman", 10), relief=GROOVE,
                            command=frame_loading.destroy)

    label__choose = Label(frame_point_file, text="Wskaż projekt nalewki, któy chcesz załadować.", justify = LEFT,
                        font=("Times New Roman",11))
    button_load= Button(frame_point_file, text="WYBIERZ PLIK", font=("Times New Roman", 10), relief=GROOVE,
                           command=lambda:point_file(frame_loading))

    button_clear.grid(row = 5, column=2, padx=5, pady=5)
    button_close.grid(row= 5, column=0, padx=5, pady=5)

    frame_point_file.grid(row=0, column=1)
    frame_loading.grid(row=3, column=1)

    label__choose.grid(row=0, column=1, columnspan=3)
    button_load.grid(row=2, column=2, padx=5, pady=5)

def next(variable_radio_menu):
    """Function that calling functions based user choice"""
    if variable_radio_menu  == "calc_window":
        calc_window()
    elif variable_radio_menu  == "nowy":
        new_project()
    elif variable_radio_menu  == "wczytaj":
        load_project()




root = Tk()
root.title("Tincture")
variable_radio_menu = StringVar()
variable_radio_menu.set("0")
state_next = variable_radio_menu.get()


label_hello = Label(root, relief = RIDGE, text = "Witaj w Tincture!\nJest to program przeznaczony zarówno do wykonywania obliczeń koniecznych\n"
                         "do stworzenia nalewki, jak również pozwalający je projektować od zera\n"
                         "oraz otwierać wcześniej zrealizowane i zapisane projekty.\nWybierz co chcesz zrobić:", justify = LEFT, font = ("Times New Roman", 11))
radio_calc_window = Radiobutton(root, text = "Kalkulator",font = ("Times New Roman", 11),  variable = variable_radio_menu , value = "calc_window", command=lambda: check(state_next))
radio_new_project = Radiobutton(root, text = "Nowy projekt", font = ("Times New Roman", 11), variable = variable_radio_menu , value = "nowy", command=lambda: check(state_next) )
radio_load_project = Radiobutton(root, text = "Wczytaj projekt", font = ("Times New Roman", 11),  variable = variable_radio_menu , value = "wczytaj", command=lambda: check(state_next))
button_next = Button(root, text = "DALEJ", font = ("Times New Roman", 10), command = lambda: next(variable_radio_menu.get()), relief = GROOVE, state=DISABLED)
button_close = Button(root, text = "ZAMKNIJ", font = ("Times New Roman", 10), command = root.quit, relief = GROOVE)



label_hello.grid(row= 0, column = 1, columnspan = 3, padx = 10, pady = 10)
radio_calc_window.grid(row = 1, column = 1, padx = 10)
radio_new_project.grid(row = 1, column = 2, padx = 10)
radio_load_project.grid(row = 1, column = 3, padx = 10, pady = 5)
button_next.grid(row = 3, column = 4, padx = 10, pady = 10)
button_close.grid(row = 3, column = 0, padx = 10, pady = 10)

root.mainloop()
