from appearance.table import show_graph
from random import randint
import subprocess

dictionary = {'a':randint(0,1), 'b':randint(0,1), 'c':randint(0,1)}


subprocess.run(['cls'], shell=True)

show_graph(dictionary, {'a':'c', 'b':'a', 'c':'b'})

""" 

Linhas = de onde a seta sai

Colunas = para onde ela vai

 """
