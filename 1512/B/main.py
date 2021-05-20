#!/usr/bin/env python3

import sys


class Point:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x


class Solver:
    rows_count = 0
    matrix = []
    points = []

    def __init__(self, rows_count: int):
        self.rows_count = 0
        self.matrix = []
        self.points = []

    def add_line(self, line: str):
        line = line.rstrip()
        cells = [line[i] for i in range(len(line))]
        self.matrix.append(cells)

    def get_result(self):
        self.define_points()
        if len(self.points) != 2:
            raise Exception("Non two points detected")

        new_points: list
        if self.is_dots_on_one_axis():
            new_points = self.one_axis_solution()
        else:
            new_points = self.non_one_axis_solution()

        self.put_new_points_to_matrix(new_points)

        return self.prepare_matrix_as_strings()

    def prepare_matrix_as_strings(self):
        lines = []
        for y in range(len(self.matrix)):
            line = self.matrix[y]
            lines.append("".join(line))

        return "\n".join(lines)

    def put_new_points_to_matrix(self, new_points: list):
        for i in range(len(new_points)):
            point = new_points[i]
            self.matrix[point.y][point.x] = '*'

    def one_axis_solution(self):
        point1 = self.points[0]
        point2 = self.points[1]

        axis = self.what_parallel_axis()
        if axis == '':
            raise Exception('one axis solution: no common axis')

        if axis == 'x':
            in_top = point1.y == 0
            common_y = point1.y - 1
            if in_top:
                common_y = point1.y + 1

            point3 = Point(point1.x, common_y)
            point4 = Point(point2.x, common_y)

            return [point3, point4]
        else:  # axis y
            in_left = point1.x == 0
            common_x = point1.x - 1
            if in_left:
                common_x = point1.x + 1

            point3 = Point(common_x, point1.y)
            point4 = Point(common_x, point2.y)

            return [point3, point4]

    def non_one_axis_solution(self):
        point1 = self.points[0]
        point2 = self.points[1]
        point3 = Point(point1.x, point2.y)
        point4 = Point(point2.x, point1.y)

        return [point3, point4]

    def define_points(self):
        for y in range(len(self.matrix)):
            line = self.matrix[y]
            for x in range(len(line)):
                if line[x] == '*':
                    point = Point(x, y)
                    self.points.append(point)

    def is_dots_on_one_axis(self):
        point1 = self.points[0]
        point2 = self.points[1]

        if point1.x == point2.x:
            return True

        if point1.y == point2.y:
            return True

        return False

    def what_parallel_axis(self):
        point1 = self.points[0]
        point2 = self.points[1]

        if point1.x == point2.x:
            return 'y'

        if point1.y == point2.y:
            return 'x'

        return ''


def main():
    blocks_number = 0
    rows_count = 0
    matrix: Solver

    with sys.stdin as f:
        while True:
            if blocks_number == 0:
                line = f.readline()
                if len(line) == 0:
                    break
                blocks_number = int(line)
                continue

            if rows_count == 0:
                line = f.readline()
                if len(line) == 0:
                    break
                rows_count = int(line)
                continue

            matrix = Solver(rows_count)
            for _ in range(rows_count):
                matrix.add_line(f.readline())

            result = matrix.get_result()
            print(result)

            rows_count = 0
            matrix = None


if __name__ == '__main__':
    main()
