
# Shopping Cart — Test Cases

## Overview

- Related User Story: US-001
- Application: SauceDemo
- Module: Shopping Cart and Checkout
- Environment: https://www.saucedemo.com/

## Common Preconditions

- The user is logged in as `standard_user`.
- The inventory page is displayed.
- The shopping cart is empty.

## TC-001 — Add Product to Cart

**Acceptance Criterion:** CA-01\
**Type:** Positive\
**Priority:** High

### Steps

1. Locate Sauce Labs Backpack.
2. Click "Add to cart".

### Expected Result

The product is successfully added to the shopping cart.

## TC-002 — Validate Cart Counter

**Acceptance Criterion:** CA-02\
**Type:** Positive\
**Priority:** Medium

### Steps

1. Add Sauce Labs Backpack to the cart.
2. Observe the shopping cart counter.

### Expected Result

The shopping cart counter displays 1.

## TC-003 — Validate Product Button

**Acceptance Criterion:** CA-03\
**Type:** Positive\
**Priority:** Medium

### Steps

1. Locate Sauce Labs Backpack.
2. Click "Add to cart".
3. Observe the product button.

### Expected Result

The button changes from "Add to cart" to "Remove".

## TC-004 — Validate Product Visibility in Cart

**Acceptance Criterion:** CA-04\
**Type:** Positive\
**Priority:** High

### Steps

1. Add Sauce Labs Backpack to the cart.
2. Open the shopping cart.
3. Inspect the cart contents.

### Expected Result

Sauce Labs Backpack is displayed in the shopping cart.

## TC-005 — Validate Product Information

**Acceptance Criterion:** CA-05\
**Type:** Positive\
**Priority:** High

### Steps

1. Add Sauce Labs Backpack to the cart.
2. Open the shopping cart.
3. Verify the product name, price, and quantity.

### Expected Result

- Product name: Sauce Labs Backpack.
- Price: $29.99.
- Quantity: 1.

## TC-006 — Attempt Checkout with an Empty Cart

**Acceptance Criterion:** CA-06\
**Type:** Negative\
**Priority:** High

### Steps

1. Open the shopping cart without adding products.
2. Verify that the cart is empty.
3. Click "Checkout".
4. If allowed, enter valid customer information.
5. Continue to the checkout overview.
6. Attempt to complete the purchase.

### Expected Result

The system prevents the customer from completing a purchase with an empty shopping cart.

### Actual Result

The system allows the customer to complete a purchase without any products in the shopping cart.

### Execution Status

FAILED — Manual execution.

### Related Defect

BUG-003 — Checkout Allowed with an Empty Cart (potential defect).
