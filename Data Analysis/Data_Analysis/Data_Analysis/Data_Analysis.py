#added functions to analyze the csv file. Added an input for the user to search for specific countries.

import csv

def analyze_csv(filename):
    entities = []
    codes = []
    years = []
    life_expectancies = []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the first line

        for line in csv_reader:
            entity = line[0]
            entities.append(entity)
            code = line[1]
            codes.append(code)
            year = line[2]
            years.append(int(year))
            life_expectancy = line[3]
            life_expectancies.append(float(life_expectancy))

    return entities, codes, years, life_expectancies


filename = "life-expectancy.csv"
entities, codes, years, life_expectancies = analyze_csv(filename)


while True:
    try:
        year_typed = input("Enter the year of interest: ")
        integer_value = int(year_typed)
        break
    except ValueError:
        print("Invalid input. Please enter a year.")

year_typed = int(year_typed)  # Convert to integer


lowest_life_expectancy = float('inf')  # Initialize with a large value
lowest_life_expectancy_year = None
lowest_life_expectancy_country = None

highest_life_expectancy = 0
highest_life_expectancy_year = None
highest_life_expectancy_country = None


for i, life_expectancy in enumerate(life_expectancies):
    if life_expectancy > highest_life_expectancy:
        highest_life_expectancy = life_expectancy
        highest_life_expectancy_year = years[i]
        highest_life_expectancy_country = entities[i]

for i, life_expectancy in enumerate(life_expectancies):
    if life_expectancy < lowest_life_expectancy:
        lowest_life_expectancy = life_expectancy
        lowest_life_expectancy_year = years[i]
        lowest_life_expectancy_country = entities[i]


print(f"The overall max life expectancy is: {highest_life_expectancy} from {highest_life_expectancy_country} in {highest_life_expectancy_year}")

print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_life_expectancy_country} in {lowest_life_expectancy_year}")


entity_in_year = []
life_expectancy_in_year = []
average_life_expectancy = 0.00

for i, year in enumerate(years):
    if year == year_typed:
        life_expectancy_in_year.append(life_expectancies[i])
        entity_in_year.append(entities[i])

if len(life_expectancy_in_year) > 0:
    highest_life_expectancy_in_year = max(life_expectancy_in_year)
    highest_life_expectancy_year_in_year = year_typed
    highest_life_expectancy_country_in_year = entity_in_year[life_expectancy_in_year.index(highest_life_expectancy_in_year)]

    lowest_life_expectancy_in_year = min(life_expectancy_in_year)
    lowest_life_expectancy_year_in_year = year_typed
    lowest_life_expectancy_country_in_year = entity_in_year[life_expectancy_in_year.index(lowest_life_expectancy_in_year)]

    average_life_expectancy = sum(life_expectancy_in_year) / len(life_expectancy_in_year)

print(f"For the year {year_typed}:\n"
      f"The average life expectancy across all countries was {average_life_expectancy:.2f}\n"
      f"The max life expectancy was in {highest_life_expectancy_country_in_year} with {highest_life_expectancy_in_year}\n"
      f"The min life expectancy was in {lowest_life_expectancy_country_in_year} with {lowest_life_expectancy_in_year}")


entity_typed = None
valid_countries = set(entities)

while entity_typed not in valid_countries:
    entity_typed = input("Enter the country of interest: ")
    if entity_typed not in valid_countries:
        print("Invalid input. Please enter a valid country.")

entity_typed = str(entity_typed)  # Convert to string


lowest_life_expectancy = float('inf')  # Reinitialize with a large value
lowest_life_expectancy_year = None
lowest_life_expectancy_country = None

highest_life_expectancy = 0
highest_life_expectancy_year = None
highest_life_expectancy_country = None

year_in_entity = []
life_expectancy_in_entity = []
average_life_expectancy = 0.00

for i, entity in enumerate(entities):
    if entity == entity_typed:
        life_expectancy_in_entity.append(life_expectancies[i])
        year_in_entity.append(years[i])

if len(life_expectancy_in_entity) > 0:
    highest_life_expectancy_in_entity = max(life_expectancy_in_entity)
    highest_life_expectancy_year_in_entity = year_in_entity[life_expectancy_in_entity.index(highest_life_expectancy_in_entity)]

    lowest_life_expectancy_in_entity = min(life_expectancy_in_entity)
    lowest_life_expectancy_year_in_entity = year_in_entity[life_expectancy_in_entity.index(lowest_life_expectancy_in_entity)]

    average_life_expectancy = sum(life_expectancy_in_entity) / len(life_expectancy_in_entity)

print(f"For the country {entity_typed}:\n"
      f"The average life expectancy across all years was {average_life_expectancy:.2f}\n"
      f"The max life expectancy was {highest_life_expectancy_in_entity} in {highest_life_expectancy_year_in_entity}\n"
      f"The min life expectancy was {lowest_life_expectancy_in_entity} in {lowest_life_expectancy_year_in_entity}")