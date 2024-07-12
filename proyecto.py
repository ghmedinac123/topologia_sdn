#!/usr/bin/python3

from mininet.net import Containernet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def myNetwork():

    net = Containernet(topo=None,
                       build=False,
                       link=TCLink,
                       ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='172.17.0.2',
                           protocol='tcp',
                           port=6653)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, protocols=["OpenFlow13"])
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, protocols=["OpenFlow13"])
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, protocols=["OpenFlow13"])

    info('*** Add docker containers\n')
    h1 = net.addDocker('h1', ip='10.0.0.1', dimage="server_web:latest", 
                       ports=[80], port_bindings={80: 8080},privileged=True, cap_add=['NET_ADMIN'])  # Exponer puerto 80 de Apache
    h2 = net.addDocker('h2', ip='10.0.0.2', dimage="mariadb:latest",
                       ports=[3306], port_bindings={3306: 3306},privileged=True, cap_add=['NET_ADMIN'])  # Exponer puerto 3306 de MariaDB
    h3 = net.addDocker('h3', ip='10.0.0.3', dimage="user:latest",
                       ports=[5901], port_bindings={5901: 5901}, privileged=True, cap_add=['NET_ADMIN'])

    info('*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s2, s3)
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s3)
    net.addLink(h5, s3)
    net.addLink(h6, s3)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()

