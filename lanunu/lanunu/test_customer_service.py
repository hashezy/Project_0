from bad_customer_info import BadCustomerInfo
from customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer
from customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


def test_catch_first_name_too_long_create():
    customer = Customer(0, "This is too long of a first name", "Roger")
    try:
        customer_service.service_create_customer(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_create():
    customer = Customer(0, "Roger", "This is too long of a last name")
    try:
        customer_service.service_create_customer(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Last name is too long"




def test_non_int_provided_for_id_get_customer():
    try:
        customer_service.service_get_customer_by_id("1")
    except BadCustomerInfo as e:
        assert str(e) == "Please provide a valid Id"


def test_catch_first_name_too_long_update():
    customer = Customer(1, "This is too long of a first name", "this is fine")
    try:
        customer_service.service_update_customer_information(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_update():
    customer = Customer(0, "roger", "This is too long of a last name")
    try:
        customer_service.service_update_customer_information(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Last name is too long"


def test_non_int_provided_for_id_delete():
    try:
        customer_service.service_delete_customer_by_id("1")
    except BadCustomerInfo as e:
        assert str(e) == "Please provide a valid Id"
