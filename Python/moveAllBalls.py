def minOperations(boxes: str) -> list[int]:
    #Set up an list that can hold the size of the given string
    minimumOperations = [None]*len(boxes)
    #Set up counters for keeping track of moving balls to the left, the right and the total steps
    leftBalls = 0
    rightBalls = 0
    steps = 0
    #Loop over the box string
    for box in range(0, len(boxes)):
        if boxes[box] == "1":
            steps += box
            rightBalls +=1
    
    for box in range(0, len(boxes)):
        minimumOperations[box] = steps

        if boxes[box] == "1":
            rightBalls -=1
            leftBalls += 1
        
        steps += leftBalls
        steps -= rightBalls

    return minimumOperations

def main():
    ballsOne = "001011"
    print(minOperations(ballsOne))

if __name__ in "__main__":
    main()