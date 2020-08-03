from unittest import TestCase
from zeroinger.msg import FeishuSender
import unittest
class TestDingSender(TestCase):

    def test_send_msg_to_robot(self):
        obj  =FeishuSender('cli_9fa2afe0b072100e','upP4TyBqDkuiBl6lgzm8MfqJG2Ray8Zy')
        # obj.send_message('测试消息')
        token = obj._get_tenant_access_token()

        print(token)
        group = obj.list_group()
        print(group)
        admin = obj.list_admin()
        print(admin)
        # self.fail()


if __name__ == '__main__':
    unittest.main()
