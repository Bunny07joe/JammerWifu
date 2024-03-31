clear
cd .. 
dir=$(pwd)
echo "TOOL NAME wifize"
python  $dir/wifi/pyscript/name.py

echo -n "you have external wifi adpeter with monitor mode supported y/n :"
read response 

interface=$(cat $dir/wifi/pyscript/workspace/NETWORK/interface.txt) 

if [ $response = y -o $response = Y ]
then 

	nmcli -f BSSID,SSID,CHAN dev wifi list ifname $interface >  $dir/wifi/pyscript/workspace/NETWORK/start.txt  
	sudo airmon-ng check kill
	sudo airmon-ng start $interface > $dir/wifi/pyscript/workspace/adpater.txt
	
	if test `python $dir/wifi/pyscript/workspace/main/wifi.py` = no
	then 
		echo "sorry you dont pulg in external wifi adpater "
	fi

	if test `python $dir/wifi/pyscript/workspace/main/wifi.py` = None
	then 
		python $dir/wifi/pyscript/workspace/main/scan.py > $dir/wifi/pyscript/workspace/NETWORK/scaned.txt # for scaning network
		cat $dir/wifi/pyscript/workspace/NETWORK/scaned.txt
		echo -n "enter number to attck on : "
		read input 
		echo $input > $dir/wifi/pyscript/workspace/input.txt
		python $dir/wifi/pyscript/workspace/main/attack.py > $dir/wifi/pyscript/workspace/command-script/cmd.sh
		

		bash  $dir/wifi/pyscript/workspace/command-script/cmd.sh
		
	fi
	
fi

if [ $response = n -o $response = N ]
then 
	echo "plz insert adpater after run script..."
fi
 
