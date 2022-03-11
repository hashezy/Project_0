from id_not_found import IdNotFound
from customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer

customer_dao = CustomerDAOImp()

def test_create_customer_success():
    test_customer = Customer(0,"New","Customer")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0


def test_catch_non_unique_id():
    test_customer = Customer(1,"Bad","Id")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1


def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_by_id(1)
    assert result.customer_id == 1


def test_get_acct_using_non_existant_id():
    try:
        customer_dao.get_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


def test_update_acct_by_id_success():
    new_customer_name = Customer(1, "John", "Doe")
    result = customer_dao.update_customer_by_id(new_customer_name)
    assert result.first_name == "John"


def test_update_acct_using_non_existant_id():
    try:
        new_customer_name = Customer(0,"Shmitty","Begoods")
        customer_dao.update_customer_by_id(new_customer_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


def test_delete_team_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_team_with_non_existant_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"
