import os
path = f'{os.getcwd()}/wifi/pyscript/workspace/NETWORK/start.txt'
name = []
addr_ch = dict()
def serching () :
    with open(path, "r") as f: 
        view = f.readline() 
        poinlenght = len(view) 
        pointer = poinlenght
        lenght = len(f.readlines())
        chpointx = 0
        for i in view :
            if i == 'C':
                break
            chpointx +=1
        for i in range (lenght):
            f.seek(pointer)
            view = f.readline()
            mac = view[0:17]

            ch = view[chpointx:].replace(" ","").replace("\n","")

            Name = view[19:chpointx-1]

            name.append(Name)
            temp_dic = {mac:ch}
            addr_ch.update(temp_dic)
            pointer += poinlenght
    lopp = len(name)
    
    i = 0
    k = 1
    while i < lopp :
        print(f"{k} {name[i]}")
        i += 1
        k += 1
serching()
