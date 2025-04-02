import csv

def load_distance_table(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            distance_table = [row for row in reader]
        return distance_table
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)

def print_distance_table(distance_table):
    for row in distance_table:
        print("\t".join(row))

def find_city_index(city, city_list):
    try:
        return city_list.index(city)
    except ValueError:
        return -1

def main():
    filename = "09.Project Distances.csv"
    distance_table = load_distance_table(filename)
    
    print("\nDistance Table:\n")
    print_distance_table(distance_table)
    
    from_city = input("Enter From City: ").strip().title()
    to_city = input("Enter To City: ").strip().title()
    
    row_index = find_city_index(from_city, [row[0] for row in distance_table])
    col_index = find_city_index(to_city, distance_table[0])
    
    if row_index == -1:
        print("Invalid From City")
    elif col_index == -1:
        print("Invalid To City")
    else:
        distance = distance_table[row_index][col_index]
        print(f"{from_city} to {to_city} - {distance} miles")

if __name__ == "__main__":
    main()