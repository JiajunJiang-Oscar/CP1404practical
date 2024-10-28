"""
Wimbledon
Estimate: 30 minutes
Actual:   49 minutes

function main
    filename = wimbledon.csv
    datas = function read_data(filename)
    name_of_champions = function champions_name(data)
    country_of_champions = function champions_country(data)
    call the function information_display with name and country
function read_data
        with open filename in read model encoding = utf-8-sig as in_file
        lines = read each line in in_file
        datas = line strip space and split by "," and for line in lines start with second line
    return datas
function champions_name
    name_of_champions = empty dictionary
    for information in datas loop
        name = the last one in information
        if name in name_of_champions
            name_of_champions[name] = name_of_champions[name] + 1
        else
            name_of_champions[name] = 1
    return name_of_champions
function champions_country
    country_of_champions = for country in datas loop pick the second in country
    return country_of_champions
function information_display
    for champ_name, champ_count in items of name_of_champions
        display champ_name and champ_count
    country_number = length of country_of_champions
    display country_number and country join ","
"""


def main():
    # This function for set the filename and call all functions
    filename = "wimbledon.csv"
    datas = read_data(filename)
    name_of_champions = champions_name(datas)
    country_of_champions = champions_country(datas)
    information_display(name_of_champions, country_of_champions)


def read_data(filename):
    # This function for open and read the file with filename and return what read
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        datas = [line.strip().split(",")[:3]for line in lines[1:]]
    return datas


def champions_name(datas):
    # This function for get the champions name with return data and return the name
    name_of_champions = {}
    for information in datas:
        name = information[-1]
        if name in name_of_champions:
            name_of_champions[name] += 1
        else:
            name_of_champions[name] = 1
    return name_of_champions


def champions_country(datas):
    # This function for get the champions country with return data and return the country
    country_of_champions = {country[1] for country in datas}
    return country_of_champions


def information_display(name_of_champions, country_of_champions):
    # This function for display the champions name and country in correct format and count the number of countries
    for champ_name, champ_count in name_of_champions.items():
        print(f"{champ_name}: {champ_count}")
    country_number = len(country_of_champions)
    print(f"For these {country_number} countries have won Wimbledon:"
          f"\n{", ".join(country_of_champions)}")


main()