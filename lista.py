from abstract_lista import AbstractList

class Lista(AbstractList):

    def returnList(self):
        return super().returnList()

    def returnFirst(self):
        return super().returnFirst()

    def returnLast(self):
        return super().returnLast()

    def showList(self):
        super().showList()
    
    def limparList(self):
        super().limparList()
    
    def showSizeList(self):
        super().showSizeList()

    def returnIndexValue(self, valor):
        return super().returnIndexValue(valor)


if __name__ == '__main__':
    lista = Lista()
    lista.insertValue('Andre')
    lista.insertValue('Marcos')
    lista.insertValue('Paulo')
    lista.insertValue('Ligia')
    print('*********************')
    lista.showSizeList()
    print('*********************')
    lista.showList()
    print('*********************')
    print('Retornando posição de cada elemento: ')
    print()
    print('Andre '+str(lista.returnIndexValue('Andre')))
    print('Marcos '+str(lista.returnIndexValue('Marcos')))
    print('Paulo '+str(lista.returnIndexValue('Paulo')))
    print('Ligia '+str(lista.returnIndexValue('Ligia')))
    print('*********************')
    print('Primeiro elemento: '+lista.returnFirst())
    print('Último elemento: '+lista.returnLast())

    print('Andre index: '+str(lista.returnIndexValue('Andre')))
    print('Jobim index: '+str(lista.returnIndexValue('Jobim')))
    print('Ligia index: '+str(lista.returnIndexValue('Ligia')))


