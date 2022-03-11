from bad_bank_info import BadBankInfo
from bank_dao_imp import BankDAOImp
from entities.bank_class_information import Bank
from bank_service_imp import BankServiceImp

acct_dao = BankDAOImp()
acct_service = BankServiceImp(acct_dao)

same_acct = Bank(0, "Checking", 400.01, 0)
non_string_acct_type = Bank(0, 10.7, 50.01, 0)
non_float_balance = Bank(0, "Savings", True, 0)
no_change_same_acct_update = Bank(1, "Checking", 45.45, 0)
non_string_acct_type_update = Bank(1, 10.7, 250.01, 0)


def test_check_same_acct_type():
    try:
        acct_service.service_create_acct(same_acct)
        assert False
    except BadBankInfo as e:
        assert str(e) == "This is the same account type"


def test_balance_not_a_float_type():
    try:
        acct_service.service_create_acct(non_float_balance)
        assert False
    except BadBankInfo as e:
        assert str(e) == "The bank can only withdraw and deposit numeric amounts"


def test_catch_non_string_acct_name_create_acct():
    try:
        acct_service.service_create_acct(non_string_acct_type)
        assert False
    except BadBankInfo as e:
        assert str(e) == "Please pass in a valid account type, Checking or Savings"


def test_cant_typecast_to_int(): #because of the new features I need to add, I actually need to change this test
    try:
        acct_service.service_get_acct_by_id("one")
        assert False
    except BadBankInfo as e:
        assert str(e) == "Please provide a valid acct Id"

def test_get_acct_successfuly_typecast_string():
    result = acct_service.service_get_acct_by_id("1")
    assert result.acct_id == 1


def test_same_acct_update():
    try:
        acct_service.service_update_acct_by_id(no_change_same_acct_update)
        assert False
    except BadBankInfo as e:
        assert str(e) == "This is the correct account type"
	

def test_catch_non_string_acct_type_update_acct():
    try:
        acct_service.service_update_acct_by_id(non_string_acct_type_update)
        assert False
    except BadBankInfo as e:
        assert str(e) == "Please pass in a valid account type, Checking or Savings"


def test_catch_non_numeric_id_delete_acct():
    try:
        acct_service.service_delete_acct_by_id("one")
        assert False
    except BadBankInfo as e:
        assert str(e) == "Please provide a valid account Id"
