
from city_functions import Employee as e

def test_give_default_raise():
    lmn= e("pallavi",'Bisht',20000)
    k=lmn.salary
    lmn.give_raise()
    l=lmn.salary
    assert l-k==5000 

def test_give_custom_raise():
    lmn= e("pallavi",'Bisht',20000)
    k=lmn.salary
    lmn.give_raise(2000)
    l=lmn.salary
    assert l-k==2000 
 