#!/usr/bin/python
"""
This is the simple example to showcase retrans control.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
d1 = net.addDocker('d1', ip='10.0.0.252', dimage="ubuntu:dsn")
d2 = net.addDocker('d2', ip='10.0.0.251', dimage="ubuntu:dsn")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
info('*** Creating links\n')
net.addLink(d1, s1,cls=TCLink,delay='50ms')
net.addLink(s1, d2,cls=TCLink,delay='50ms',bw=100,loss=5)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
