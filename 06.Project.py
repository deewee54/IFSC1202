# Open the necessary files
input_file_path = "06.Project Input File.txt"
merge_file_path = "06.Project Merge File.txt"
output_file_path = "06.Project Output File.txt"

# Initialize counters
input_count = 0
merge_count = 0
output_count = 0

# Open files manually
input_file = open(input_file_path, "r")
merge_file = open(merge_file_path, "r")
output_file = open(output_file_path, "w")

# Read and merge files
for line in input_file:
    if line.strip() == "**Insert Merge File Here**":
        for merge_line in merge_file:
            output_file.write(merge_line)
            merge_count += 1
            output_count += 1
    else:
        output_file.write(line)
        input_count += 1
        output_count += 1

# Close all files
input_file.close()
merge_file.close()
output_file.close()

# Print the results
print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")