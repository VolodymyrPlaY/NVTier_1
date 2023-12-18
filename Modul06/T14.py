"""
РОБОТА З АРХІВАМИ
"""
'''
Створіть функціонал для розпакування архіву.

Зробіть import пакету shutil

Створіть функцію unpack(archive_path, path_to_unpack), 
яка викликатиме метод пакета shutil unpack_archive та 
розпаковуватиме архів archive_path у місце path_to_unpack.

Функція нічого не повертає.

STARTING CODE:

import shutil


def unpack(archive_path, path_to_unpack):
    
'''
#   Ось ваша функція unpack для розпакування архіву за допомогою shutil.unpack_archive:

import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)
#   Ця функція приймає шлях до архіву (archive_path) та шлях, 
#   де треба розпакувати архів (path_to_unpack). 
#   Вона використовує shutil.unpack_archive для розпакування архіву.





