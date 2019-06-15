from cars import (get_all_jeeps, get_first_model_each_manufacturer, get_all_matching_models, sort_car_models)


def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    actual = get_first_model_each_manufacturer()
    assert type(actual) == list
    assert actual == expected

