from lib.highvalue import *

def test_init_1():
    mytest = HighValue(5,8)
    assert mytest.value_first == 5

def test_init_2():
    mytest = HighValue(5,8)
    assert mytest.value_second == 8

def test_get_highest_first():
    mytest = HighValue(8,5)
    assert mytest.get_highest() == "First value is higher"

def test_get_highest_second():
    mytest = HighValue(5,8)
    assert mytest.get_highest() == "Second value is higher"

def test_get_highest_equal():
    mytest = HighValue(5,5)
    assert mytest.get_highest() == "Values are equal"

def test_add_first():
    mytest = HighValue(5,8)
    # pass to the method
    mytest.add(5, 'first')
    # first should now == 10
    #test if first == 10
    assert mytest.value_first == 10

def test_add_second():
    mytest = HighValue(5,8)
    # pass to the method
    mytest.add(5, 'second')
    # first should now == 10
    #test if first == 10
    assert mytest.value_second == 13