class Vehiculos:

    def __init__(self, marca, modelo):
        
        self.marca = marca

        self.modelo = modelo

        self.enMarcha = False

        self.acelera = False

        self.frena = False

    def arrancar(self):

        self.enMarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frenar = True            

    def estado(self):

        print("Marca: ",  self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",  self.enMarcha, "\nAcelerar: ", self.acelera, "\nFrenar: ", self.frena)    

class Moto(Vehiculos):

    hCaballito = "No hay caballito"

    def caballito(self):

        self.hCaballito = "Voy haciendo el caballito"

    def estado(self):
        
        #self.estado() 

        print("Marca: ",  self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",  self.enMarcha, "\nAcelerar: ", self.acelera, "\nFrenar: ", self.frena, "\nCaballito: ", self.hCaballito )


class Furgoneta(Vehiculos):

    def carga(self, carga):

        self.cargado = carga

        if(self.cargado):

            return "La furgoneta esta cargada"
        
        else:

            return "La furgoneta no esta cargada"


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        
        self.autonimia = 100



    def cargarEnergia(self):

        self.cargando = True    

