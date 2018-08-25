# Setup

### Install serverless
´´´
sudo npm install -g serverless
sudo npm install -g serverless-python-requirements
´´´

## Install docker
´´´
sudo pacman -S docker
sudo usermod -a -G docker ovski
sudo systemctl start docker
sudo systemctl enable docker
newgrp docker
´´´

## Deploy
´´´
serverless deploy -v
´´´

