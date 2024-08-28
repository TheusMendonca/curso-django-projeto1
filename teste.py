velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[4;30;41mMULTADO! Você excedeu o limite de velocidade que é de 80km/h\033[m ')
    multa = (velocidade-80) * 7
    print('\033[33;40mVocê vai pagar uma multa de R$ {:.2f}\033[m'.format(multa))
print('\033[32;40mTenha um bom dia! Diriga com segurança!\033[m ')

