# Object_Oriented_Programming_School_Catalogue

A lab activity on classes

Objective: to create a digital school catalog for the New York City Department of Education

Requirements and Specifications:

1. School class
    - Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
    - Getters: all properties have getters
    - Setters: the numberOfStudents property has a setter
    - Methods: A __repr__ method that displays information about the school.

2. Primary class
    - Includes everything in the School class, plus one additional property
    - Properties: pickupPolicy (string, like "Pickup after 3pm")

3. Middle class
    - Does not include any additional properties or methods

4. High class
    - Includes everything in the School class, plus one additional property
    - Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])