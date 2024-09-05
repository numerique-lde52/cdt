'''
Voici le principe d'encodage :

    Le message en entrée est constitué de caractères ASCII (7 bits)
    Le message encodé en sortie est constitué de blocs de 0
    Un bloc est séparé d'un autre bloc par un espace
    Deux blocs consécutifs servent à produire une série de bits de même valeur (que des 1 ou que des 0) :
    - Premier bloc : il vaut toujours 0 ou 00. S'il vaut 0 la série contient des 1, sinon elle contient des 0
    - Deuxième bloc : le nombre de 0 dans ce bloc correspond au nombre de bits dans la série
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
message = "CC" # input()

bin_string = ""
for letter in message:
    l_ascii_code = ord(letter)
    l_binary_code = str(bin(l_ascii_code)[2:])
    bin_string = bin_string + l_binary_code

print(bin_string, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
blocks = ""

def get_unary_code(bin_value):
    return "0" if bin_value == "1" else "00"

current_value = get_unary_code(l_binary_code[0])
count = 1

for v in range(1, len(bin_string)):
    print(bin_string[v], file=sys.stderr, flush=True)
    if bin_string[v] == bin_string[v-1]:
        count += 1
        print("count = " + str(count), file=sys.stderr, flush=True)
    else:
        blocks = blocks + current_value + " " + ("0" * count) + " "
        current_value = get_unary_code(bin_string[v])
        count = 1

    blocks = blocks + current_value + " " + ("0" * count) + " "

print(blocks.strip())