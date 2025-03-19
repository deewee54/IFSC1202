filename = "constitution.txt"

# Read the Constitution text file into a list of lines
file = open(filename, "r", encoding="utf-8")
lines = file.readlines()
file.close()

# Remove trailing newline characters but keep blank lines
lines = [line.rstrip('\n') for line in lines]

while True:
    term = input("\nEnter search term: ")
    if not term:
        break
    
    index = 0
    while index < len(lines):
        if term.lower() in lines[index].lower():
            # Find the start of the section (first preceding blank line)
            start = index
            while start > 0 and lines[start] != "":
                start -= 1
            
            # Ensure start includes the preceding blank line
            if start > 0:
                start -= 1
            
            # Find the end of the section (next blank line)
            end = index
            while end < len(lines) and lines[end] != "":
                end += 1
            
            # Print the section, including correct blank line handling
            for i in range(start, end + 1):
                print(f"Line {i + 1}: {lines[i]}")
            
            index = end  # Skip to the end of the section to avoid duplicate printing
        else:
            index += 1