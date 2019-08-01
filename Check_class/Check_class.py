# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=W0105
# pylint: disable=C0303

"""
Декоратор для проверки типов входящих переменных
"""
import time
import sys

"""
from Check_class import Check_class
@Check_class(1) 
def Entrance_VK(logins:str, passwords:str)-> True:
    pass
Entrance_VK(123,'12312')
"""

def Check_class(Reg=0):
    def actual_decorator(func):
        def decorator_function(*Items, **Dicts):
            """
            Комбенированная проврека
            0.008 Длительность проверки
            """

            if Reg:
                print('___________________________________')
                print(f'Func_Name: {func.__name__}')

                if Dicts:
                    print('**Kargs: {}'.format(['{0}|=|{1}|=|{2}-Байт'.format(x, type(x), sys.getsizeof(x))
                                                for x in Dicts.values()]))
                if Items:
                    print(
                        '*Arg: {}'.format(['{0}|=|{1}|=|{2}-Байт'.format(x, type(x), sys.getsizeof(x)) for x in Items]))

            value_function = func.__annotations__
            if value_function.get('return'):  # отчистка от ->
                value_function.pop('return')

            # Если значения переданы без присваивания - fanc(login,password_VK)
            if Items:
                test_Gen_Items = [x for x in zip(
                    value_function.keys(), Items, value_function.values())]
                for x in test_Gen_Items:
                    if not isinstance(x[1], x[2]):
                        raise Exception(f'\n\n*Args-| {x[0]} != {x[2]}\n')

            # Если присваиваться значение - fanc(passwords=password_VK)
            if Dicts:
                test_Gen_Dicts = [list(x)+[value_function.get(x[0])]
                                  for x in zip(Dicts.keys(), Dicts.values())]
                for x in test_Gen_Dicts:
                    if not isinstance(x[1], x[2]):
                        raise Exception(f'\n\n**Kargs-| {x[0]} != {x[2]}\n')

            if Reg:
                start = time.time()
                func_Time = func(*Items, **Dicts)
                print('Time: {} секунд.'.format(time.time()-start))
                print('-----------------------------------')
                return func_Time

            return func(*Items, **Dicts)
        return decorator_function
    return actual_decorator


if __name__ == '__main__':
    Check_class()
