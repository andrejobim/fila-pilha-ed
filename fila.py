from abstract_lista import AbstractList

class Fila(AbstractList):

    def returnList(self):
        return super().returnList()

    def returnFirst(self):
        try:
            return self._base_list[len(self._base_list)-1]        
        except:
            print('Primeiro elemento da fila não encontrado.')

    def returnLast(self):
        try:
            return self._base_list[0]
        except:
            print('Último elemento da fila não encontrado')

    def showList(self):
        super().showList()

    def limparList(self):
        super().limparList()
    
    def showSizeList(self):
        super().showSizeList()

    def removeFirstOut(self):
        self.removeValue(self.returnFirst())

    def removeLastIn(self):
        self.removeValue(self.returnLast())

if __name__ == '__main__':
    fila = Fila()
    fila.insertValue('Andre')
    fila.insertValue('Marcos')
    fila.insertValue('Paulo')
    fila.insertValue('Ligia')
    print('*********************')
    fila.showSizeList()
    print('*********************')
    fila.showList()
    print('*********************')
    print('Último da Fila: '+fila.returnLast())
    print('Primeiro da Fila: '+ fila.returnFirst())
    print('*********************')
    fila.removeFirstOut()
    print('Removendo primeiro a sair da fila: ')
    print()
    print('Último da Fila: '+fila.returnLast())
    print('Primeiro da Fila: '+ fila.returnFirst())  