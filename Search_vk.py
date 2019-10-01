
import os
import re
import requests
import vk_api
from vk_api.audio import VkAudio
from Check_class.Check_class import Check_class


@Check_class(0)
def search_aidio(Choice_fanc: str, vk_sessions: vk_api.vk_api.VkApi, name: str, count: int):
    """
    Поиск аудио записей из общего поиска вк
    или из плей листа пользователя
    """
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


@Check_class(0)
def clear_id(name: str):
    """
    Отчитска ID вк
    """
    #_______________________________#

    name = re.findall(re.compile("\\w+(?![https://vk.com/])"), name)[0]
    list_name = list(name)
    if list_name[0] == 'i' and list_name[1] == 'd':  # pylint: disable=R1705
        list_name.pop(0)
        list_name.pop(0)
        return ''.join(list_name)

    else:
        iad = re.findall(re.compile('[a-z]'), name)
        if iad:
            return False
        if not iad:
            return ''.join(name)

    return False


@Check_class(0)
def save_id(name_id:int,REG:bool):

    # Запись в файл
    if REG == True:
        with open("id_save.txt","w") as id_txt:
            id_txt.write(f'{name_id}')

    # Чтение из файла
    if REG == False:
        try:
            with open("id_save.txt","r") as id_txt:
                name_id = id_txt.read()

        except FileNotFoundError:
            with open("id_save.txt","w") as id_txt:
                pass

    return str(name_id)
