

# [0]Вызывается один раз
import time

def Check_class(Reg=0):# Переменная в Декоратор
    # !!! - Неписать сюда код 
    # [1] Вызываеться столько раз сколько есть Декораторов 
    # Reg - все значения у всех декораторов
    # vars() - locals() = значения переданные в декоратор

    def actual_decorator(func):# Функция под Декоратором
        # !!! - Неписать сюда код
        # [2] Вызываеться столько раз сколько есть Декораторов
        # func.__name__ - Все идентификаторы функций 
        # vars() - locals() - {'func':'<function>','Reg':'_'}

        def decorator_function(*Items, **Dicts):
            # Писать сюда
            # [3] Вызыввается при обращение к Декоратору
            # {'Items':'()','Dicts':'{}','Reg':'_','func':'<function>'}


            return func(*Items, **Dicts)
        return decorator_function
    return actual_decorator





if __name__ == '__main__':
    quit()


"""
print(dir(func))
print(func.__annotations__)# описание def Audio_VK(vk_sessions:vk_api.vk_api.VkApi):
#print(func.__name__)# имя функции
#print(func.__kwdefaults__)# все стандартные значения  функции
#print(func.__globals__)#  Словарь, определяющий глобальное пространство имен
#print(dir(func.__eq__))#?
#print(func.__doc__)# Строка документирования
#print(func.__dict__)# Словарь, содержащий атрибуты функции
#print(dir(func.__delattr__))# ?
#print(func.__defaults__) # Кортеж с аргументами по умолчанию
#print(dir(func.__code__))# не надо
#print(func.__class__)# прсто класс
#print(dir(func.__call__)) # ?
"""
