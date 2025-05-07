class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_numberOfStudents(self):
        return self.numberOfStudents
    
    def set_numberOfStudents(self, new_number):
        self.numberOfStudents = new_number

    def __repr__(self):
        return "The {school} is a {level} school with {number_students} students.".format(school = self.name, level = self.level, number_students = self.numberOfStudents)
    

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy
    
    def get_pickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + " The pick up policy is: {pickupPolicy}.".format(pickupPolicy = self.pickupPolicy)

test_school = School('Abbott', 'Middle', 100)
test_primary = PrimarySchool('Ateneo', 176, 'pick up at 3:30pm')

print(test_primary.get_name())
print(test_primary.get_level())
print(test_primary.get_numberOfStudents())
print(test_primary.get_pickupPolicy())

print(test_primary.set_numberOfStudents(250))

print(test_primary)
