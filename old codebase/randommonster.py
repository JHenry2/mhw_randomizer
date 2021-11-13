import random
import os
import fileinput
import sys
import shutil

beh_low_attack=bytearray.fromhex("D6 96 BB B3 DB 06 51 A7")
beh_high_attack=bytearray.fromhex("D6 96 BB B3 DB 06 51 A7")
beh_G_attack=bytearray.fromhex("1D 16 A0 EC 25 1B 94 AE")

monsters_in_run=[]

#speeds 1.05 to 1.20

#bytearray.fromhex("66 66 86"), bytearray.fromhex("CD CC 8C"),bytearray.fromhex("33 33 93"),
#bytearray.fromhex("9A 99 99"),

#speeds listed in intervals of 5% starting from 1.05 and ending at 1.50
speeds=[bytearray.fromhex("00 00 A0"),bytearray.fromhex("66 66 A6"),
        bytearray.fromhex("CD CC AC"), bytearray.fromhex("33 33 B3"),bytearray.fromhex("9A 99 B9"),
        bytearray.fromhex("00 00 C0")]

rank="low"
companion=""

print('Enter random seed')
random.seed(input())

print("Wacky Monster Sizes? y/n")
opt_size=input()
if (opt_size != "y") and (opt_size != "n"):
    print("please enter either y or n")
    sys.exit()
print("Boss Quests? y/n")
opt_boss=input()
if opt_boss != "y" and opt_boss != "n":
    print("please enter either y or n")
    sys.exit()
print("Special Arena only?")
opt_arena=input()
if (opt_arena != "y") and (opt_arena != "n"):
    print("please enter either y or n")
print("randomize enraged speed (hyper mode)?")
opt_speed=input()
if (opt_speed != "y") and (opt_speed != "n"):
    print("please enter either y or n")



path=os.getcwd()

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
maps=[special_arena]
icemaps=[alat_arena, seliana]

if opt_arena != "y":
    for item in non_arena:
        maps.append(item)
else:
    temp=[special_arena]
    maps=temp

murder_quests=['questData_00306.mib','questData_00401.mib','questData_00503.mib', 'questData_00504.mib',]

murder_monsters=["uragaan.mib", "great jagras.mib", "barroth.mib" , "nerg.mib"]

iter= ['questData_00101','questData_00103','questData_00201','questData_00205','questData_00301','questData_00302','questData_00305','questData_00306','questData_00401',
'questData_00405','questData_00407','questData_00408','questData_00501','questData_00502','questData_00503']

high=['questData_00601','questData_00605', 'questData_00607','questData_00701','questData_00801','questData_00802','questData_00803']

boss=['questData_00504.mib','questData_00804.mib']
iceboss=['questData_01306.mib','questData_01404.mib','questData_01501.mib','questData_01601.mib','questData_01602.mib']

iter2=['questData_01101','questData_01102','questData_01201','questData_01202','questData_01203','questData_01301','questData_01302',
'questData_01303','questData_01304','questData_01305','questData_01401','questData_01402',
'questData_01403','questData_01405','questData_01502','questData_01503',
'questData_01504']

music_dmc=bytearray.fromhex("A5 62 69 8E 44 47 11 5D")
music_default=bytearray.fromhex("D6 96 BB B3 DB 06 51 A7")
#heac, chest, arms, tasset, waist descending order
#male=False
#armor=False

size=["60.mib","70.mib","80.mib","90.mib","100.mib","110.mib",
      "120.mib","130.mib","140.mib"
     ]
wacky_sizes=["40.mib","50.mib","150.mib","160.mib"]
if opt_size == "y":
    for item in wacky_sizes:
        size.append(item)

head=['166','167','174','175','179','180','181','182','183','184','191','192','193','194','195','196','197','226','231']
chest=['621','622','629','630','670','675']
arms=['1469','1470','1477','1488','1505','1506','1507','1508','1523']
waist=['1047','1048','1083','1084','1085','1086','1096','1101']
pants=['1891','1892','1899','1900','1927','1928','1929','1930','1945']

gs=['150','151','152','153','154','155','156','240']
sns=['219','220','222','224','225,''239','261']
ds=['225','226','227','231','232','233','234','237','238','247','269']
ls=['223','224','226','243']
ham=['221','222','223','224','235','238','239','240','245']
hh=['212','213','214','216','217','218','220','221','235']
lan=['236']
gl=['220','221','240']
cb=['215','216','232','233','234','256']
sa=['228','229','243']
ig=['221','222','245','267']
bow=['238']
lbg=['240']
hbg=['227']
#armors
for item in range(32,100):
    head.append(str(item))
for item in range(104,129):
    head.append(str(item))
for item in range(134,146):
    head.append(str(item))
for item in range(202,210):
    head.append(str(item))
for item in range(503,569):
    chest.append(str(item))
for item in range(573,601):
    chest.append(str(item))
for item in range(634,640):
    chest.append(str(item))
for item in range(646,661):
    chest.append(str(item))
for item in range(1353,1417):
    arms.append(str(item))
for item in range(1421,1449):
    arms.append(str(item))
for item in range(1482,1488):
    arms.append(str(item))
for item in range(1492,1501):
    arms.append(str(item))
for item in range(929,995):
    waist.append(str(item))
for item in range(999,1027):
    waist.append(str(item))
for item in range(1060,1066):
    waist.append(str(item))
for item in range(1072,1079):
    waist.append(str(item))
for item in range(1773,1839):
    pants.append(str(item))
for item in range(1843,1871):
    pants.append(str(item))
for item in range(1904,1910):
    pants.append(str(item))
for item in range(1916,1923):
    pants.append(str(item))

#GS
for item in range(158,166):
    gs.append(str(item))
for item in range(167,198):
    gs.append(str(item))
for item in range(199,209):
    gs.append(str(item))
for item in range(210,216):
    gs.append(str(item))
for item in range(217,221):
    gs.append(str(item))
for item in range(229,236):
    gs.append(str(item))
#sns
for item in range(150,160):
    sns.append(str(item))
for item in range(161,201):
    sns.append(str(item))
for item in range(203,209):
    sns.append(str(item))
for item in range(210,218):
    sns.append(str(item))
for item in range(229,236):
    sns.append(str(item))
#DS
for item in range(150,188):
    ds.append(str(item))
for item in range(189,192):
    ds.append(str(item))
for item in range(194,207):
    ds.append(str(item))
for item in range(208,224):
    ds.append(str(item))
for item in range(229,236):
    ds.append(str(item))
#LS
for item in range(150,158):
    ls.append(str(item))
for item in range(160,198):
    ls.append(str(item))
for item in range(200,214):
    ls.append(str(item))
for item in range(215,222):
    ls.append(str(item))
for item in range(230,239):
    ls.append(str(item))
#hammer
for item in range(150,178):
    ham.append(str(item))
for item in range(180,201):
    ham.append(str(item))
for item in range(202,210):
    ham.append(str(item))
for item in range(211,220):
    ham.append(str(item))
for item in range(228,234):
    ham.append(str(item))
#hunting horn
for item in range(150,160):
    hh.append(str(item))
for item in range(162,211):
    hh.append(str(item))
for item in range(225,232):
    hh.append(str(item))
#lance
for item in range(150,172):
    lan.append(str(item))
for item in range(173,196):
    lan.append(str(item))
for item in range(197,203):
    lan.append(str(item))
for item in range(204,215):
    lan.append(str(item))
for item in range(216,221):
    lan.append(str(item))
for item in range(224,232):
    lan.append(str(item))
#gunlance
for item in range(150,184):
    gl.append(str(item))
for item in range(185,188):
    gl.append(str(item))
for item in range(190,199):
    gl.append(str(item))
for item in range(200,207):
    gl.append(str(item))
for item in range(208,219):
    gl.append(str(item))
for item in range(225,234):
    gl.append(str(item))
#charge blade
for item in range(150,156):
    cb.append(str(item))
for item in range(158,196):
    cb.append(str(item))
for item in range(198,214):
    cb.append(str(item))
for item in range(220,226):
    cb.append(str(item))
#switch axe
for item in range(150,162):
    sa.append(str(item))
for item in range(163,179):
    sa.append(str(item))
for item in range(180,192):
    sa.append(str(item))
for item in range(193,200):
    sa.append(str(item))
for item in range(201,211):
    sa.append(str(item))
for item in range(212,222):
    sa.append(str(item))
for item in range(223,227):
    sa.append(str(item))
for item in range(233,239):
    sa.append(str(item))
#insect glaive
for item in range(150,156):
    ig.append(str(item))
for item in range(158,166):
    ig.append(str(item))
for item in range(167,191):
    ig.append(str(item))
for item in range(192,220):
    ig.append(str(item))
for item in range(226,234):
    ig.append(str(item))
#bow
for item in range(150,156):
    bow.append(str(item))
for item in range(158,190):
    bow.append(str(item))
for item in range(191,213):
    bow.append(str(item))
for item in range(193,200):
    bow.append(str(item))
for item in range(214,217):
    bow.append(str(item))
for item in range(220,232):
    bow.append(str(item))
for item in range(223,227):
    bow.append(str(item))
for item in range(233,239):
    bow.append(str(item))
#light bowgun
for item in range(150,162):
    lbg.append(str(item))
for item in range(163,177):
    lbg.append(str(item))
for item in range(179,202):
    lbg.append(str(item))
for item in range(203,207):
    lbg.append(str(item))
for item in range(208,215):
    lbg.append(str(item))
for item in range(215,220):
    lbg.append(str(item))
for item in range(221,224):
    lbg.append(str(item))
for item in range(227,233):
    lbg.append(str(item))
#medium bowgun (RIP)
#heavy bowgun
for item in range(150,165):
    hbg.append(str(item))
for item in range(167,174):
    hbg.append(str(item))
for item in range(175,193):
    hbg.append(str(item))
for item in range(194,208):
    hbg.append(str(item))
for item in range(209,215):
    hbg.append(str(item))
for item in range(218,224):
    hbg.append(str(item))


#defenderf='pl/f_equip/pl121_0000'
#defenderm='pl/m_equip/pl121_0000'
#'questData_00101' jagras
#'questData_00102' kestodon
#'questData_00401' history books
#'questData_00504' colossal task
# 306 anjanath
#301 wildspire intro

QID=[]



hard=['alat','xeno','shara','behemoth','leshen','kulve']


any=['nerg.mib','vaal.mib','teo.mib','kushala.mib','kirin.mib','luna.mib','bazel.mib','jho.mib','azure.mib','black.mib','dodo.mib','diablos.mib','rathalos.mib','odo.mib','legiana.mib',
'rathian.mib','rado.mib','pukei.mib','tobi.mib','kulu.mib','tzizi.mib','lavasioth.mib','barroth.mib','great jagras.mib','great girros.mib','paolumu.mib','behemoth.mib','jyura.mib','pink.mib','anjanath.mib','uragaan.mib']
#lavasioth crashes the game
ice=['coral.mib','beo.mib','banbaro.mib','acid.mib','glav.mib','tigrex.mib','narga.mib','barioth.mib','savage.mib','brachy.mib',
'fulgur.mib','ruiner.mib','viper.mib','nightshade.mib','shrieking.mib',
'ebony.mib','blackveil.mib','seething.mib','gold.mib','silver.mib','brute.mib',
'rajang.mib','scarred.mib','zin.mib','nami.mib','velk.mib','stygian.mib','furious.mib','frostfang.mib','alat.mib']
#,'frostfang.mib'

base=['nerg.mib','vaal.mib','teo.mib','kushala.mib','kirin.mib','luna.mib','bazel.mib','jho.mib','azure.mib','black.mib','dodo.mib','diablos.mib','rathalos.mib','odo.mib','legiana.mib',
'rathian.mib','rado.mib','pukei.mib','tobi.mib','kulu.mib','tzizi.mib','barroth.mib','great jagras.mib','great girros.mib','paolumu.mib','jyura.mib','pink.mib','anjanath.mib','uragaan.mib','lavasioth.mib']

dlc=['coral.mib','beo.mib','banbaro.mib','acid.mib','glav.mib','tigrex.mib','narga.mib','barioth.mib','savage.mib','brachy.mib',
'fulgur.mib','ruiner.mib','viper.mib','nightshade.mib','shrieking.mib',
'ebony.mib','blackveil.mib','seething.mib','gold.mib','silver.mib','brute.mib',
'rajang.mib','scarred.mib','zin.mib','nami.mib','velk.mib',"stygian.mib",'furious.mib','frostfang.mib','behemoth.mib',]

em_id = ["em001_00", "em001_01", "em001_02", "em002_00", "em002_01", "em002_02", "em007_00", "em007_01", "em011_00", "em018_00", "em018_05", "em023_00", "em023_05",
"em024_00", "em026_00", "em027_00", "em032_00", "em032_01", "em036_00", "em037_00", "em042_00", "em042_05", "em043_00", "em043_05", "em044_00", "em045_00", "em050_00",
"em057_00", "em057_01", "em063_00", "em063_05", "em080_00", "em080_01", "em100_00", "em100_01", "em102_00", "em102_01", "em103_00", "em103_05", "em104_00", "em105_00",
"em106_00", "em107_00", "em108_00", "em109_00", "em109_01", "em110_00", "em110_01", "em111_00", "em111_05", "em112_00", "em113_00", "em113_01", "em114_00", "em115_00",
"em115_05", "em116_00", "em117_00", "em118_00", "em118_05", "em120_00", "em121_00", "em122_00", "em123_00", "em124_00", "em125_00", "em126_00", "em127_00",]

#elders

#armor Lists



#mArmor=['pl/m_equip/pl020_0000','pl/m_equip/pl008_0000','pl/m_equip/pl003_0000','pl/m_equip/pl004_0000',
#'pl/m_equip/pl007_0000','pl/m_equip/pl009_0000','pl/m_equip/pl010_0000','pl/m_equip/pl011_0000',
#'pl/m_equip/pl012_0000','pl/m_equip/pl013_0000','pl/m_equip/pl014_0000','pl/m_equip/pl017_0000',
#'pl/m_equip/pl021_0000','pl/m_equip/pl022_0000','pl/m_equip/pl023_0000','pl/m_equip/pl024_0000',
#'pl/m_equip/pl025_0000','pl/m_equip/pl026_0000','pl/m_equip/pl027_0000','pl/m_equip/pl028_0000',
#'pl/m_equip/pl029_0000','pl/m_equip/pl031_0000','pl/m_equip/pl033_0000','pl/m_equip/pl034_0000',
#'pl/m_equip/pl035_0000','pl/m_equip/pl036_0000']
#fArmor=['pl/f_equip/pl020_0000','pl/f_equip/pl008_0000','pl/f_equip/pl003_0000','pl/f_equip/pl004_0000',
#'pl/f_equip/pl007_0000','pl/f_equip/pl009_0000','pl/f_equip/pl010_0000','pl/f_equip/pl011_0000',
#'pl/f_equip/pl012_0000','pl/f_equip/pl013_0000','pl/f_equip/pl014_0000','pl/f_equip/pl017_0000',
#'pl/f_equip/pl021_0000','pl/f_equip/pl022_0000','pl/f_equip/pl023_0000','pl/f_equip/pl024_0000',
#'pl/f_equip/pl025_0000','pl/f_equip/pl026_0000','pl/f_equip/pl027_0000','pl/f_equip/pl028_0000',
#'pl/f_equip/pl029_0000','pl/f_equip/pl031_0000','pl/f_equip/pl033_0000','pl/f_equip/pl034_0000',
#'pl/f_equip/pl035_0000','pl/f_equip/pl036_0000']

def randomspeed():
    for item in em_id:
        mID = item[0:5]
        subID = item[6:8]
        #print(mID)
        #print(subID)

        myspeed= path + "\\" + 'nativepc' + '\\' + 'em' + "\\" + mID + "\\" +subID + "\\data\\" + mID + ".dtt_agr"

        if opt_speed =="y":
            with open(myspeed,"rb+") as f:
                f.seek(24)
                f.write(random.choice(speeds))
                f.seek(88)
                f.write(random.choice(speeds))
    if opt_speed == "n":
        shutil.rmtree(path + "\\nativepc" + "\\em")
        shutil.copytree(path + "\\" +"default_speed", path + "\\nativepc" + "\\em")
    return()

def hexedit(quest,monster,monster2,monster3):
    objId=0
    spawnId=0

    if quest == "questdata_0501.mib":
        if opt_arena != "y":
            maps.appaned(vale)

    #Old fix for immortal nergigante.

    #while quest =="questData_00301.mib" and monster=="nerg.mib":
        #monster=random.choice(any)
        #if "nerg.mib" not in any:
        #    any.append("nerg.mib")




    myMonster=path + "\\" + 'myquest' + "\\" + monster
    myQuest=path + "\\" + "nativepc" + "\\" + 'quest' + "\\" + quest
    CleanQuest= path + "\\" + 'clean_quest' + "\\" + quest
    mySize= path + "\\" + 'size matters' + "\\" + random.choice(size)


    area=0
    pp=0
    hp=0
    att=0

    #seek 200 for size

    print (monster)
    monsters_in_run.append(monster)
  
    with open(CleanQuest, 'rb+') as f:
        f.seek(184)
        hp=f.read(8)
        f.seek(192)
        att=f.read(8)

    #Get map and objextive info
    with open(myMonster, 'rb') as f:
        #get map info
        f.seek(24)
        area=random.choice(maps)
        #print(area)
        #get objective info
        f.seek(88)
        objId=f.read(8)
        #get monster spawn id
        f.seek(176)
        spawnId=f.read(8)
        #get difficulty
    #get size data for monster 1
        if (monster == "behemoth.mib"):
            if (rank=="low"):
                att=beh_low_attack
                hp=bytearray.fromhex("CE C6 12 81 93 35 64 C7")
                #print(att)
            elif rank=="high":
                att=beh_high_attack
                #79% hp
                hp=bytearray.fromhex("CE C6 12 81 93 35 64 C7")
                #print(att)
            elif rank=="G":
                att=beh_G_attack
                hp=bytearray.fromhex("CE C6 12 81 93 35 64 C7")
            #    print(att)

    with open(mySize, 'rb') as f:
        f.seek(200)
        pp=f.read(8)
    if (monster == "behemoth.mib"):
        pp=bytearray.fromhex("F8 93 52 14 0D 1C BE 9B")
    #clear monsters 2 and 3 if they exist in case of 1 mmonster quest
    removeaux(myQuest)
    #write area info

    #alatreon is broken in coral, fix the rng so it doesn't happen
    while area == coral and monster == "alat.mib":
        area=random.choice(maps)

    with open(myQuest, 'rb+') as f:
        f.seek(24)
        f.write(area)
        f.seek(120)
        if area==alat_arena or area==seliana:
            f.write(music_dmc)
        else:
            f.write(music_default)

        #write objective, monster, stats, and size
    with open(myQuest, 'rb+') as f:
        f.seek(88)
        f.write(objId)
        f.seek(176)
        f.write(spawnId)
        f.seek(184)
        f.write(hp)
        f.seek(192)
        f.write(att)
        #print(att)
        f.seek(200)
        f.write(pp)

    myMonster=path + "\\" + 'myquest' + "\\" + monster2
    mySize= path + "\\" + 'size matters' + "\\" + random.choice(size)

    if (monster2 != "none"):
        with open(myMonster, 'rb') as f:
            #get monster spawn id
            f.seek(240)
            spawnId=f.read(8)

        #print(mySize)

        with open(mySize, 'rb') as f:
            f.seek(264)
            pp=f.read(8)

        #print(pp)

        with open(myQuest, 'rb+') as f:
            f.seek(240)
            f.write(spawnId)
            f.seek(264)
            f.write(pp)

    myMonster=path + "\\" + 'myquest' + "\\" + monster3
    mySize= path + "\\" + 'size matters' + "\\" + random.choice(size)

    if (monster3 != "none"):

        with open(myMonster, 'rb') as f:
            #get monster spawn id
            f.seek(304)
            spawnId=f.read(8)

        with open(mySize, 'rb') as f:
            f.seek(328)
            pp=f.read(8)

        #print(pp)

        with open(myQuest, 'rb+') as f:
            f.seek(304)
            f.write(spawnId)
            f.seek(328)
            f.write(pp)


def removeaux(file):
    myTemplate=path + "\\" + 'myquest' + "\\" + 'none.mib'
    monster2=0
    monster3=0
    with open(myTemplate, 'rb') as f:
        f.seek(240)
        monster2=f.read(8)
        f.seek(304)
        monster3=f.read(8)
    with open(file, 'rb+') as f:
        f.seek(240)
        f.write(monster2)
        f.seek(304)
        f.write(monster3)

def setMonster(monster):
    tabUntil(2)
    gui.write(monster)
    tabUntil(-2)

def clearAuxMonsters():
    count=0
    while count < 6:
        gui.press('right')
        setMonster('No')
        count=count+1
    #set tabs back to neutral position
    gui.press('left',presses=6)


def writeJson(armorset):
    #index=-1
    #for line in fileinput.input("HR.eq_crt.json", inplace=1):
     #   if '|' in line:
      #      index=index+1
       #     line = ('\"' + str(index) + "|" + set[index] + '\"' + ":" + "{\n")
        #sys.stdout.write(line)
    #fileinput.close()
    index=-1
    for line in fileinput.input("shop.sed.json", inplace=1):
        if 'd": ' in line:
            index=index+1
            line = ('"Equip_Id": ' + random.choice(allweapons[index//3]) + '}' +',' + "\n")
        sys.stdout.write(line)
    fileinput.close()

any.remove("behemoth.mib")
removed_behe=False
mycount=0
#print('No restrictions? (True or False):')
#fullrandom=input()
fullrandom=True

allweapons=[gs,sns,ds,ls,ham,hh,lan,gl,sa,cb,ig,hbg,lbg,bow]
writeJson('anusgurt')

for item in iter:
    QID.append((item + ".mib"))

#print(QID)

randomspeed()
#GENERATE LOW RANK
for item in QID:
    quest=item
    monster=random.choice(any)
    while(monster in murder_monsters):
        if (quest in murder_quests):
            print("I prevented a muurder :)" + quest)
            monster=random.choice(any)
            #print("murdered mosnter replaced with " + monster)
        else:
            break
    any.remove(monster)
    hexedit(quest,monster,"none","none")

QID=[]

for item in high:
    QID.append((item + ".mib"))


#generate high rank
any.append("behemoth.mib")
rank="high"

for item in QID:
    quest=item
    monster=random.choice(any)
    while(monster in murder_monsters):
        if (quest in murder_quests):
            print("I prevented a muurder :)" +quest)
            monster=random.choice(any)
            #print("murdered mosnter replaced with " + monster)
        else:
            break
    any.remove(monster)
    hexedit(quest,monster,"none","none")

#generate low+high bosses
if opt_boss == "y":
    for item in boss:
        quest=item
        if "behemoth.mib" in any:
            any.remove("behemoth.mib")
            removed_behe=True
        monster=random.choice(any)
        while(monster in murder_monsters):
            if (quest in murder_quests):
                print("I prevented a muurder :)" + quest)
                monster=random.choice(any)
                #print("murdered mosnter replaced with " + monster)
            else:
                break
        any.remove(monster)
        companion=random.choice(any)
        any.remove(companion)
        hexedit(quest,monster,companion,random.choice(any))
else:
    for item in boss:
        quest=item
        monster=random.choice(any)
        while(monster in murder_monsters):
            if (quest in murder_quests):
                print("I prevented a muurder :)" + quest)
                monster=random.choice(any)
                #print("murdered mosnter replaced with " + monster)
            else:
                break

        any.remove(monster)
        hexedit(quest,monster,"none","none")

print("END OF LOW/HIGH RANK")
QID=[]

#MASTER RANK SECTION
if removed_behe == True:
    any.append("behemoth.mib")

for item in ice:
    any.append(item)

for item in iter2:
    QID.append((item + ".mib"))

rank="G"

if opt_arena != "y":
    for item in icemaps:
        maps.append(item)

for item in QID:
    quest=item
    monster=random.choice(any)
    any.remove(monster)
    hexedit(quest,monster,"none","none")

if opt_boss == "y":
    for item in iceboss:
        quest=item
        if "behemoth.mib" in any:
            any.remove("behemoth.mib")
            removed_behe=True
        monster=random.choice(any)
        any.remove(monster)
        companion=random.choice(any)
        any.remove(companion)
        hexedit(quest,monster,companion,random.choice(any))
else:
    for item in iceboss:
        quest=item
        monster=random.choice(any)
        any.remove(monster)
        hexedit(quest,monster,"none","none")
