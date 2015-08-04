class SolveMeSecond:
    def __init__(self, lines, values):
        self._set_constraints()
        self.lines = int(lines)
        self.values = values
        self.output = []

    def _set_constraints(self):
        self.lines_minimum_size = 1
        self.element_maximum_size = 1000
        self.element_minimum_size = 0

    def _verify_size(self):
        if self.lines <= self.lines_minimum_size:
            exit(0)

    def _verify_elements(self, x):
        if int(x) > self.element_maximum_size or int(x) < self.element_minimum_size:
            exit(0)

    def _read_lines(self):
        self._verify_size()
        for x in self.values:
            self._sum_each_row(x.split())

    def _sum_each_row(self, values):
        acum = 0
        for x in values:
            self._verify_elements(int(x))
            acum += int(x)
        self.output.append(acum)

    def resolve(self):
        self._read_lines()
        return self.output

def main():
    lines = int(input())
    values = []
    for x in range(0, lines):
        read_line = input()
        values.append(read_line)

    output = SolveMeSecond(lines, values).resolve()
    for x in output:
        print(x)

if __name__ == "__main__":
    main()
