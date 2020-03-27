Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.define "microblog"
  config.vm.provider "virtualbox" do |vm|
    vm.name = "microblog"
    vm.memory = "1024"
  end
end

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.33.11"
  config.vm.define "microblog-docker"
  config.vm.provider "virtualbox" do |vm|
    vm.name = "microblog-docker"
    vm.memory = "1024"
  end
  config.vm.provision "shell" do |shell|
    shell.inline = "chown root:ubuntu /opt && chmod g+w /opt && setfacl -m 'g:vagrant:rwx' /opt && setfacl -m 'g:ubuntu:r-x' /opt"
  end
end
