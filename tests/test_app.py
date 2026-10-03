import json
import threading
import unittest
import urllib.error
import urllib.request

from app.main import make_server


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0, "127.0.0.1")  # port 0 = any free port
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def get(self, path):
        return urllib.request.urlopen(self.base + path, timeout=5)

    def test_root_returns_greeting(self):
        with self.get("/") as r:
            self.assertEqual(r.status, 200)
            self.assertIn("Hello", r.read().decode())

    def test_healthz_is_ok_and_non_empty(self):
        with self.get("/healthz") as r:
            self.assertEqual(r.status, 200)
            self.assertTrue(r.read().strip())

    def test_notes_returns_list(self):
        with self.get("/notes") as r:
            notes = json.loads(r.read().decode())
        self.assertIsInstance(notes, list)
        self.assertGreaterEqual(len(notes), 1)
        self.assertIn("text", notes[0])

    def test_unknown_path_is_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.get("/nope")
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
