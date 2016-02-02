"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.nodelib import NAT

class MyTopo( Topo ):
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        natIP='10.0.0.254'
        for i range (2,102):
            h = self.addHost( 'h%d' % i, ip = "10.0.0.%d" % i ,defaultRoute= 'via ' + natIP )
            s1 = self.addSwitch( 's1', mac = "00:00:00:00:00:01" )
            nat1 = self.addNode('nat1', cls=NAT, ip=natIP,inNamespace=False)
            self.addLink( h, s1 )
            self.addLink( nat1, s1)
     

topos = { 'mytopo': ( lambda: MyTopo() ) }