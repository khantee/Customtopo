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