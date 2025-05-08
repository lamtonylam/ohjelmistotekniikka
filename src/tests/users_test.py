import unittest

from services.elo_service import EloService

from build import build


class TestUsers(unittest.TestCase):
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

    def test_adding_user(self):
        self.user_service.create_user("tomppa")
        all_users = self.user_service.get_all_users()

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].name, "tomppa")

    def test_getting_a_user_by_username(self):
        self.user_service.create_user("tomppa")
        user = self.user_service.find_user_by_username("tomppa")

        self.assertEqual(user.name, "tomppa")

    def test_getting_a_user_by_username_that_doesnt_exist(self):
        self.user_service.create_user("tomppa")
        user = self.user_service.find_user_by_username("toooombaaa")

        self.assertEqual(user, None)

    def test_getting_a_user_by_id(self):
        self.user_service.create_user("tomppa")
        user = self.user_service.find_user_by_id(1)

        self.assertEqual(user.name, "tomppa")

    def test_getting_a_user_by_id_that_doesnt_exist(self):
        self.user_service.create_user("tomppa")
        user = self.user_service.find_user_by_id(99999999)

        self.assertEqual(user, None)

    def test_adding_user_with_same_name_doesnt_add_two_users(self):
        self.user_service.create_user("tomppa")
        with self.assertRaises(Exception):
            self.user_service.create_user("tomppa")

        all_users = self.user_service.get_all_users()
        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].name, "tomppa")
