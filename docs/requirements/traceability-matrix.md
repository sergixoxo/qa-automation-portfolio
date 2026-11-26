
# Requirements Traceability Matrix (RTM)

## Overview

- Application: SauceDemo
- User Story: US-001 — Shopping Cart Management
- Module: Shopping Cart and Checkout
- Automation Framework: Playwright and Pytest

## Traceability Matrix

| User Story | Acceptance Criterion | Test Case | Automated Test | Result | Related Defect |
|---|---|---|---|---|---|
| US-001 | CA-01 | TC-001 | test_complete_purchase_flow | PASSED | N/A |
| US-001 | CA-02 | TC-002 | test_complete_purchase_flow | PASSED | N/A |
| US-001 | CA-03 | TC-003 | test_complete_purchase_flow | PASSED | N/A |
| US-001 | CA-04 | TC-004 | test_complete_purchase_flow | PASSED | N/A |
| US-001 | CA-05 | TC-005 | test_complete_purchase_flow | PASSED | N/A |
| US-001 | CA-06 | TC-006 | test_checkout_with_empty_cart | XFAIL | BUG-003 |

## Coverage Summary

- Total user stories: 1
- Total acceptance criteria: 6
- Designed test cases: 6
- Acceptance criteria covered by automation: 6
- Automated test functions: 2
- Acceptance criteria satisfied: 5
- Acceptance criteria not satisfied: 1
- Requirements automation coverage: 100%
- Acceptance criteria satisfaction rate: 83.33%

## Related Documentation

- [User Story US-001](US-001.md)
- [Shopping Cart Test Cases](../test-cases/shopping-cart.md)
- [BUG-003 — Checkout Allowed with an Empty Cart](../bugs/BUG-003.md)
- [Automated Purchase Tests](../../tests/test_saucedemo_purchase.py)

## Notes

Multiple acceptance criteria are validated within a
single end-to-end automated test.

The XFAIL result represents a reproduced potential
defect associated with a proposed business rule.

The acceptance criteria were defined for portfolio
purposes and are not official SauceDemo requirements.

Coverage does not imply that all requirements are
satisfied or that the application is defect-free.
