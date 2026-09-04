#!/usr/bin/env python3

autor = "Fugencio"

#Lista: é uma sequencia ordenada de valores.

portas_alvo = [22, 80, 443, 3306, 8080, 3000, 5000, 8000, 137, 138, 139, 445, "DNS"]
portas_alvo.append(21) #Adiciona a porta 21 na variavel portas_alvo
servicos = ["ssh", "https", "dns"]

print('A lista de portas é:', portas_alvo)
print(f'A lista de portas é: {portas_alvo}')

print("O indice 2, tem o valor: ", portas_alvo[2])
print("O indice -1, tem o valor: ", portas_alvo[-1])


for NUM in range(1,11):
print(NUM)
 
#Dicionarios: é um tipo de dado que trabalho sobre chave:valor
 
status_servico = {
'host': '8.8.8.8',
'porta': '443',
'estado': 'aberta',
'servico': 'https',
}
 
print(status_servico['host'])
print(status_servico['servico'])
 
servicos = {
22: 'SSH',
80: 'HTTP',
443: 'HTTPS',
3306: 'MYSQL',
'DNS': 53
}
 
for PORTA in portas_alvo:
nome = servicos.get(PORTA, 'desconhecido')
print(f'Porta {PORTA}: Servico {nome}')


