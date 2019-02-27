import unittest
from emergency_traffic import main
from emergency_traffic import startambulance
from emergency_traffic import check_ambulance_arrival_time
from emergency_traffic import print_target_info
from emergency_traffic import print_ambulance_info
sumo_vanet = __import__('sumo-vanet')


class test_emergency_traffic(unittest.TestCase):
	def test_main(self):
		self.assertEqual(main(),True)

	def test_startambulance(self):
		self.assertEqual(startambulance(False,0), (True,"ambulance started"))

	def test_check_ambulance_arrival_time(self):
		self.assertEqual(check_ambulance_arrival_time(), False)

	def test_print_target_info(self):
		self.assertEqual(print_target_info("4"), True)

	def test_print_ambulance_info(self):
		self.assertEqual(print_ambulance_info("9"), True )

class test_sumo_vanet(unittest.TestCase):
	def test_topology(self):
		self.assertEqual(sumo_vanet.topology(),True)



if __name__ == '__main__':
	unittest.main(exit=False)

