from bad_bank_info import BadBankInfo
from bank_dao_interface import BankDAOInterface
from entities.bank_class_information import Bank
from bank_service_interface import BankServiceInterface

class BankServiceImp(BankServiceInterface):

    def __init__(self, acct_dao: BankDAOInterface):
        self.acct_dao = acct_dao

    def service_create_acct(self, acct: Bank) -> Bank:
        if type(acct.acct_name) != str:
            raise BadBankInfo("Please pass in a valid account type, Checking or Savings")
        elif type(acct.acct_balance) != float:
            raise BadBankInfo("The bank can only withdraw and deposit numeric amounts")
        for existing_acct in self.acct_dao.accts_list:
            if existing_acct.acct_name == acct.acct_name:
                raise BadBankInfo(
                    "This is the same account type")
        return self.acct_dao.create_acct(acct)

    def service_get_acct_by_id(self, acct_id: str) -> Bank:
        try:
            return self.acct_dao.get_acct_by_id(int(acct_id))
        except ValueError:
            raise BadBankInfo("Please provide a valid acct Id")

    def service_update_acct_by_id(self, acct: Bank) -> Bank:
        if type(acct.acct_name) != str:
            raise BadBankInfo("Please pass in a valid account type, Checking or Savings")
        for existing_acct in self.acct_dao.accts_list:
            if existing_acct.acct_name == acct.acct_name: 
                raise BadBankInfo("This is the correct account type") 
        return self.acct_dao.update_acct_by_id(acct) 

    def service_delete_acct_by_id(self, acct_id: int) -> bool:
        if type(acct_id) == int:
            return self.acct_dao.delete_acct_by_id(acct_id)
        else:
            raise BadBankInfo("Please provide a valid account Id")
"""
    def service_deposit_withdraw(self, acct: Bank) -> Bank:
        for existing_acct in self.acct_dao.accts_list:
            if existing_acct.acct_id == acct.acct_id and acct.acct_balance > existing_acct.acct_balance:
                deposit = acct.acct_balance - existing_acct.acct_balance
                print(f"You deposited ${deposit} successfully")
            elif existing_acct.acct_id == acct.acct_id and acct.acct_balance < existing_acct.acct_balance:
                withdraw = existing_acct.acct_balance - abs(acct.acct_balance)
                print(f"You withdrew ${withdraw} successfully")
            elif acct.acct_balance == 0:
                raise BadBankInfo("This is the correct account type")
        return self.acct_dao.update_acct_by_id(acct)
"""
