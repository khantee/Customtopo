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
        natIP='10.0.0.254'
       
        for i  in range (2,101):
            host  = self.addHost( 'h%d' % i, 
                                ip = '10.0.0.%d' % i ,
                                defaultRoute= 'via ' + natIP)
            s1 = self.addSwitch( 's1', mac = "00:00:00:00:00:01" )
            
            self.addLink( host, s1 )
            
        nat1 = self.addNode('nat1', cls=NAT, ip=natIP,
                            inNamespace=False)
        self.addLink( nat1, s1)


topos = { 'mytopo': ( lambda: MyTopo() ) }
