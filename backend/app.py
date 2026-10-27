import csv
from pathlib import Path

from flask import Flask, jsonify, send_from_directory

from binary_search import binary_search

app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path="/static"
)

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = BASE_DIR / "products.csv"


def load_products():
    with open(PRODUCTS_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Inventory API is running"
    })


@app.route("/api/products/<sku>", methods=["GET"])
def get_product(sku):
    products = load_products()
    skus = [product["sku"] for product in products]

    sku = sku.strip().upper()
    index = binary_search(skus, sku)

    if index == -1:
        return jsonify({"error": "Product not found"}), 404

    product = products[index]

    return jsonify({
        "sku": product["sku"],
        "name": product["name"],
        "category": product["category"],
        "price": float(product["price"]),
        "quantity": int(product["quantity"])
    })


if __name__ == "__main__":
    app.run(debug=True)