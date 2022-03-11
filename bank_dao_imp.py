from id_not_found import IdNotFound
from bank_dao_interface import BankDAOInterface
from entities.bank_class_information import Bank



class BankDAOImp(BankDAOInterface):


    def __init__(self):
        acct_needed_for_id_catch = Bank(1, "Checking", 00.00, 1)
        self.accts_list = []
        self.id_generator = 2

        self.accts_list.append(acct_needed_for_id_catch)

    def create_acct(self, acct: Bank) -> Bank:
        acct.acct_id = self.id_generator  
        self.id_generator += 1  
        self.accts_list.append(acct)
        return acct

    def get_acct_by_id(self, acct_id: int) -> Bank:
        for acct in self.accts_list:
            if acct.acct_id == acct_id:
                return acct
        raise IdNotFound("No account matches the id given: please try again!")

    def update_acct_by_id(self, acct: Bank) -> Bank:
        for old_acct in self.accts_list:
            if acct.acct_id == old_acct.acct_id:
                old_acct = acct
                return old_acct
        raise IdNotFound("No account matches the id given: please try again!")

    def delete_acct_by_id(self, acct_id: int) -> bool:
        for account in self.accts_list:
            if account.acct_id == acct_id:
                self.accts_list.remove(account)
                return True
        raise IdNotFound("No account matches the id given: please try again!")

