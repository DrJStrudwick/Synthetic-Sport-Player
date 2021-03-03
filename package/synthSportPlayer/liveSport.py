from sportplayer import *

class liveTourn(tournament):
    def __init__(self, playerList,pointPerRound=5):
        super().__init__(playerList,pointPerRound)
    
    def playTourn(self):
        """
        A function to play the entire tournament. When this one is called it will only play the next step
        """
        if len(self.currentRound)>1:
            nextRound = self.playRound()
            self.currentRound = nextRound
            self.round+=1
            if len(self.currentRound)==1:
                self.currentRound[0].gainPoints(self.round*self.points)
                self.tournRes = pd.DataFrame(self.matchRec,columns=["Round", "Match",
                                                                    "player1_id","player1_rnkPoints","player1_perform",
                                                                    "player2_id","player2_rnkPoints","player2_perform","winner_id"])
                return True
            else:
                return False
        else:
            return True
        
class liveSeason(season):
    def __init__(self,numPlayers=16,tournToPlay=20, players=None, playerSum=None):
        super().__init__(numPlayers=16,tournToPlay=20, players=None, playerSum=None)
        shuffle(self.players)
        self.currentTourn = liveTourn(self.players)
        self.currentTournComplete = False
        
    def playSeason(self):
        """
        A function to play out the season of tournaments. when it is called it just does one step of the tournament.
        """
        if self.week == self.tournsToPlay:
            return True
        else:
            if self.currentTournComplete:
                shuffle(self.players)
                self.currentTourn = liveTourn(self.players)

            self.currentTournComplete = self.currentTourn.playTourn()
            if self.currentTournComplete:
                self.gatherPoints()
                self.tournRecs.append(self.currentTourn.tournRes)
                self.week+=1
            return False
            
