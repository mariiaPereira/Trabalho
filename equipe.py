#coding: utf-8

from aluno import aluno1

class equipe:
    def __init__(self,projeto):
        self.projeto = projeto
        self.list = []

    def getProjeto(self):
        return self.projeto

    def addNovoAluno(self,nome,cpf):
        alun = aluno1(nome, cpf)
        self.list.append(alun)
        print"Aluno cadastrado com sucesso!"

    def removerA(self, cpf):
        aluno = self.procuraA(cpf)
        if aluno == None:
            return
        else:
            self.list.remove(aluno)
    def procuraA(self, cpf):
        for i in range(len(self.list)):
            if self.list[i].getCpf() == cpf:
                return self.list[i]
        return None

    def imprimir(self):
        for i in range(len(self.list)):
            print "Aluno: %s \n CPF: %i" % (self.list[i].getNome(), self.list[i].getCpf())

equi = equipe('DAHAS')

while True:
    print '1 - Cadastrar aluno'
    print '2 - Remover aluno'
    print '3 - Mostrar aluno'
    op = int(raw_input('informe sua opção:'))
    if op == 1:
        while True:
            nome = raw_input("Informe seu nome:")
            cpf = int(raw_input("Informe seu cpf:"))
            equi.addNovoAluno(nome,cpf)
            opcao = raw_input('Deseja cadastrar outro aluno ?')

            if opcao.upper() == "SIM":
                continue
            else:
                break

    elif op == 2:
        while True:
            remove = int(raw_input("Informe o nome que deseja remover: "))
            equi.removerA(remove)
            opcao2 = raw_input('Deseja remover outro aluno ?')

            if opcao2.upper() == "SIM":
                continue
            else:
                break
    elif op == 3:
        while True:
            equi.imprimir()
            opcao3 = raw_input('Deseja consultar novamente ?')

            if opcao3.upper() == "SIM":
                continue
            else:
                break


