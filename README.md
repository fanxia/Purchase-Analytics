# Purchase-Analytics

## Table of Contents
1. [Problem Approaching](README.md#problem)
1. 
1. ![#f03c15](https://placehold.it/15/f03c15/000000?text=+)[Running Instructions](README.md#instructions)
1. [Output](README.md#output)
1. [Questions?](README.md#questions?)

## Problem

Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders. We calculate for each department, the number of times a product was ordered, number of times a product was ordered for the first time and the ratio of those two number.

We loop through the products to find the corresponding department and save the infomatin as a dictionary. Then we loop through the orders, for each product, use the previous dict to check its department id, and increase the order number for that department by 1. If that product wasn't ordered before, increase the new order number for that department by 1.


## Running Instruction

### Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── purchase_analytics.py
    ├── input
    │   └── products.csv
    |   └── order_products.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── products.csv
            |   │   └── order_products.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── your-own-products.csv
                |   └── your-own-order_products.csv
                |── output
                    └── report.csv

### Default Setting

* Input product file: `../input/products.csv`
* Input order_product file: `../input/order_products.csv`
* Output file: `../output/report.csv`
![#f03c15](https://placehold.it/15/f03c15/000000?text=+)[Please modify the setting in `run.sh`]

### Run Script

* `chmod +x run.sh`
* `./run.sh`


# Questions?
Email me at fanxia08@gmail.com
