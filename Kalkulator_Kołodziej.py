# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *

window=Tk()
window.geometry("325x400")
window.title("Kalkulator")
#window.resizable(0,0)

#responsywnosc
n_rows=6
n_columns=4
for i in range(n_rows):
    window.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    window.grid_columnconfigure(i,  weight =1)
    
    
def btn_press(i): #klikanie klawiszy
    global expression 
    expression = expression+str(i)
    tekst2.set(expression)
    if expression.startswith("*"):
            tekst.set("Wprowadź liczbę, nie znak!")
            expression=""
    elif expression.startswith("+"):
            tekst.set("Wprowadź liczbę, nie znak!")
            expression=""
    elif expression.startswith("-"):
             tekst.set("Wprowadź liczbę, nie znak!")
             expression=""
    elif expression.startswith("^"):
             tekst.set("Wprowadź liczbę nie znak!")
             expression=""
    elif expression.startswith("/"):
             tekst.set("Wprowadź liczbę, nie znak!")
             expression=""
    
def btn_equal(): #rowna sie
    global expression
    try:
        result = str(eval(expression)) #evaluate
        tekst.set(result) #w oknie wpisz rezultat
        expression=""
                
    except:
        tekst.set("Błąd. Spróbuj ponownie.")
        expression=""
    
def clear_button(): 
    global expression 
    expression = "" 
    tekst2.set("")
    tekst.set("")
    
def back_btn():
    global expression
    delete_char=expression[:-1]
    tekst2.set(delete_char)
    expression=""

expression=""
#rodzaj wpisywanego tekstu
tekst = StringVar()
tekst2=StringVar()
#definiuje ramke dla okna
frame_text=Frame(window, width=315, height=75, bd=0)
frame_text2=Frame(window, width=315, height=75, bd=0)
#umozliwiam wyswieltenie, zastosowanie widzetow
frame_text.pack()  
frame_text2.pack()
 

#tworze okno wpisywania
fill_field=Entry(frame_text, state= DISABLED, font=('helvetica', 18, 'bold'), textvariable=tekst, width=50, bg="white", bd=1, justify=RIGHT)
fill_field.grid(row=1, column=0) 
fill_field.pack(ipady=12) #wysokosc inputu


#drugie okno
fill_field2=Entry(frame_text2, font=('helvetica', 18, 'bold'), textvariable=tekst2, width=50, bg="white", bd=1, justify=RIGHT)
fill_field2.grid(row=0, column=0)
fill_field2.pack(ipady=12) #wysokosc inputu

    
frame_btn = Frame(window, width=315, height = 290, bg='pink')
frame_btn.pack() #zastowowanie widzetow

#definiowanie rows and columns
#AC <- ^ / 
# 1 2 3 *
# 4 5 6 +
# 7 8 9 - 
#. 0 [ = ]

#pierwszy wiersz
AC = Button(frame_btn, text="AC", fg="pink",width=5, height=3, bd=0, command = lambda: clear_button()).grid(row = 1, column = 0, padx = 1, pady = 1)
Back= Button(frame_btn, text="<-", fg="pink", width=5, height=3, bd=0, command = lambda: back_btn()).grid(row = 1, column = 1, padx = 1, pady = 1)
Up = Button(frame_btn, text="^",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press("**")).grid(row = 1, column = 2, padx = 1, pady = 1)
Divide= Button(frame_btn, text="/", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press("/")).grid(row = 1, column = 3, padx = 1, pady = 1)


#drugi wiersz
Btn1= Button(frame_btn, text="1", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(1)).grid(row = 2, column = 0, padx = 1, pady = 1)
Btn2 = Button(frame_btn, text="2",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(2)).grid(row = 2, column = 1, padx = 1, pady = 1)
Btn3= Button(frame_btn, text="3", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(3)).grid(row = 2, column = 2, padx = 1, pady = 1)
Multiply = Button(frame_btn, text="*",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press("*")).grid(row = 2, column = 3, padx = 1, pady = 1)

#trzeci wiersz
Btn4= Button(frame_btn, text="4", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
Btn5 = Button(frame_btn, text="5",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
Btn6= Button(frame_btn, text="6", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(6)).grid(row = 3, column = 2, padx = 1, pady = 1)
Add = Button(frame_btn, text="+",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

#drugi wiersz
Btn7= Button(frame_btn, text="7", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(7)).grid(row = 4, column = 0, padx = 1, pady = 1)
Btn8 = Button(frame_btn, text="8",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(8)).grid(row = 4, column = 1, padx = 1, pady = 1)
Btn9= Button(frame_btn, text="9", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(9)).grid(row = 4, column = 2, padx = 1, pady = 1)
Substract = Button(frame_btn, text="-",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

#czwarty wiersz
BtnDot= Button(frame_btn, text=".", fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(".")).grid(row = 5, column = 0, padx = 1, pady = 1)
Btn0 = Button(frame_btn, text="0",fg="pink", width=5, height=3, bd=0, command = lambda: btn_press(0)).grid(row = 5, column = 1, padx = 1, pady = 1)
Btn_Equal= Button(frame_btn, text="=", fg="pink", width=15, height=3, bd=0, command = lambda: btn_equal()).grid(row = 5, column = 2, columnspan = 2, padx = 1, pady = 1)

window.mainloop()