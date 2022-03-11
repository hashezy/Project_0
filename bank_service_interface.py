from abc import ABC, abstractmethod

from entities.bank_class_information import Bank

class BankServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_acct(self, acct: Bank) -> Bank:
        pass

    # read
    @abstractmethod
    def service_get_acct_by_id(self, acct_id: str) -> Bank:
    	pass

    # update
    @abstractmethod
    def service_update_acct_by_id(self, acct: Bank) -> Bank:
    	pass

    # delete
    @abstractmethod
    def service_delete_acct_by_id(self, acct_id: int) -> bool:
    	pass
