# coding=utf-8

from tests import XDANTTestCase
from flask import url_for


class IndexTestCase(XDANTTestCase):
    """docstring for IndexTestCase"""

    def test_demo(self):
        self.assertEqual(1, 2 - 1)

    def test_index(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)


class TestAdminAPI(XDANTTestCase):
    """docstring for TestAdminAPI"""

    def test_register(self):
        response = self.client.get(url_for('main.login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'windard',
            'email': 'mail@mail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post('api.register', data=data)
        self.assertEqual(response.status_code, 404)

    def test_login(self):
        response = self.client.get(url_for('main.login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'windard',
            'email': 'password'
        }
        response = self.client.post(url_for('api.sessions'), data=data)
        self.assertEqual(response.status_code, 200)
