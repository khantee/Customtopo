#!/usr/bin/python

"""
Script created by VND - Visual Network Description (SDN version)
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, OVSLegacyKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    s3 = net.addSwitch( 's3', listenPort=6633, mac='00:00:00:00:00:01' )
    c4 = net.addController( 'c4', controller=RemoteController, ip='192.168.56.104', port=6633 )

    print "*** Creating links"
    net.addLink(h2, s3, 0, 2)
    net.addLink(h1, s3, 0, 1)

    print "*** Starting network"
    net.build()
    s3.start( [c4] )
    c4.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

