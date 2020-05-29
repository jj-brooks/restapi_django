# -*- mode: ruby -*-
# vi: set ft=ruby :

# 1
Vagrant.configure("2") do |config|
 
  # 2 set OD for box
  config.vm.box = "ubuntu/bionic64"

  # 3 set OS version 
  config.vm.box_version = "~> 20200304.0.0"
 
  # 4 set network port 
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # 5 run scripts for runtime setup 
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
  
    sudo apt-get update
    sudo apt-get install -y python3-venv zip
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
 end