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
    status_id = [0,1,2,3,4,5,6,7,8]
    spam_receivers=[]
    spam_senders=[]
    all_shells=[]

    path = os.getcwd()
    editor = path + "\\" + 'test_env' + "\\" +'MHW-Editor.exe'
    clean = path + "\\" + 'clean'
    native = path + "\\" + 'nativepc'

    #messy stuff from my old code
    high=['00601','00605', '00607','00701','00801','00802','00803']
    base_game= ['00101','00103','00201','00205','00301','00302','00305','00306','00401',
                '00405','00407','00408','00501','00502','00503']
    iceborn=['01101','01102','01201','01202','01203','01301','01302',
            '01303','01304','01305','01401','01402',
            '01403','01405','01502','01503',
            '01504']
    base=[7, 9, 10, 1, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39]
    print(base)
    base_done=len(base)-24
    dlc=[87, 88, 89, 90, 91, 93, 94, 95, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,  92, 100]
    if mixed==True:
        base.extend(dlc)
        random.shuffle(base)
    else:
        random.shuffle(base)

   # em_to_id={"em001_00": 9, "em001_01" : 10, "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00", "em018_05", "em023_00", "em023_05",
   # "em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
    #"em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05",
    #"em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
    #"em115_05", "em116_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00", "em126_00"]}

    em_id = ["em001_00", "em001_01", "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00", "em018_05", "em023_00", "em023_05",
    "em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
    "em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05",
    "em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
    "em115_05", "em116_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00", "em126_00"]
    #leshen em127_00 ?
    #"em102_00",	"em102_01", pukeis? frostfang? "em42_05"

    #needs to be tested
    #em_good_projectiles = ["em013_00", "em024_00",  "em026_00", "em027_00", "em032_01",
    #                       "em036_00", "em050_00", "em057_00", "em057_01",	 
    #                       "em100_00", "em102_01"] 

    #paused = "em126_00", "em127_00",  "em124_00" # "em042_00", try frostfang instead
    #tested to a mostly working degree
    em_good_projectiles = ["em036_00", "em050_00", "em105_00", "em108_00", "em115_00", "em102_00", 'em042_05']
    # tested, needs garbage filtered might have unlucky crashes
    #em_good_projectiles = ["em027_00"]                       

    #active
    em_good_projectiles=["em036_00", 'em108_00']

    #same as em_id but with most variants removed
    em_has_projectiles = ["em001_00", "em001_01", "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00",  "em023_00", 
    "em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
    "em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05",
    "em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
    "em115_05", "em116_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00"]

    murder_quests=['00306','00401','00503', '00504',]

    murder_monsters=[22, 7, 21 , 25]

    all_maps=[101, 102, 103, 104, 105, 108, 109, 201, 202, 203, 405, 411, 412, 413, 416,]
    unkown_maps=[101, 102, 103, 104, 105]
    known_maps=[ 201, 202, 411, 412, 413]
    maps=[201, 202, 203, 412, 413]
    mute=[203, 411, 412, 413, 416]
    #maps=[413]
    #icemaps=[alat_arena, seliana]
    #if opt_arena == False:
     #   for item in non_arena:
      #      maps.append(item)
       # else:
        #    temp=[special_arena]
         #   maps=temp

def declare_spam():
    global spam_senders  
    spam_senders = [ 'gurt'



    ]   

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
        else:
            if item in em_has_projectiles:
                #random.choice(em_id)
                replacement = random.choice(em_good_projectiles)
                mID_2 = replacement[0:5]

                switch_shells(item, item)

def populate_sh():
    for monster in em_good_projectiles:
        mID = monster[0:5]
        subID = monster[6:8]
        path_2= clean + '\\' + 'em' + "\\" + mID + "\\" + subID + '\\shell' 
        for path, subdirs, files in os.walk(path_2):
            for name in files:
                if name.endswith('.shlp'):
                    all_shells.append(os.path.join(path, name))

def edit_quests():
    #map id at 27
    #monster objective at 91
    #monster spawn at 176
    files=next(os.walk(clean +"\\" + 'de_quest'))[2]
    file_paths=[]

    for item in files:
        if (item.endswith('.mib')):
            file_paths.append(clean +"\\" +'de_quest\\' + item)
        
    for item in file_paths:
        qid=item[-9:]
        qid=qid[0:5]
        if (len(base) == base_done and mixed == False):
            base.extend(dlc)
            random.shuffle(base)
        if(qid in murder_quests):
            for monstie in base:
                if monstie not in murder_monsters:
                    monster=monstie
                    base.remove(monstie)
                    break
        else:
            monster=base.pop(0)
        edit_mib(item, monster)

def edit_mib(path, monster):
    output_path = native +"\\" +'quest\\' + path[-19:]
    if size:
        my_size=random.randrange(min_size, max_size)
    else:
        my_size=100
    #print(path)
    #print(output_path)
    eighteen=24
    zero=0
    my_map=random.choice(maps)
    with open(path, 'rb+') as file:
        file.seek(27)
        file.write(my_map.to_bytes(2, "little"))
        if my_map in mute:
            file.seek(124)
            file.write(eighteen.to_bytes(1, 'little'))
        else:
            file.seek(124)
            file.write(zero.to_bytes(1, 'little'))
        file.seek(91)
        file.write(monster.to_bytes(1, 'little'))
        file.seek(176)
        file.write(monster.to_bytes(1, 'little'))
        file.seek(205)
        file.write(my_size.to_bytes(1, 'little'))

    encrypt(path, output_path)


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

def decrypt_shells():
    """
    very slow, exists only for science
    """
    file_paths=[]
    for path, subdirs, files in os.walk(clean + "\\em"):
        for name in files:
            if name.endswith('.shlp'):
                file_paths.append(os.path.join(path, name))
    for item in file_paths:
        decrypt(item, item+"_de")
        print('decrypted something')

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
    zero=0

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
        move_count = int.from_bytes(file.read(4), "little")
        file.seek(4,1)
        #get ready to add status
        for num in range(move_count):
            #element id is at position 39
            file.seek(36,1)
            cur_el=int.from_bytes(file.read(1), "little")
            if cur_el != 0:
                file.seek(-1, 1)
                file.write(element.to_bytes(4, "little"))
            elif (adding_element == True) and (num % element_percent == 0):
                file.seek(-1, 1)
                file.write(element.to_bytes(4, "little"))
            else:
                file.seek(-1, 1)
                file.write(zero.to_bytes(4, "little"))                

            file.seek(8,1)

            statpos=file.tell()
            #status assingments
            if(num % status_percent == 0 or num==0) and adding_status:
                for item in range(9):
                    file.seek(2,1)
                    cur_stat=file.read(2)
                    file.seek(-2, 1)
                    if item == status:
                        file.write(bytes.fromhex('C842'))
                    elif(item != 6):
                        file.write(bytes.fromhex('0000'))
                    if item == 6:
                        file.seek(2,1)
            file.seek(statpos+123)
            
def switch_shells(id1, id2):
    """
    takes two monster ids, copies shells from id2 to id1
    """
    loud=False
    mID = id1[0:5]
    subID = id1[6:8]
    #id2=id1 # for fixing fuckups
    mID_2 = id2[0:5]
    subID_2 = id2[6:8]

    print(mID + subID + " " +mID_2 + subID_2)
    #debug, set to monster problems are happening with
    if(id1 == 'em026_00'):
        pass
        loud=True
        #random.seed('anus')
        #id2='em042_05'
        #mID_2 = id2[0:5]
        #subID_2 = id2[6:8]
    path_1=native + '\\' + 'em' + "\\" + mID + "\\" +subID + '\\shell'
    path_2= clean + '\\' + 'em' + "\\" + mID_2 + "\\" +subID_2 + '\\shell' 

    shells_1=[]
    shells_2=[]
    if mixed_shell==False:
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
        for index, shell in enumerate(shells_1):
            gurt=random.choice(shells_2)

            #print(replacer.name)
            #shutil.copy(shells_2[index], shell)
            if (id1 != id2):
                shutil.copy(gurt, shell)
            else:
                shutil.copy(shells_2[index], shell)
            #shutil.copyfileobj(replacer, replaced)
            if loud:
                #print(shell)
                #print(gurt)
                pass
    else:
        for path, subdirs, files in os.walk(path_1):
            for name in files:
                if name.endswith('.shlp'):
                    shells_1.append(os.path.join(path, name))
        for index, shell in enumerate(shells_1):
            gurt=random.choice(all_shells)
            myID = gurt[-13:-8]
            if(len(myID) != 5):
                print(myID)
            while(myID == mID):
                    gurt=random.choice(all_shells)
                    myID = gurt[-13:-8]
            
            shutil.copy(gurt, shell)
            #shutil.copyfileobj(replacer, replaced)
            if loud:
                #print(shell)
                #print(gurt)
                pass

def rename_sobj():
    file_paths=[]
    output_paths=[]
    for path, subdirs, files in os.walk(os.getcwd() +"\\" + 'test_env\\sobj'):
        for name in files:
            file_paths.append(os.path.join(path, name))
            output_paths.append(os.path.join(path, name[0:-11]+'203_00.sobj'))
    for index, file in enumerate(file_paths):
        os.rename(file, output_paths[index])

def truncate_sobj():
    """
    removes desire setter data from sobjs
    """
    file_paths=[]
    zero=0
    one=1
    for path, subdirs, files in os.walk(native +"\\" + 'quest\\enemy\\boss'):
        for name in files:
            file_paths.append(os.path.join(path, name))
    for file in file_paths:
        with open(file, 'rb+') as f:
            f.seek(20)
            f.write(one.to_bytes(1, 'little'))
            f.seek(403)
            f.truncate()


def update_sobjl(sobjl, n_sobjl):
    """
    only works for replacing 3 characters
    """
    path = native + "\\quest\\enemy\\zako\\" + sobjl
    #how many entries
    count=59
    with open(path, 'rb+') as file:
        file.seek(52)
        file.write(n_sobjl.encode(encoding='ascii'))
        for x in range(count):
            file.seek(48,1)
            file.write(n_sobjl.encode(encoding='ascii'))

def get_alnk():
    """
    gets lits of all alnk files
    """
    file_paths=[]
    for path, subdirs, files in os.walk(native +"\\" + 'em'):
        for name in files:
            if(name.endswith('.dtt_alnk')):
                file_paths.append(os.path.join(path, name))
    return file_paths

def edit_alnk(alnk):
    """
    edits alnks to be empty-ish so monsters shouldn't move
    """
    map_count=len(all_maps)
    one=1
    with open(os.getcwd()+'\\dont_move', 'rb+') as f:
        dont_move=f.read()
    for item in alnk:
        with open(item, 'rb+') as f:
            f.seek(40)
            f.write(map_count.to_bytes(4, 'little'))
            for map in all_maps:
                f.write(map.to_bytes(4, 'little'))
                f.write(one.to_bytes(4, 'little'))
                f.write(map.to_bytes(4, 'little'))
                if map in known_maps:
                    with open(os.getcwd()+'\\maps\\' + str(map), 'rb+') as file:
                        contents=file.read()
                        f.write(contents)
                else:
                    f.write(dont_move)
            f.truncate()

def clean_data():
    """
    remove most unnecessary files from the data folder
    """
    trash=['.thk', '.actp2']
    file_paths=[]
    for path, subdirs, files in os.walk(native +"\\" + 'em'):
        for name in files:
            for item in trash:
                if(name.endswith(item)):
                    file_paths.append(os.path.join(path, name))

    for item in file_paths:
        os.remove(item)
    
def decrypt(file_path, output_path, key=""):
    """
    take file path, decrypt it and send to output path
    """
    clean_path= clean + file_path
    os.system('MHW-Editor.exe ' + '-decrypt ' + file_path + ' ' + output_path)
    return('decrypted\\' + file_path)

def encrypt(file_path, output_path):
    os.system('MHW-Editor.exe ' + '-encrypt ' + file_path + ' ' + output_path)
    return(output_path)
            
def main():
    populate_sh()
    edit_monsters()
    #decrypt_quest()
    #encrypt_quest()
    edit_quests()
    print('done')

main()

#declare_spam()
#print(spam_senders)

#clean_data()
#(get_alnk())
#truncate_sobj()
#rename_sobj()
#update_sobjl('zako_st203.sobjl', '203')
