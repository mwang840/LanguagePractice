class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        INT_MAX = 10000000
        word1Length = len(word1)
        word2Length = len(word2)
        distanceMatrix = [[INT_MAX for i in range(word2Length + 1)] for j in range(word1Length + 1)]
        for i in range(word1Length + 1):
            for j in range(word2Length + 1):
                if i == 0:
                    distanceMatrix[i][j] = j
                elif j == 0:
                    distanceMatrix[i][j] = i    
                elif word1[i - 1] == word2[j - 1]:
                    distanceMatrix[i][j] = distanceMatrix[i - 1][j - 1]
                else:
                    distanceMatrix[i][j] = 1 + min(min(distanceMatrix[i][j-1], distanceMatrix[i - 1][j]), distanceMatrix[i-1][j-1])
        return distanceMatrix[word1Length][word2Length]