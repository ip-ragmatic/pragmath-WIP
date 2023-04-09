"""
Defines a Matrix class that allows mathematical operations (addition, subtraction, and multiplication) to be perfromed on matrices. The matrix must be set up like the following 3x3 matrix:
    [
        [n, n, n],
        [n, n, n],
        [n, n, n]
    ]

"""
#TODO: Create multiplication function (look @ function definiton to see what needs to be built).
#TODO: Add self.determinant attribute to Matrix class.
#TODO: Don't allow the creation of matrices that have rows and/or columns with different lengths.
#TODO: Handle errors that occur from improper matrix addition.
#TODO: Handle errors raised when user passes improper parameters into class constructor.
#TODO: Figure out how to create a function that determines how the matrix is created when class 
#      constructor is called.


class Matrix:
    
    def __init__(self, *args, **kw):
        """ *args - Accepts lists as a way to automatically create a matrix with values inside corresponding entries. To 
                    create 2x2 identity matrix:
                    (1)    mtrx = Matrix([[1,0],
                                          [0,1]])
                    (2)    mtrx2 = Matrix([1,0],
                                          [0,1])
                    
            **kw - Currently serves as the way to construct an empty n by n matrix. Only use kw["row"] and kw["col"] as a 
                   keyword argument. For example, to make an empty 3x4 matrix:
                        mtrx = Matrix(row=3,col=4)

            This __init__ func is an attemp at using conditionals to detect the kind 
            of matrix creation function to use when a user passes parameters into class 
            constructor """
        if args:
            if len(args) == 1:
                self.matrix = args[0]
            else:
                self.matrix = [item for item in args]
        elif kw:
            self.matrix = [[0 for x in range(kw["col"])] for y in range(kw["row"])]
        else:
            self.matrix = list()

        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        #self.determinant = None


    def create_mtrx(self):
        """ I really want to create a function that determines how to create matrix when class
            constructor is called. It will make the __init__ function look cleaner. """
        pass


    def mtrx_add(self, *args):
        """ Performs addition on any number of matrices put into parameter field and returns
            the sum of all the matrices into the self.matrix attribute of the object this was
            called on. """
            
        for mtrx in args:
            if type(mtrx) == type(list()):
                pass
            else:
                mtrx = mtrx.matrix

            for row,entries in enumerate(mtrx):
                for i in range(len(entries)):
                    self.matrix[row][i] += mtrx[row][i]
        return self.matrix

    
    def mtrx_subt(self, *args):
        """ Performs subtraction on any number of matrices put into parameter field and returns 
            the difference of all the matrices into the self.matrix attribute of the object this 
            was called on. """

        for mtrx in args:
            if type(mtrx) == type(list()):
                pass
            else:
                mtrx = mtrx.matrix
            for row,entries in enumerate(mtrx):
                for i in range(len(entries)):
                    self.matrix[row][i] -= mtrx[row][i]
        return self.matrix


    def mtrx_mult(self, *args):
        """ Performs multiplication on any number of matrices and/or scalar multiples in parameter
            field and returns the product of all the matrices.

            The returned product will be assigned to the self.matrix attribute, which means that 
            there must be a Matrix object that this function is being called from (obviously).

            *** Further documentation will be provided once the definition is created. *** """
        # TODO: Build a type check for each individual element being looped through in *args. Check
        #       if element is an array type or a float (matrices can be multiplied by a float).
        # TODO: For matrix multiplication, figure out how to multiply each entry in the row of 
        #       one matrix by each entry in the column of another matrix, find the sum of each
        #       product, and place the sum in the corresponding entry of product matrix.
        # TODO: Maybe to some kind of list comprehension for scalar multiples, shouldn't be too complex.

        pass


    def display_matrix(self):
        """ Prints the specified matrix in a somewhat prettier way. """
        pretty = f"~~~~~ {self.rows}x{self.cols} Matrix ~~~~~"
        print(pretty)
        print(*self.matrix, sep="\n")
        print("-" * len(pretty))
        

