"""
Defines a Matrix class that allows mathematical operations (addition, subtraction, and multiplication) to be perfromed on matrices. The matrix must be set up like the following 3x3 matrix:
    [
        [n, n, n],
        [n, n, n],
        [n, n, n]
    ]

"""
#1 TODO: Create subtraction function(s)
#2 TODO: Create multiplication function(s)
#1 TODO: Don't allow the creation of matrices that have rows and/or columns with different lengths.
#2 TODO: Handle errors that occur from improper matrix addition. """
#3 TODO: Handle errors raised when user passes improper parameters into class constructor
#4 TODO: Figure out how to better implement functions into __init__ function


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


    def mtrx_add(self, *args):
        """ Performs addition on any number of matrices put into parameter field, and returns
            the sum of all the matrices. """
            
        for mtrx in args:
            if type(mtrx) == type(list()):
                pass
            else:
                mtrx = mtrx.matrix

            for row,entries in enumerate(mtrx):
                for i in range(len(entries)):
                    self.matrix[row][i] += mtrx[row][i]
        return self.matrix


    def display_matrix(self):
        """ Prints the specified matrix in a somewhat prettier way. """
        pretty = f"~~~~~ {self.rows}x{self.cols} Matrix ~~~~~"
        print("\n"*2, pretty)
        print(*self.matrix, sep="\n")
        print("-" * len(pretty))
        

