#barra de carregamento
import os 
import time

print("\033[?25l", end="")
x = 1    
tamanho, _ = os.get_terminal_size()
tamanho = tamanho - 5
while x <= tamanho - 5:
    bar = chr(9608) * x + f" {x * 100 / tamanho:.0f}"
    print(bar)
    time.sleep(.1)
    os.system('cls')
    x = x + 1
