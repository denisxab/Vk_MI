# -*- coding: utf-8 -*-
"""
Скачивание музыки из ВК
"""
# pylint!: disable=C0103
# pylint!: disable=R1702
# pylint!: disable=R0911

def save_audio_os(name: str, url: str):
    """
    Скачивание муызки по прямой ссылки
    """
    if not isinstance(url, str):
        return False
    if not isinstance(name, str):
        return False
    #_________________________________________________#
    name = '_'.join(re.findall(re.compile('[а-яА-Яa-zA-Z0-9]+'), name))
    if not 'Audio' in os.listdir():
        os.mkdir('Audio')

    if not f'{name}.mp3' in os.listdir('Audio'):
        with open(f'Audio//{name}.mp3', "wb") as file:
            file.write(requests.get(url).content)
        return True

    return False


def search_aidio(Choice_fanc, vk_sessions, name: str, count: int):
    """
    Поиск аудио записей из общего поиска вк
    или из плей листа пользователя
    """
    #_________________________________________________#
    if not isinstance(Choice_fanc, str):
        return False
    if not isinstance(vk_sessions, vk_api.vk_api.VkApi):
        return False
    if not isinstance(name, str):
        return False
    if not isinstance(count, int):
        return False
    #_________________________________________________#

    vkaudio = VkAudio(vk_sessions)
    if Choice_fanc == 'all':
        search_111 = []
        for lists_music in vkaudio.search(name, count):
            search_111.append(
                (lists_music['artist'],
                 lists_music['title'],
                 lists_music['url']))
        return search_111

    if Choice_fanc == 'id':
        search_111 = []
        if not isinstance(name, int):
            try:
                name = int(name)
            except ValueError:
                return False

        for lists_music in enumerate(vkaudio.get_iter(owner_id=name)):
            if lists_music[0] <= count:
                search_111.append(
                    (lists_music[1]['artist'],
                     lists_music[1]['title'],
                     lists_music[1]['url']))
            else:
                break
        return search_111

    return False



def Entrance_VK(logins, passwords):
    """
    Вход в ВК
    """

    vk_sessions = vk_api.VkApi(logins, passwords)
    try:
        vk_sessions.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    except requests.exceptions.ConnectionError:
        return False

    return vk_sessions


def clear_id(name: str):
    """
    Отчитска ID вк
    """
    if not isinstance(name, str):
        return False
    #_______________________________#

    name = name.split('/')

    if len(name) != 1:
        name = name[3].split('id')

        if len(name) == 2:
            name = name[1]
        else:
            name = name[0]

    else:
        name = name[0]

    if re.findall(re.compile('[a-z]'), name):
        return False

    return name



def Search(vk_sessions, REG: str):
    """
    Цикл поиск Вк
    """
    if not isinstance(REG, str):
        return False
    if not isinstance(vk_sessions, vk_api.vk_api.VkApi):
        return False
    #______________________________________________________#
    os.system('cls')

    while True:

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
            Name = clear_id(Name)

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
            RES = search_aidio('all', vk_sessions, Name, Max)

        elif REG == 'id':
            RES = search_aidio('id', vk_sessions, Name, Max)

        print('--------------------')
        if RES:
            for x in enumerate(RES):
                print(f'{x[0]} - {x[1][0]} = {x[1][1]}', end='\n')
            print('--------------------')

            Nomer = input('Nomer : ').split('-')
            print(Nomer)

            if len(Nomer) == 2:

                try:
                    Nomer0 = int(Nomer[0])
                    Nomer1 = int(Nomer[1])
                except ValueError:
                    os.system('cls')
                    print('False - Nomer is int')
                    continue

                if Nomer0 < Nomer1:

                    if Nomer1 < Max:

                        for x in range(Nomer0, Nomer1+1):

                            RES1 = save_audio_os(f'{RES[x][0]} {RES[x][1]}', RES[x][2])
                            if RES1:
                                print(f'{x} - True')
                            elif not RES1:
                                print(f'{x} - False - Install Before')
                        input(f'- {RES1}\n')
                        os.system('cls')

                    elif Nomer1 >= Max:
                        os.system('cls')
                        print('False - Nomer > Max')
                        continue

                elif Nomer0 < Nomer1:
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

def Audio_VK(vk_sessions):
    """
    Проводник к Search
    """
    if not isinstance(vk_sessions, vk_api.vk_api.VkApi):
        return False
    #______________________________________________________#

    while True:
        print('-------- Audio VK ----------')
        types = input('Type Search - (help) : ')
        if types == 'help':
            print(
                "\nall - Глабальынй поиск\nid - Поиск по плейлисту пользователя Указать (ID)\
                \nВернуться обрато - '<<<' ")
            input()
            os.system('cls')

        elif types == 'all':
            Search(vk_sessions, 'all')

        elif types == 'id':
            Search(vk_sessions, 'id')

        else:
            os.system('cls')
            print('False - No command')
    return False

def Test_install_libs():
    """
    Проверка устоновелнных библиотек
    """
    #__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
    import INSTALL_LIB
    Modules = INSTALL_LIB.INSTALL_LIB({
        'all': {'requests': 'requests',
                'vk-api': 'vk-api',
                },
    })
    if not Modules or isinstance(Modules, dict):
        print(Modules)
        quit()

    #__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

if __name__ == '__main__':
    Test_install_libs()
    import os
    import re
    import requests
    import vk_api
    from vk_api.audio import VkAudio

    with open('PAW.txt', 'r') as FIL:
        login, password = FIL.read().split(' ')
        vk_session = Entrance_VK(login, password)

    if vk_session:
        Audio_VK(vk_session)

    if not vk_session:
        print('False - No Internet')
        input()
