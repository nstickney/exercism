class Garden(object):

    species = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'
    }

    def __init__(self, diagram, students=None):
        self.rows = diagram.split('\n')
        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                             "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
                             "Larry"]
        else:
            self.students = sorted(students)

    def plants(self, student):
        pot = self.students.index(student) * 2
        return [self.species[p] for r in self.rows for p in r[pot:pot + 2]]
