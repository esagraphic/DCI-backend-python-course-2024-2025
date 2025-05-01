import unittest

from .src.server import Server


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        self.server1 = Server()
        self.server2 = Server()

    def test_server_uses_metaclass(self):
        _type = str(type(Server))
        self.assertEqual(
            "<class 'src.singleton.MetaSingleton'>",
            _type,
            "Server should use MetaSingleton as it's type",
        )

    def test_server_is_singleton(self):
        self.assertIs(
            self.server1,
            self.server2,
            "server1 and server2 are not the same. Hence, not singleton.",
        )


if __name__ == "__main__":
    unittest.main()
