from city_functions import get_name
def test_city_country():
    correct_string= get_name('santiago','chile')
    assert correct_string=='santiago, chile'

def test_city_country_population():    
    correct_string= get_name('santiago','chile','19386912864')
    assert correct_string=='santiago, chile -19386912864'