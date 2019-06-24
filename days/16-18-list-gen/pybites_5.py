NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    titled = [name.title() for name in names]

    for person in titled:
        if titled.count(person) > 1:
            titled.pop(titled.index(person))

    return titled


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    title_names = [title_names.split() for title_names in names]
    title_names.sort(key=lambda x: x[1], reverse=True)
    title_names = [" ".join(title_names) for title_names in title_names]

    return title_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names = [names.split()[0] for names in names]

    name = names[0]
    for _ in names:
        if len(_) < len(name):
            name = _

    return name


if __name__ == '__main__':
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))
