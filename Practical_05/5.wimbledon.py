"""
Write a program to read this file, process the data and display processed information.
the champions and how many times they have won.
the countries of the champions in alphabetical order
"""

FILENAME = 'wimbledon.csv'


def main():
    """display the count of how many time champions and the countries that won the wimbledon"""
    data_list = load_data(FILENAME)

    data_dictionary = {}
    column_names = data_list[0]
    column_names[1] = 'Country champion'
    column_names[4] = 'Country Runner-up'

    for number in range(len(column_names)):
        data_dictionary[column_names[number]] = []
        for line in data_list[1:]:
            data_dictionary[column_names[number]].append(line[number])

    champions_count = count_champion(data_dictionary)
    champions_unique = sorted(find_country(data_dictionary))
    for person in champions_count.keys():
        print(f'{person.title()} {champions_count[person]}')
    print(f'These {len(champions_unique)} countries have won Wimbledon:')
    print(', '.join(champions_unique))


def find_country(data_dictionary):
    """find the list of champion country"""
    champions_countries = data_dictionary['Country champion']
    champion_unique = []
    for champion in champions_countries:
        if champion not in champion_unique:
            champion_unique.append(champion)
    return champion_unique


def count_champion(data_dictionary):
    """counting how many time a champion has won the wimbledon"""
    champions_persons = data_dictionary['Champion']
    champions_count = {}
    for person in champions_persons:
        if person not in champions_count.keys():
            champions_count[person] = 1
        else:
            champions_count[person] += 1
    return champions_count


def load_data(filename):
    """load the data to a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        data_list = []
        for line in data:
            item = line.strip().split(",")
            data_list.append(item)
    return data_list


main()