# Open the necessary files
input_file_path = "06.Project Input File.txt"
merge_file_path = "06.Project Merge File.txt"
output_file_path = "06.Project Output File.txt"

# Initialize counters
input_count = 0
merge_count = 0
output_count = 0

# Read and merge files
with open(input_file_path, "r") as input_file, open(merge_file_path, "r") as merge_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        input_count += 1
        if "**Insert Merge File Here**" in line:
            for merge_line in merge_file:
                output_file.write(merge_line)
                merge_count += 1
                output_count += 1
        else:
            output_file.write(line)
            output_count += 1

# Print the results
print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")