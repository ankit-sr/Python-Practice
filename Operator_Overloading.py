'''
    Operator Overloading is a concept of rewriting the functionalites of opeartors provided by the python
    to fulfill our needs.
    Operator overloading can also be seen in the '+' operator, as it changes its behavior with 
    integers and strings.
    When operated with integers, it adds the given operands, while with strings it concatenates the operands,
    which shows that the operator functional definition is already overloaded in both of these classes.

    How to achieve operator overloading?
    Every operator have a method associated with it, such as the functionality of + operator is written in
    __add__ () method, and we can change the definition of this operator to achieve our task.
'''


class Distance:
    def __init__(self, feet, inch):
        self.feet = feet
        self.inch = inch
    
    def __str__(self):
        return f"Feet: {self.feet}, Inches: {self.inch}"

    #This method overrides the __add__() defined in Operator class
    def __add__(self, other):
        feet = self.feet + other.feet 
        inch = self.inch + other.inch
        if inch>=12:
            feet += 1
            inch = inch%12

        distance = Distance(feet, inch)
        return distance


distance1 = Distance(5, 11)
distance2 = Distance(6, 3)

distance3 = distance1 + distance2
# this line of code means: distance3 = distance1.__add__(distance2)
# so distance1 reference serve as self, and distance2 is passed as other.

print(distance3)
