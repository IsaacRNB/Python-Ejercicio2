import datetime

listaPersonas = []

class Persona(object):
    def __init__(self, _id, _nombre, _correo, _balon, _valla, _porteria):
        self.id = _id
        self.nombre = _nombre
        self.correo = _correo
        self.balon = _balon
        self.valla = _valla
        self.porteria = _porteria

    def entregarDatos(self):
        today = datetime.date.today()
        print("{ Id: ", self.id, ",", "Nombre: " , self.nombre, ",", "Correo: ", self.correo, "," ,  "Balones: ", self.balon, ",", "Vallas:", self.valla, ",", "Porterias:", self.porteria, ",", "FechaPrestamo", today, "}")

    def editarPrestamo(self, _balon, _valla, _porteria):
        self.balon = _balon
        self.valla = _valla
        self.porteria = _porteria
        print("")
        print("Modificacion exitosa!")


    def registrarPrestamo(id, nombre, correo, balon, porteria, valla):
        objPersona = Persona(id, nombre, correo, balon, porteria, valla)
        listaPersonas.append(objPersona)


    def listadoPrestamos():
        for objPersona in listaPersonas:
            objPersona.entregarDatos()

    def modificarPrestamo(id):
        for objPersona in listaPersonas:
            if id == objPersona.id:
                balon = int(input("Balones: " ))
                porteria = int(input("Porterias: " ))
                valla = int(input("Vallas: " )) 
                objPersona.editarPrestamo(balon, valla, porteria)
                objPersona.entregarDatos()

    def eliminarPrestamo(id):
        for objPersona in listaPersonas:
            if id == objPersona.id:
                listaPersonas.remove(objPersona)           
                
    def salir():
        print("Programa finalizado...!")
        exit()

