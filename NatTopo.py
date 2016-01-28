
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import Node
from mininet.net import Mininet
from mininet.node import RemoteController

class NatTopo( Topo ):
    def build( self, natIP='10.0.0.254' ):
        self.hopts = { 'defaultRoute': 'via ' + natIP }
        hosts  = [ self.addHost( h ) for h in 'h1', 'h2' ]
        s1 = self.addSwitch( 's1' )
        for h in hosts:
            self.addLink( s1, h )
        nat1 = self.addNode( 'nat1', cls=NAT, ip=natIP,
                             inNamespace=False )
        self.addLink( nat1, s1 )

 def simpleTest():
        "Create and test a simple network"
        topo = SingleSwitchTopo(n=4)
        net = Mininet(topo)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        print "Testing network connectivity"
        net.pingAll()
        net.stop()

if __name__ == '__main__':
        # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()