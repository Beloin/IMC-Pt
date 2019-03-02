import time
while True:
    try:
        print('')
        print('Cálculo do IMC:')
        print('')
        h = float(input('Primeiro, digite sua altura:'))
        print('')
        m = float(input('Agora escreva sua massa corporal:'))
        print('')
        IMC = float((m/(h**2)))
        IMC = float('{0:.2f}'.format(IMC))
        if IMC < 17:
            print('Seu IMC equivale a {}, e você está muito abaixo do peso.'.format(IMC))
        if 17 < IMC < 18.49:
            print('Seu IMC equivale a {}, e você está abaixo do peso.'.format(IMC))
        if 18.5 < IMC < 24.99:
            print('Parabéns, você está com um IMC de {} e no peso ideal!'.format(IMC))
        if 25 < IMC < 29.99:
            print('Seu IMC equivale a {} e você está acima do peso.'.format(IMC))
        if 30 < IMC < 34.55:
            print('Seu IMC equivale a {} e você está com um ínicio de obesidade.'.format(IMC))
        if 35 < IMC < 39.99:
            print('Seu IMC equivale a {} e você está com obesidade Severa.'.format(IMC))
        if IMC > 40.00:
            print('Seu IMC equivale a {} e você está com obesidade mórbida.'.format(IMC))
            print('Aconselhamos dar uma olhada no site do Ministério da Saúde: http://dab.saude.gov.br/portaldab/ape_promocao_da_saude.php?conteudo=prevencao_e_controle')
        print('')
        a = int(input('Aperte em 1 para fechar, ou 0 para fazer outra conta.'))
        if a == 1:
            print('O programa irá fechar, obrigado por utilizar.')
            time.sleep(1.5)
            break
    except ValueError:
        print('Escreva o número de sua altura e massa.')
        time.sleep(1)
