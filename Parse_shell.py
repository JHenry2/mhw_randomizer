from construct.core import *
import pandas as pd
import os
clean = os.getcwd() + '\\clean' + '\\em'
#clean = os.getcwd() + '\\cursed' + '\\em'
def main():
    file_paths=[]
    for path, subdirs, files in os.walk(clean):
        for name in files:
            if name.endswith('.shlp_de'):
                file_paths.append(os.path.join(path, name))
    shlp = Struct(
    "magic1" / Int32sl,
    "slp" / CString('ascii'),
    "magic2" / Int32sl,
    
    
    )
    assets=Struct(
    "header" / Int32sl,
    'path' / If(this.header,CString('ascii'))
    

    )

    child_shell_params=Struct(
    
    'header' / Int32sl,
    'path' / CString('ascii'),
    'unk 1' / Int32sl,
    'flags' / Int32sl,
    'unk 3' / Int32sl

    )

    shell=Struct(
    'shlp' / shlp,
    'assets' / assets[25],

    'projectile body epv index' / Int32sl,
    'projectile body epv element' / Int32sl,
    'projectile muzzle index' / Int32sl,
    'projectile muzzle element' / Int32sl,
    'muzzle joints' / Bytes(4),
    'col_header' / Int32sl,
    'col_path' / If(this.col_header,CString('ascii')),
    'col_index' / Int32sl,
    'timeline_list' / Int32sl,
    'timeline path' / If(this.timeline_list,CString('ascii')),
    'unk 2' / Int32sl,
    'unk 3' / Int32sl,
    'unk 4' / Int32sl,
    'unk 5' / Int32sl,
    'unk 6' / Int32sl,

    'number_linked_shell' / Int32sl,
    'children' / If(this.number_linked_shell > 0, child_shell_params[this.number_linked_shell]),
    'the_rest' / GreedyBytes


    )

    #print(file_paths)
    my_df=pd.DataFrame(columns=['shell', 'children', 'is_child'])
    #my_df['shell'] = file_paths
    not_cursed=True
    if not_cursed:
        for path in file_paths:
            #print(path)
            parsed = shell.parse_file(path)
            children=parsed.children
            if children:
                #print(children[0:][0]['path'])
                #print(children)
                for item in children[0:]:
                    my_df.loc[item['path'], 'is_child'] = True
        my_df.to_csv('shells2.csv')

    my_df=pd.DataFrame(columns=['collision', 'index', 'holder', 'location'])
    for index, path in enumerate(file_paths):
        #print(path)
        parsed = shell.parse_file(path)
        colindex=parsed.col_index
        colpath=parsed.col_path
        print(colpath, colindex)
        my_df.loc[index] = colpath, colindex, path[-16:-11], path[-16:-5]
    my_df.to_csv('shells_cursed.csv')
main()