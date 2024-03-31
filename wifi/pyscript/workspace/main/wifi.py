# this code check adapter is pulg or not 
import os 
path = f'{os.getcwd()}/wifi/pyscript/workspace/adpater.txt'
def checkadpeter():
    with open(path, "r") as f:
        view = f.readlines()
    viewlist = []
    for i in view:
        viewlist.append(i)
        wlan1  = None
    for i in viewlist :
        if i == 'Requested device "wlan1" does not exist.\n':
            wlan1 = "no"
    return wlan1    
        
    

        
pointer = checkadpeter()
print(pointer)
