#!/usr/bin/env python3



from unittest import main, TestCase
from GitGud import gud, rekt, spooked, help
import sys

class TestNetflix (TestCase):
	# ----
	# read
	# ----

	def testGud(self):
		gud(sys.stdin, sys.stdout)
		self.assertEqual(1, 1)

	def testRekt(self):
		rekt(sys.stdin, sys.stdout)
		self.assertEqual(1, 1)

	def testHelp(self):
		help()
		self.assertEqual(1, 1)






































if __name__ == "__main__":
	main()
