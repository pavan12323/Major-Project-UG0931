
from mininet.topo import Topo, Node

class RFTopo( Topo ):
    "RouteFlow Demo Setup"

    def __init__( self, enable_all = True ):
        "Create custom topo."

        # Add default members to class.
        super( RFTopo, self ).__init__()

        # Set Node IDs for hosts and switches
        h1 = 1
        h2 = 2
        h3 = 3
        h4 = 4
        sA = 5
        sB = 6
        sC = 7
        sD = 8
	sE = 9
	sF = 10

        # Add nodes
        self.add_node( h1, Node( is_switch=False ) )
        self.add_node( h2, Node( is_switch=False ) )
        self.add_node( h3, Node( is_switch=False ) )
        self.add_node( h4, Node( is_switch=False ) )
        self.add_node( sA, Node( is_switch=True ) )
        self.add_node( sB, Node( is_switch=True ) )
        self.add_node( sC, Node( is_switch=True ) )
        self.add_node( sD, Node( is_switch=True ) )
	self.add_node( sE, Node( is_switch=True) )
	self.add_node( sF, Node( is_switch=True) )

        # Add edges
        self.add_edge( h1, sA )
        self.add_edge( h2, sB )
        self.add_edge( h3, sC )
        self.add_edge( h4, sD )
        self.add_edge( sE, sF )
        self.add_edge( sB, sD )
        self.add_edge( sD, sF )
        self.add_edge( sC, sA )
        self.add_edge( sA, sE )
	self.add_edge( sC, sD )	
#	self.add_edge( sE, sD )
#	self.add_edge( sA, sB )	



        # Consider all switches and hosts 'on'
        self.enable_all()


topos = { 'rftopo': ( lambda: RFTopo() ) }
