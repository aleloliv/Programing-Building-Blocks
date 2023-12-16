youngest_age = 100
youngest_person = ""

with open("test.txt") as test_file: 
    for line in test_file:
        line = line.split(" ")
        person = line[0]
        age = int(line[1])

        if (age < youngest_age):
            youngest_age = age
            youngest_person = person


    print(youngest_person, youngest_age)

line = "     text"

line.strip()

print(line)