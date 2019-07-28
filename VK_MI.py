#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
import INSTALL_LIB
z = INSTALL_LIB.INSTALL_LIB(
    {'all': {'requests': 'requests',
             'vk-api': 'vk-api',
             },
     })
if not z or isinstance(z, dict):print(z);quit()
#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

from vk_api.audio import VkAudio
import vk_api
import requests
import os
import re


def save_Audio(name: str, url: str):
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


def search_aidio(vk_session, name: str, count: int):
    if not isinstance(vk_session, vk_api.vk_api.VkApi) or not isinstance(name, str) or not isinstance(count, int):
        return False
    #_________________________________________________#

    vkaudio = VkAudio(vk_session)
    search = vkaudio.search(name, count)

    search_111 = []
    for x in search:
        search_111.append((x['artist'], x['title'], x['url']))
    return search_111


def VK_G0():
    with open('PAW.txt', 'r') as FIL:
        login, password = FIL.read().split(' ')

    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    return vk_session


vk_session = VK_G0()

i = True
while i == True:
	print('-------- Audio VK ----------')
	Name = str(input('Name Audio : '))
	Max = int(input('Max : '))
	RES = search_aidio(vk_session, Name, Max)
	print('--------------------')
	for x in enumerate(RES):
		print(f'{x[0]} - {x[1][0]} = {x[1][1]}', end='\n')
	print('--------------------')
	Nomer = int(input('Nomer : '))
	RES1 = save_Audio(f'{RES[Nomer][0]} {RES[Nomer][1]}', RES[Nomer][2])
	if RES1:input(f'{RES1}\n')
	else: i = False
	os.system('cls')

