
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from productos import Productos
from lista_simple import listaSimple
import os


class menu:

    def __init__(self) -> None:
        

        self.mostrarMenu()
    def mostrarMenu(self):
        opcion =''
        while opcion != '5':
            print("-------------Menu-------------")
            print("1. Abrir archivo")
            print("2. Productos con mayor margen de ganancia")
            print("3. Productos con mayor valor del inventario")
            print("4. Mostrar inventario  ")
            print("5. Salir")
            opcion=input("Ingrese una de las opciones: ")
            
            if opcion== '1':
                archivo=askopenfilename(title="Abrir un archivo")
                archivoxml=minidom.parse(archivo)
                self.procesoInformacion(archivoxml)
                print("Se cargo el archivo!")
                
                    
            elif opcion=='2':
                pass
                
                

            elif opcion=='3':
                self.valor_inventario()

            elif opcion=='4':
                self.valores()


    def procesoInformacion(self,archivoXml):
        self.lista_item=listaSimple()

        itemXML=archivoXml.getElementsByTagName('Item')

        for aux in itemXML:
            a=aux.getElementsByTagName('ItemCode')[0]
            b=aux.getElementsByTagName('QuantityOnHand')[0]
            c=aux.getElementsByTagName('PriceLevel1')[0]
            d=aux.getElementsByTagName('PriceLevel2')[0]
            e=aux.getElementsByTagName('PriceLevel3')[0]
            f=aux.getElementsByTagName('LastTotalUnitCost')[0]
            


            self.simbolo1=a.firstChild.data
            self.simbolo2=b.firstChild.data
            self.simbolo3=c.firstChild.data
            self.simbolo4=d.firstChild.data
            self.simbolo5=e.firstChild.data
            self.simbolo6=f.firstChild.data

            self.nuevo_item=Productos(self.simbolo1,self.simbolo2,self.simbolo3,self.simbolo4,self.simbolo5,self.simbolo6)
            self.lista_item.insertar(self.nuevo_item)
    
    def valores(self):
        
        self.lista1=self.lista_item

        nodo_actual=self.lista1.cabeza
        self.lista_nivel1=listaSimple()
        self.lista_nivel2=listaSimple()
        self.lista_nivel3=listaSimple()
        self.lista_valores=listaSimple()

        while nodo_actual !=None:
            celda_producto:Productos=nodo_actual.datos
            if celda_producto!=None:
                nombre=celda_producto.item

                a=celda_producto.cantidad
                b=celda_producto.total
                a1=celda_producto.precio_1
                a2=celda_producto.precio_2
                a3=celda_producto.precio_3

                
                self.nivel1=((float(a1)-float(b))/float(b))*100
                self.nivel2=((float(a2)-float(b))/float(b))*100
                self.nivel3=((float(a3)-float(b))/float(b))*100

                self.total=float(a)*float(b)

                self.lista_nivel1.insertar(self.nivel1)
                self.lista_nivel2.insertar(self.nivel2)
                self.lista_nivel3.insertar(self.nivel3)
                self.lista_valores.insertar(self.total)

                print(nombre+" cantidad: ", a+" precio nivel1: ", a1+" precio nivel2: ",a2 +" precio nivel3: ",a3 +" total: ",b+ " Margen nivel1", self.nivel1+ " Margen nivel2", self.nivel2+ " Margen nivel3", self.nivel3+ " Valor:", self.total)
                


                
            nodo_actual=nodo_actual.siguiente

    def valor_margen(self):
        self.lista1.ordenar(self.lista_nivel1)
        


cargarmenu=menu()
cargarmenu.mostrarMenu()