# General updates
sudo apt-get update && sudo apt-get upgrade

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
## Add pi user to docker group
sudo usermod -aG docker pi

# Install docker-compose
sudo apt-get -y install libffi-dev libssl-dev python3-dev python3 python3-pip
sudo pip3 -v install docker-compose

# Install nodejs & npm
sudo apt-get install nodejs
sudo apt-get install npm

# Install respeaker
git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh --compat-kernel

# Reboot after all this installation
sudo reboot