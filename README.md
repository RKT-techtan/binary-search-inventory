BinarySearch Inventory

A simple lookup application built with pythone, flask, html, css and javascript. It uses binary search to find products by SKU in a sorted inventory.

Features
. Search products by sku.
. Use binary search to locate products efficiently.
. Display product name, category, price and stock quantity.
. Handle missing products and empty search input.
. Test the search algorithm and API using pythons unnitest framework.

Tech Stack
. Python --- binary search algorithm and backend logic.
. Flask ---- API and web server.
. HTML ----- Page structure.
. CSS ------ Styling and responsive layout.
. CSV ------ Sample inventory data.
. unittest - automated tests.

Project structre
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

Getting started
1. Install python and flask
Make sure python is installed. Open a terminal in the backend directory and run:
. python -m pip install flask

2. Start the application
From the backend directory run:
. python app.py
Open this adress in browser:
. http://127.0.0.1:5000/

3. Run the tests:
Stop the server ctrl + c, then, from backend directory run:
. python -m unittest discover -v

Example searches:

SKU100
Wireless Mouse
Product details returned

SKU300
USB-C Cable
Product details returned

SKU999
—
Product not found

What I learned
. Implementing binary search in Python
. Working with sorted data and SKU lookups
. Connecting a frontend to a FLASK API
. Reading inventory data from a csv file
. Writing automated tests for algorithms and API endpoints

Future Improvements
. Add product-name search if needed
. Improve input validation and error handling
. Deploy the application