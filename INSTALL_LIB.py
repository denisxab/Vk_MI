# -*- coding: utf-8 -*-
import os
import re
import pip._internal.utils.misc as pip
import sys


#########################################


def insatll_lib(name: str):
    if not isinstance(name, str):return False
    #____________________________________________#
    command = f'pip install {name}'
    cash_text = re.findall(re.compile('[^\n-- ]+'), os.popen(command).read())

    if cash_text[0] == 'Requirement':
        return True

    elif cash_text[0] == 'Collecting':
        return False


def chek_libs(list_libr: dict):
    if not isinstance(list_libr, dict):return False
    #____________________________________________#
    installed_packages_list = sorted(
        ["%s" % i.key for i in pip.get_installed_distributions()])
    return_list = {'ERROR': []}

    for x in list_libr.items():

        if x[0] in installed_packages_list:
            continue

        if not x[0] in installed_packages_list:
            res = (insatll_lib(f'{x[1]}'))
            if not res:
                return_list['ERROR'].append({x[0]: x[1]})

    return True if not return_list['ERROR'] else return_list


def INSTALL_LIB(list_libr: dict):

    # print(help(INSTALL_LIB.INSTALL_LIB))
    """
    #__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#
    import INSTALL_LIB
    z = INSTALL_LIB.INSTALL_LIB(
        {'all': {'requests': 'requests'},
        })
    if not z or isinstance(z, dict): print(z);quit()
    #__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#__#

    {
    'all': {'requests': 'requests'},   # all для всех платформ
    '64bit': {'requests': 'requests'}, # Windows 64bit
    '32bit': {'requests': 'requests'}, # Windows 32bit
    'linux': {'requests': 'requests'}, # Linux
    'darwin': {'requests': 'requests'} # MacOS
    }
    """

    if not isinstance(list_libr, dict):return False

    #____________________________________________#
    try:
        if list_libr['all']:
            bit64 = bit32 = linux = darwin = list_libr['all']

    except KeyError:
        try:
            bit64 = list_libr['64bit']
        except KeyError:
            return 'Error 64bit'

        try:
            bit32 = list_libr['32bit']
        except KeyError:
            return 'Error 32bit'

        try:
            linux = list_libr['linux']
        except KeyError:
            return 'Error linux'

        try:
            darwin = list_libr['darwin']
        except KeyError:
            return 'Error darwin'

    if sys.platform == 'win32':  # Windows
        import platform

        if platform.architecture()[0] == '64bit':  # Windows x64
            res = chek_libs(bit64)

        if platform.architecture()[0] == '32bit':  # Windows x32
            res = chek_libs(bit32)

    elif sys.platform == 'linux':  # Linux
        res = chek_libs(linux)

    elif sys.platform == 'darwin':  # MacOS
        res = chek_libs(darwin)

    return res

#########################################

if __name__ == '__main__':
    print(INSTALL_LIB({
        'all': {'requests': 'requests'},
        '64bit': {'requests': 'requests'},
        '32bit': {'requests': 'requests'},
        'linux': {'requests': 'requests'},
        'darwin': {'requests': 'requests'},
    }))

