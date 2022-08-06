from cProfile import run
import pandas as pd
from pathlib import Path

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_20_(2008%E2%80%9309)')

# print(simpsons[1])
# print(type(simpsons))

def run():
    directory = input('''
how would be the name of your new directory?:
''')
    Path(f'{directory}').mkdir(parents=True, exist_ok=True)
    for i, table in enumerate(simpsons):
        with open(f'./{directory}/{i}-table.txt', 'w', encoding='utf-8') as f:
            f.write(str(table))


if __name__ == '__main__':
    run()