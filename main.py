#Задание 1.
#Условие:
#Написать функцию на Python, которой передаются в качестве параметров команда и текст.
#Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
#и False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
#Задание 2. (повышенной сложности)
#Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
#в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из с
#писка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе**


import string
import subprocess


def my_func(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out:
        return True
    return False

def my_func_without_marks(command, word):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout.translate(str.maketrans('', '', string.punctuation))
    if word in out:
        print(out)
        return True
    return False



if __name__ == '__main__':
    print(my_func("cat /etc/os-release", "VERSION_CODENAME"))
    print(my_func_without_marks("cat /home/user/test.txt", "Караул"))


