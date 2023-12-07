
def contagem():

    while True:
        try:
            numbers = int(input("Digite um numero: "))

        except ValueError:
            print("valor enviado não é um numero.")

        else:
            for number in range(numbers+1):
                print(number)
            break


contagem()
