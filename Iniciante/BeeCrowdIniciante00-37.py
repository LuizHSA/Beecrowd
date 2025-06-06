#def zero():
#     print('Hello World!')
    #
#zero()

# def um():
    
#     print(f'X = {int(input()) + int(input())}')    
# um()

# def dois():
    
#     print(f'A={3.14159*float(input())**2:.4f}')
# dois()

# def tres():
#     a, b = int(input()), int(input())
#     print(f'SOMA = {a+b}')
# tres()

# def quatro():
#   a,b = int(input()), int(input())
#   print(f'PROD = {a*b}')
# quatro()    

# def cinco():    
#     a, b = float(input()), float(input())
#     print(f'MEDIA = {(a*3.5+b*7.5)/11:.5f}')
# cinco()    

# def seis():
#     a, b, c = float(input()), float(input()), float(input())
#     print(f'MEDIA = {(a*2+b*3+c*5)/10:.1f}')
# seis()

# def sete():
#     a,b,c,d = int(input()), int(input()), int(input()), int(input())
#     print(f'DIFERENCA = {a*b-c*d}')
# sete()    

# def oito():
#     number, hours, value = int(input()), int(input()), float(input())
#     print(f'NUMBER = {number}')
#     print(f'SALARY = U$ {hours*value:.2f}')
# oito()

# def nove():
#     nome, salario, vendas = input(), float(input()), float(input())
#     print(f'TOTAL = R$ {(salario + vendas * 0.15):.2f}')
# nove()

# def dez():
#     nome1, num1, valor1 = input().split()
#     nome2, num2, valor2 = input().split()
#     num1 = int(num1)
#     valor1 = float(valor1)
#     num2 = int(num2)
#     valor2 = float(valor2)
#     print(f'VALOR A PAGAR: R$ {(num1*valor1 + num2*valor2):.2f}')
# dez()

# def onze():
#     pi= 3.14159
#     raio = float(input())
#     print(f'VOLUME = {((4/3)*pi*raio**3):.3f}')
# onze()    

# def doze():
#     a, b, c = input().split()
#     a,b,c = float(a), float(b), float(c)
#     print(f'TRIANGULO: {a*c/2:.3f}')
#     print(f'CIRCULO: {3.14159*c**2:.3f}')
#     print(f'TRAPEZIO: {((a+b)*c)/2:.3f}')
#     print(f'QUADRADO: {b**2:.3f}') 
#     print(f'RETANGULO: {a*b:.3f}')
# doze()

# def treze():
    
#     a, b, c = input().split()
#     a, b, c = int(a), int(b), int(c)
    
#     def maiorAB(a, b): 
#         resultado= (a+b + abs(a-b)) /2
#         return int(resultado)
    
#     maior = maiorAB(a, b)
#     maior = maiorAB(maior, c)
#     print(f'{maior} eh o maior')
# treze()

# def quatorze():
#     a = int(input())
#     b = float(input())
#     print(f'{a/b:.3f} km/l')
# quatorze()

# def quinze():
#     x1, y1 = input().split()
#     x1, y1 = float(x1), float(y1)
#     x2, y2 = input().split()
#     x2, y2 = float(x2), float(y2)
#     distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     print(f'{distancia:.4f}')
# quinze()

# def dezesseis():
#     a = int(input())
#     print(f'{a*2} minutos')
# dezesseis()  

# def dezessete():
#     a = int(input())
#     b = int(input())
#     distancia = a * b
#     print(f'{distancia/12:.3f}')
# dezessete()  

# def dezoito():
#     valor = int(input())
#     notas = [100, 50, 20, 10, 5, 2, 1]
#     print(valor)
#     def decompor(valor,notas):
#         for i in notas:
#             quantidade = valor // i
#             valor= valor - quantidade * i
#             print(f'{quantidade} nota(s) de R$ {i},00')
#     decompor(valor, notas)
# dezoito()

# def dezenove():
#     a= int(input())
#     tempos =[3600,60,1]
#     tempos2=[]
    
#     def decompor(a, tempos):
#         for i in tempos:
#             quantidade = a//i
#             a -= quantidade *i
#             tempos2.append(quantidade)
#     decompor(a, tempos)        
#     print(f'{tempos2[0]}:{tempos2[1]}:{tempos2[2]}')    
    
# dezenove()    

# def vinte():

#     a = int(input())
#     tempos = [365, 30,1]
#     prints = [' ano(s)', ' mes(es)', ' dia(s)']
#     def decompor(a, tempos,prints):
#         for i in tempos:
#             quantidade = a//i
#             a -= quantidade *i
#             print(f'{quantidade}{prints[tempos.index(i)]}')
#     decompor(a, tempos,prints)
# vinte()

# def vinteUm():
#     valor = float(input())
#     total_centavos = round(valor * 100)  
    
#     notas = [10000, 5000, 2000, 1000, 500, 200]  
#     moedas = [100, 50, 25, 10, 5, 1]             

#     print('NOTAS:')
#     for nota in notas:
#         quantidade = total_centavos // nota
#         total_centavos %= nota  
#         print(f'{quantidade} nota(s) de R$ {nota/100:.2f}')

#     print('MOEDAS:')
#     for moeda in moedas:
#         quantidade = total_centavos // moeda
#         total_centavos %= moeda
#         print(f'{quantidade} moeda(s) de R$ {moeda/100:.2f}')

# vinteUm()

# def trintaCinco():
#     a, b, c, d = map(int, input().split())
#     if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
#         print('Valores aceitos')    
#     else:
#         print('Valores nao aceitos')
# trintaCinco()

# import math

# def trintaSeis() :
#     A, B, C = map(float, input().split())
    
#     delta = B**2 - 4*A*C
    
#     if A == 0 or delta < 0:
#         print("Impossivel calcular")
#     else:
        
#         raiz_delta = math.sqrt(delta)
#         R1 = (-B + raiz_delta) / (2*A)
#         R2 = (-B - raiz_delta) / (2*A)
        
#         print(f"R1 = {R1:.5f}")
#         print(f"R2 = {R2:.5f}")

# trintaSeis() 

# def trintaSete():
#     a = float(input())
#     if a < 0 or a >100:
#         print('Fora de intervalo')
#     else:
#          if 0 <= a <= 25:
#             print('Intervalo [0,25]') 
                    
#          elif 25 < a <= 50:  
#             print('Intervalo (25,50]') 
          
#          elif 50 < a <= 75:
#             print('Intervalo (50,75]') 
           
#          else:
#             print('Intervalo (75,100]') 
            
            
# trintaSete()