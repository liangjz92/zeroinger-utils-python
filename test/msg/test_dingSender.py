from unittest import TestCase
from zeroinger.msg import DingSender
import unittest
class TestDingSender(TestCase):

    def test_send_msg_to_robot(self):
        obj  =DingSender('87a7d1c5601998334c5fefe882659d11efa68495af4013cb60fd8d99765')
        obj.send_msg_to_robot('测试消息')
        # self.fail()
if __name__ == '__main__':
    unittest.main()
