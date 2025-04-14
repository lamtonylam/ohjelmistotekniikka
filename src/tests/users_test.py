import unittest

from services.elo_service import EloService

from build import build

class TestUserCreation(unittest.TestCase):
    def setUp(self):
        build()
        self.user_service = EloService()

    def test_getting_all_users(self):
        self.user_service.create_user("tomppa1")
        self.user_service.create_user("tomppa2")
        
        all_users = self.user_service.get_all_users()

        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].name, "tomppa1")
        self.assertEqual(all_users[1].name, "tomppa2")