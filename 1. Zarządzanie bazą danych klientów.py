from tkinter import *
from  tkinter import messagebox
import sqlite3

user_base = sqlite3.connect("user_base.db")
user_cursor = user_base.cursor()

#Create database if not exists with table in:
user_cursor.execute("""CREATE TABLE IF NOT EXISTS user_base (
login text,
password text)
""")

user_cursor.execute("INSERT INTO user_base VALUES (:login, :password)",
                            {'login': 'default',
                              'password': 'default01'
                             })
user_base.commit()

customer_base=sqlite3.connect("customer_base.db")
customer_cursor=customer_base.cursor()
#Create database if not exists
customer_cursor.execute("""CREATE TABLE IF NOT EXISTS customer_base (
f_name text,
s_name text,
city text,
zipcode text,
street text,
house_nr text,
apartment_nr text,
e_mail text,
phone_nr integer
)""")

def clear(f_name, s_name, city, zip_code_1, zip_code_2, street, house, apartment, email, phone):
    """This function clear all entry field."""
    f_name.delete(0,END)
    s_name.delete(0, END)
    city.delete(0, END)
    zip_code_1.delete(0, END)
    zip_code_2.delete(0, END)
    street.delete(0, END)
    house.delete(0, END)
    apartment.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)

def add_customer(f_name, s_name, city, zip_code_1, zip_code_2, street, house, apartment, email, phone):
    """Function adding new customer to the customer database"""
    customer_base = sqlite3.connect("customer_base.db")
    customer_cursor = customer_base.cursor()
    customer_cursor.execute("INSERT INTO customer_base VALUES (:f_name, :s_name, :city, :zipcode, :street, :house_nr, :apartment_nr, :e_mail, :phone_nr)",
                           {
                               'f_name': f_name.get(),
                               's_name': s_name.get(),
                               'city': city.get(),
                               'zipcode': zip_code_1.get()+"-"+zip_code_2.get(),
                               'street': street.get(),
                               'house_nr': house.get(),
                               'apartment_nr': apartment.get(),
                               'e_mail': email.get(),
                               'phone_nr': phone.get()
                           })
    customer_base.commit()
    messagebox.showinfo("Sukces!", "Klient został dodany!")

def numerical_entry(inp):
    """"This function allow to enter only numerical data"""
    if inp.isdigit():
        return TRUE
    elif inp is "":
        return TRUE
    else: return FALSE

def text_entry(inp):
    """This function allow to enter only alpha data"""
    if inp.isalpha():
        return TRUE
    elif inp is "":
        return TRUE
    else: return False

def confirm(id):
    """Funkcja żądająca od użytkownika confirmenia deleteięcia recordu z bazy, a następni go usuwająca w przypadku
    otrzymania answerowiedzi pozytywnej."""
    answer = messagebox.askyesno("Potwierdź", "Czy jesteś pewien, że chcesz deleteąć record o id {}?".format(id.get()))
    if answer == 'yes':
        customer_base = sqlite3.connect("customer_base.db")
        customer_cursor = customer_base.cursor()
        customer_cursor.execute("DELETE FROM customer_base WHERE oid = " + id.get())
        id.delete(0, END)
    else: pass

def update(f_name, s_name, city, zipcode, street, house, apartment, email, phone, id):
    """Function that update record in db"""
    customer_base = sqlite3.connect("customer_base.db")
    customer_cursor = customer_base.cursor()
    customer_cursor.execute("""UPDATE customer_base SET
    f_name = :f_name,
    s_name = :s_name,
    city = :city,
    zipcode= :zipcode,
    street = :street,
    house_nr = :house,
    apartment_nr = :apartment,
    e_mail = :email,
    phone_nr = :phone
    WHERE oid= :oid""", {
        'f_name': f_name.get(),
        's_name': s_name.get(),
        'city': city.get(),
        'zipcode': zipcode.get(),
        'street': street.get(),
        'house': house.get(),
        'apartment': apartment.get(),
        'email': email.get(),
        'phone': phone.get(),
        'oid': id

    })
    customer_base.commit()

def search_in_data_base(frame, parameter_1, parameter_2, id, id_or_selected, selected_parameters):
    """Funkcja SEARCHąca recordu w bazie, a następnie wypisująca wynik w ramce."""
    customer_base = sqlite3.connect("customer_base.db")
    customer_cursor = customer_base.cursor()
    if id_or_selected.get() == "id":
        customer_cursor.execute('SELECT *, oid FROM customer_base WHERE oid = ?', (id.get(),))
        customer_base.commit()
    elif id_or_selected.get() == "select":
        if selected_parameters.get() == "imię i nazwisko":
            customer_cursor.execute('SELECT *, oid FROM customer_base WHERE f_name = ? AND s_name = ?',(parameter_1.get(),
                                                                                                  parameter_2.get(),))
            customer_base.commit()
        elif selected_parameters.get() == "miasto:":
            customer_cursor.execute('SELECT * ,oid FROM customer_base WHERE city = ?', (parameter_1.get(),))
            customer_base.commit()
        elif selected_parameters.get() == "e-mail:":
            customer_cursor.execute('SELECT *, oid FROM customer_base WHERE e_mail = ?', (parameter_1.get(),))
            customer_base.commit()
        elif selected_parameters.get() == "nr tel.:":
            customer_cursor.execute('SELECT *, oid FROM customer_base WHERE phone_nr = ?', (parameter_1.get(),))
            customer_base.commit()
        else:pass
    else: pass
    customer_records = customer_cursor.fetchall()

    label_id_heading = Label(frame, text="ID:", font=("Times New Roman", 12, "bold italic"))
    label_f_name_heading = Label(frame, text="Imię", font=("Times New Roman", 12, "bold italic"))
    label_s_name_heading = Label(frame, text="Nazwisko:", font=("Times New Roman", 12, "bold italic"))
    label_city_heading = Label(frame, text="Miasto:", font=("Times New Roman", 12, "bold italic"))
    label_zipcode_heading = Label(frame, text="Kod pocztowy:", font=("Times New Roman", 12, "bold italic"))
    label_street_heading = Label(frame, text="Ulica:", font=("Times New Roman", 12, "bold italic"))
    label_house_heading = Label(frame, text="Nr domu:", font=("Times New Roman", 12, "bold italic"))
    label_apartment_heading = Label(frame, text="Nr mieszkania:", font=("Times New Roman", 12, "bold italic"))
    label_email_heading = Label(frame, text="E-MAIL:", font=("Times New Roman", 12, "bold italic"))
    label_phone_heading = Label(frame, text="NR tel.:", font=("Times New Roman", 12, "bold italic"))

    id_customer=""
    f_name_customer=""
    s_name_customer = ""
    city_customer = ""
    zipcode_customer = ""
    street_customer = ""
    house_customer = ""
    apartment_customer = ""
    email_customer = ""
    phone_customer = ""

    for record in customer_records:
        id_customer += str(record[9])+"\n"
        f_name_customer += str(record[0])+"\n"
        s_name_customer += str(record[1])+"\n"
        city_customer += str(record[2])+"\n"
        zipcode_customer += str(record[3])+"\n"
        street_customer += str(record[4])+"\n"
        house_customer += str(record[5])+"\n"
        apartment_customer += str(record[6])+"\n"
        email_customer += str(record[7])+"\n"
        phone_customer += str(record[8])+"\n"

        label_id = Label(frame, text=id_customer,font=("Times New Roman", 12), justify=LEFT)
        label_f_name = Label(frame, text=f_name_customer,font=("Times New Roman", 12), justify=LEFT)
        label_s_name = Label(frame, text=s_name_customer,font=("Times New Roman", 12), justify=LEFT)
        label_city = Label(frame, text=city_customer,font=("Times New Roman", 12), justify=LEFT)
        label_zipcode = Label(frame, text=zipcode_customer,font=("Times New Roman", 12), justify=LEFT)
        label_street = Label(frame, text=street_customer,font=("Times New Roman", 12), justify=LEFT)
        label_house = Label(frame, text=house_customer,font=("Times New Roman", 12), justify=LEFT)
        label_apartment = Label(frame, text=apartment_customer,font=("Times New Roman", 12), justify=LEFT)
        label_email = Label(frame, text=email_customer,font=("Times New Roman", 12), justify=LEFT)
        label_phone = Label(frame, text=phone_customer,font=("Times New Roman", 12), justify=LEFT)

        label_id.grid(row=1, column=0, rowspan=10, padx=5)
        label_f_name.grid(row=1, column=1, rowspan=10, padx=5)
        label_s_name.grid(row=1, column=2, rowspan=10, padx=5)
        label_city.grid(row=1, column=3, rowspan=10, padx=5)
        label_zipcode.grid(row=1, column=4, rowspan=10, padx=5)
        label_street.grid(row=1, column=5, rowspan=10, padx=5)
        label_house.grid(row=1, column=6, rowspan=10, padx=5)
        label_apartment.grid(row=1, column=7, rowspan=10, padx=5)
        label_email.grid(row=1, column=8, rowspan=10, padx=5)
        label_phone.grid(row=1, column=9, rowspan=10, padx=5)


    label_id_heading.grid(row=0, column=0, padx=5, pady=10)
    label_f_name_heading.grid(row=0, column=1, padx=5, pady=10)
    label_s_name_heading.grid(row=0, column=2, padx=5, pady=10)
    label_city_heading.grid(row=0, column=3, padx=5, pady=10)
    label_zipcode_heading.grid(row=0, column=4, padx=5, pady=10)
    label_street_heading.grid(row=0, column=5, padx=5, pady=10)
    label_house_heading.grid(row=0, column=6, padx=5, pady=10)
    label_apartment_heading.grid(row=0, column=7, padx=5, pady=10)
    label_email_heading.grid(row=0, column=8, padx=5, pady=10)
    label_phone_heading.grid(row=0, column=9, padx=5, pady=10)
    customer_base.commit()

def entry_unlocking(parameter_1, parameter_2, id,id_or_selected, selected_parameters, button_search):
    """window that blocks the ability to enter data and search a record before user chooses searching parameter."""
    if id_or_selected.get() == "select":
        if selected_parameters.get() == "imię i nazwisko":
            parameter_1.configure(state=NORMAL)
            parameter_2.configure(state=NORMAL)
            button_search.configure(state=NORMAL)
        elif selected_parameters.get() != "0":
            parameter_1.configure(state=NORMAL)
            parameter_2.configure(state=DISABLED)
            button_search.configure(state=NORMAL)
        else: pass
    elif id_or_selected.get() == "id":
        id.configure(state=NORMAL)
        button_search.configure(state=NORMAL)
    else: pass

def search_record_window():
    """Function that creates a window which allows to choose searching parameter and enter
    searching value and then it develops searching base function"""
    search_window = Toplevel()
    search_window.title("Szukaj rekordu")
    frame_entry = LabelFrame(search_window, text="Wprowadź dane do wyszukania:")
    frame_found = LabelFrame(search_window, text="Znaleziony rekord:")
    parameters = ["imię i nazwisko:", "miasto:","e-mail:","nr tel.:"]
    selected_parameters = StringVar()
    selected_parameters.set(parameters[1])
    id_or_selected =StringVar()
    id_or_selected.set("0")

    entry_parameters_1 = Entry(frame_entry, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    entry_parameters_2 = Entry(frame_entry, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    label_or = Label(frame_entry, text="lub", font=("Times New Roman", 12))

    entry_id = Entry(frame_entry, font=("Times New Roman", 12), relief=GROOVE, state=DISABLED)
    parameter_1 = entry_parameters_1
    parameter_2 = entry_parameters_2
    id = entry_id
    button_search = Button(frame_entry, text="SZUKAJ", font=("Times New Roman", 12), state=DISABLED,
                           command=lambda: search_in_data_base(frame_found, parameter_1, parameter_2, id,
                                                                  id_or_selected,  selected_parameters) )
    button_close = Button(frame_entry, text="ZAMKNIJ", font=("Times New Roman", 12), command=search_window.destroy)
    radio_select = Radiobutton(frame_entry, text="Wubierz parametr", variable=id_or_selected,
                                value="select", font=("Times New Roman", 12),
                                command=lambda: entry_unlocking(parameter_1, parameter_2, id,id_or_selected,
                                                                          selected_parameters, button_search))
    radio_id = Radiobutton(frame_entry, text="Szukaj po ID:", variable=id_or_selected, value="id",
                           font=("Times New Roman", 12),
                           command=lambda: entry_unlocking(parameter_1, parameter_2, id,id_or_selected,
                                                                     selected_parameters, button_search))
    om_wybierz = OptionMenu(frame_entry, selected_parameters, *parameters)
    frame_entry.grid(row=0, column=0)
    frame_found.grid(row=1, column=0)
    radio_select.grid(row=0, column=0, sticky=W)
    label_or.grid(row=1, column=0)
    radio_id.grid(row=2, column=0, sticky=W)
    om_wybierz.grid(row=0, column=1, padx=1)
    entry_parameters_1.grid(row=0, column=2, padx=5, sticky=W)
    entry_parameters_2.grid(row=0, column=3, padx=5, sticky=W)
    entry_id.grid(row=2, column=1, sticky=W)
    button_search.grid(row = 3, column=3, pady= 20)
    button_close.grid(row=3, column=0, pady= 20)

def update_record_fill_window(id, window):
    """Function creates an extra frame in update window,
    put text field and entry field in it then it fills them with taken data from customer data base."""
    id = id.get()

    customer_base = sqlite3.connect("customer_base.db")
    customer_cursor = customer_base.cursor()
    customer_cursor.execute("SELECT * FROM customer_base WHERE oid=" +id)
    records = customer_cursor.fetchall()


    frame_data = LabelFrame(window, text="data recordu:")
    label_f_name_edit = Label(frame_data, text="Imię:", font=("Times New Roman", 12))
    entry_f_name_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE)
    label_s_name_edit = Label(frame_data, text="Nazwisko:", font=("Times New Roman", 12))
    entry_s_name_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE)
    label_city_edit = Label(frame_data, text="Miasto:", font=("Times New Roman", 12))
    entry_city_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE)
    label_zipcode_edit = Label(frame_data, text="Kod pocztowy:", font=("Times New Roman", 12))
    entry_zipcode_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE, widt=6)
    label_street_edit = Label(frame_data, text="Ulica:", font=("Times New Roman", 12))
    entry_street_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE)
    label_house_nr_edit = Label(frame_data, text="Nr domu:", font=("Times New Roman", 12))
    entry_house_nr_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_apartment_nr_edit = Label(frame_data, text="Nr mieszkania:", font=("Times New Roman", 12))
    entry_apartment_nr_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_e_mail_edit = Label(frame_data, text="E-mail:", font=("Times New Roman", 12))
    entry_e_mail_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE)
    label_phone_nr_edit = Label(frame_data, text="Nr tel.:", font=("Times New Roman", 12))
    entry_phone_nr_edit = Entry(frame_data, font=("Times New Roman", 12), relief=GROOVE, width=9)

    f_name = entry_f_name_edit
    s_name = entry_s_name_edit
    city = entry_city_edit
    zipcode = entry_zipcode_edit
    street = entry_street_edit
    house = entry_house_nr_edit
    apartment = entry_apartment_nr_edit
    email = entry_e_mail_edit
    phone = entry_phone_nr_edit

    button_update = Button(frame_data, text="ZAKTUALIZUJ", font=("Times New Roman", 12),
                               command=lambda:update(f_name,s_name,city,zipcode,street,house,apartment,email,phone, id))

    frame_data.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
    label_f_name_edit.grid(row=0, column=1, pady=10, padx=5, sticky=W)
    entry_f_name_edit.grid(row=0, column=2, pady=10, padx=5, sticky=W)
    label_s_name_edit.grid(row=1, column=1, pady=10, padx=5, sticky=W)
    entry_s_name_edit.grid(row=1, column=2, pady=10, padx=5, sticky=W)
    label_city_edit.grid(row=2, column=1, pady=10, padx=5, sticky=W)
    entry_city_edit.grid(row=2, column=2, pady=10, padx=5, sticky=W)
    label_zipcode_edit.grid(row=3, column=1, pady=10, padx=5, sticky=W)
    entry_zipcode_edit.grid(row=3, column=2, pady=10, padx=5, sticky=W)
    label_street_edit.grid(row=4, column=1, pady=10, padx=5, sticky=W)
    entry_street_edit.grid(row=4, column=2, pady=10, padx=5, sticky=W)
    label_house_nr_edit.grid(row=5, column=1, pady=10, padx=5, sticky=W)
    entry_house_nr_edit.grid(row=5, column=2, pady=10, padx=5, sticky=W)
    label_apartment_nr_edit.grid(row=6, column=1, pady=10, padx=5, sticky=W)
    entry_apartment_nr_edit.grid(row=6, column=2, pady=10, padx=5, sticky=W)
    label_e_mail_edit.grid(row=7, column=1, pady=10, padx=5, sticky=W)
    entry_e_mail_edit.grid(row=7, column=2, pady=10, padx=5, sticky=W)
    label_phone_nr_edit.grid(row=8, column=1, pady=10, padx=5, sticky=W)
    entry_phone_nr_edit.grid(row=8, column=2, pady=10, padx=5, sticky=W)
    button_update.grid(row=9, column=3, padx=5, pady=5)

    for record in records:
        entry_f_name_edit.insert(0, record[0])
        entry_s_name_edit.insert(0, record[1])
        entry_city_edit.insert(0, record[2])
        entry_zipcode_edit.insert(0, record[3])
        entry_street_edit.insert(0, record[4])
        entry_house_nr_edit.insert(0, record[5])
        entry_apartment_nr_edit.insert(0, record[6])
        entry_e_mail_edit.insert(0, record[7])
        entry_phone_nr_edit.insert(0, record[8])

def window_update_record_point():
    """Function allowing to search data with entery ID"""
    window_update = Toplevel()
    window_update.title("Aktualizacja rekordu")
    frame_point_record = LabelFrame(window_update, text="Wskaż identyfikator aktualizowanego rekordu:")
    label_id = Label(frame_point_record, text="Identyfikator:", font=("Times New Roman", 12))
    entry_id = Entry(frame_point_record, font=("Times New Roman", 12), relief=GROOVE)
    id=entry_id
    button_search = Button(frame_point_record, text="SZUKAJ", font=("Times New Roman", 12),
                           command=lambda: update_record_fill_window(id, window_update))
    button_close = Button(window_update, text="ZAMKNIJ", font=("Times New Roman", 12),
                           command=window_update.destroy)
    frame_point_record.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    label_id.grid(row=0, column=0)
    entry_id.grid(row=0, column=1)
    button_search.grid(row=1, column=1, padx=5, pady=5)
    button_close.grid(row=2, column=1, padx=5, pady=5, sticky=E)

def window_delete_record():
    """Function that creates  window allowing to entry record ID and then to develop function
    that deletes it from data base"""
    window_delete = Toplevel()
    window_delete.title("Usuwanie rekordu z bazy klientów")
    label_info = Label(window_delete, text="Wprowadź identyfikator usuwanego klienta:",
                       font=("Times New Roman", 14, "bold italic"))
    entry_record_id = Entry(window_delete, font=("Times New Roman", 12), relief=GROOVE)
    record_id = entry_record_id
    button_close = Button(window_delete, text="ZAMKNIJ", font=("Times New Roman", 12), command=window_delete.destroy)
    button_delete_record = Button(window_delete,text="USUŃ", font=("Times New Roman", 12),
                                command=lambda: confirm(record_id))
    label_info.grid(row=0, column=1, padx=10, pady=10)
    entry_record_id.grid(row=1, column=1)
    button_close.grid(row=2, column=0, padx=5, pady=5)
    button_delete_record.grid(row=2, column=2, padx=5, pady=5)

    reg_numerical = root.register(numerical_entry)
    entry_record_id.config(validate="key", validatecommand=(reg_numerical, '%P'))

def window_entry_record():
    """Function that creates a window that allows to entry a new customer data, then it developes entry function to data base"""

    window_entry = Toplevel()
    window_entry.title("Wprowadź nowego klienta do bazy")
    label_info = Label(window_entry, text="Wprowadź dane nowego klienta:",
                       font=("Times New Roman", 14, "bold italic"))
    label_f_name = Label(window_entry, text="Imię:", font=("Times New Roman", 12))
    entry_f_name = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE)
    label_s_name = Label(window_entry, text="Nazwisko:", font=("Times New Roman", 12))
    entry_s_name = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE)
    label_city = Label(window_entry, text="Miasto:", font=("Times New Roman", 12))
    entry_city = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE)
    label_zipcode= Label(window_entry, text="Kod pocztowy:", font=("Times New Roman", 12))
    entry_zipcode_1 = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE, widt=2)
    label_lacznik_zipcode = Label(window_entry,text="-", font=("Times New Roman", 12))
    etry_zipcode_2  = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE, width=3)
    label_street = Label(window_entry, text="Ulica:", font=("Times New Roman", 12))
    entry_street = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE)
    label_house_nr = Label(window_entry, text="Nr domu:", font=("Times New Roman", 12))
    entry_house_nr= Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_apartment_nr = Label(window_entry, text="Nr mieszkania:", font=("Times New Roman", 12))
    entry_apartment_nr = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE, width=5)
    label_e_mail = Label(window_entry, text="E-mail:", font=("Times New Roman", 12))
    entry_e_mail  = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE)
    label_phone_nr = Label(window_entry, text="Nr tel:", font=("Times New Roman", 12))
    entry_phone_nr  = Entry(window_entry, font=("Times New Roman", 12), relief=GROOVE, width=9)

    reg_numerical = root.register(numerical_entry)
    reg_text = root.register(text_entry)

    entry_phone_nr.config(validate="key", validatecommand=(reg_numerical, '%P'))
    entry_f_name.config(validate="key", validatecommand=(reg_text, '%P'))
    entry_zipcode_1.config(validate="key", validatecommand=(reg_numerical, '%P'))
    etry_zipcode_2.config(validate="key", validatecommand=(reg_numerical, '%P'))
    entry_s_name.config(validate="key", validatecommand=(reg_text, '%P'))
    entry_city.config(validate="key", validatecommand=(reg_text, '%P'))

    f_name = entry_f_name
    s_name = entry_s_name
    city = entry_city
    zip_code_1 = entry_zipcode_1
    zip_code_2 = etry_zipcode_2
    street = entry_street
    house = entry_house_nr
    apartment = entry_apartment_nr
    email = entry_e_mail
    phone = entry_phone_nr

    button_close =  Button(window_entry, text="ZAMKNIJ", font=("Times New Roman", 12),
                            command=window_entry.destroy)
    button_clear = Button(window_entry, text="WYCZYSĆ", font=("Times New Roman", 12),
                            command=lambda:clear(f_name, s_name, city, zip_code_1, zip_code_2, street, house,
                                                   apartment, email, phone))
    button_add= Button(window_entry, text="DODAJ", font=("Times New Roman", 12),
                         command=lambda: add_customer(f_name, s_name, city, zip_code_1, zip_code_2, street, house,
                                                 apartment, email, phone))

    label_info.grid(row=0, column=1, columnspan=5, pady=10)
    label_f_name.grid(row=1, column=1, pady=10, padx=5, sticky=W)
    entry_f_name.grid(row=1, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_s_name.grid(row=2, column=1, pady=10, padx=5, sticky=W)
    entry_s_name.grid(row=2, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_city.grid(row=3, column=1, pady=10, padx=5, sticky=W)
    entry_city.grid(row=3, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_zipcode.grid(row=4, column=1, pady=10, padx=5, sticky=W)
    entry_zipcode_1.grid(row=4, column=2, pady=10, padx=5, sticky=W)
    label_lacznik_zipcode.grid(row=4, column=3, pady=10, sticky=W)
    etry_zipcode_2.grid(row=4, column=4, pady=10, sticky=W)
    label_street.grid(row=5, column=1, pady=10, padx=5, sticky=W)
    entry_street.grid(row=5, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_house_nr.grid(row=6, column=1, pady=10, padx=5, sticky=W)
    entry_house_nr.grid(row=6, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_apartment_nr.grid(row=7, column=1, pady=10, padx=5, sticky=W)
    entry_apartment_nr.grid(row=7, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_e_mail.grid(row=8, column=1, pady=10, padx=5, sticky=W)
    entry_e_mail.grid(row=8, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    label_phone_nr.grid(row=9, column=1, pady=10, padx=5, sticky=W)
    entry_phone_nr.grid(row=9, column=2, pady=10, padx=5, sticky=W, columnspan=3)
    button_close.grid(row=10, column=0, pady=5, padx=10, sticky=W)
    button_clear.grid(row=10, column=5, pady=5, padx=10)
    button_add.grid(row=10, column=6, pady=5, padx=10, sticky=E)

def register_in_database(login_field, password_field, confirm_password_field, window):
    """Function that verifies entry data correctness while registing. After that function puts them in user data base"""
    login = login_field.get()
    password = password_field.get()
    confirm_password = confirm_password_field.get()
    if password == "" or login== "" or confirm_password == "":
        messagebox.showinfo("BŁĄD!", "Żadne z pól nie może być puste!")
    elif password == confirm_password:
        user_base = sqlite3.connect("user_base.db")
        user_cursor = user_base.cursor()
        user_cursor.execute("INSERT INTO user_base VALUES (:login, :password)",
                                 {'login': login,
                                  'password': password})
        user_base.commit()
        messagebox.showinfo("SUKCES!", "Użytkownik został zarejestrowany!" )
    else:
        messagebox.showinfo("BŁĄD!", "Pola 'hasło' i 'potwierdź hasło' nie są takie same!")

def window_register():
    """Window creating function that allows to entry new user data and develop register function in user db."""
    window_register = Toplevel()
    window_register.title("Zarejestruj nowego użytkownika")
    label_rejestracja = Label(window_register, text="Rejestracja", font=("Times New Roman", 14, "bold italic"))
    label_login = Label(window_register, text="Wprowadź login:", font=("Times New Roman", 12))
    entry_login = Entry(window_register, font=("Times New Roman", 12), relief=GROOVE)
    label_password= Label(window_register, text="Wprowadź hasło:", font=("Times New Roman", 12))
    entry_password= Entry(window_register, font=("Times New Roman", 12), relief=GROOVE, show="*")
    label_confirm_pass=Label(window_register, text="Potwierdź hasło:", font=("Times New Roman", 12))
    entry_confirm_pass = Entry(window_register, font=("Times New Roman", 12), relief=GROOVE, show="*")
    login = entry_login
    password = entry_password
    pot_password = entry_confirm_pass
    button_register = Button(window_register,text="ZAREJESTRUJ", font=("Times New Roman", 12),
                                command=lambda:register_in_database(login, password, pot_password, window_register))
    button_close = Button(window_register, text="ZAMKNIJ", font=("Times New Roman", 12),
                            command=window_register.destroy)

    label_rejestracja.grid(row=0, column=0, columnspan=3, pady=10)
    label_login.grid(row=1, column=0, pady=10, padx=5)
    entry_login.grid(row=1, column=1, pady=10, padx=5)
    label_password.grid(row=2, column=0, pady=10, padx=5)
    entry_password.grid(row=2, column=1, pady=10, padx=5)
    label_confirm_pass.grid(row=3, column=0, pady=10, padx=5)
    entry_confirm_pass.grid(row=3, column=1, pady=10, padx=5)
    button_register.grid(row=4, column=1, sticky=E, pady=5, padx=5)
    button_close.grid(row=4, column=0, sticky=W, pady=5, padx=5)

def window_main_menu_after_log_in(frame):
    """Function that destroy log in frame and replace it with main menu frame after successfull veryfying login and password."""
    frame.destroy()

    frame_window_main_menu = LabelFrame(root)
    label_info_general = Label(frame_window_main_menu,
                              text="Witaj,\n"
                                   "w bazie danych zawierającej rekordu klientów.\n"
                                   "Pozwala ona na zarejestrowanie nowego użytkownika,\n"
                                   "szukanie recordów klientów w bazie, ich modyfikację oraz usuwanie. \n"
                                   "Wybierz co chcesz zrobić:", font=("Times New Roman", 14), justify=CENTER)
    button_register = Button(frame_window_main_menu, text="Zarejestruj nowego użytkownika",
                                font=("Times New Roman", 12), command=window_register)
    button_search = Button(frame_window_main_menu, text="Szukaj rekordu w bazie", font=("Times New Roman", 12),
                           command=search_record_window)
    button_entry = Button(frame_window_main_menu, text="Wprowadź nowy rekord", font=("Times New Roman", 12),
                             command=window_entry_record)
    button_update = Button(frame_window_main_menu, text="Zaktualizuj rekord", font=("Times New Roman", 12),
                                command=window_update_record_point)
    button_delete = Button(frame_window_main_menu, text="Usuń record z bazy", font=("Times New Roman", 12),
                         command=window_delete_record)
    button_close = Button(frame_window_main_menu, text="ZAMKNIJ", font=("Times New Roman", 12), command=root.quit)
    frame_window_main_menu.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    label_info_general.grid(row=0, column=0, columnspan=3, pady=20)
    button_register.grid(row=1, column=1,pady=10, ipadx=150, ipady=5)
    button_search.grid(row=2, column=1,pady=10, ipadx=176, ipady=5)
    button_entry.grid(row=3, column=1,pady=10, ipadx=173, ipady=5)
    button_update.grid(row=4, column=1,pady=10, ipadx=193, ipady=5)
    button_delete.grid(row=5, column=1,pady=10, ipadx=190, ipady=5)
    button_close.grid(row=6, column=1,pady=10, sticky=E)

def verify_data(login, password, frame):
    verify_login=login.get()
    verify_password=password.get()
    user_base = sqlite3.connect("user_base.db")
    user_cursor = user_base.cursor()
    user_cursor.execute('SELECT * FROM user_base WHERE login = ? AND password = ?',(verify_login, verify_password))
    user_base.commit()
    if user_cursor.fetchall():
        window_main_menu_after_log_in(frame)
    else:
        messagebox.showerror("Błąd logowania!", "Wprowadzony login lub hasło są nieprawidłowe!")
        login.delete(0, END)
        password.delete(0, END)

def window_log_in():
    """window with frame that demands from user data to verify. After getting them and verifying their correctness it
    developes a frame in main window"""
    global root
    root = Tk()
    root.title("Baza klientów")

    frame_log = LabelFrame(root, padx=5, pady=5)
    label_entry = Label(frame_log, text="Wprowadź dane logowania:", font=("Times New Roman", 12, "bold italic"),
                           justify=CENTER)
    label_login = Label(frame_log, text="Login:", font=("Times New Roman", 12))
    entry_login = Entry(frame_log, relief=GROOVE, font=("Times New Roman", 12))
    label_password = Label(frame_log, text="Hasło:", font=("Times New Roman", 12))
    entry_password = Entry(frame_log, relief=GROOVE, font=("Times New Roman", 12), show='*')
    button_close = Button(frame_log, text="ZAMKNIJ", font=("Times New Roman", 10), command=root.quit)

    button_log_in = Button(frame_log, text="ZALOGUJ", font=("Times New Roman", 10),
                            command=lambda: verify_data(entry_login, entry_password, frame_log))
    frame_log.grid(row=0, column=0)
    label_entry.grid(row=0, column=0,columnspan=2, padx=60, pady=10)
    label_login.grid(row=1, column=0)
    label_password.grid(row=2, column=0)
    entry_login.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)
    button_close.grid(row=3, column=0, pady=10)
    button_log_in.grid(row=3, column=1, pady=10)

if __name__== "__main__":
    window_log_in()
    root.mainloop()
