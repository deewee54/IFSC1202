class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  # U = up, D = down, L = left, R = right
        self.pen = 'U'  # U = up, D = down
        self.canvas = [[' ' for _ in range(size)] for _ in range(size)]

    def printsketch(self):
        print('+' + '-' * self.size + '+')
        for y in range(self.size - 1, -1, -1):
            print('|', end='')
            for x in range(self.size):
                print(self.canvas[y][x], end='')
            print('|')
        print('+' + '-' * self.size + '+')
        print(f'X = {self.xpos}  Y = {self.ypos}  Direction = {self.direction}')

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        directions = {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'}
        self.direction = directions[self.direction]

    def turnright(self):
        directions = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
        self.direction = directions[self.direction]

    def move(self, distance):
        for _ in range(distance):
            if self.pen == 'D':
                self.canvas[self.ypos][self.xpos] = '*'

            # Move based on direction
            if self.direction == 'U':
                if self.ypos < self.size - 1:
                    self.ypos += 1
            elif self.direction == 'D':
                if self.ypos > 0:
                    self.ypos -= 1
            elif self.direction == 'L':
                if self.xpos > 0:
                    self.xpos -= 1
            elif self.direction == 'R':
                if self.xpos < self.size - 1:
                    self.xpos += 1

        # After last move, if pen is down, mark the last position
        if self.pen == 'D':
            self.canvas[self.ypos][self.xpos] = '*'

# --- Main Program ---

def main():
    # Open file manually without 'with'
    file = open('Cshape.txt', 'r')
    lines = []
    for line in file:
        line = line.strip()
        if line != '':
            lines.append(line)
    file.close()

    size = int(lines[0])
    sketch = Sketch(size)

    for line in lines[1:]:
        if ',' in line:
            parts = line.split(',')
            command = int(parts[0])
            value = int(parts[1])

            if command == 5:
                sketch.move(value)
        else:
            command = int(line)
            if command == 1:
                sketch.penup()
            elif command == 2:
                sketch.pendown()
            elif command == 3:
                sketch.turnright()
            elif command == 4:
                sketch.turnleft()
            elif command == 6:
                sketch.printsketch()

if __name__ == '__main__':
    main()