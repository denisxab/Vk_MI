# -*- coding: utf-8 -*-
"""
Скачивание музыки из ВК
"""
# pylint: disable=C0103

import os
import re
import requests
import vk_api
from vk_api.audio import VkAudio
from Check_class.Check_class import Check_class
import concurrent.futures
import Search_vk


def save_audio_os(name: str, url: str):
    """
    Скачивание муызки по прямой ссылки
    """
    #_________________________________________________#
    name = '_'.join(re.findall(re.compile('[а-яА-Яa-zA-Z0-9]+'), name))
    if not 'Audio' in os.listdir():
        os.mkdir('Audio')

    if not f'{name}.mp3' in os.listdir('Audio'):
        with open(f'Audio//{name}.mp3', "wb") as file:
            file.write(requests.get(url).content)
        return True

    return False


@Check_class(0)
def Entrance_VK(logins: str, passwords: str)-> True:
    """
    Вход в ВКs
    """

    vk_sessions = vk_api.VkApi(logins, passwords)
    try:
        vk_sessions.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    except requests.exceptions.ConnectionError:
        return False

    del logins, passwords
    return vk_sessions


def Pred_dowload(item_dowload: tuple):

    RES1 = save_audio_os(item_dowload[0], item_dowload[1])

    if RES1:
        return f'{item_dowload[0]} - True'

    elif not RES1:
        return f'{item_dowload[0]} - False - Install Before'


@Check_class(0)
def Search(vk_sessions: vk_api.vk_api.VkApi, REG: str):
    """
    Цикл поиск Вк
    """

    #______________________________________________________#
    # os.system('cls')

    while True:  # pylint: disable=R1702
        if REG == 'all':
            print('-------- All Search --------')
            Name = str(input('Name Audio : '))
            if Name == '<<<':
                os.system('cls')
                return False

        elif REG == 'id':
            print('-------- ID Search List --------')
            Name = str(input('ID Audio : '))

            if Name == '<<<':
                os.system('cls')
                return False

            if Name == 'my':
                Name = vk_session.token['user_id']

            else:
                Name = Search_vk.clear_id(Name)

            if Name:
                print(f'ID = {Name}')
                Name = str(Name)

            elif not Name:
                os.system('cls')
                print('False - No ID int')
                continue

        try:
            Max = int(input('Max : '))
        except ValueError:
            os.system('cls')
            print('False - Max is int')
            continue

        if REG == 'all':
            RES = Search_vk.search_aidio('all', vk_sessions, Name, Max)

        elif REG == 'id':
            RES = Search_vk.search_aidio('id', vk_sessions, Name, Max)

        print('--------------------')
        if RES:
            for x in enumerate(RES):
                print(f'{x[0]} - {x[1][0]} = {x[1][1]}', end='\n')
            print('--------------------')

            Nomer = input('Nomer : ').split('-')

            if len(Nomer) == 2:

                try:
                    Nomer0 = int(Nomer[0])
                    Nomer1 = int(Nomer[1])
                except ValueError:
                    os.system('cls')
                    print('False - Nomer is int')
                    continue

                if Nomer0 <= Nomer1:

                    if Nomer1 <= Max:

                        List_dowload = []
                        for x in range(Nomer0, Nomer1+1):
                            List_dowload.append((f'{RES[x][0]} {RES[x][1]}', RES[x][2]))

                        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                            for x in executor.map(Pred_dowload, List_dowload):
                                print(x)

                        # for x in map(Pred_dowload,List_dowload):
                        #     print(x)

                        input('-End\n')
                        os.system('cls')

                    elif Nomer1 >= Max:
                        os.system('cls')
                        print('False - Nomer > Max')
                        continue

                elif Nomer0 > Nomer1:
                    os.system('cls')
                    print('False - Nomer[0] > Nomer[1]')
                    continue

            elif len(Nomer) == 1:
                try:
                    Nomer0 = int(Nomer[0])

                    if Nomer0 < Max:
                        RES1 = save_audio_os(f'{RES[Nomer0][0]} {RES[Nomer0][1]}', RES[Nomer0][2])

                        if RES1:
                            input(f'- {RES1}\n')
                            os.system('cls')

                        elif not RES1:
                            os.system('cls')
                            print('False - Install Before')
                            continue

                    elif Nomer0 >= Max:
                        os.system('cls')
                        print('False - Nomer0 > Max')
                        continue

                except ValueError:
                    os.system('cls')
                    print('False - Nomer is int')
                    continue

        if not RES:
            os.system('cls')
            print('False - No Audio')

    return False


@Check_class(0)
def Audio_VK(vk_sessions: vk_api.vk_api.VkApi)-> True:
    """
    Проводник к Search
    """
    #______________________________________________________#

    while True:
        print('-------- Audio VK ----------')
        types = input('Type Search - (help) : ')
        if types == 'help':
            print(
                "\nall - Глобальный поиск\nid - Поиск по плейлисту пользователя Указать (ID)\
                \nВернуться обратно - '<<<' ")
            input()
            os.system('cls')

        elif types == 'all':
            Search(vk_sessions=vk_sessions, REG='all')

        elif types == 'id':
            Search(vk_sessions=vk_sessions, REG='id')

        else:
            os.system('cls')
            print('False - No command')

    return False


if __name__ == '__main__':

    with open('PAW.txt', 'r') as FIL:
        login_VK, password_VK = FIL.read().split(' ')
        if login_VK == '*' or password_VK == '*':
            print('Введите логин и пороль в PAW.txt')
            login_VK = input("Login: ")
            password_VK = input("Passwords: ")
            os.system('cls')

        vk_session = Entrance_VK(login_VK, password_VK)
        del login_VK, password_VK

    if vk_session:
        Audio_VK(vk_sessions=vk_session)

    if not vk_session:
        print('False - No Internet')
        input()
        quit()
