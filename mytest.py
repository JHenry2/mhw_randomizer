from rando_config import *
import sys
import os
import subprocess
import random
import shutil
random.seed(seed)

if __name__=="__main__":
    #thunder=1,water=2, ice=3, fire=4, dragon=5
    element_id = [1,2,3,4,5]
    #string atk in bytes, use to locate start of attack array
    atk = bytes.fromhex('41544B00')
    #poison, deadly poison, para, sleep, blast, slime, stun, bleed, miasma
    status_id = [0,1,2,34,5,6,7,8]
    path = os.getcwd()
    editor = path + "\\" + 'test_env' + "\\" +'MHW-Editor.exe'
    clean = path + "\\" + 'clean'
    native = path + "\\" + 'nativepc'

    #messy stuff from my old code
    high=['questData_00601','questData_00605', 'questData_00607','questData_00701','questData_00801','questData_00802','questData_00803']
    base_game= ['questData_00101','questData_00103','questData_00201','questData_00205','questData_00301','questData_00302','questData_00305','questData_00306','questData_00401',
                'questData_00405','questData_00407','questData_00408','questData_00501','questData_00502','questData_00503']
    iceborn=['questData_01101','questData_01102','questData_01201','questData_01202','questData_01203','questData_01301','questData_01302',
            'questData_01303','questData_01304','questData_01305','questData_01401','questData_01402',
            'questData_01403','questData_01405','questData_01502','questData_01503',
            'questData_01504']
    base=['nerg.mib','vaal.mib','teo.mib','kushala.mib','kirin.mib','luna.mib','bazel.mib','jho.mib','azure.mib','black.mib','dodo.mib','diablos.mib','rathalos.mib','odo.mib','legiana.mib',
    'rathian.mib','rado.mib','pukei.mib','tobi.mib','kulu.mib','tzizi.mib','barroth.mib','great jagras.mib','great girros.mib','paolumu.mib','jyura.mib','pink.mib','anjanath.mib','uragaan.mib','lavasioth.mib']

    dlc=['coral.mib','beo.mib','banbaro.mib','acid.mib','glav.mib','tigrex.mib','narga.mib','barioth.mib','savage.mib','brachy.mib',
    'fulgur.mib','ruiner.mib','viper.mib','nightshade.mib','shrieking.mib',
    'ebony.mib','blackveil.mib','seething.mib','gold.mib','silver.mib','brute.mib',
    'rajang.mib','scarred.mib','zin.mib','nami.mib','velk.mib',"stygian.mib",'furious.mib','frostfang.mib','behemoth.mib',]

    em_id = ["em001_00", "em001_01", "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00", "em018_05", "em023_00", "em023_05",
    "em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
    "em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05",
    "em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
    "em115_05", "em116_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00", "em126_00"]
    #leshen em127_00 ?
    #"em102_00",	"em102_01", pukeis?
    em_good_projectiles = ["em013_00", "em024_00",  "em026_00", "em027_00", "em032_01", "em036_00", "em042_00" "em042_05", "em050_00", "em057_00", "em057_01",	 
                           "em100_00", 	"em102_00",	"em102_01", "em115_00", "em124_00",  "em126_00", "em127_00"]                          
    #same as em_id but with most variants removed
    em_has_projectiles = ["em001_00", "em001_01", "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00",  "em023_00", 
    "em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
    "em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05",
    "em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
    "em115_05", "em116_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00", "em126_00"]


    special_arena=bytearray.fromhex("D4 3B 7A EB 03 C2 99 AF")
    challenge_arena=bytearray.fromhex("C7 12 14 83 70 2A EB 43")
    alat_arena=bytearray.fromhex("FE 9E C2 93 DD 92 CA 0D")
    seliana=bytearray.fromhex("A0 62 CB 99 34 FB AC D3")
    forest=bytearray.fromhex("94 6C A8 7D 41 02 48 4F")
    spire=bytearray.fromhex("1A 8D 25 57 CD 6E EE A6")
    coral=bytearray.fromhex("23 8C 88 0D C4 45 D0 60")
    vale=bytearray.fromhex("E5 1C D5 0E 67 A3 5E 0F")
    recess=bytearray.fromhex("C8 6A 73 EA D2 E7 98 02")
    non_arena=[forest, spire, coral, recess, challenge_arena]
    maps=[special_arena, alat_arena, seliana]
    #icemaps=[alat_arena, seliana]
    if opt_arena == False:
        for item in non_arena:
            maps.append(item)
        else:
            temp=[special_arena]
            maps=temp
    murder_quests=['questData_00306.mib','questData_00401.mib','questData_00503.mib', 'questData_00504.mib',]
    murder_monsters=["uragaan.mib", "great jagras.mib", "barroth.mib" , "nerg.mib"]

def edit_monsters():
    """
    unfinished, plan to edit all mosnter params with this function
    """
    for item in em_id:
        mID = item[0:5]
        subID = item[6:8]
        #print(mID)
        #print(subID)
        monster_path= path + "\\" + 'clean' + '\\' + 'em' + "\\" + mID + "\\" +subID
        rage =  monster_path + "\\data\\" + mID + ".dtt_agr"
        hitzones = monster_path +"\\data\\" + mID + ".dtt_epg"
        phys_attacks ="\\collision\\" + mID + ".col"
        if random_phys:
            edit_phys_col(item, phys_attacks, random.choice(element_id), random.choice(status_id))
        else:
            edit_phys_col(item, phys_attacks, 0, 0)
        if random_shell:
            if item in em_has_projectiles:
                #random.choice(em_id)
                replacement = random.choice(em_good_projectiles)
                mID_2 = replacement[0:5]
                while (mID == mID_2):
                    replacement = random.choice(em_good_projectiles)
                    mID_2 = replacement[0:5]
                switch_shells(item, replacement)

def edit_quest():
    files=next(os.walk(clean))[2]
    file_paths=[]
    output_paths=[]
    for item in files:
        file_paths.append(clean +"\\" +'quest\\' + item)
        output_paths.append(native +"\\" +'quest\\' + item)

def decrypt_quest():
    files=next(os.walk(clean + "\\quest"))[2]
    file_paths=[]
    output_paths=[]
    for item in files:
        file_paths.append(clean +"\\" + 'quest\\' + item)
        output_paths.append(clean +"\\" + 'de_quest\\' + item)
       # print(file_paths[-1], output_paths[-1])
        decrypt(file_paths[-1], output_paths[-1])
    #print(output_paths)

def encrypt_quest():
    files=next(os.walk(clean + "\\quest"))[2]
    file_paths=[]
    output_paths=[]
    for item in files:
        file_paths.append(clean +"\\" + 'de_quest\\' + item)
        output_paths.append(clean +"\\" + 'en_quest\\' + item)
       # print(file_paths[-1], output_paths[-1])
        encrypt(file_paths[-1], output_paths[-1])
    #print(output_paths)
    

def edit_phys_col(id, file_path,  element=0, status=0):
    """
    Changes attack attributes to match given element and status, while maintaining stun
    """
    mID = id[0:5]
    subID = id[6:8]
    if subID == "05":
        return()
    original=clean + '\\' + 'em' + "\\" + mID + "\\" +subID + file_path
    new_file = native + '\\em' + '\\' + mID + "\\" + subID + file_path
    
    with open(original, 'rb+') as file:
        # get contents into string, then return to start
        contents = file.read()
    with open(new_file, 'wb+') as file:
        file.write(contents)
        file.seek(0,0)
    with open(new_file, 'rb+') as file:
        #go to the section where attack arr starts
        #print(contents.find(atk))
        file.seek(contents.find(atk))
        file.seek(8,1)
        move_count = int.from_bytes(file.read(1), "big")
        file.seek(10,1)
        #get ready to add status
        for num in range(move_count):
            #element id is at position 39
            file.seek(39,1)
            cur_el=int.from_bytes(file.read(1), "big")
            if cur_el != 0:
                file.seek(-1, 1)
                file.write(element.to_bytes(1, "big"))
            elif (adding_element == True) and (num % element_percent == 0):
                file.seek(-1, 1)
                file.write(element.to_bytes(1, "big"))


            file.seek(3,1)
            file.seek(4,1)

            statpos=file.tell()
            #status assingments
            if(num % status_percent == 0 or num==0) and adding_status:
                for item in range(9):
                    cur_stat=file.read(2)
                    file.seek(-2, 1)
                    if item == status:
                        file.write(bytes.fromhex('C842'))
                    elif(item != 6):
                        file.write(bytes.fromhex('0000'))
                    if item == 6:
                        file.seek(2,1)
                    file.seek(2,1)
            file.seek(statpos+124)
            
def switch_shells(id1, id2):
    """
    takes two monster ids, copies shells from id2 to id1
    """
    mID = id1[0:5]
    subID = id1[6:8]
    mID_2 = id2[0:5]
    subID_2 = id2[6:8]

    path_1=native + '\\' + 'em' + "\\" + mID + "\\" +subID + '\\shell'
    path_2=clean + '\\' + 'em' + "\\" + mID_2 + "\\" +subID_2 + '\\shell' 

    shells_1=[]
    shells_2=[]
   # shells_1 = [path_1 for f in os.scandir(path) if f.is_dir()]
   # shells_2 = [path_2 for f in os.scandir(path) if f.is_dir()]
    for path, subdirs, files in os.walk(path_1):
        for name in files:
            if name.endswith('.shlp'):
                shells_1.append(os.path.join(path, name))
    for path, subdirs, files in os.walk(path_2):
        for name in files:
            if name.endswith('.shlp'):
                shells_2.append(os.path.join(path, name))
    if len(shells_2) == 0:
        print(id2)
        return
    for shell in shells_1:
        replaced=open(shell, 'wb')
        replacer=open(random.choice(shells_2), 'rb+')
        #print(replacer.name)
        shutil.copyfileobj(replacer, replaced)
        replaced.close()
        replacer.close()




def decrypt(file_path, output_path, key=""):
    """
    take file path, decrypt it and send to output path
    """
    clean_path= clean + file_path
    os.system('MHW-Editor.exe ' + '-decrypt ' + file_path + ' ' + output_path)
    return('decrypted\\' + file_path)

def encrypt(file_path, output_path):
    os.system('MHW-Editor.exe ' + '-decrypt ' + file_path + ' ' + output_path)
    return(output_path)
            
def main():
    #edit_monsters()
    #edit_quest()
    decrypt_quest()
    encrypt_quest()
    print('done')

main()