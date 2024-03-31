
echo "re-config file is running...."
echo "check your interface card is connected "
iwconfig
echo -n "ENTER YOUR interface card name : "
read interface
sudo airmon-ng stop $interface
sudo airmon-ng check kill
sudo service NetworkManager start

echo "now RE-connect your adpater ..."
echo "now run [main.py] FILE "
