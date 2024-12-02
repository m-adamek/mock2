 

# (p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. 
# The other cards have the value indicated by the card number. 
# Define a function f(player1,player2) that returns true if the first player has cards of the same or higher value,
# and false otherwise. Example: 

# f("AJ972","AQT72") à False 
# f("9532","K8") à True 

def f(player1,player2):
    special_cards = {'A': 10, 'B': 10, 'Q': 10, 'J': 10, 'T': 10}

    def calculate_total(player):
        total  = 0
        for card in player:
            if card in special_cards:
                total += special_cards[card]
            else:
                total += int(card)
        return total
    
    total1 = calculate_total(player1)
    total2 = calculate_total(player2)

    return total1 >= total2

