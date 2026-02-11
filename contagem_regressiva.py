import time

def contador(tempo):

    while tempo > 0:
        minutos, segundos =  divmod(tempo,60)

        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)

        print(temporizador, end="\r")

        time.sleep(1)

        tempo -=1
    print('Contagem completa')


def verificador(msg):
   
    valor = 0 

    while True:
        num = str(input(msg))

        if num.isnumeric():
            valor = int(num)
            break
        elif num == '':
            print('\033[31mValor não informado. Tente novamente!\033[m')
    
        else: 
            print(f'\033[31mERRO! \"{num}\" não é um número inteiro!\033[m')
        
    return valor 
            

try:

    tempo = verificador('Digite um número para começar a contagem regressiva: ')

    contador(tempo)

except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário')


