class Teacher:

    def __init__(self, firstname, lastname, hire_date, email):
        self.firstname = firstname
        self.lastname = lastname
        self.hire_date = hire_date
        self.email = email


    def teach(self, course):
        print( self.firstname + " " + self.lastname + " donne cours de " + course)
