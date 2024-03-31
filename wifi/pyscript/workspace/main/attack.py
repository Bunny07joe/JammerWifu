import os
path = f'{os.getcwd()}/wifi/pyscript/workspace/NETWORK/start.txt'
path2 = f'{os.getcwd()}/wifi/pyscript/workspace/input.txt'
path3 = f'{os.getcwd()}/wifi/pyscript/workspace/command-script/cmd.sh' 
path4 = f'{os.getcwd()}/wifi/pyscript/workspace/handshake/psk' # this path for handshake 

name = []
addr_ch = dict()
cmd = ""

def attck () :
    found = 0
    global mac 
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
    with open(path2,'r') as f:
        Input = f.read()
    while True : 
        try :
            print("\n")
            target = Input
            if  target == 'n':
                print("attcking all  target plz wait....") # work on attck on every access point network 
                break

            elif int(target) == 0:
                print("0 target dosen't exists ! ")
                break

            elif int(target) == lopp :
                mc = list(addr_ch)[int(target)-1]
                mc = str(mc).replace(" ","")
                channel = list(addr_ch.values())[int(target)-1]
                command = f'konsole --noclose -e sudo airodump-ng -c {channel} -w {path4} -d {mc} wlan1' #command 
                cmd = command
                found = 1
                print(cmd)
                break
                

            elif int(target) > lopp :
                print(f"target not found \nnumber{target} is not exist sorry  !\n")
                break

            elif name[int(target)] in name :
                INDEX = None
                for i in range(len(name)):
                    if name[i] == name[int(target)-1]:
                        INDEX = i
                mc = list(addr_ch)[int(INDEX)]
                mc = str(mc).replace(" ","")
                channel = list(addr_ch.values())[int(target)-1]
                command = f'konsole --noclose -e sudo airodump-ng -c {channel} -w {path4} -d {mc} wlan1' # make command 
                cmd = command
                found = 1
                print(cmd)
                break

            else :
                print("command not found ")
        except ValueError :
            print("$ invaild input $")
            break
    if found == 1 :
        with open(path3,'w') as f:
            f.writelines(cmd) # write command to cmd.txt

        
       
        
attck()

