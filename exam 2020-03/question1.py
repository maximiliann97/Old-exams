fn = 'scb_degrees_per_year.csv'

# Part A

def read_degree_data(filename):
    year_labels = []
    degrees = {}
    counter = 0
    with open(filename) as file:
        file.readline()     #Skip two first lines
        file.readline()

        for line in file:
            line = line.strip().replace('"', "").split(',')
            if counter == 0:
                for item in line:
                    year_labels.append(item)
                    counter += 1
                continue
            school, degree, gender, age = line[:4]
            degrees_per_year = [int(x) for x in line[4:]]
            key = (school, degree, gender, age)
            degrees[key] = degrees_per_year

    for i in range(4):
        year_labels.pop(0)

    return degrees, year_labels

# Part B
def accumulated_degrees_per_school(degrees):
    degrees_per_school = {}
    for (school, degree, gender, age), degrees_per_year in degrees.items():
        if school in degrees_per_school:
            degrees_per_school[school] = \
            [x + y for x, y in zip(degrees_per_year, degrees_per_school[school])]
        else:
            degrees_per_school[school] = degrees_per_year

    return degrees_per_school


degrees, years = read_degree_data(fn)
degrees_per_school = accumulated_degrees_per_school(degrees)
#print(degrees_per_school)

# Part C
def print_degree_table(years, degrees_per_school):
    header = 'Year    |   CTH   KTH'
    line = '-'*24
    print(header)
    print(line)
    for item in zip(years, *degrees_per_school.values()):
        year, numbers = item[0], item[1:]
        print('{:>7s} | {:5d} {:5d}'.format(year, *numbers))


print_degree_table(years, degrees_per_school)
