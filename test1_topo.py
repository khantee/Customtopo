"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel
from mininet.cli import CLI

class MyTopo( Topo ):
    "Simple topology example." 
  
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' , ip='10.0.0.5/8')
        rightHost = self.addHost( 'h2',ip='10.0.0.6/8')
        leftSwitch = self.addSwitch( 's3' )
        c1 = self.addController('c1',ip='192.168.56.104',port='6633')
        

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( rightHost, leftSwitch )
        self.addLink( c1, leftSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
