#!/usr/bin/env python

import unittest
import os
import re
from mininet.util import quietRun, pexpect


class testnetworktopo( unittest.TestCase ):
    prompt = 'mininet>'

    def test_networktopo( self ):
        p = pexpect.spawn( 'sudo python network-topo.py' )
        p.expect( self.prompt )
        p.sendline( 'exit' )
        p.wait()
        p.expect( pexpect.EOF )



if __name__ == '__main__':
    unittest.main()
