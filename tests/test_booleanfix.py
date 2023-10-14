from booleanfix import true, false, null, undefined

def test_true():
    assert true


def test_false():
    assert not false


def test_if_true():
    if true:
        assert True
    else:
        assert False


def test_if_false():
    if false:
        assert False
    else:
        assert True


def test_false_false():
    assert false == false
    assert false == False
    assert False == false
    assert False == False


def test_false_true():
    assert false != true
    assert false != True
    assert False != true
    assert False != True


def test_true_false():
    assert true != false
    assert true != False
    assert True != false
    assert True != False


def test_true_true():
    assert true == true
    assert true == True
    assert True == true
    assert True == True


def test_false_false():
    assert false is false
    assert false is False
    assert False is false
    assert False is False


def test_false_true():
    assert false is not true
    assert false is not True
    assert False is not true
    assert False is not True


def test_true_false():
    assert true is not false
    assert true is not False
    assert True is not false
    assert True is not False


def test_true_true():
    assert true is true
    assert true is True
    assert True is true
    assert True is True


def test_null():
    assert null is None


def test_undefined():
    assert undefined is None


def test_null_undefined():
    assert null == undefined


def test_null_is_undefined():
    assert null is undefined


def test_undefined_null():
	assert undefined == null


def test_undefined_is_null():
	assert undefined is null


def test_null_true():
	assert null != true


def test_null_false():
	assert null != false


def test_undefined_true():
	assert undefined != true


def test_undefined_false():
	assert undefined != false


def test_array_manipulation():
    array = [1, 2, 3, 4, 5]
    for i in range(len((array))):
        if array[i] % 2 == 0:
            array[i] = true
        else:
            array[i] = false

    assert array == [false, true, false, true, false]


def test_array_element_type_and_value():
    array = [1, 2, 3, 4, 5]
    for i in range(len((array))):
        if array[i] % 2 == 0:
            array[i] = true
        else:
            array[i] = false

    for elem in array:
        assert type(elem) == bool
        assert isinstance(elem, bool)
        assert elem in [true, false]


def test_array_index_error():
    array = [1, 2, 3, 4, 5]
    try:
        _ = array[5]
        assert False
    except IndexError:
        assert True


def test_array_null_comparison():
    array = [1, 2, 3, 4, 5]
    array.append(null)

    assert array[5] == null
    assert array[5] is null
