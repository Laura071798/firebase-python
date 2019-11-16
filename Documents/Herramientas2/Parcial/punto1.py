import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time


placa = Arduino ('COM4')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
time.sleep(0.5)
ventana = Tk()
ventana.geometry('800x400')
ventana.title("UI para sistemas de control")

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial3-65f7c.firebaseio.com/'
})

marco1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)
b=Label(marco1,text="")




valor= Label(marco1, bg='sky blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data=StringVar()
valor2 = Label(marco1, bg='sky blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data2=StringVar()
valor3= Label(marco1, bg='sky blue', font=("Arial Bold", 15), fg="white", width=5)
adc_data3=StringVar()


def adc_read():
        x=a_0.read()
        print(x)
        adc_data.set(x)
        y=a_1.read()
        print(y)
        adc_data2.set(y)
        z=a_2.read()
        print(z)
        adc_data3.set(z)
        time.sleep(0.7)
        ref = db.reference('Potenciometro')
        ref.update({
            'Potenciometro/Potenciometro1': a_0.read(),
            'Potenciometro/Potenciometro2': a_1.read(),
            'Potenciometro/Potenciometro3': a_2.read()
    })
     



valor.configure(textvariable=adc_data)
valor.place(x=130, y=90)
valor2.configure(textvariable=adc_data2)
valor2.place(x=200, y=90)
valor3.configure(textvariable=adc_data3)
valor3.place(x=270, y=90)

prom_15=Button(marco1,text="send",command=adc_read)
prom_15.place(x=60, y=90)


ventana.mainloop()