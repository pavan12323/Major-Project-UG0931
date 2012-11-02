
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
	h5 = 5
        h6 = 6
        h7 = 7
        h8 = 8
 	h9 = 9
        h10 = 10
        h11 = 11
        h12 = 12
 	h13 = 13
        h14 = 14
        h15 = 15
        h16 = 16
        
	sA = 17
        sB = 18
        sC = 19
        sD = 20
        sE = 21
        sF = 22
        sG = 23
        sH = 24
        sI = 25
        sJ = 26
        sK = 27
        sL = 28
 	sM = 29
        sN = 30
        sO = 31

        sP = 32
        sQ = 33
        sR = 34
        sS = 35
        sT = 36


        # Add nodes
        # Add hosts
        self.add_node( h1, Node( is_switch=False ) )
        self.add_node( h2, Node( is_switch=False ) )
        self.add_node( h3, Node( is_switch=False ) )
        self.add_node( h4, Node( is_switch=False ) )
        self.add_node( h5, Node( is_switch=False ) )
        self.add_node( h6, Node( is_switch=False ) )
        self.add_node( h7, Node( is_switch=False ) )
        self.add_node( h8, Node( is_switch=False ) )
        self.add_node( h9, Node( is_switch=False ) )
        self.add_node( h10, Node( is_switch=False ) )
        self.add_node( h11, Node( is_switch=False ) )
        self.add_node( h12, Node( is_switch=False ) )
        self.add_node( h13, Node( is_switch=False ) )
        self.add_node( h14, Node( is_switch=False ) )
        self.add_node( h15, Node( is_switch=False ) )
        self.add_node( h16, Node( is_switch=False ) )

        self.add_node( sA, Node( is_switch=True ) )
        self.add_node( sB, Node( is_switch=True ) )
        self.add_node( sC, Node( is_switch=True ) )
        self.add_node( sD, Node( is_switch=True ) )
        self.add_node( sE, Node( is_switch=True ) )
        self.add_node( sF, Node( is_switch=True ) )
        self.add_node( sG, Node( is_switch=True ) )
        self.add_node( sH, Node( is_switch=True ) )
        self.add_node( sI, Node( is_switch=True ) )
        self.add_node( sJ, Node( is_switch=True ) )
        self.add_node( sK, Node( is_switch=True ) )
        self.add_node( sL, Node( is_switch=True ) )
        self.add_node( sM, Node( is_switch=True ) )
        self.add_node( sN, Node( is_switch=True ) )
        self.add_node( sO, Node( is_switch=True ) )
        self.add_node( sP, Node( is_switch=True ) )
        self.add_node( sQ, Node( is_switch=True ) )
        self.add_node( sR, Node( is_switch=True ) )
        self.add_node( sS, Node( is_switch=True ) )
        self.add_node( sT, Node( is_switch=True ) )




        # Add edges
        # LEVEL 4
        self.add_edge( h1, sI )
        self.add_edge( h2, sI )
        self.add_edge( h3, sJ )
        self.add_edge( h4, sJ )
        self.add_edge( h5, sK )
        self.add_edge( h6, sK )
        self.add_edge( h7, sL )
        self.add_edge( h8, sL )
        self.add_edge( h9, sM )
        self.add_edge( h10, sM )
        self.add_edge( h11, sN )
        self.add_edge( h12, sN )
        self.add_edge( h13, sO )
        self.add_edge( h14, sO )
        self.add_edge( h15, sP )
        self.add_edge( h16, sP )
           
        # LEVEL 2 TO 3
        self.add_edge( sA, sI )
        self.add_edge( sA, sJ )
        self.add_edge( sB, sI )
        self.add_edge( sB, sJ )
        self.add_edge( sC, sK )
        self.add_edge( sC, sL )
        self.add_edge( sD, sK )
        self.add_edge( sD, sL )
        self.add_edge( sE, sM )
        self.add_edge( sE, sN )
        self.add_edge( sF, sM )
        self.add_edge( sF, sN )
        self.add_edge( sG, sO )
        self.add_edge( sG, sP )
        self.add_edge( sH, sO )
        self.add_edge( sH, sP )
        
        #LEVEL 1 TO 2
        self.add_edge( sQ, sA )
        self.add_edge( sQ, sC )
        self.add_edge( sQ, sE )
        self.add_edge( sQ, sG )
        self.add_edge( sR, sA )
        self.add_edge( sR, sC )
        self.add_edge( sR, sE )
        self.add_edge( sR, sG )
        self.add_edge( sS, sB )
        self.add_edge( sS, sD )
        self.add_edge( sS, sF )
        self.add_edge( sS, sH )
        self.add_edge( sT, sB )
        self.add_edge( sT, sD )
        self.add_edge( sT, sF )
        self.add_edge( sT, sH )



       


        # Consider all switches and hosts 'on'
        self.enable_all()


topos = { 'rftopo': ( lambda: RFTopo() ) }
