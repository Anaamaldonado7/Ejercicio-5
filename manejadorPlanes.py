from clasePlan import PlanAhorro #para acceder a los metodos de esta clase
import csv

class manejadorPlan:
    __listaPlan = []  #defino un atributo de tipo lista
    
    def __init__(self): 
      self.iniciar()   #llamo al metodo que crea la lista
    
    def iniciar (self): #creo la lista
      archivo=open('planes.csv')
      reader=csv.reader(archivo,delimiter=';')
      for fila in reader:
        unPlan = PlanAhorro (fila[0],fila[1],fila[2],fila[3])
        self.__listaPlan.append(unPlan)  #la funcion append agrega un valor a la lista
        
    def actualizarValor (self):
        for i in range(len(self.__listaPlan)): #la funcion len cuenta la cantidad de componentes en la lista
          print("\n Codigo: {} ".format(self.__listaPlan[i].getCod()))
          print("\n Modelo: {} ".format(self.__listaPlan[i].getModel()))
          print("\n Version: {} ".format(self.__listaPlan[i].getVersion()))
          nuevo = input ("Ingrese el valor nuevo del vehiculo: ")
          self.__listaPlan[i].nuevoValor(nuevo)
          
    def mostrarDatos (self, valor):
        for i in range (len(self.__listaPlan)):
            if float(valor) > self.__listaPlan[i].valorCuota(): 
                print("\n Codigo: {} ".format(self.__listaPlan[i].getCod()))
                print("\n Modelo: {} ".format(self.__listaPlan[i].getModel()))
                print("\n Version: {} ".format(self.__listaPlan[i].getVersion()))
            else: 
                print("ERROR \n")  
    
    def mostrarMonto (self):
        for i in range (len(self.__listaPlan)):
            print("\n El monto que se debe pagar para licitar es: {}".format(self.__listaPlan[i].Monto()))             
                
    def modificarCuotas (self, cod):
        i = 0
        encontrado = False
        while i < len(self.__listaPlan) and not encontrado:
         print(i)
         if cod == int(self.__listaPlan[i].getCod()):
            nuevo = int(input('Nuevas cuotas para pagar: '))
            self.__listaPlan[i].nuevoValor2(nuevo)
            print('¡Cuotas actualizadas!')
            encontrado = True
         i += 1
         if not encontrado:
           print('No se encontró el código especificado en la lista.')
            
        
            
            
                
    
          
    
   