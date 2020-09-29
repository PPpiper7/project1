def main():
    infies = open('week7/cities.txt','r')
    cities = infies.readlines()
    infies.close()
    index = 0
    while index < lne(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print(cities)
main()