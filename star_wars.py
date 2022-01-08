# A simple class to rank the order in which star wars movie should be watched. 
# The class contains methods that take in users ranks, returns ranks, returns highest rank, lowest rank, list of all ranks and their scores ...
# The list used here is a star wars (because why not the greatest sci fi piece?) list of movies each assigned a letter that is taken as an input upon class initialization. 
# You can replace this list with any list you want you want. 

# Format of list being used. Replace the list using this format 
list = {
            'A' : 'Episode I: The phantom menace',
            'B' : 'Episode II: Attack of the clones',
            'C' : 'Star Wars: The Clone Wars',      
            'D' : 'Episode III: Revenge of the Sith',
            'E' : 'Solo : A star wars story',
            'F' : 'Rogue One',
            'G' : 'Episode IV: A new hope',
            'H' : 'Episode V: The empire strikes back',
            'I' : 'Episode VI: Return of the Jedi',
            'J' : 'Episode VII:  The force awakens',
            'K' : 'Episode VIII: The last Jedi',
            'L' : 'Episode IX: The rise of Skywalker',
            'M' : 'Star wars rebels (Animation Star wars series)',
            'N' : 'The Mandalorian (Live action Star Wars series)',
            'O' : 'The bad batch (Animation Star wars series)',
            'P' : 'The book of Boba Fett (Animation Star wars series)',
            'Q' : 'Star Wars : Resistance (Animation Star Wars series)'
        }

# the class methods

# displayList - displays the list being ranked
# addRank - add a ranking new ranking (takes in name, rank)
# displayRanks - display all user ranks
# deleteRanks - delete rank from a particular user (takes in name)
# displayRankScores - display all unique ranked orders and their scores
# displayHighestRankScores - display highest ranked order
# displayLowestRankScores - display lowest ranked order
# convertRankToList - converts the order in which movies are ranked to their full list (takes in an order)

class StarWars:

    def __init__(self, list):
        self.ranks = {}
        self.list = list
        self.scores = {}


    def displayList(self):
        for key in self.list:
            print (key + '-->' + self.list[key])

    def addRank(self, name, rank):
        for key in self.ranks:
            if key == name:
                print ("Name already exists")
                return
        self.ranks[name] = rank
        if rank not in self.scores:
            self.scores[rank] = 1
        else:
            self.scores[rank] += 1

    def displayRanks(self):
        if len(self.ranks) < 1:
            print ("There are no ranks yet")
            return
        for key in self.ranks:
            print (key + '----->' + self.ranks[key])

    def deleteRanks(self, name):
        self.ranks.pop(name)
        self.displayRanks()
    
    def displayRankScores(self):
        for key in self.scores:
            print (key + '--->' + str(self.scores[key]))

    def displayHighestRankScore(self):
        highest_scores = max(self.scores.values())
        highest_scores_key = max(self.scores, key = self.scores.get)
        print (highest_scores_key + '--> ' + str(highest_scores))
        # for key in self.scores:
        #     for key_2 in highest_scores:
        #         if self.scores[key] > highest_scores[key_2]:
        #             highest_scores.pop(key_2)
        #             highest_scores[key] = self.scores[key]
        #         if self.scores[key] == highest_scores[key_2]:
        #             highest_scores[key] = self.score[key]


    def displayLowestRankScore(self):
        lowest_scores = min(self.scores.values())
        lowest_scores_key = min(self.scores, key = self.scores.get)
        print (lowest_scores_key + '--> ' + str(lowest_scores))

    def convertRankToList(self, rank):
        for i in rank:
            if i not in self.list:
                print ('incorrect input at this point')
                return
            print (self.list[i])
    


S = StarWars(list)
S.addRank('Innocent', 'ABCDEFGHIJKLMNOPQ')
S.addRank('Grace', 'ABCDEFGHIJKLMNOPQ')
S.addRank('Gabriel', 'ABCDEFGHIJKLMNOPQ')
S.addRank('Dickson', 'ABCDEFGHIJKLMNO')

S.displayLowestRankScore()




