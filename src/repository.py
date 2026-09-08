from src.customer import Customer, update_customer_email

class CustomerRepository:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def save(self, customer):
        self.customers[customer.customer_id] = customer

    def update_customer_email(self, customer_id: int, new_email: str, updated_by: str):
        customer = self.get_customer(customer_id)
        if customer is None:
            raise ValueError("customer not found")
        customer = update_customer_email(customer, new_email, updated_by)
        self.save(customer)
        return customer


    