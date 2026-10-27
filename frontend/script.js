
const skuInput = document.getElementById("sku-input");
const searchButton = document.getElementById("search-button");
const statusMessage = document.getElementById("status-message");
const productResult = document.getElementById("product-result");

const productName = document.getElementById("product-name");
const productSku = document.getElementById("product-sku");
const productCategory = document.getElementById("product-category");
const productPrice = document.getElementById("product-price");
const productQuantity = document.getElementById("product-quantity");

async function searchProduct() {
    const sku = skuInput.value.trim().toUpperCase();

    productResult.hidden = true;
    statusMessage.className = "";

    if (!sku) {
        statusMessage.textContent = "Please enter a product SKU.";
        statusMessage.classList.add("error");
        return;
    }

    statusMessage.textContent = "Searching inventory...";
    searchButton.disabled = true;

    try {
        const response = await fetch(
            `/api/products/${encodeURIComponent(sku)}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Product not found.");
        }

        productName.textContent = data.name;
        productSku.textContent = data.sku;
        productCategory.textContent = data.category;
        productPrice.textContent = Number(data.price).toLocaleString();
        productQuantity.textContent = data.quantity;

        productResult.hidden = false;
        statusMessage.textContent = "Product found!";
        statusMessage.classList.add("success");
    } catch (error) {
        statusMessage.textContent =
            error.message || "Unable to connect to the inventory server.";
        statusMessage.classList.add("error");
    } finally {
        searchButton.disabled = false;
    }
}

searchButton.addEventListener("click", searchProduct);

skuInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        searchProduct();
    }
});
