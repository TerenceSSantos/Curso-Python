# import math
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor de um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O valor do seno é {:.1f} \ndo cosseno é {:.1f} \ne da tangente é {:.1f}'.format(seno, cosseno, tangente))