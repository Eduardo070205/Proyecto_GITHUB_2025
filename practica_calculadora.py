from tkinter import *

raiz = Tk()

raiz.title("Calculadora")

raiz.iconbitmap('cal.ico')

raiz.config(relief="groove")

raiz.config(bg="grey")

raiz.config(bd=50)

miFrame = Frame()

miFrame.config(bg="#fb8663")

miFrame.pack()

operacion = ""

reset_pantalla=False

resultado = 0

#------------------------Patalla

numeroPantalla = StringVar()

miPantalla = Entry(miFrame, textvariable=numeroPantalla)

miPantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

miPantalla.config(background="red", fg="#13fe00", justify="right")


# ------------------Pulsaciones de teclado--------------------------

def borrar():

    numeroPantalla.set("0")

def numeroEnPantalla(num):

    global operacion

    global reset_pantalla

    if reset_pantalla!=False:

        numeroPantalla.set(num) 
		
        reset_pantalla = False

    else:

        numeroPantalla.set(numeroPantalla.get() + num)	




# -----------------funcion suma--------

def suma(num):

    global operacion

    global resultado
	
    global reset_pantalla

    resultado+=int(num)

    operacion = "suma"
	
    reset_pantalla=True

    numeroPantalla.set(resultado)

#-------------------Funcion resta--------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True

#-------------- Funcion el_resultado ----------
def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0

#----------- Fila 1

boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroEnPantalla("7"))

boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroEnPantalla("8"))

boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroEnPantalla("9"))

boton9.grid(row=2, column=3)

botonDiv = Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))

botonDiv.grid(row=2, column=4)



#----------- Fila 2



boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroEnPantalla("4"))

boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroEnPantalla("5"))

boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroEnPantalla("6"))

boton6.grid(row=3, column=3)

botonMult = Button(miFrame, text="X", width=3, command=lambda:multiplica(numeroPantalla.get()))

botonMult.grid(row=3, column=4)


#----------- Fila 3



boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroEnPantalla("1"))

boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroEnPantalla("2"))

boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroEnPantalla("3"))

boton3.grid(row=4, column=3)

botonRestar = Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))

botonRestar.grid(row=4, column=4)


#----------- Fila 4


boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroEnPantalla("0"))

boton0.grid(row=5, column=1)

botonPunto = Button(miFrame, text=".", width=3, command=lambda:numeroEnPantalla("."))

botonPunto.grid(row=5, column=2)

botonIgual = Button(miFrame, text="=", width=3, command=lambda:el_resultado())

botonIgual.grid(row=5, column=3)

botonSuma = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))

botonSuma.grid(row=5, column=4)

#-----------------Fila 5

botonBorrar = Button(miFrame, text="C", width=3, command=borrar)

botonBorrar.grid(row=6, column=4)



raiz.mainloop()