def main():
    testCases = int(input())
    for test in range(testCases):
        planetDict = {}
        temp = 1
        cost = 0
        '''
        Takes in how many planets, the number of planets in an array and the destroying num
        '''
        n = input()
        n = n.split(" ")
        n = [int(num) for num in n]
        destroyMachine = n[1]
        planets = (input())
        
        planets = (planets.split(" "))
        planets = [int(planet) for planet in planets]
        '''
        Stores the planets in a dictionary
        '''
        for planet in planets:
            if planet in planetDict:
                temp = planetDict[planet] + 1
                planetDict.update({planet: temp})
            else:
                planetDict.update({planet: 1})    
        

        for k in planetDict:
            if planetDict[k] < destroyMachine:
                cost = cost + planetDict[k]
            else:
                cost = cost + destroyMachine
        print(cost)            

    return



if __name__  == "__main__":
    main()       