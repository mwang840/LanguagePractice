class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

        '''
        Calculates the progress of the current users rank and activity
        '''
    def find_progress(self, activity_rank):
        '''
        Checks to see if the users rank and the activity rank falls out of the required rankings
        '''
        if(activity_rank < -8 or activity_rank == 0 or activity_rank > 8 or self.rank < -8 or self.rank == 0 or self.rank > 8 or self.progress < 0 or self.progress > 100):
            raise Exception("Whoopsies, your rank fell out of the required rankings, -8 through 8 excluding rank zero!")

        '''Another check to see if the activity rank is exactly equal to the self rank, then add the progress by three'''
        if activity_rank == self.rank:
            return 3 

        '''
        Another check to see if the difference from the activity ranking and the self rank is 2 levels or lower, then make no changes to the progress
        '''
        if activity_rank < 0:
            '''
            If activity rank and the self rank is two levels lower then the self rank, return 0, otherwise if the activity rank is higher then the users rank return 10*progress*progress
            '''
            if self.rank < 0:
                if abs(self.rank - activity_rank) == 1 and self.rank > activity_rank:
                    return 1
                elif abs(self.rank - activity_rank) >= 2 and self.rank > activity_rank:
                    return 0  
                else:
                    return 10 * abs(self.rank - activity_rank) * abs(self.rank - activity_rank)
            else:
                if abs(self.rank - activity_rank - 1) == 1 and self.rank > activity_rank:
                    return 1  
                elif abs(self.rank - activity_rank - 1) >= 2 and self.rank > activity_rank:
                    return 0                   
        else:
            '''
            If activity rank and the self rank is two levels lower then the self rank, return 0, otherwise if the activity rank is higher then the users rank return 10*progress*progress
            '''
            if self.rank < 0:
                if abs(self.rank - activity_rank + 1) == 1 and self.rank > activity_rank:
                    return 1
                elif abs(self.rank - activity_rank + 1) >= 2 and self.rank > activity_rank:
                    return 0  
                else:
                    return 10 * abs(self.rank - activity_rank + 1) * abs(self.rank - activity_rank + 1)
            else:        
                if abs(self.rank - activity_rank) == 1 and self.rank > activity_rank:
                    return 1
                elif abs(self.rank - activity_rank) >= 2 and self.rank > activity_rank:
                    return 0 
                else:
                    return 10 * abs(self.rank - activity_rank) * abs(self.rank - activity_rank)     
                         
        
    def inc_progress(self, activity_rank):
        '''
        Increments the progress based on the users ranking and the current activity rank (starting from the lowest rank -8 and to the highest rank)
        Also need to account the users progress on that activity rank
        '''
        
        print("Your activity rank is " , activity_rank , " and your current ranking is " , self.rank , " with your current progress points of " , self.progress)
        usersProgress = self.find_progress(activity_rank)
        '''
        Logic fix
        '''
        levelUp = 0
        self.progress += usersProgress
        if self.progress >= 100:
            while self.progress >=100:
                self.progress -= 100
                levelUp += 1
        if levelUp != 0:
            if self.rank + levelUp >= 8:
               self.rank = 8
               self.progress = 0
            else:
                if self.rank < 0 and self.rank + levelUp >=0:
                    levelUp+=1
                self.rank += levelUp
        else:
            if self.rank >= 8:
                self.rank = 8
                self.progress = 0



def main():
    user = User()
    user.rank
    user.progress
    user.inc_progress(-7)
    print(user.progress)
    user.inc_progress(-5)
    print(user.progress)
    print(user.rank)
if __name__ == "__main__":
    main()