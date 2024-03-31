import multiprocessing
import os
import platform

run = f'{os.getcwd()}/mainscript/WIFIZE.sh'
path2 = f'{os.getcwd()}/mainscript/WIFITE.sh'
path3 = f'{os.getcwd()}/pyscript/workspace/handshake/remove.sh'
attck = f'konsole --noclose -e sudo  {path2}'

os_name = platform.system()
if (os_name == "Linux"):
    try:

        def run_wifize_script(): 
            os.system(run)

        def run_wifite_script():
            os.system(attck)


        if __name__ == '__main__':
            process_a = multiprocessing.Process(target=run_wifize_script)
            process_b = multiprocessing.Process(target=run_wifite_script)

            process_a.start()
            process_b.start()

            process_a.join()
            process_b.join()
    except :
        print('*'*20,"ERROR",'*'*20)

    finally:
        remove = f"bash {path3} "
        os.system(remove)
        print("\n"*2)
        print("closing the terminal......")
        print("having any problem run re-config.sh file ")
else:
    print("Sorry ! it only work on LINUX Machine .")
