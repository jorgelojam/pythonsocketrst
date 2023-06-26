Vagrant.configure("2") do |config|
    config.vm.define "vm1" do |vm1|
        vm1.vm.box = "almalinux/8"
        vm1.vm.hostname = "web1"
        vm1.vm.provider "virtualbox" do |vb|
            vb.memory = 1024
            vb.cpus = 1
        end
        vm1.vm.network :private_network, ip: "192.168.56.10"
    end
    config.vm.define "vm2" do |vm2|
        vm2.vm.box = "almalinux/8"
        vm2.vm.hostname = "cliente1"
        vm2.vm.provider "virtualbox" do |vb|
            vb.memory = 1024
            vb.cpus = 1
        end
        vm2.vm.network :private_network, ip: "192.168.56.11"
    end
end