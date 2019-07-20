import research


# data from https://www.data.brisbane.qld.gov.au/data/dataset/food-safety-complaints

def main():
    research.init()

    print("Safest 5 suburbs to eat out")
    print(research.data)
    print(research.safest_suburbs())
    print(research.sickest_suburbs())


if __name__ == '__main__':
    main()
