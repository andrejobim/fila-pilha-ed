from abc import ABC, abstractmethod

class AbstractList(ABC):

    _base_list = []

    @abstractmethod
    def returnList(self):
        return self._base_list

    def insertValue(self, valor):
        self._base_list.append(valor)

    def removeValue(self, valor):
       try:
           self._base_list.remove(valor)
       except:
           print('Exception |  Valor '+valor+' não encontrado')

    @abstractmethod
    def returnFirst(self):
        try:
            return self._base_list[0]
        except:
            print('Exception | Primeiro elemento da lista não encontrado')

    @abstractmethod
    def returnLast(self):
        try:
            return self._base_list[len(self._base_list)-1]        
        except:
            print('Exception | Último elemento da lista não encontrado.')

    @abstractmethod
    def showSizeList(self):
        print('Total: '+ str(len(self._base_list)))

    @abstractmethod
    def showList(self):
        for el in self._base_list:
            print(el)

    @abstractmethod
    def limparList(self):
        self._base_list.clear()

    def returnIndexValue(self, valor):
        try:
            return self._base_list.index(valor)
        except:
            print('Exception | Elemento '+valor+' não encontrado.')
        
