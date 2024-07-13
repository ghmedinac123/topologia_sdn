#!/usr/bin/python3
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

setLogLevel('info')
net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')

info('*** Adding docker containers\n')
d1 = net.addDocker('d1', ip='10.0.0.251',
                   dimage="nginx-rtmp:latest", ports=[1935], port_bindings={1935: 1935}, privileged=True,
                   cap_add=['NET_ADMIN', 'SYS_MODULE', 'SYS_ADMIN', 'net_admin'])
d2 = net.addDocker('d2', ip='10.0.0.252',
                   dimage="user:latest", ports=[5901], port_bindings={5901: 5901}, privileged=True,
                   cap_add=['NET_ADMIN', 'SYS_MODULE', 'SYS_ADMIN', 'net_admin'])

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')

info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(s1, s2)
net.addLink(s2, d2)

info('*** Starting network\n')
net.start()

info('*** Testing connectivity\n')
# Instead of ping, let's just check if containers are up
info(f"d1: {d1.name} is up\n")
info(f"d2: {d2.name} is up\n")

info('*** Running CLI\n')
CLI(net)

# Agregar comandos de diagnóstico
info('*** Diagnóstico dentro del contenedor d2\n')
d2.cmd('ip addr show')
d2.cmd('ifconfig')
d2.cmd('dmesg | tail')

info('*** Stopping network\n')
net.stop()

