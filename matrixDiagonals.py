#! python3

class Diagonals:
    def __init__(self, size, matrix):
        self._set_constraints()
        self.size = int(size)
        self.matrix = self._set_matrix_values(matrix)
        self.first = self._get_first_diagonal()
        self.second = self._get_second_diagonal()


    def _set_constraints(self):
        self.matrix_maximum_size = 100
        self.matrix_minimum_size = 1
        self.element_maximum_size = 100
        self.element_minimum_size = -100

    def _verify_size(self):
        if self.size > self.matrix_maximum_size or self.size < self.matrix_minimum_size:
            exit(0)

    def _verify_elements(self, line):
        for x in line:
            if int(self.element_maximum_size) > 100 or int(self.element_minimum_size) < -100:
                exit(0)

    def _get_first_diagonal(self):
        ## self.matrix[0][0] + self.matrix[1][1] + self.matrix[2][2]
        first = 0
        for x in range(0, self.size):
            first += int(self.matrix[x][x])
        return(first)

    def _get_second_diagonal(self):
        ## self.matrix[2][0] + self.matrix[1][1] + self.matrix[0][2]
        second = 0
        acum = (self.size)
        for x in range(0, self.size):
            acum -= 1
            second += int(self.matrix[acum][x])
        return(second)

    def _set_matrix_values(self, matrix):
        self._verify_size()
        m = []
        for x in matrix:
            self._verify_elements(x.split())
            m.append(x.split())
        return m

    def _sum_diagonal(self):
        return(self.first - self.second)

    def resolve(self):
        return abs(self._sum_diagonal())

def main():
    size = input()
    matrix = []
    for x in range(0, int(size)):
        read_line = input()
        matrix.append(read_line)
    output = Diagonals(size, matrix).resolve()
    print(output)

if __name__ == "__main__":
    main()
