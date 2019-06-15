cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = ''
    for make, model in cars.items():
        if make == 'Jeep':
            for i in model:
                if jeeps == '':
                    jeeps = jeeps + i
                else:
                    jeeps = (jeeps + ', ' + i)

    return jeeps


print(get_all_jeeps())


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    brooms = []
    for keys, values in cars.items():
        brooms.append(values[0])

    return brooms


print(get_first_model_each_manufacturer())


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    greps = []
    for makes, models in cars.items():
        for i in models:
            if grep in i.lower() or grep in i.upper():
                greps.append(i)

    return greps


print(get_all_matching_models())


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for makes, models in cars.items():
        models.sort()

    return cars


print(sort_car_models())
