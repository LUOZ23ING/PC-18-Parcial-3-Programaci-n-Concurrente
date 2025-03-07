import concurrent.futures



def suma(A,B):
    return A+B
def resta(A,B):
    return A-B
def multiplicacion(A,B):
    return A*B
def division(A,B):
    return A/B

def ejecutar(A,B):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_suma = executor.submit(suma, A, B)
        future_resta = executor.submit(resta, A, B)
        future_multi = executor.submit(multiplicacion, A, B)
        future_divi = executor.submit(division, A, B)
        print("Suma: ",future_suma.result())
        print("Resta: ",future_resta.result())
        print("Multiplicacion: ",future_multi.result())
        print("Division: ",future_divi.result())

if __name__ == '__main__':
    A = 10
    B = 5
    ejecutar(A,B)