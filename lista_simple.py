from nodo import Nodo

class listaSimple:
    def __init__(self):
        self.cabeza=None
        self.tamaño=0
         

    def insertar(self,datos):
        nuevoNodo=Nodo(datos)
        if self.tamaño == 0:
            self.cabeza = nuevoNodo

        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente !=None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevoNodo 
        self.tamaño += 1

    def listar(self):
        auxiliar_dato=self.cabeza
        while auxiliar_dato !=None:
            print(auxiliar_dato.datos )
           
            auxiliar_dato=auxiliar_dato.siguiente

    def ordenar(self,datos):
        for i in range(1,self.tamaño):
            aux=self.cabeza
            for j in range(0,self.tamaño-1):
                if aux.datos > aux.datos.siguiente:
                    temporal=aux.datos
                    aux.datos=aux.siguiente.datos
                    aux.siguiente.datos=temporal
                
                aux=aux.siguiente
                
        