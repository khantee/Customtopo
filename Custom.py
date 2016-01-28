"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1', ip = "10.0.0.8"  )
        h2 = self.addHost( 'h2', ip = "10.0.0.9"  )
        s1 = self.addSwitch( 's1', mac = "00:00:00:00:00:01" )
       

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s2 )
     

topos = { 'mytopo': ( lambda: MyTopo() ) }