#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
import INSTALL_LIB
z = INSTALL_LIB.INSTALL_LIB(
    {'all': {'requests': 'requests',
             'vk-api': 'vk-api',
             },
     })
if not z or isinstance(z, dict):print(z);quit()
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

import os
import re
import requests
import vk_api
from vk_api.audio import VkAudio


def save_Audio(name: str, url: str):
	"""
	Скачивание муызки по прямой ссылки
	"""
    if not isinstance(name, str) or not isinstance(url, str):
        return False
    #_________________________________________________#
    name = '_'.join(re.findall(re.compile('[а-яА-Яa-zA-Z0-9]+'), name))
    if not 'Audio' in os.listdir():
        os.mkdir('Audio')

    if not f'{name}.mp3' in os.listdir('Audio'):
        with open(f'Audio//{name}.mp3', "wb") as file:
            file.write(requests.get(url).content)
        return True

    else:
        return False


def search_aidio(REG, vk_session, name: str, count: int):
    if not isinstance(REG, str):
        return False
    if not isinstance(vk_session, vk_api.vk_api.VkApi):
        return False
    if not isinstance(name, str):
        return False
    if not isinstance(count, int):
        return False
    #_________________________________________________#

    """
	Поиск аудио записей из общего поиска вк
	или из плей листа пользователя 
	"""
    vkaudio = VkAudio(vk_session)
    if REG == 'all':
        search_111 = []
        for x in vkaudio.search(name, count):
            search_111.append((x['artist'], x['title'], x['url']))
        return search_111

    elif REG == 'id':
        search_111 = []
        if not isinstance(name, int):
            try:
                name = int(name)
            except ValueError:
                return False

        for x in enumerate(vkaudio.get_iter(owner_id=name)):
            if x[0] <= count:
                search_111.append((x[1]['artist'], x[1]['title'], x[1]['url']))
            else:
                break
        return search_111


def VK_G0(login, password):
	"""
	Вход в ВК
	"""

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    except requests.exceptions.ConnectionError:
        return False

    return vk_session


def clear_id(name: str):
    if not isinstance(name, str):
        return False
    #_______________________________#
    """
    Отчитска ID вк
    """

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

    else:
        return name


def Search(vk_session, REG: str):
    if not isinstance(REG, str):
        return False
    if not isinstance(vk_session, vk_api.vk_api.VkApi):
        return False
    #______________________________________________________#
    os.system('cls')
    
    i = True
    while i == True:

        if REG == 'all':
            print('-------- All Search --------')
            Name = str(input('Name Audio : '))
            if Name == '<<<':
                os.system('cls')
                return

        elif REG == 'id':
            print('-------- ID Search List --------')
            Name = str(input('ID Audio : '))
            if Name == '<<<':
                os.system('cls')
                return
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
            RES = search_aidio('all', vk_session, Name, Max)

        elif REG == 'id':
            RES = search_aidio('id', vk_session, Name, Max)

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

                    if Nomer1 <= Max:

                        for x in range(Nomer0, Nomer1+1):
                            RES1 = save_Audio(f'{RES[x][0]} {RES[x][1]}', RES[x][2])

                        if RES1:
                            input(f'- {RES1}\n')
                            os.system('cls')

                        elif not RES1:
                            os.system('cls')
                            print('False - Install Before')
                            continue

                    elif Nomer0 > Max:
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
                    if Nomer0 <= Max:
                        RES1 = save_Audio(f'{RES[Nomer0][0]} {RES[Nomer0][1]}', RES[Nomer0][2])

                        if RES1:
                            input(f'- {RES1}\n')
                            os.system('cls')

                        elif not RES1:
                            os.system('cls')
                            print('False - Install Before')
                            continue

                    elif Nomer0 > Max:
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


def Audio_VK(vk_session):
    if not isinstance(vk_session, vk_api.vk_api.VkApi):
        return False
    #______________________________________________________#

    i = True
    while i == True:
        print('-------- Audio VK ----------')
        types = input('Type Search - (help) : ')
        if types == 'help':
            print(
                "\nall - Глабальынй поиск\nid - Поиск по плейлисту пользователя Указать (ID)")
            input()
            os.system('cls')

        elif types == 'all':
            Search(vk_session, 'all')

        elif types == 'id':
            Search(vk_session, 'id')

        else:
            os.system('cls')
            print('False - No command')


if __name__ == '__main__':
    with open('PAW.txt', 'r') as FIL:
        login, password = FIL.read().split(' ')

    vk_session = VK_G0(login, password)
    if vk_session:
        Audio_VK(vk_session)

    if not vk_session:
        print('False - No Internet')
        input()



