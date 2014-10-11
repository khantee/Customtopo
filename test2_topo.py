#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=RemoteController )

    info( '*** Adding controller\n' )
    net.addController( 'c1',controller=RemoteController,ip="192.168.56.101",port=6633 )

    info( '*** Adding hosts\n' )
    h3 = net.addHost( 'h3', ip="10.0.0.3" )
    h4 = net.addHost( 'h3', ip="10.0.0.4" )

    info( '*** Adding switch\n' )
    s2 = net.addSwitch( 's2' ,mac="00:00:00:00:00:02" )

    info( '*** Creating links\n' )
    net.addLink( h3, s2 )
    net.addLink( h4, s2 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()