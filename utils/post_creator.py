import datetime
import time

def zeroformat(num):
    if (num < 10):
        return f'0{num}'
    
    return num

now = datetime.datetime.fromtimestamp(int(time.time()))
nome = input("Escolha um nome para o post:").replace(' ','-')
fileName = f'{now.year}-{zeroformat(now.month)}-{zeroformat(now.day)}-{nome}'

with open(f'../_posts/{fileName}.md','w') as file:
    header  =   ""
    header  +=  "---\n"
    header  += f'layout:    post\n'
    header  += f'title:    "{nome}"\n'
    header  += f'date:  {now.isoformat()}\n'
    header  +=  "---\n"
    file.write(header)