import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
         2 - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = ["auto", "camioneta", "moto", "auto"]
        self.lista_marca_vehiculo = [100, 200, 300, 400]

    def btn_agregar_on_click(self):
        while True:
            tipo = prompt("Tipo", "Ingrese el tipo de su vehículo (auto, camioneta o moto)")
            while not tipo or (tipo != "auto" and tipo != "camioneta" and tipo != "moto"):
                tipo = prompt("Tipo", "Por favor, ingrese el tipo de su vehículo (auto, camioneta o moto)")
            self.lista_tipo_vehiculo.append(tipo)

            kilometros = prompt("kilometros", "Ingrese la cantidad de kilometros")
            while not kilometros or not kilometros.isdigit() or int(kilometros) <= 0:
                kilometros = prompt("kilometros", "Por favor, ingrese la cantidad de kilometros")
            kilometros = int(kilometros)
            self.lista_marca_vehiculo.append(kilometros)

            continuar = question("Continuar", "¿Desea agregar más vehiculos?")
            if continuar == True:
                continue
            else:
                break

    
    def btn_mostrar_on_click(self):
        for i, tipo in enumerate(self.lista_tipo_vehiculo):
            print(f"{i} - {self.lista_tipo_vehiculo[i]} - {self.lista_marca_vehiculo[i]} km")


    def btn_informar_on_click(self):
       #3- Precio promedio de todos los servicios.

        lista_servicios = []
        acumulador_servicios = 0



        for tipo in self.lista_tipo_vehiculo:
            if tipo == "auto":
                lista_servicios.append(15000)
                acumulador_servicios += 15000
            elif tipo == "camioneta":
                lista_servicios.append(25000)
                acumulador_servicios += 25000
            elif tipo == "moto":
                lista_servicios.append(10000)
                acumulador_servicios += 10000
            else:
                alert("Error", "La lista está vacía")
        
        promedio = acumulador_servicios / len(lista_servicios)

        alert("Promedio", f"El promedio de todos los servicios es: {promedio}")

        # 6- Informar la cantidad de vehiculos de cada tipo.
        cont_autos = 0
        cont_camionetas = 0
        cont_motos = 0

        for tipo in self.lista_tipo_vehiculo:
            if tipo == "auto":
                cont_autos += 1
            elif tipo == "camioneta":
                cont_camionetas += 1
            elif tipo == "moto":
                cont_motos += 1
            else:
                alert("Error", "La lista está vacía:")
        
        alert("Cantidades", f"La cantidad de autos es {cont_autos};\nLa cantidad de camionetas es {cont_camionetas};\nLa cantidad de motos es {cont_motos}")





       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()
