class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os="debian"):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = 0
        self.proc = 0


    def stop(self):
        self.status = 0

    def start(self):
        self.status = 1

    def suspend(self):
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def run(self, pid, ram, cpu, hdd):
        proc = {
        'pid' = pid
        'ram' = ram
        'cpu' = cpu
        'hdd' = hdd
        }

#def ram_usage(self):
    #return

    def __str__(self):
        return "Sistema {} memoria ram {} cpu {} HDD {}".format(self.os, self.ram, self.cpu, self.hdd)


if __name__ == '__main__':
    vm1 = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'Ubuntu')
    vm1.start()
    vm1.status

    vm2 = VirtualMachine('Rohan', 6, 1.9, 250, 'Debian')
    vm2.start()
    vm2.status

    vm3 = VirtualMachine('Rivendel', 16, 3, 100, 'OpenSuse')
    vm3.start()
    vm3.status

print(vm1, vm2, vm3)









 #

#def ram_usage(self):
    #return

#def hdd_usage(self):
    #return


#for proceso in self.proc
#proceso['ram']

#ram += proceso['ram']
#


#return self.ram / self.porcenta.ram *100
