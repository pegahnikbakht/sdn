import random

from mn_wifi.link import wmediumd, mesh
from mn_wifi.wmediumdConnector import interference
from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi

def Vanet_topology():

    net = Mininet_wifi(controller=Controller,
                       link=wmediumd,
                       wmediumd_mode=interference)

    
    #creating vehicles
    vehicles = []
    for id in range(0, 10):
        min_ = random.randint(1, 4)
        max_ = random.randint(11, 30)
        vehicles.append(net.addCar('vehicle%s' % (id+1), wlans=2,
                               min_speed=min_,
                               max_speed=max_))

    rsu11 = net.addAccessPoint('RSU11', ssid='RSU11', mode='g',
                               channel='1')
    rsu12 = net.addAccessPoint('RSU12', ssid='RSU12', mode='g',
                               channel='6')
    rsu13 = net.addAccessPoint('RSU13', ssid='RSU13', mode='g',
                               channel='11')
    rsu14 = net.addAccessPoint('RSU14', ssid='RSU14', mode='g',
                               channel='11')

    c1 = RemoteController('c', '130.235.202.50', 6653)
    net.addController(c1)
    

    info("*** Configuring Model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(rsu11, rsu12)
    net.addLink(rsu11, rsu13)
    net.addLink(rsu11, rsu14)

    for vehicle in vehicles:
        net.addLink(vehicle, intf=vehicle.params['wlan'][1],
                    cls=mesh, ssid='mesh-ssid', channel=5)

    net.plotGraph(max_x=500, max_y=500)

    net.roads(10)

    net.startMobility(time=0)

    info("*** Network start\n")

    net.build()
    c1.start()
    rsu11.start([c1])
    rsu12.start([c1])
    rsu13.start([c1])
    rsu14.start([c1])

    for vehicle in vehicles:
        vehicle.setIP('192.168.0.%s/24' % (int(vehicles.index(vehicle))+1),
                  intf='%s-wlan0' % vehicle)
        vehicle.setIP('192.168.1.%s/24' % (int(vehicles.index(vehicle))+1),
                  intf='%s-mp1' % vehicle)

    CLI_wifi(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Vanet_topology()
