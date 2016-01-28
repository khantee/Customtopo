#!/usr/bin/python

"""
Example to create a Mininet topology and connect it to the internet via NAT
"""

from mininet.cli import CLI
from mininet.node import Node
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel, info

if __name__ == '__main__':

    setLogLevel( 'info')
    net = Mininet( controller=RemoteController )
    info( '*** Adding controller\n' )
    net.addController( 'c1',controller=RemoteController,ip="10.0.0.118",port=6653 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip="10.0.0.1" )
    h2 = net.addHost( 'h2', ip="10.0.0.2" )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', mac="00:00:00:00:00:01" )

    info( '*** Creating links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )



    info( '*** Starting network\n')
    
    # Add NAT connectivity
    net.addNAT().configDefault()
    net.start()
    print "*** Hosts are running and should have internet connectivity"
    print "*** Type 'exit' or control-D to shut down network"
    CLI( net )
    # Shut down NAT
    net.stop()