# coding=utf-8

from tests import XdAntTestCase
from flask import url_for


class IndexTestCase(XdAntTestCase):
    """docstring for IndexTestCase"""

    def test_demo(self):
        self.assertEqual(1, 2-1)

    def test_index(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
