from id_not_found import IdNotFound
from bank_dao_imp import BankDAOImp
from entities.bank_class_information import Bank

bank_dao = BankDAOImp()

def test_create_acct_success():
    test_acct = Bank(0, "Checking", 01.00, 0)
    result = bank_dao.create_acct(test_acct)
    assert result.acct_id != 0	


def test_catch_non_unique_id():
    test_bank = Bank(1, "Savings", 201.00, 1)
    result = bank_dao.create_acct(test_bank)
    assert result.acct_id != 1


def test_get_acct_id_success():
    result = bank_dao.get_acct_by_id(1)
    assert result.acct_id == 1


def test_get_acct_using_non_existant_id():
    try:
        bank_dao.get_acct_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_update_acct_by_id_success():
    new_acct_type = Bank(1, "Checking", 20.00, 1)
    result = bank_dao.update_acct_by_id(new_acct_type)
    assert result.acct_name == "Checking"


def test_update_acct_using_non_existant_id():
    try:
        new_acct_name = Bank(0, "Savings", 20.01, 0)
        bank_dao.update_acct_by_id(new_acct_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"

#test for failure
"""
def test_update_acct_using_non_existant_id():
    try:
        new_acct_name = Bank(1, "Savings", 20.01, 0)
        bank_dao.update_acct_by_id(new_acct_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"
"""

def test_delete_acct_by_id_success():
    result = bank_dao.delete_acct_by_id(1)
    assert result


def test_delete_acct_with_non_existant_id():
    try:
        bank_dao.delete_acct_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"
