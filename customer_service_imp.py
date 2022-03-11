from bad_customer_info import BadCustomerInfo
from entities.customer_class_information import Customer
from customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_customer(self, customer: Customer) -> Customer:
        if len(customer.first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(customer.last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        return self.customer_dao.create_customer(customer)

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        if type(customer_id) == int:
            return self.customer_dao.get_customer_by_id(customer_id)
        else:
            raise BadCustomerInfo("Please provide a valid Id")

    def service_update_customer_information(self, customer: Customer) -> Customer:
        if len(customer.first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(customer.last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        return self.customer_dao.update_customer_by_id(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        if type(customer_id) == int:
            return self.customer_dao.delete_customer_by_id(customer_id)
        else:
            raise BadCustomerInfo("Please provide a valid Id")
