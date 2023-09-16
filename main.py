#funções de conversão de acordo com a unidade de temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

#exibindo as opções de conversão na tela do usuário até ocorrer a escolha

while True:
    
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair \n")
    
    escolha = input('Digite o número da opção desejada: ')
    
    if escolha == '7':
        break
    
    if escolha in ['1', '2', '3', '4', '5', '6']:
        try:
            valor = float(input('Digite a temperatura: '))
        #possíveis resultados
            if escolha == '1':
                resultado = celsius_para_fahrenheit(valor)
                print(f"{valor} Celsius é igual a {resultado} Fahrenheit \n")
            elif escolha == '2':
                resultado = fahrenheit_para_celsius(valor)
                print(f"{valor} Fahrenheit é igual a {resultado} Celsius\n")
            elif escolha == '3':
                resultado = celsius_para_kelvin(valor)
                print(f"{valor} Celsius é igual a {resultado} Kelvin \n")
            elif escolha == '4':
                resultado = kelvin_para_celsius(valor)
                print(f"{valor} Kelvin é igual a {resultado} Celsius \n ")
            elif escolha == '5':
                resultado = fahrenheit_para_kelvin(valor)
                print(f"{valor} Fahrenheit é igual a {resultado} Kelvin \n")
            elif escolha == '6':
                resultado = kelvin_para_fahrenheit(valor)
                print(f"{valor} Kelvin é igual a {resultado} Fahrenheit \n ")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido. \n ")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida. \n ")
