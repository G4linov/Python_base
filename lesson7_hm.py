import os
import shutil

'''
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
'''

os.makedirs('my_project', exist_ok=True)
os.makedirs('my_project/settgins', exist_ok=True)
os.makedirs('my_project/mainapp', exist_ok=True)
os.makedirs('my_project/adminapp', exist_ok=True)
os.makedirs('my_project/authnapp', exist_ok=True)

'''
 Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
'''

os.makedirs('my_project/templates', exist_ok=True)
os.makedirs('my_project/templates/mainapp', exist_ok=True)
os.makedirs('my_project/templates/authnapp', exist_ok=True)
shutil.copy('my_project/mainapp/base.html', 'my_project/templates/mainapp')
shutil.copy('my_project/mainapp/index.html', 'my_project/templates/mainapp')
shutil.copy('my_project/authnapp/base.html', 'my_project/templates/authnapp')
shutil.copy('my_project/authnapp/index.html', 'my_project/templates/authnapp')

'''
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла
(пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, 
но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
'''

print(os.stat('my_project/authnapp/index.html').st_size)
print(list(os.listdir('my_project/mainapp')))

dev_dict = {0: 0}

size_files = [file for file in os.listdir('my_project/mainapp')]
for el in size_files:
    if os.stat(f'my_project/mainapp/{el}').st_size < 100:
        try:
            dev_dict[100] += 1
        except KeyError:
            dev_dict[100] = 0
            dev_dict[100] += 1

print(dev_dict)