"""
***THIS IS SOMETHING THAT YOU SHOULD _NOT_ DO.***

This is a demo to show how Python is a "weakly typed"
Object-Orientated Programming (OOP) language.
"""

class A:
    """
    """

    def this(self):
        """
        """
        return 'this'

class B:
    """
    """

    def that(self):
        """
        """
        return 'that'

obj = A()
print("obj's type:", type(obj))
print("obj.this():", obj.this())
try:
    print("obj.that():", obj.that())
except Exception as ex:
    print("obj.that() Exception:", ex)

# NEVER DO THIS
obj.__class__ = B

print("obj's type:", type(obj))
try:
    print("obj.this():", obj.this())
except Exception as ex:
    print("obj.this() Exception:", ex)
print("obj.that():", obj.that())
