
import unittest
from app import app


class TestInventoryAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_check(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)

    def test_find_product(self):
        response = self.client.get("/api/products/sku300")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "USB-C Cable")
        self.assertEqual(response.json["quantity"], 50)

    def test_product_not_found(self):
        response = self.client.get("/api/products/SKU999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Product not found")


if __name__ == "__main__":
    unittest.main()