echo "waiting for client sometimes if found awnser y or not awnser n" 
echo ""
echo -n "start the attcking  :"
read awnser
echo ""
cd .. 
dir=$(pwd)
if [ $awnser = y -o $awnser = Y ]
then 

    python $dir/wifi/pyscript/workspace/main/deauther.py 
    bash  $dir/wifi/pyscript/workspace/command-script/cmd2.sh
fi
if [ $awnser = n -o $awnser = N ]
then 
    echo "closing terminal...."
fi

