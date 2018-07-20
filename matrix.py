import random
from copy import deepcopy

class Matrix:

    def __init__(self, nrows_arg, ncols_arg):
        """Construct a (nrows X ncols) matrix"""
        self.nrow = int(nrows_arg)
        self.ncol = int(ncols_arg)
        self.matrix = []

        for i in range(self.nrow):
            for i in range(self.ncol):
                self.matrix.append(random.randint(0, 9))

    
    def add(self, matrix_arg):
        """return a new Matrix object after summation"""
        matrix_other = matrix_arg
        self.matrix_add = []
        for i in range(self.nrow * self.ncol):
            self.matrix_add.append(self.matrix[i] + matrix_other.matrix[i])
        

    def sub(self, matrix_arg):
        """return a new Matrix object after substraction"""
        matrix_other = matrix_arg
        self.matrix_sub = []
        for i in range(self.nrow * self.ncol):
            self.matrix_sub.append(self.matrix[i] - matrix_other.matrix[i])


    def mul(self, matrix_arg):
        """return a new Matrix object after multiplication"""
        matrix_other = matrix_arg
        self.matrix_mul = []
        sum = 0
        x = 0
        while x < self.nrow:
            for i in range (self.nrow):
                for j in range(self.ncol):
                    sum += self.matrix[j + self.ncol*x] * matrix_other.matrix[i]
                    i += self.ncol
                self.matrix_mul.append(sum)
                sum = 0
            x += 1


    def transpose(self, matrix_arg):
        """return a new Matrix object after transpose"""
        matrix_other = matrix_arg
        self.matrix_transpose = []
        sum = 0
        x = 0
        while x < self.nrow:
            for i in range (self.nrow):
                for j in range(self.ncol):
                    sum += self.matrix[j + self.ncol*i] * matrix_other.matrix[j*self.ncol + x]
                self.matrix_transpose.append(sum)
                sum = 0
            x += 1

    
    def display(self):
        """Display the content in the matrix"""
        t = 0
        for i in self.matrix:
            t += 1
            print(i, end = ' ')
            if t % self.nrow == 0:
                print('')

    
    def display_add(self):
        """display the content in matrix_c after def add()"""
        t = 0
        for i in self.matrix_add:
            t += 1
            print(i, end = ' ')
            if t % self.nrow == 0:
                print('')


    def display_sub(self):
        """display the content in matrix_c after def sub()"""
        t = 0
        for i in self.matrix_sub:
            t += 1
            print(i, end = ' ')
            if t % self.nrow == 0:
                print('')


    def display_mul(self):
        """display the content in matrix_c after def mul()"""
        t = 0
        for i in self.matrix_mul:
            t += 1
            print(i, end = ' ')
            if t % self.nrow == 0:
                print('')


    def display_transpose(self):
        """display the content in matrix_c after def mul()"""
        t = 0
        for i in self.matrix_transpose:
            t += 1
            print(i, end = ' ')
            if t % self.nrow == 0:
                print('')


nrowsA = input('Enter A matrix\'s row:')
ncolsA = input('Enter A matrix\'s col:')
# nrowsA = int(nrowsA)
# ncolsA = int(ncolsA)
print('Matrix A({}, {}):'.format(nrowsA, ncolsA))
matrixA = Matrix(nrowsA, ncolsA)
matrixA.display()
print('')
nrowsB = input('Enter B matrix\'s row:')
ncolsB = input('Enter B matrix\'s col:')
nrowsB = int(nrowsB)
ncolsB = int(ncolsB)
print('Matrix B({}, {}):'.format(nrowsB, ncolsB))
matrixB = Matrix(nrowsB, ncolsB)
matrixB.display()
print('')
###
print("="*10 + "A+B" + "="*10)
matrixA.add(matrixB)
matrixA.display_add()
###
print("="*10 + "A-B" + "="*10)
matrixA.sub(matrixB)
matrixA.display_sub()
###
print("="*10 + "A*B" + "="*10)
matrixA.mul(matrixB)
matrixA.display_mul()
###
print("="*10 + "The transpose of A*B" + "="*10)
matrixA.transpose(matrixB)
matrixA.display_transpose()
# 輸入端的變數設定
# 轉換成矩陣格式換行
# 排版