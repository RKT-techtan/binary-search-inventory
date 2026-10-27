BinarySearch Inventory

A simple inventory lookup web application built with Python and Flask. It uses binary search to find products by SKU and displays their details.

Features

- Search for products by SKU
- Use binary search to locate products in sorted inventory data
- Display product name, category, price, and stock quantity
- Handle missing products and empty search input
- Test the search algorithm and API using Python's `unittest` framework

Tech Stack

1. Python — Binary search algorithm and backend logic
2. Flask — API and web server
3. HTML — Page structure
4. CSS — Styling and responsive layout
5. JavaScript — Search interaction and API requests
6. CSV — Sample inventory data
7. unittest — Automated tests

Project Structure

~~~
binary-search-inventory/
├── backend/
│   ├── app.py
│   ├── binary_search.py
│   ├── products.csv
│   ├── test_app.py
│   └── test_binary_search.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md
~~~

Getting Started

Prerequisites
- Python 3
- Flask

1. Open the backend directory
bash cd backend

2. Install Flask
bash python -m pip install flask

3. Start the application
bash python app.py

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

Keep the terminal running while you use the application.

Running the Tests

Open a second terminal in VS Code and navigate to the backend directory:
bash cd backend

Run the automated tests:
bash python -m unittest discover -v

The tests check the binary search algorithm, the API health endpoint, successful product lookups, and missing products.

Example Searches
~~~
| SKU | Product | Expected result |
|---|---|---|
| `SKU100` | Wireless Mouse | Product found |
| `SKU300` | USB-C Cable | Product found |
| `SKU999` | — | Product not found |
~~~

What I Learned
- Implementing binary search in Python
- Working with sorted data and search boundaries
- Building API endpoints with Flask
- Connecting a frontend to a backend using JavaScript
- Loading inventory data from a CSV file
- Writing automated tests with `unittest`
- Organizing and publishing a project using Git and GitHub

Future Improvements
- Add inventory items dynamically
- Support searching by product name
- Store inventory data in a database