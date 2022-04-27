import sys, random, time
from webbrowser import get
from server_connection import insert, get_values
from random_datetime import gen_timestamp

cidades = ['Sao Paulo', 'Rio de Janeiro', 'Florianopolis', 'Curitiba', 'Alagoas', 'Natal']
produtos = ['Hortifruti', 'Higiene', 'Moda', 'Mecanica', 'Bebidas', 'Padaria']
pagamento = ['Dinheiro', 'Debito', 'Credito']
semana = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

def transaction(range):
    tempo_inicial = (time.time())
    lista = []
    for item in range:
        cidade = cidades[random.randrange(0, (len(cidades)-1), 1)]
        produto = produtos[random.randrange(0, (len(produtos)-1), 1)]
        formaPagamento = pagamento[random.randrange(0, (len(pagamento)-1), 1)]
        dia = semana[random.randrange(0, (len(semana)-1), 1)]
        quantidade = random.randint(1, 1000)
        tempo_append = (time.time())
        tempo_final = (tempo_append - tempo_inicial)
        lista.append(item)
        tamanho = sys.getsizeof(lista)
        values = (cidade, produto, formaPagamento, dia, quantidade, tempo_final, tamanho, gen_timestamp(2020,2022))
        print(values)
        insert(values)

print('*_* Menu *_*')
print('*Por favor selecione um numero')
print('1 - Inserir Dados')
print('2 -Verificar')
print('3 - Sair')
 
while True:
    do = input('O que voce deseja fazer?').split()
    
    operation = do[0]
    if int(operation) == 1:
      valorInicial = input('Digite o valor inicial: ')
      valorFinal = input('Digite o valor final: ')
      intervalo = input('Digite o intervalo: ')
      transaction(range(int(valorInicial), int(valorFinal), int(intervalo)))

    elif int(operation) == 2:
      print('Buscando dados...')
      get_values()

    elif int(operation) == 3:
        print('Obrigado por usar!')
        break

    else:
      print('Informe um numero correto')
      print('1 - Inserir Dados')
      print('2 -Verificar')
      print('3 - Sair')
