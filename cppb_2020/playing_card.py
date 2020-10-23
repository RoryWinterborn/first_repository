class PlayingCard(object):
      
    def __init__(self,rank,suit,colour):
        ranks = ["Joker","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        suits = ["null","Diamonds", "Hearts", "Spades", "Clubs"]
        colours = ["Red", "Black"]
        self.rank = ranks[rank]
        self.suit = suits[suit]
        if suit == "Diamons" or "Hearts":
            colour = "Red"
        self.colour = colours[colour]

    def return_suit(self):
        return self.suit
    
    def return_rank(self):
        return self.rank
    
    def return_colour(self):
        return self.colour

    def __str__(self):
        return self.rank + " of " + self.suit + "."

my_card = PlayingCard(0,2)
print(my_card.__str__())