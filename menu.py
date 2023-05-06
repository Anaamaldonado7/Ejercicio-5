from manejadorPlanes import manejadorPlan
class Menu:
    opcion=None
    
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self):
        Obj=manejadorPlan()
        while self.__opcion!=-1:
            print('[1] Actualizar Valor ')
            print('[2] Valor menor a cant cuota')
            print('[3] Monto Licitacion Vehiculo')
            print('[4] Cod Plan modificar cant cuota licitar')
            self.__opcion=input('\nIngrese numero: ')
            if self.__opcion=='1':
                    Obj.actualizarValor()
            elif self.__opcion=='2':
                valor=int(input('\nIngrese valor del vehiculo'))
                Obj.mostrarDatos(valor)
            elif self.__opcion=='3':
                Obj.mostrarMonto()
            elif self.__opcion=='4':
                cod=int(input('\n Ingrese codigo de plan: '))
                Obj.modificarCuotas(cod)
                