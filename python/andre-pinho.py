# boas vindas, esse é um software gentil
print('Olá, tudo bem? Espero que sim.')

# QUESTÃO 1
print('Vou lhe pedir para digitar algumas coisas. Tecle ENTER para enviar.\n')

# coletando inputs do usuário e convertendo os numeros para integer
print('Digite uma palavra:')
palavra1 = input()
print('Agora digite um número inteiro:')
numero1 = int(input())
print('Digite a segunda palavra:')
palavra2 = input()
print('Digite o segundo número inteiro:')
numero2 = int(input())
print('Digite a terceira palavra:')
palavra3 = input()
print('Digite o terceiro número inteiro:')
numero3 = int(input())

print('\nResutado 1.a)')
# concatenando e imprimindo na ordem digitada
print(f"{palavra1}-{numero1}-{palavra2}-{numero2}-{palavra3}-{numero3}")

print('Resultado 1.b)')
# concatenando e imprimindo na ordem inversa da digitada com o dobro dos valores
print(palavra3 +"-"+ str(numero3 * 2) +"-"+ palavra2 +"-"+ str(numero2*2) +"-"+ palavra1 +"-"+ str(numero1*2))

# QUESTÃO 2
print('\nInforme um valor em reais:')
# coletando input do usuário e convertando para float
valor_reais = float(input())

# multiplicando pelas cotações para obter valor
valor_euro = valor_reais * 0.25
valor_iene = valor_reais * 26.38
valor_yuan = valor_reais * 1.75
valor_dolar = valor_reais * 0.25

# formatando número de caracteres e limitando casas decimais
valor_reais_formatado = '%010.2f' % valor_reais
valor_euro_formatado = '%010.2f' % valor_euro
valor_iene_formatado = '%010.2f' % valor_iene
valor_yuan_formatado = '%010.2f' % valor_yuan
valor_dolar_formatado = '%010.2f' % valor_dolar

# imprimindo respostas
print('\nResultado 2)')
print('R$:', valor_reais_formatado)
print('Euro:', valor_euro_formatado)
print('Iene:', valor_iene_formatado)
print('Yuan:', valor_yuan_formatado)
print('Dolar:', valor_dolar_formatado)

# questão 3

# coletando inputs dos usuários
print('\nAgora vamos agendar sua viagem. Digite seu nome completo por favor:')
name = input()
print('Agora digite seu local de origem:')
origem = input()
print('Agora digite seu destino:')
destino = input()
print('Digite seu assento:')
assento = input()
print('Digite a data da viagem:')
data = input()
print('Digite o horário da viagem:')
hora = input()

# formatando multiline string da passagem com as variáves
passagem = f"""#######################################################
COMPANHIA AÉREA VOLARE
#######################################################
Nome do passageiro: {name}
          Origem: {origem}
          Destino: {destino}
               Data de embarque: {data}
               Horário: {hora}
Assento: {assento}
**********
Obrigado por voar conosco!
**********
"""

print('\nResultado 3)')

# imprimindo resultado
print(passagem)

# despedida, afinal esse é um software gentil
print('\nObrigado pelas respostas. Até a próxima.')
