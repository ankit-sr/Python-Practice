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
    Other methods are : 
            Addition :      +   __add__()
            Subtraction:    -   __sub__()
            Multiplication: *   __mul__() 
            Power:         **   __pow__()
            Division:       /   __truediv__()
            FloorDivision:  //  __floordiv__()
            Remainder:      %   __mod__()   
            and mony more for comparison, shorthand(-=, +=,...) operators   
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
            feet += int(inch/12)    # or feet += inch//12 (floor division)
            inch = inch%12

        distance = Distance(feet, inch)
        return distance

    # below method is the overloading of == operator
    def __eq__(self, other):
        return ( (self.feet*12 + self.inch) == (other.feet*12 + other.inch) )


distance1 = Distance(5, 11)
distance2 = Distance(6, 32)

distance3 = distance1 + distance2
# this line of code means: distance3 = distance1.__add__(distance2)
# so distance1 reference serve as self, and distance2 is passed as other.
print(distance3)

isequal = (distance1 == distance2)
print(isequal)



'''
    The above code can not work with other data types apart from Distance, as it will raise AttributeError'
    For eg. distance1 + 10  will give AttributeError as feet and inch are not attributes of int class
    We can overcome using

    def __add__(self, other):
        if isinstance(other, Distance):
            ...above written code
        else:
            self.feet += other
            self.inch += other

        if inch>=12     .......


    Here also the associativity does not hold good meaning 10+distance is not same as distance+10
    and will give TypeError.
    To overcome this situation, we have reflected operators, which start with 'r'
    For example:        reflected addition:     __radd__()
                        reflected subtraction:  __rsub__()
    now, 'distance + 10' will call __add__() while
    '10 + distance' will call __radd__(), here also self will be the object of the current class and other will be
    the object of another class.
'''
