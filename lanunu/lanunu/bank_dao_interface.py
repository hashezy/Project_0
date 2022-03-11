from abc import ABC, abstractmethod

from entities.bank_class_information import Bank


class BankDAOInterface(ABC):

    # create
    @abstractmethod
    def create_acct(self, acct: Bank)-> Bank:
        pass

    # read
    @abstractmethod
    def get_acct_by_id(self, acct_id: int)-> Bank:
        pass

    # update
    @abstractmethod
    def update_acct_by_id(self, acct: Bank)-> Bank:
        pass

    # delete
    @abstractmethod
    def delete_acct_by_id(self, acct_id: int)-> bool:
        pass
