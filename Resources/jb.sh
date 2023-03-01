#!/bin/bash

cd ~ 

if [ "$arch" == 'arm64' ]; then


wget http://static.ironside.org.uk/bootstraps/silicon.tar
sudo tar -xpkf silicon.tar -C /
printf 'export PATH="/opt/procursus/bin:/opt/procursus/sbin:/opt/procursus/games:$PATH"\nexport CPATH="$CPATH:/opt/procursus/include"\nexport LIBRARY_PATH="$LIBRARY_PATH:/opt/procursus/lib"\n' | sudo tee -a /etc/zshenv /etc/profile
export PATH="/opt/procursus/bin:/opt/procursus/sbin:/opt/procursus/games:$PATH"
export CPATH="$CPATH:/opt/procursus/include"
export LIBRARY_PATH="$LIBRARY_PATH:/opt/procursus/lib"
wget http://static.ironside.org.uk/scripts/refresh-apt.sh
chmod +x refresh-apt.sh
bash refresh-apt.sh
else
wget http://static.ironside.org.uk/bootstraps/intel.tar
sudo tar -xpkf intel.tar -C /
printf 'export PATH="/opt/procursus/bin:/opt/procursus/sbin:/opt/procursus/games:$PATH"\nexport CPATH="$CPATH:/opt/procursus/include"\nexport LIBRARY_PATH="$LIBRARY_PATH:/opt/procursus/lib"\n' | sudo tee -a /etc/zshenv /etc/profile
export PATH="/opt/procursus/bin:/opt/procursus/sbin:/opt/procursus/games:$PATH"
export CPATH="$CPATH:/opt/procursus/include"
export LIBRARY_PATH="$LIBRARY_PATH:/opt/procursus/lib"
wget http://static.ironside.org.uk/scripts/refresh-apt.sh
chmod +x refresh-apt.sh
bash refresh-apt.sh
fi