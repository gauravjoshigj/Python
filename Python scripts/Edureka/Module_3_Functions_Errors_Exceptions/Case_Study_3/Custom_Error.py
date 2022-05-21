# Author : Gaurav
# Custom Error class for module 2, case study 3
#
class CustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'CustomError, {0} '.format(self.message)
        else:
            return 'Custom Error has been raised'
