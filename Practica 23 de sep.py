#Gabriel Eduardo Henriquez Gonzalez
#Salvador Mauricio Chavarria Carranza
from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import Combobox
window = Tk()
window.title("Cajero de Supermercado")
window.geometry('400x200')
window.configure(bg='blue')
window.resizable(0,0)
lbl1 = Label(window,text="Precio: ",bg = "blue",fg = "white")
lbl1.grid(column=1, row=0)
input1 = Entry(window,width=15)
input1.grid(column=2,row=0) 
lbl2 = Label(window,text="Cantidad:",bg = "blue",fg = "white") 
lbl2.grid(column=1, row=1) 
input2 = Entry(window,width=15)
input2.grid(column=2,row=1) 
lbl3 = Label(window,text="Pago:",bg = "blue",fg = "white") 
lbl3.grid(column=1, row=2) 
pago = Combobox(window,state="readonly")
pago['values']=("Efectivo","Tarjeta Credito","Tarjeta Debito")
pago.grid(column=2,row=2)
def lacompra():
  if(input1.get() != "" and input2.get() != "" and pago.get() != ""):
    precio = float(input1.get())
    cant = int(input2.get())
    formapago = pago.get()
    if(formapago == "Tarjeta Credito"):
      total = precio * cant
      descuento = total * 0.20
      preciototal = total - descuento
      messagebox.showinfo("Cajero",f"El precio es de {precio} y la cantidad de {cant} Con un total de {total} se pago con {formapago} Descuento: {round(descuento,2)} Total con descuento: {round(preciototal,2)}")
    elif(formapago == "Tarjeta Debito"):
      total = precio * cant
      descuento = total * 0.20
      preciototal = total - descuento
      messagebox.showinfo("Cajero",f"El precio es de {precio} y la cantidad de {cant} Con un total de {total} se pago con {formapago} Descuento: {round(descuento,2)} Total con descuento: {round(preciototal,2)}")
    elif(formapago == "Efectivo"):
      total = precio * cant
      if(total >= 20):
        descuento = total * 0.10
        preciototal = total - descuento
        messagebox.showinfo("Cajero",f"El precio es de {precio} y la cantidad de {cant} Con un total de {total} se pago con {formapago} Descuento: {round(descuento,2)} Total con descuento: {round(preciototal,2)}")
      else:
        descuento = 0
        preciototal = total - descuento
        messagebox.showinfo("Cajero",f"El precio es de {precio} y la cantidad de {cant} Con un total de {total} se pago con {formapago} Descuento: {round(descuento,2)} Total con descuento: {round(preciototal,2)}")
  else:
    messagebox.showerror("Cajero","Rellene y seleccione las opciones necesarias.")
buton = Button(window,text = "Comprar",command=lacompra,bg = "green",fg = "white")
buton.grid(column = 2,row = 3)
def cerrar():
  window.destroy()
butonsalir = Button(window,text = "Salir",command= cerrar,bg = "red",fg = "white")
butonsalir.grid(column = 3,row = 3)
window.mainloop()