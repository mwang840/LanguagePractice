def showMatrix(matrix: list[list[int]]):
        print("\n")
        for row in matrix:
            for col in row:
                print(col, end="\t\t")
            print("\n")

##
def convertToOne(row: int, col: int):
     for ro in range(row):
          for co in range(col):
               pass


def main():
    simpleMatrix = [
         [1,2], 
         [3, 4]
         ]
    showMatrix(simpleMatrix)


if __name__ in "__main__":
     main()