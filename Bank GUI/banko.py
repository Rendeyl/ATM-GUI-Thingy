from tkinter import *
from PIL import ImageTk, Image
import time

balance = 100
def clear_screen():
    view_balance_text.place(x=1000,y=1000)
    withdraw_text.place(x=1000,y=1000)
    deposit_text.place(x=1000,y=1000)
    second_title.place(x=1000,y=1000)
    frame.place(x=1000,y=1000)
    quote.place(x=8500, y=1000)

def new_screen():
    screen = Canvas(window, width=1000, height=1300, bg="#4287f5")
    screen.pack(padx=100, pady=10)

def restart_screen():
    second_title.place(x=450, y=60)
    view_balance_text.place(x=110, y=120)
    withdraw_text.place(x=110, y=270)
    deposit_text.place(x=110, y=420)
    frame.place(x=560, y=90)
    quote.place(x=850, y=100)

def disable_buttons():
    view_balance_d.place(x=10, y=130)
    withdraw_d.place(x=10, y=280)
    deposit_d.place(x=10, y=440)

def enable_buttons():
    view_balance_d.place(x=1000, y=1300)
    withdraw_d.place(x=1000, y=2800)
    deposit_d.place(x=1000, y=4400)
    view_balance.place(x=10, y=130)
    withdraw.place(x=10, y=280)
    deposit.place(x=10, y=440)
def keyboard():
    clear_screen()
    a1.place(x=500, y=360)
    a2.place(x=550, y=360)
    a3.place(x=600, y=360)
    a4.place(x=650, y=360)
    a5.place(x=500, y=405)
    a6.place(x=550, y=405)
    a7.place(x=600, y=405)
    a8.place(x=650, y=405)
    a9.place(x=500, y=450)
    a0.place(x=550, y=450)
    aClear.place(x=600, y=450)
    aBackspace.place(x=650, y=450)

def clear_keyboard():
    p = 1000
    a1.place(x=p, y=p)
    a2.place(x=p, y=p)
    a3.place(x=p, y=p)
    a4.place(x=p, y=p)
    a5.place(x=p, y=p)
    a6.place(x=p, y=p)
    a7.place(x=p, y=p)
    a8.place(x=p, y=p)
    a9.place(x=p, y=p)
    a0.place(x=p, y=p)
    aClear.place(x=p, y=p)
    aBackspace.place(x=p, y=p)

def exit_command():
    restart_screen()
    clear_keyboard()
    withdrawal_screen.place(x=1000,y=1000)
    withdraw_submit.place(x=1000,y=1000)
    withdraw_exit.place(x=1000,y=1000)
    view_balance.place(x=10, y=130)
    enable_buttons()
    exit_text.place(x=1000,y=1000)
    withdraw_title.place(x=1000,y=1000)
    keypad_note.place(x=1000,y=1000)
    transaction.place(x=1000,y=1000)
    withdrawal_screen.delete(0, END)
    deposit_title.place(x=1000,y=1000)
    deposit_screen.place(x=1000,y=1000)
    deposit_submit.place(x=1000, y=1000)

def view_balance_command():
    disable_buttons()
    def exit_command():
        enable_buttons()
        restart_screen()
        showing_balance.destroy()
        view_balance_active.destroy()
        exit_view_balance.destroy()
        exit_text.place(x=1000,y=1000)
    clear_screen()
    view_balance_active = Label(window, text="Current Balance is: ", font=('Courier New', 30), bg="#4287f5", fg="black")
    showing_balance = Label(window, text="$" + str(balance), font=('Courier New', 30), bg="#4287f5", fg="green")
    view_balance_active.place(x=380, y=250)
    showing_balance.place(x=550, y=300)
    exit_view_balance = Button(window, text="1", bg="#cad2de", width=8, height=5, command=exit_command)
    exit_text = Label(window, text="---Exit---", font=("Courier New", 20), width=12, height=3, bg="#4287f5", pady=5,)
    exit_text.place(x=102, y=120)
    exit_view_balance.place(x=10, y=130)

def withdraw_command():
    disable_buttons()
    clear_screen()
    keyboard()
    withdraw_title.place(x=305, y=250)
    exit_text.place(x=102, y=120)
    withdraw_submit.place(x=545, y=300) #submit button
    withdrawal_screen.place(x=360, y= 200) #entry
    withdraw_exit.place(x=10, y=130) #place the exit button
    keypad_note.place(x=450, y=500)
def withdraw_active():
    def exit_command():
        restart_screen()
        clear_keyboard()
        withdrawal_screen.place(x=1000,y=1000)
        withdraw_submit.place(x=1000,y=1000)
        withdraw_exit.place(x=1000,y=1000)
        view_balance.place(x=10, y=130)
        enable_buttons()
        exit_text.place(x=1000,y=1000)
        withdraw_title.place(x=1000,y=1000)
        keypad_note.place(x=1000,y=1000)
        transaction.place(x=4000, y=2500)
        transaction_error.place(x=4300, y=2500)
        withdrawal_screen.delete(0, END)
    global balance
    user_withdraw = withdrawal_screen.get()
    if int(user_withdraw) > balance:
        withdraw_title.place(x=1000, y=1000)
        transaction_error.place(x=410, y=250)
        window.after(3000, exit_command)
    else:
        balance = balance - int(user_withdraw)
        transaction.place(x=430, y=250)
        withdraw_title.place(x=1000, y=1000)
        window.after(3000, exit_command)

def deposit_command():
    disable_buttons()
    clear_screen()
    keyboard()
    deposit_title.place(x=305, y=250)
    exit_text.place(x=102, y=120)
    deposit_submit.place(x=545, y=300)  # submit button
    deposit_screen.place(x=360, y=200)  # entry
    withdraw_exit.place(x=10, y=130)  # place the exit button
    keypad_note.place(x=450, y=500)

def deposit_active():
    def exit_command():
        restart_screen()
        clear_keyboard()
        deposit_screen.place(x=1000,y=1000)
        deposit_submit.place(x=1000,y=1000)
        withdraw_exit.place(x=1000,y=1000)
        view_balance.place(x=10, y=130)
        enable_buttons()
        exit_text.place(x=1000,y=1000)
        deposit_title.place(x=1000,y=1000)
        keypad_note.place(x=1000,y=1000)
        deposit_transaction.place(x=4000, y=2500)
        transaction_error.place(x=4300, y=2500)
        deposit_screen.delete(0, END)
    global balance
    user_deposit = deposit_screen.get()
    balance = balance + int(user_deposit)
    deposit_transaction.place(x=430, y=250)
    deposit_title.place(x=1000, y=1000)
    window.after(3000, exit_command)

window = Tk()
window.geometry("1200x600")
window.title("BANKO BA TO??")
window.configure(background='gray')
banker = ImageTk.PhotoImage(Image.open("rdbank.png.jpg"))
#-------------------SCREEN-------------------------------
screen = Canvas(window, width=1000, height=1300, bg="#4287f5")
screen.pack(padx=100, pady=10)

frame = Frame(window, width=5, height=5, pady=1, padx=1, bg="#4287f5")
banker_rd = Label(frame, image=banker,width=500, height=1300, pady=500)
#banker_rd_image = Label(window, text="a",image=banker, width=60, height=32, pady=1, padx=1)
#banker_rd_image.place(x=560,y=90)
frame.place(x=560,y=90)
banker_rd.pack()
quote = Label(window, text="(Banker rd)", font=('Courier New',18),fg="black", width=10, height=1, bg="#4287f5", padx=18)
quote.place(x=850, y=100)
title = Label(window, text="ATM MACHINE?? NI RD", font=('Courier New',30), fg="green", width=40, height=1, bg="#c7c3c3", padx=18)
title.place(x=100, y=1)
title = Label(window, text="ATM MACHINE?? NI RD", font=('Courier New',30), fg="#c7c3c3", width=40, height=1, bg="#c7c3c3", padx=18)
title.place(x=100, y=560)
second_title = Label(window, text="What would you like to do?", font=('Courier New',15), bg="#4287f5", fg="black")
second_title.place(x=450, y= 60)
#-------------------VIEW BALANCE-------------------------------
view_balance = Button(window, text="1", bg="#cad2de", width=8, height=5, command=view_balance_command)
view_balance_text = Label(window, text="---View Balance---", font=("Courier New",20), width=18, height=3, bg="#4287f5", pady=5)
view_balance.place(x=10, y=130)
view_balance_text.place(x=110, y=120)
#-------------------WITHDRAW-------------------------------
withdraw = Button(window, text="2", bg="#cad2de", width=8, height=5, command=withdraw_command)
withdraw_text = Label(window, text="----Withdraw----", font=("Courier New",20), width=18, height=3, bg="#4287f5", pady=5)
withdraw.place(x=10, y=280)
withdraw_text.place(x=110, y=270)
withdrawal_screen = Entry(window, font=("Courier New", 30))
withdraw_submit = Button(window, text="Submit", bg="#7af211", fg="#ddedce", width=15, height=3, activebackground="#c3ff00", command=withdraw_active)
#-------------------DEPOSIT-------------------------------
deposit = Button(window, text="3", bg="#cad2de", width=8, height=5, command=deposit_command)
deposit_text = Label(window, text="----Deposit----", font=("Courier New",20), width=18, height=3, bg="#4287f5", pady=5)
deposit.place(x=10, y=440)
deposit_text.place(x=110,y=420)
#-------------------KEYPAD-------------------------------
a1 = Button(text="1", font=('Courier New', 10), width=5, height=2)
a2 = Button(text="2", font=('Courier New', 10), width=5, height=2)
a3 = Button(text="3", font=('Courier New', 10), width=5, height=2)
a4 = Button(text="4", font=('Courier New', 10), width=5, height=2)
a5 = Button(text="5", font=('Courier New', 10), width=5, height=2)
a6 = Button(text="6", font=('Courier New', 10), width=5, height=2)
a7 = Button(text="7", font=('Courier New', 10), width=5, height=2)
a8 = Button(text="8", font=('Courier New', 10), width=5, height=2)
a9 = Button(text="9", font=('Courier New', 10), width=5, height=2)
a0 = Button(text="0", font=('Courier New', 10), width=5, height=2)
aClear = Button(text="C", font=('Courier New', 10), width=5, height=2, bg="#edcf26")
aBackspace = Button(text="<", font=('Courier New', 10), width=5, height=2, bg="red")

view_balance_d = Button(window, text="1", bg="#cad2de", width=8, height=5, state=DISABLED)
withdraw_d = Button(window, text="2", bg="#cad2de", width=8, height=5, state=DISABLED)
deposit_d = Button(window, text="3", bg="#cad2de", width=8, height=5, state=DISABLED)

keypad_note = Label(window, text="(Di to gumagana, hirap icode eh HAHAHAHAHHA)", font=('Courier New', 15), bg="#4287f5", fg="black")
withdraw_title = Label(window, text="How Much Would You Like To Withdraw?", font=('Courier New', 20), bg="#6198f2", fg="black")
exit_text = Label(window, text="---Exit---", font=("Courier New", 20), width=12, height=3, bg="#4287f5", pady=5, )
withdraw_exit = Button(window, text="1", bg="#cad2de", width=8, height=5, command=exit_command) #exit button
transaction = Label(window, text="Withdrawn Succesfully!", font=('Courier New', 20),bg="#51f542", fg="black", relief=RAISED)
transaction_error = Label(window, text="ERROR! Insufficient Funds", font=('Courier New', 20),bg="#fa3737", fg="black", relief=RAISED)

deposit_title = Label(window, text="How Much Would You Like To Deposit?", font=('Courier New', 20), bg="#6198f2", fg="black")
deposit_screen = Entry(window, font=("Courier New", 30))
deposit_submit = Button(window, text="Submit", bg="#7af211", fg="#ddedce", width=15, height=3, activebackground="#c3ff00", command=deposit_active)
deposit_transaction = Label(window, text="Deposited Succesfully!", font=('Courier New', 20),bg="#51f542", fg="black", relief=RAISED)

window.mainloop()