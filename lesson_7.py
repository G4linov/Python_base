import os

for i in range(0, 100):
    with open(f'text_{i}.txt', 'w') as f:
        f.write(str(i**10))

#print(os.listdir())

os.makedirs('data', exist_ok=True)
#os.mkdir('data/odd_num')
#os.mkdir('data/even_num')

os.makedirs('copy_data/odd_num', exist_ok=True)
os.makedirs('copy_data/even_num', exist_ok=True)
print(sorted(os.listdir('data')))