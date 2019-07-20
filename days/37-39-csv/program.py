import research


# data from https://www.data.brisbane.qld.gov.au/data/dataset/food-safety-complaints

def main():
    research.init()
    print('')
    print('Here are the suburbs with the lowest number of complaints')
    for i in research.safest_suburbs():
        print(f'{i[0]} has {i[1]} food saftey complaints')
    print('')
    print('Here are the suburbs with the highest number of complaints')
    for i in research.sickest_suburbs():
        print(f'{i[0]} has {i[1]} food saftey complaints')


if __name__ == '__main__':
    main()
