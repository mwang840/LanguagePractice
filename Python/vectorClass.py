class Vector:
    def __init__(self, vector) -> None:
        self.vector = vector
    
    def length(self):
        return len(self.vector)
    
    def push(self, val):
        self.vector.append(val)

    def get(self, index):
        return self.vector[index]
    
    def minus(self, val):
        self.vector.pop(val)
    #adds the matrices together
    def add(self, matrix):
        resultingMatrix = Vector([])
        assert(self.length() == matrix.length())
        for s in range(0, self.length()):
               resultingMatrix.push(self.get(s) + matrix.get(s))

        return resultingMatrix
    #subtracts the two matrices together
    def subtract(self, matrix):
        resultingMatrix = Vector([])
        assert(self.length() == matrix.length())
        for s in range(0, self.length()):   
            resultingMatrix.push(self.get(s) - matrix.get(s))
        return resultingMatrix
    #Finds the dot product of the matrixes
    def dot(self, matrix):
        sum = 0
        assert(self.length() == matrix.length())
        for s in range(0, self.length()):
            sum += self.get(s) * matrix.get(s)
        return sum
    #function to normalize a matrix
    def norm(self):
        normalize = 0
        for s in self.vector:
            normalize += s ** 2
        return normalize ** 0.5
    #Check if the matrices are EXACTLY equal to each other
    def equals(self, matrix):
        if self.length() != matrix.length():
            return False
        for s in range(0, self.length()):
            if self.get(s) != matrix.get(s):
                return False
        return True    
    #a string version of a vector
    def __str__(self):
        vectorToString = "("
        for s in range(0, self.length()):
            if s != self.length() - 1:
                vectorToString += str(self.get(s)) + ","
            else:
                vectorToString += str(self.get(s))    
        vectorToString += ")"    
        return vectorToString

def main():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    print(a.add(b))
    print(a.norm())
    print(a.__str__())


if __name__ in "__main__":
    main()            