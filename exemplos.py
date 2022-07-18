print('Calculadora de IMC')
peso = float(input('Qual seu peso em kg?'))
altura = float(input('Qual sua altura em metros?'))

IMC = (peso/(altura**2))
if IMC < 18.5: 
        print(" seu IMC aponta: magreza", IMC)
elif IMC > 18.6 and IMC < 24.9:
        print("Seu IMC aponta: normalidade", IMC) 
elif IMC > 25  and IMC < 29.9:
        print("Seu IMC aponta: Obsesidade I", IMC)
elif IMC > 30 and IMC < 39.9:
        print("Seu IMC aponta: Obsesidade II", IMC)
else: 
        print("Seu IMC aponta: Obsesidade GRAVE", IMC)
