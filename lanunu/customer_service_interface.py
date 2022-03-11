from abc import ABC, abstractmethod

from customer_dao_imp import CustomerDAOImp
from customer_dao_interface import CustomerDAOInterface
from entities.customer_class_information import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao: CustomerDAOImp = customer_dao

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass
