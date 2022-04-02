import os
import shutil

'''
OK i know the code is bad but cut me some slack
Its a free program that i made at litterally midnight
Anyways i never liked melon loader so here ya go
'''


try:
    mods_list = os.listdir("./mods")
    l = os.listdir(".")
    wanted = 'Data'

    # using startswith
    result = list(filter(lambda x: x.startswith(wanted), l))

    # using in
    result = list(filter(lambda x: wanted in x, l))

    game_path = f"{result[0]}/Managed"
    dlls = os.listdir(game_path)

    #make copy folder to house original files
    os.system("mkdir Managed-Copy")

    #make backup of all affected files
    for mod in mods_list:
        for i in dlls:
            if mod == i:
                shutil.copy2(f'{game_path}/{i}', 'Managed-Copy')
                os.remove(f'{game_path}/{i}')

    #transfer mods
    for mod in mods_list:
        shutil.copy2(f"mods/{mod}", f"{game_path}")

except:
    print("ERROR application is either broken or needs to be updated.")