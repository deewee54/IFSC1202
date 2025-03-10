input_file = "07.Project Angles Input.txt"
output_file = "07.Project Angles Output.txt"

infile = open(input_file, 'r')
lines = infile.readlines()
infile.close()

decimal_values = []
for line in lines:
    line = line.strip()
    if line:
        degrees = float(line.split('°')[0])
        minutes = float(line.split('°')[1].split("'")[0])
        seconds = float(line.split("'")[1].split('"')[0])
        decimal_value = degrees + (minutes / 60) + (seconds / 3600)
        decimal_values.append(decimal_value)

outfile = open(output_file, 'w')
for value in decimal_values:
    outfile.write(f"{value}\n")
outfile.close()

print(f"{len(decimal_values)} records processed")