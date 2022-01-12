# Paula Santos - UFPA

# CG - Algoritmo de Bresenham

import matplotlib.pyplot as plt

plt.title("Algoritmo de Bresenham")
plt.xlabel("X axis")
plt.ylabel("Y axis")

def bresenham (x1, y1, x2, y2):
      x, y = x1, y1
      dx = abs(x2 - x1)
      dy = abs(y2 - y1)
      gradient = dy/float(dx)

      if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1 
        x2, y2 = y2, x2 
    
      p = 2 * dy - dx
      print ('x = %s, y = %s' % (x,y))

      #Inicializa o pontos plotting
      xcoordinates = [x]
      ycoordinates = [y]

      for k in range (dx):
        
        if p > 0:
          y = y + 1 if y < y2 else y - 1
          
          p = p + 2 * (dy - dx)
        
        else:
          p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print ('x = %s, y = %s' % (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)

      plt.plot(xcoordinates, ycoordinates)
      plt.show()

escolha = 0
while escolha != 5:
  print ('''QUAL TIPO DE IMAGEM VC DESEJA VISUALIZAR: 
  [1] - Bresenhan
  [2] - Circulos
  [3] - Curvas
  [4] - Polilinhas
  [5] - Sair ''')
  escolha = int(input('Informe sua escolha: '))
  print ('Vc escolheu a opção: ', escolha)
  if escolha == 1:

      x1 = int(input("Entre ponto inicial de x: "))
      y1 = int(input("Entre ponto inicial de y: "))
      x2 = int(input("Entre ponto de x: "))
      y2 = int(input("Entre ponto de y: "))

      bresenham(x1, y1, x2, y2)
  else:
    print ('''Opção inválida!!
    Tente Novamente''')
  print('-------------------------------------------')
  print('Programa finalizado!!!!')
