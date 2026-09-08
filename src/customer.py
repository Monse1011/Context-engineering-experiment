from dataclasses import dataclass
import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    created_by: str
    updated_by: str


def update_customer_email(customer: Customer, new_email: str, updated_by: str):
    if customer is None:
        raise ValueError("customer not found")
    if not isinstance(new_email, str) or not EMAIL_PATTERN.match(new_email):
        raise ValueError("Invalid email")

    customer.email = new_email.lower()
    customer.updated_by = updated_by
    return customer


