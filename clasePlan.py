class PlanAhorro:
    __codigo = ''
    __modelo = ''
    __version = ''
    __valor = 0
    __cantCuotas = 60  #variable de clase (tiene un valor estatico)
    __cantCuotasPagas = 10   # =
    
    def __init__(self, codigo, modelo, version, valor): #no agrego las variables de clase al constructor para que no se modifique nunca su valor
      self.__codigo = codigo    
      self.__modelo = modelo
      self.__version = version 
      self.__valor = valor
    
    def getCod (self):  #los get me sirven para acceder a los valores de los atributos fuera de la clase 
        return self.__codigo
    
    def getModel (self):
        return self.__modelo
    
    def getVersion (self):
        return self.__version
    
    def getValor (self):
        return self.__valor
    
    def nuevoValor (self, nuevo):
        self.__valor = nuevo
        return self.__valor
    
    def valorCuota (self):  #tip: hacer siempre la conversion correspondiente segun el tipo de dato que pide el inciso
        val = float(self.__valor) / float(self.__cantCuotas) + float(self.__valor)*0.10
        return float(val) 
    
    def Monto (self):
        m = float(self.__cantCuotasPagas) * self.valorCuota()
        return float(m) 
    
    def nuevoValor2 (self,nuevo):
        self.__cantCuotasPagas=nuevo
        return self.__cantCuotasPagas
    