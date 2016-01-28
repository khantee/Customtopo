#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import Node

def build( self, natIP='10.0.0.254' ):
    
    nat1 = self.addNode( 'nat1', cls=NAT, ip=natIP, inNamespace=False )
    net = Mininet( controller=RemoteController )
   
    info( '*** Adding controller\n' ) 
  
    net.addController( 'c1',controller=RemoteController,ip="10.0.0.118",port=6653 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip="10.0.0.1" )
    h2 = net.addHost( 'h2', ip="10.0.0.2" )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', mac="00:00:00:00:00:01" )

    info( '*** Creating links\n' )
    nat1 = self.addNode( 'nat1', cls=NAT, ip=10.0.0.254,inNamespace=False)
    self.addLink( nat1, s1 )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )

    info( '*** Starting network\n')
    net.start()

   
    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    build()
