import unittest
from charpy.factory import create_app


class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_404_not_found(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/404', content_type='html/text')
        self.assertTrue(b'WAS NOT FOUND' in response.data)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
