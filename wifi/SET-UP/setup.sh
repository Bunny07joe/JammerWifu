dir=$(pwd)

python $dir/setup.py
sudo apt-get install konsole
mkdir $dir/pyscript/workspace/permnent-files
echo ""
ifconfig
echo ""
echo "for exmaple name of interface or wifi adpater : wlan1, wlan0mon, eth0 "
echo ""
echo -n "ENTER THE EXTERNAL adpter name shown in above  : "
read interface 
cd ..
interfaceF=$(pwd)

echo $interface > $interfaceF/pyscript/workspace/NETWORK/interface.txt

