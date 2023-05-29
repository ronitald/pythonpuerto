from intro_modulo import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

from sys import path

path.append('..\\modules')

import intro_modulo

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(intro_modulo.suml(zeroes))
print(intro_modulo.prodl(ones))