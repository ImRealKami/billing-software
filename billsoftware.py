from tkinter import *
from tkinter import messagebox
import random
import os
import tempfile
import smtplib as smtp

window = Tk()
screen_width = 1920
screen_height = 1080
window.geometry(f"{screen_width}x{screen_height}")
window.title("Billing")
photo = PhotoImage(file = "billing.png")
window.iconphoto(False, photo)
window.update()

def email():
    def send_mail():
        try:
            connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
            email_addr = sender_entry.get()
            email_passwd = password_entry.get()
            connection.login(email_addr, email_passwd)
            message=email_textarea.get(1.0, END)
            to_addrs=reciever_entry.get()
            connection.sendmail(email_addr, to_addrs, message)
            connection.close()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root)
        except:
            messagebox.showerror('Error', 'We think you did not enter an application passkey', parent=root)



    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root = Toplevel()
        root.title('Send Mail')
        root.config(bg='gray20')
        root.resizable(0, 0)

        senderframe = LabelFrame(root, text='SENDER', font=('times new roman', 18, 'bold'), fg="white", bg="gray20", bd=5)
        senderframe.grid(row=0, column=0)
        
        senderlabel = Label(senderframe, text="Sender's Email", font=("times new roman", 15))
        senderlabel.grid(row=0, column=0)

        sender_entry = Entry(senderframe, font=("arial", 14), bd=3, width=22, relief=GROOVE)
        sender_entry.grid(row=0, column=1, padx=10, pady=10)
        
        password_label = Label(senderframe, text="Password", font=("times new roman", 15))
        password_label.grid(row=1, column=0, padx=10, pady=8)

        password_entry = Entry(senderframe, font=("arial", 14), bd=3, width=22, relief=GROOVE, show='*')
        password_entry.grid(row=1, column=1, padx=10, pady=8)

        reciptent_frame = LabelFrame(root, text="RECIPTENT", font=("times new roman", 18, 'bold'), fg="white", bg="gray20", bd=5)
        reciptent_frame.grid(row=1, column=0, padx=40, pady=20)

        reciever_label = Label(reciptent_frame, text="Email Address", font=("times new roman", 15))
        reciever_label.grid(row=0, column=0, padx=10, pady=8)
        
        reciever_entry = Entry(reciptent_frame, font=("arial", 14), bd=3, width=22, relief=GROOVE)
        reciever_entry.grid(row=0, column=1, padx=10, pady=10)

        message_label = Label(reciptent_frame, text="Message", font=("times new roman", 18, 'bold'), fg="white", bg="gray20", bd=5)
        message_label.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(reciptent_frame, font=("arial", 15), bd=3, relief=SUNKEN, width=40, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END))

        send_button = Button(root, text="Send", font=("times new roman", 15, 'bold'), width=15, command=send_mail)
        send_button.grid(row=2, column=0, pady=20)
        
def print():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w', encoding="utf-8").write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_entry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)  
            f.close()
            break
        else:
            messagebox.showerror('Error', 'Invalid Bill')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Yes or No', 'Do you want to save the bill?')
    file = Text(window, font=("arial", 15))
    if result>0:
        f = open(f'bills/{billnumber}.txt', 'w', encoding='utf-8')
        f.write(bill_data)
        f.close()
        messagebox.showinfo('Saved', f'Bill {billnumber} been saved')
        billnumber = random.randint(1000, 10000)
    else:
        return

billnumber = random.randint(1000, 10000)

def bill():
    if name_entry.get() == '' or contact_entry.get() == '':
        messagebox.showerror('Error', 'Customer Details not entered')
    elif cos_entry.get() == '' or groc_entry.get() == '' or dri_entry == '':
        messagebox.showerror('Error', 'No Products Purchased')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, "\t\t**Welcome to Target Market**\n")
        textarea.insert(END, f"\nBill Number: {billnumber}\n")
        textarea.insert(END, f"Customer Name: {name_entry.get()}\n")
        textarea.insert(END, f"Customer Number: {contact_entry.get()}\n")
        textarea.insert(END, "\n==================================================")
        textarea.insert(END, "\nProduct\t\tQuantity\t\t\tPrice")
        textarea.insert(END, "\n==================================================")
        if soap_entry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{soap_entry.get()}\t\t{soap_price} Rs')
        if cream_entry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{cream_entry.get()}\t\t{cream_price} Rs')
        if face_entry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{face_entry.get()}\t\t{facewash_price} Rs' )
        if lotion_entry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{lotion_entry.get()}\t\t{lotion_price} Rs')
        if hair_entry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hair_entry.get()}\t\t{hairgel_price} Rs')
        if comb_entry.get() != '0':
            textarea.insert(END, f'\nHair Comb\t\t\t{comb_entry.get()}\t\t{comb_price} Rs')
        
        if rice_entry.get() != '0':
            textarea.insert(END, f'\nRice kg\t\t\t{rice_entry.get()}\t\t{rice_price} Rs')
        if wheat_entry.get() != '0':
            textarea.insert(END, f'\nWheat kg\t\t\t{wheat_entry.get()}\t\t{wheat_price} Rs')
        if sugar_entry.get() != '0':
            textarea.insert(END, f'\nSugar kg\t\t\t{sugar_entry.get()}\t\t{sugar_price} Rs')
        if salt_entry.get() != '0':
            textarea.insert(END, f'\nSalt kg\t\t\t{salt_entry.get()}\t\t{salt_price} Rs')
        if coffee_entry.get() != '0':
            textarea.insert(END, f'\nCoffee\t\t\t{coffee_entry.get()}\t\t{coffee_price} Rs')
        if peanuts_entry.get() != '0':
            textarea.insert(END, f'\nPeanuts\t\t\t{peanuts_entry.get()}\t\t{peanuts_price} Rs')
        
        if cocacola_entry.get() != '0':
            textarea.insert(END, f'\nCocacola mini\t\t\t{cocacola_entry.get()}\t\t{cocacola_price} Rs')
        if sprite_entry.get() != '0':
            textarea.insert(END, f'\nSprite Mini\t\t\t{sprite_entry.get()}\t\t{sprite_price} Rs')
        if pepsi_entry.get() != '0':
            textarea.insert(END, f'\nPepsi Mini\t\t\t{pepsi_entry.get()}\t\t{pepsi_price} Rs')
        if sevenup_entry.get() != '0':
            textarea.insert(END, f'\nSevenup Mini\t\t\t{sevenup_entry.get()}\t\t{sevenup_price} Rs')
        if mountaindew_entry.get() != '0':
            textarea.insert(END, f'\nMoutaindew Mini\t\t\t{mountaindew_entry.get()}\t\t{mountaindew_price} Rs')
        if mirinda_entry.get() != '0':
            textarea.insert(END, f'\nMirinda Mini\t\t\t{mirinda_entry.get()}\t\t{mirinda_price} Rs')    

        textarea.insert(END, '\n------------------------------------------------------')
        if gsttax_entry.get() != '0':
            textarea.insert(END, f'\nGST Amount\t {gsttax_entry.get()}')
        if vat_entry.get() != '0':
            textarea.insert(END, f'\nVAT Amount\t {vat_entry.get()}')
        if amt_entry.get() != '0':
            textarea.insert(END, f'\nTotal Amount\t {amt_entry.get()}')
        textarea.insert(END, '\n------------------------------------------------------')
        save_bill()

def total():
    global soap_price, cream_price, facewash_price, lotion_price, hairgel_price, comb_price
    global rice_price, wheat_price, sugar_price, salt_price, coffee_price, peanuts_price
    global cocacola_price, sprite_price, pepsi_price, sevenup_price, mountaindew_price, mirinda_price

    soap_price = 129 * int(soap_entry.get()) 
    cream_price = 55 * int(cream_entry.get())
    facewash_price = 78 * int(face_entry.get())
    lotion_price = 109 * int(lotion_entry.get())
    hairgel_price = 120 * int(hair_entry.get())
    comb_price = 74 * int(comb_entry.get())
    rice_price = 75 * int(rice_entry.get())
    wheat_price = 89 * int(wheat_entry.get())
    sugar_price = 55 * int(sugar_entry.get())
    salt_price = 65 * int(salt_entry.get())
    coffee_price = 95 * int(coffee_entry.get())
    peanuts_price = 187 * int(peanuts_entry.get())
    cocacola_price = 20 * int(cocacola_entry.get())
    sprite_price = 20 * int(sprite_entry.get())
    pepsi_price = 20 * int(pepsi_entry.get())
    sevenup_price = 20 * int(sevenup_entry.get())
    mountaindew_price = 20 * int(mountaindew_entry.get())
    mirinda_price = 20 * int(mirinda_entry.get())

    totalcos_price = soap_price + cream_price + facewash_price + lotion_price + hairgel_price + comb_price
    totalgro_price = rice_price + wheat_price + sugar_price + salt_price + coffee_price + peanuts_price
    totaldrink_price = cocacola_price + sprite_price + pepsi_price + sevenup_price + mountaindew_price + mirinda_price
    total_price = totalcos_price + totalgro_price + totaldrink_price
    
    gst_amount = round((total_price * 0.04) / 100, 2)
    vat_amount = round((total_price * 0.01), 2)
    total_price = round(total_price + gst_amount + vat_amount, 2)

    cos_entry.delete(0, END)
    cos_entry.insert(0, '₹ ' + str(totalcos_price))
    groc_entry.delete(0, END)
    groc_entry.insert(0, '₹ ' + str(totalgro_price))
    dri_entry.delete(0, END)
    dri_entry.insert(0, '₹ ' +  str(totaldrink_price))
    amt_entry.delete(0, END)
    amt_entry.insert(0, '₹ ' + str(total_price))
    gsttax_entry.delete(0, END)
    gsttax_entry.insert(0, '₹ ' + str(gst_amount))
    vat_entry.delete(0, END)
    vat_entry.insert(0, '₹ ' + str(vat_amount))
    bill_entry.delete(0, END)
    bill_entry.insert(0, str(billnumber))

def clear():
    soap_entry.delete(0, END)
    cream_entry.delete(0, END)
    face_entry.delete(0, END)
    lotion_entry.delete(0, END)
    hair_entry.delete(0, END)
    comb_entry.delete(0, END)

    rice_entry.delete(0, END)
    wheat_entry.delete(0, END)
    sugar_entry.delete(0, END)
    salt_entry.delete(0, END)
    coffee_entry.delete(0, END)
    peanuts_entry.delete(0, END)

    cocacola_entry.delete(0, END)
    sprite_entry.delete(0, END)
    pepsi_entry.delete(0, END)
    sevenup_entry.delete(0, END)
    mountaindew_entry.delete(0, END)
    mirinda_entry.delete(0, END)

    soap_entry.insert(0, 0)
    cream_entry.insert(0, 0)
    face_entry.insert(0, 0)
    lotion_entry.insert(0, 0)
    hair_entry.insert(0, 0)
    comb_entry.insert(0, 0)

    rice_entry.insert(0, 0)
    wheat_entry.insert(0, 0)
    sugar_entry.insert(0, 0)
    salt_entry.insert(0, 0)
    coffee_entry.insert(0, 0)
    peanuts_entry.insert(0, 0)

    cocacola_entry.insert(0, 0)
    sprite_entry.insert(0, 0)
    pepsi_entry.insert(0, 0)
    sevenup_entry.insert(0, 0)
    mountaindew_entry.insert(0, 0)
    mirinda_entry.insert(0, 0)

    cos_entry.delete(0, END)
    groc_entry.delete(0, END)
    dri_entry.delete(0, END)
    amt_entry.delete(0, END)
    gsttax_entry.delete(0, END)
    vat_entry.delete(0, END)
    
    name_entry.delete(0, END)
    contact_entry.delete(0, END)
    bill_entry.delete(0, END)
    textarea.delete(1.0, END)   

head_label = Label(window, text="Billing Counter", font=("Elephant", 30, 'bold'), bg="black", fg="sky blue", relief=GROOVE, bd=5)
head_label.pack(fill=X)

customer_detail = LabelFrame(window, text="Customer Details", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue", relief=RIDGE, bd=5)
customer_detail.pack(fill=X)

name_label = Label(customer_detail, text="Name", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue")
name_label.grid(row=0, column=0, padx=30)

vcmd1 = (window.register(lambda P: P.isalpha() or P == ""), '%P')
name_entry = Entry(customer_detail, validate="key", validatecommand=vcmd1, font=("cambria", 14), relief=GROOVE, bd=5, width=22)
name_entry.grid(row=0, column=1)

contact_label = Label(customer_detail, text="Contact No.", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue")
contact_label.grid(row=0, column=2, padx=30)

vcmd2 = (customer_detail.register(lambda P: P.isdigit() and len(P) <= 10 or P == ""), '%P')
contact_entry = Entry(customer_detail, validate="key", validatecommand=vcmd2, font=("cambria", 14), relief=GROOVE, bd=5, width=22)
contact_entry.grid(row=0, column=3)

billno_label = Label(customer_detail, text="Bill No.", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue")
billno_label.grid(row=0, column=4, padx=30)

vcmd3 = (customer_detail.register(lambda P: P.isdigit() or P == ""), '%P') 
bill_entry = Entry(customer_detail, validate="key", validatecommand=vcmd3, font=("cambria", 14), relief=GROOVE, bd=5, width=22)
bill_entry.grid(row=0, column=5)

search_btn = Button(customer_detail, text="Search", font=("times new roman", 18, "bold"), bg="white", fg="black",activeforeground="sky blue", activebackground="black", relief=RIDGE, command=search)
search_btn.grid(row=0, column=6, padx=120, pady=10, sticky=E)
    
products_frame = Frame(window, bg="black")
products_frame.pack(fill=X)

cosmetics_label_frame = LabelFrame(products_frame, text="Cosmetics", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue", relief=GROOVE, bd=5)
cosmetics_label_frame.grid(row=0, column=0, pady=10, padx=3)
command = (cosmetics_label_frame.register(lambda P: P.isdigit() or P == ""), '%P') 

soap_label = Label(cosmetics_label_frame, text="Soap", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
soap_label.grid(row=0, column=0, pady=13, sticky="w")
soap_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
soap_entry.grid(row=0, column=1, padx=10)
soap_entry.insert(0, 0)

cream_label = Label(cosmetics_label_frame, text="Face Cream", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
cream_label.grid(row=1, column=0, pady=13, sticky="w")
cream_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
cream_entry.grid(row=1, column=1, padx=10)
cream_entry.insert(0, 0)

facewash_label = Label(cosmetics_label_frame, text="Face Wash", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
facewash_label.grid(row=2, column=0, pady=13, sticky="w")
face_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
face_entry.grid(row=2, column=1, padx=10)
face_entry.insert(0, 0)

lotion_label = Label(cosmetics_label_frame, text="Body Lotion", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
lotion_label.grid(row=3, column=0, pady=13, sticky="w")
lotion_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
lotion_entry.grid(row=3, column=1, padx=10)
lotion_entry.insert(0, 0)

hair_gel_label = Label(cosmetics_label_frame, text="Hair Gel", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
hair_gel_label.grid(row=4, column=0, pady=13, sticky="w")
hair_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
hair_entry.grid(row=4, column=1, padx=10)
hair_entry.insert(0, 0)

comb_label = Label(cosmetics_label_frame, text="Comb", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
comb_label.grid(row=5, column=0, pady=13, sticky="w")  
comb_entry = Entry(cosmetics_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
comb_entry.grid(row=5, column=1, padx=10)   
comb_entry.insert(0, 0)

groceries_label_frame = LabelFrame(products_frame, text="Groceries", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue", relief=GROOVE, bd=5)
groceries_label_frame.grid(row=0, column=1, pady=10, padx=8)

rice_label = Label(groceries_label_frame, text="Rice", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
rice_label.grid(row=0, column=0, pady=13, sticky="w")
rice_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
rice_entry.grid(row=0, column=1, padx=10)
rice_entry.insert(0, 0)

wheat_label = Label(groceries_label_frame, text="Wheat", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
wheat_label.grid(row=1, column=0, pady=13, sticky="w")
wheat_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
wheat_entry.grid(row=1, column=1, padx=10)
wheat_entry.insert(0, 0)

sugar_label = Label(groceries_label_frame, text="Sugar", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
sugar_label.grid(row=2, column=0, pady=13, sticky="w")
sugar_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
sugar_entry.grid(row=2, column=1, padx=10)
sugar_entry.insert(0, 0)

salt_label = Label(groceries_label_frame, text="Tata Rock Salt", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
salt_label.grid(row=3, column=0, pady=13, sticky="w")
salt_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
salt_entry.grid(row=3, column=1, padx=10)
salt_entry.insert(0, 0)

coffee_label = Label(groceries_label_frame, text="Coffee", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
coffee_label.grid(row=4, column=0, pady=13, sticky="w")
coffee_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
coffee_entry.grid(row=4, column=1, padx=10)
coffee_entry.insert(0, 0)

peanuts_label = Label(groceries_label_frame, text="Peanuts", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
peanuts_label.grid(row=5, column=0, pady=13, sticky="w")
peanuts_entry = Entry(groceries_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
peanuts_entry.grid(row=5, column=1, padx=10)
peanuts_entry.insert(0, 0)

drinks_label_frame = LabelFrame(products_frame, text="Cold Drinks", font=("times new roman", 18, 'bold'), bg="black", fg="sky blue", relief=GROOVE, bd=5)
drinks_label_frame.grid(row=0, column=2, pady=10, padx=3)

cocacola_label = Label(drinks_label_frame, text="Cocacola", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
cocacola_label.grid(row=0, column=2, pady=13, sticky="w")
cocacola_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
cocacola_entry.grid(row=0, column=3, padx=10)
cocacola_entry.insert(0, 0)

sprite_label = Label(drinks_label_frame, text="Sprite", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
sprite_label.grid(row=1, column=2, pady=13, sticky="w")
sprite_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
sprite_entry.grid(row=1, column=3, padx=10)
sprite_entry.insert(0, 0)

pepsi_label = Label(drinks_label_frame, text="Pepsi", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
pepsi_label.grid(row=2, column=2, pady=13, sticky="w")
pepsi_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
pepsi_entry.grid(row=2, column=3, padx=10)
pepsi_entry.insert(0, 0)

sevenup_label = Label(drinks_label_frame, text="Seven Up", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
sevenup_label.grid(row=3, column=2, pady=13, sticky="w")
sevenup_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
sevenup_entry.grid(row=3, column=3, padx=10)
sevenup_entry.insert(0, 0)

mountaindew_label = Label(drinks_label_frame, text="Mountain Dew", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
mountaindew_label.grid(row=4, column=2, pady=13, sticky="w")
mountaindew_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
mountaindew_entry.grid(row=4, column=3, padx=10)
mountaindew_entry.insert(0, 0)

mirinda_label = Label(drinks_label_frame, text="Mirinda", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
mirinda_label.grid(row=5, column=2, pady=13, sticky="w")
mirinda_entry = Entry(drinks_label_frame, validate="key", validatecommand=command, font=('Arial', 15), width=9, relief=GROOVE, bd=5)
mirinda_entry.grid(row=5, column=3, padx=10)
mirinda_entry.insert(0, 0)

billframe = Frame(products_frame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=4, padx=10)

bill_area_label = Label(billframe, text="Bill Area", font=("times new roman", 16, 'bold'), bd=7, relief=GROOVE)
bill_area_label.pack(fill=X)

scroll = Scrollbar(billframe, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=20, width=55, yscrollcommand=scroll.set)
textarea.pack(side="right")
scroll.config(command=textarea.yview)

billframe = LabelFrame(window, text="Bill Menu", font=("times new roman", 15, 'bold'), bg="black", fg="sky blue", relief=GROOVE, bd=5)
billframe.pack(fill=X)

total_cosmetics_label = Label(billframe, text="Total Cosmetic Price", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_cosmetics_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
cos_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
cos_entry.grid(row=0, column=1, padx=20)

total_groceries_label = Label(billframe, text="Total Groceries Price", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_groceries_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
groc_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
groc_entry.grid(row=1, column=1, padx=20)

total_drinks_label = Label(billframe, text="Total Drinks Price", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_drinks_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
dri_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
dri_entry.grid(row=2, column=1, padx=20)

total_gst= Label(billframe, text="Total GST Amt", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_gst.grid(row=0, column=2, pady=5, padx=5, sticky="w")
gsttax_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
gsttax_entry.grid(row=0, column=3, padx=10)

total_vat = Label(billframe, text="Total VAT Amt", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_vat.grid(row=1, column=2, pady=5, padx=5, sticky="w")
vat_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
vat_entry.grid(row=1, column=3, padx=10)

total_amt = Label(billframe, text="Total Amount", font=("times new roman", 20, 'bold'), bg="black", fg="sky blue")
total_amt.grid(row=2, column=2, pady=5, padx=5, sticky="w")
amt_entry = Entry(billframe, font=("Arial", 15), width=10, relief=GROOVE, bd=5)
amt_entry.grid(row=2, column=3, padx=10)

buttons_frame = Frame(billframe, relief=GROOVE, bd=8)
buttons_frame.grid(row=0, column=4, rowspan=3)

total_button = Button(buttons_frame, text="Total", font=("Angency FB", 14, 'bold'), bg="gray20", fg="white", relief=GROOVE, bd=5, width=7, padx=10, command=total)
total_button.grid(row=0, column=5, pady=20, padx=5)

generate_button = Button(buttons_frame, text="Bill", font=("Angency FB", 14, 'bold'), bg="gray20", fg="white", relief=GROOVE, bd=5, width=8, padx=10, command=bill)
generate_button.grid(row=0, column=6, pady=20, padx=5)

email_button = Button(buttons_frame, text="Email", font=("Angency FB", 14, 'bold'), bg="gray20", fg="white", relief=GROOVE, bd=5, width=8, padx=10, command=email)
email_button.grid(row=0, column=7, pady=20, padx=5)

print_button = Button(buttons_frame, text="Print", font=("Angency FB", 14, 'bold'), bg="gray20", fg="white", relief=GROOVE, bd=5, width=8, padx=10, command=print)
print_button.grid(row=0, column=8, pady=20, padx=5)

clear_button = Button(buttons_frame, text="Clear", font=("Angency FB", 14,'bold'), bg="gray20", fg="white", relief=GROOVE, bd=5, width=7, padx=10, command=clear)
clear_button.grid(row=0, column=9, pady=20, padx=5)


if __name__ == "__main__":
    window.mainloop()
