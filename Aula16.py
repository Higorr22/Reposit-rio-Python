# Introdução ao Bloco de código IF/ELIF/ELSE ----> São funções condicionais ou variáveis.
# Traduzidas são: Se/ Se não Se/ Se não respectivamente

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print(1234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')
