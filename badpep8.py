# multiple imports
# top level function (outside the class)
# should be two space to between them
# function name are generally lowcase and have an underscore between words


def foo_bar(arg1, arg2, arg3, arg4):
    return arg1, arg2, arg3, arg4


def bar(*args):
    return 2 + 2


# Bad class name, bad spacing, bad indentation
# class with two space
# class with capital T
class Treehouse:

    def one(self):
        return 1

    def two(self):
        return 2


alpha, beta, charlie, delta = foo_bar("a long string",
                                      "a longer string",
                                      "yet another long string",
                                      "and other crazy string")


one = 1
three = 3
fourteen = 14  # make fourteen equal to 12

print(alpha)
print(fourteen)

print(Treehouse().two())
