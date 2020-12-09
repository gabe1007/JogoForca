# print(max(var, key=len)) # mostra a maior string na lista

from random import *
from os import *

letrasUsadas = []
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Esta função permite o computador escolher uma palavra para o jogo
def string():
    string = '''
   Botuverá,Brunópolis,Brusque,Caçador,Calmon,Camboriú,Campo Alegre,Campo Erê,Campos Novos,Canelinha,Canoinhas,Capão Alto,Capinzal,Catanduvas,Celso Ramos,
   Cerro Negro,Chapecó,Concórdia,Cordilheira Alta,Coronel Freitas,Coronel Martins,Correia Pinto,Corupá,Criciúma,Cunha Porã,Cunhataí,Curitibanos,Descanso,Florianópolis,Forquilhinha,
   Fraiburgo,Joinville,Garopaba,Garuva,Gaspar,Grão Pará,Gravatal,Guabiruba,Guaraciaba,Guaramirim,Guatambú,Ibiam,Ibicaré,Ibirama,Içara,Ilhota,Imaruí,Imbituba,Imbuia,Indaial,Iomerê,
   Ipira,Ipuaçu'''

    texto = string.lower()
    string = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ê', 'e').replace('ã', 'a')
    texto = string.split(',')
    return texto

# Esta funcao mostra as opções para o jogador
def instrucoes():
    print('******************************* FORCA *******************************************')
    print('\n')
    nome = input('Qual o seu nome? ')
    system('cls')
    print('instruções:\n')
    print(f'1 - {nome}, o jogo irá sortear uma palavra e a sua obrigação é tentar advinhar qual palavra foi sorteada')
    print('2 - Você terá 6 palpites para tentar advinhar qual palavra foi escolhida')
    print('3 - Para cada palpite errado, uma parte do boneco será adicionada a forca')
    print(f'4 - Quando todas as partes forem adicionadas, lamento {nome}, mas é GAME OVER')
    print(f'BOA SORTE {nome}\n')

# Função jogar começa o jogo
def jogar(palavra):

    chance = 0
    lista_palavra = []

    # Cria uma lista com '-' para esconder os caractereres da palavra
    for letras in range(len(palavra)):
        lista_palavra.append('-')

    # Mostra o comprimento da palavra
    print(f'A palavra sorteada possui {len(palavra)} letras')
    letra = input('Digite uma letra: ')

    # Esta parte do código mascara a palavra selecionada e mostra somente as letras que existirem
    while chance <= 6:
        # Função 'desenho mostra o boneco que começa a ser enforcado'
        desenho(chance)
        # Este bloco checa se a letra já foi advinhada
        if letra not in alfabeto:
            print('Entrada inválida. Tente novamente')
        elif letra not in letrasUsadas:
            letrasUsadas.append(letra)
        else:
            print('Você já advinhou essa letra. Tente outra')
            print(f'letras usadas {letrasUsadas}')

        if letra in palavra:
            for l in range(len(palavra)):
                if palavra[l] == letra:
                    lista_palavra[l] = letra
                    print(lista_palavra)

        else:
            print(f"Letra '{letra}' não existe na palavra")
            print(letrasUsadas)
            chance += 1
            desenho(chance)
            print(lista_palavra)
            if chance >= 6:
                print(f'GAME OVER, você foi enforcado. A cidade era {palavra}')
                letrasUsadas.clear()
                jogarNovamente()

        if '-' not in lista_palavra:
            print('Parabéns você advinhou a palavra')
            letrasUsadas.clear()
            jogarNovamente()

        letra = input('\nDigite uma letra: ')

# Função leva o jagador a escolher se deseja jogar de novo
def jogarNovamente():
    print('Deseja jogar novamente?')
    opcao = int(input('1 - SIM    2 - NÃO\n'))
    if opcao == 1:
        system('cls')
        forca()
    elif opcao == 2:
        exit()


def forca():
    var = string()
    sortear = randrange(len(var))
    palavra = var[sortear]
    jogar(palavra)


def desenho(chance):

    if chance == 1:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|               ')
        print('|               ')
        print('|')

    if chance == 2:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|              |')
        print('|               ')
        print('|')

    if chance == 3:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|              |\\')
        print('|               ')
        print('|')

    if chance == 4:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|             /|\\')
        print('|               ')
        print('|')

    if chance == 5:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|             /|\\')
        print('|               \\')
        print('|')

    if chance == 6:
        print('+--------------+')
        print('|              |')
        print('|              |')
        print('|              O')
        print('|             /|\\')
        print('|             / \\')
        print('|')


# main
instrucoes()
forca()
