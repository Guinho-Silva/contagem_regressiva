import time

def contador(tempo):

    while tempo:
        minutos, segundos =  divmod(tempo,60)

        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)

        print(temporizador, end="\r")

        time.sleep(1)

        tempo -=1
    print('Contagem completa')


tempo = input('Digite a contagem regressiva: ')

contador(int(tempo))
