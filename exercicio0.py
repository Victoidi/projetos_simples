'''
Exercicio basico de variaveis
onde será declaradas as variavei e a verificacao de idade
'''

nome= 'Victor'
sobrenome='Felipe'
ultimo_nome='Bueno'
idade='17'
ano_nascimento=2009
data_atual=2026
vld_idade=data_atual-data_atual
if vld_idade >= 18:
    vld_idade=True
else:
    vld_idade=False

maior_de_idade=vld_idade
altura_metros=1.86


print('Nome:', nome,sobrenome,ultimo_nome, sep=" ")
print('Idade:',idade)
print('Ano de nascimento:' ,ano_nascimento)
print('É maior de idade:',maior_de_idade)
print('Altura em metros:',altura_metros)
