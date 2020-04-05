from abstract_lista import AbstractList
class Pilha(AbstractList):

    def returnList(self):
        super().returnList()

    def returnFirst(self):
        return super().returnFirst()

    def returnLast(self):
       print('Não se aplicada, O primeiro a entrar é o último a sair!')
       return ''
       
    def showSizeList(self):
        print('Total: '+ str(len(self._base_list)))

    def showList(self):
        for el in self._base_list:
            print(el)

    def limparList(self):
        super().limparList()

    def removeFirst(self):
        super().removeValue(self.returnFirst())
    

if __name__ == '__main__':
    pilha = Pilha()
    pilha.insertValue('Andre')
    pilha.insertValue('Marcos')
    pilha.insertValue('Paulo')
    pilha.insertValue('Ligia')
    print('*********************')
    pilha.showSizeList()
    print('*********************')
    pilha.showList()
    print('*********************')
    print('Topo da Pilha: '+ pilha.returnFirst())
    print('Remove Topo da Pilha: ')
    pilha.removeFirst();
    print('*********************')
    pilha.showList()

