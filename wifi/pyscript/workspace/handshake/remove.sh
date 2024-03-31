dir=$(pwd)
echo $dir 
interface=$(cat $dir/pyscript/workspace/NETWORK/interface.txt)
sudo airmon-ng stop $interface


echo "FILES"
echo "****************************************************"
ls -al  $dir/pyscript/workspace/handshake 
echo "*****************************************************"


echo -n "you realy want to  ALL remove file : "
read choise
if [ $choise = y -o $choise = Y ]
then 
    rm $dir/pyscript/workspace/handshake/psk*
    echo "all file are remove from handshke folder/dir"
fi
if [ $choise = n -o $choise = N ]
then 
    echo "okay all handhsake file protected "
    echo "" 
    mv $dir/pyscript/workspace/handshake/psk*   $dir/pyscript/workspace/permnent-files/

    echo "moved in permanent directory."
fi





sudo service NetworkManager start
