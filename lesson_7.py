from datetime import datetime
import os
import shutil
import datetime

#for i in range(0, 100):
#    with open(f'text_{i}.txt', 'w') as f:
#        f.write(str(i**10))

#print(os.listdir())

#os.makedirs('data', exist_ok=True)
#os.mkdir('data/odd_num')
#os.mkdir('data/even_num')

#os.makedirs('copy_data/odd_num', exist_ok=True)
#os.makedirs('copy_data/even_num', exist_ok=True)
print(sorted(os.listdir('data')))
EVEN_PATH = 'data/even_num'
ODD_PATH = 'data/odd_num'

txt_files = [file for file in os.listdir() if file.endswith('.txt')]

#file_tuple = [el for el in os.walk('data')]
#files = [el[2] for el in file_tuple if el != []]
#txt_files = []
#for el in files:
#    txt_files.extend(el)

for file in txt_files:
    num = file.split('_')[1][:-4]
    if int(num) % 2 == 0:
        #os.replace(file, f'data/even_num/{file}')
        os.replace(file, os.path.join(EVEN_PATH, file))
        #os.rename(os.path.join(EVEN_PATH, file), file)
    else:
        os.replace(file, os.path.join(ODD_PATH, file))
        #os.rename(os.path.join(ODD_PATH, file), file)

#os.rmdir('data/copy_data/odd_num')

#shutil.rmtree('data/copy_data')
#shutil.move('copy_data', 'data')

print(oct(os.stat('data').st_mode)[-3:])
print(datetime.datetime.fromtimestamp(os.stat('data').st_atime))
print(os.stat('data').st_size)

shutil.copy('data/even_num/text_0.txt', 'copy_data/even_num')

print(datetime.datetime.fromtimestamp(os.stat('data/even_num/text_0.txt').st_atime))
print(datetime.datetime.fromtimestamp(os.stat('data/even_num/text_0.txt').st_mtime))

print(datetime.datetime.fromtimestamp(os.stat('copy_data/even_num/text_0.txt').st_atime))
print(datetime.datetime.fromtimestamp(os.stat('copy_data/even_num/text_0.txt').st_mtime))