from unittest.case import TestCase
from integration import ci
from helpers import HTTPClient
import logging
logging.basicConfig(format=':%(lineno)d: %(asctime)s %(message)s', level=logging.DEBUG)

class Base(TestCase):
    def get_admin_node_ip(self):
        return str(ci.environment.node['admin'].ip_address)

    def get_id_by_mac(self, mac_address):
        return mac_address.replace(":", "").upper()
