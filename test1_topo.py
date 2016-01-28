#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def build( self, natIP='10.0.0.254' ):
        nat1 = self.addNode( 'nat1', cls=NAT, ip=natIP, inNamespace=False )
        hosts  = [ self.addHost( h, defaultRoute='via ' + natIP )
                   for h in 'h1', 'h2' ]
        s1 = self.addSwitch( 's1' )
       for h in hosts:
            self.addLink( s1, h )
            self.addLink( nat1, s1 )

if __name__ == '__main__':
    setLogLevel( 'info' )
    build()
