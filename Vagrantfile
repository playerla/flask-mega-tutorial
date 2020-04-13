Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.define "microblog"
  config.vm.provider "virtualbox" do |vm|
    vm.name = "microblog"
    vm.memory = "1024"
  end
  # Then manually install... or use Docker ;)
end
