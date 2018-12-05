def sort_dict_by_keys(d):
    result = {}
    for key in sorted(d.keys()):
        result[key] = d[key]
    return result


class School(object):
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if grade not in self.grades:
            self.grades[grade] = []
            self.grades = sort_dict_by_keys(self.grades)
        self.grades[grade].append(name)
        self.grades[grade].sort()

    def roster(self):
        return [student for grade in self.grades.values() for student in grade]

    def grade(self, grade_number):
        if grade_number in self.grades:
            return self.grades[grade_number]
        return []
