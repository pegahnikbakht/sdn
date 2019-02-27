from mininet.node import CPULimitedHost, RemoteController
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI

net = Mininet()

def topology():

    #Add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    #Add switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    #Add links 
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)


def network_start():
    #Remote controller
    #c1 = RemoteController('c', '192.168.1.9', 6633)
    #net.addController(c1)

    #Local controller
    c1 = net.addController('c1')
    net.build()

    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
    network_start()
