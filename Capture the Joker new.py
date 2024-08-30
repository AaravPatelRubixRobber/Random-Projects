import random

######THIS IS THE SETUP######


print('welcome to capture the joker!')
print('capture the joker is an intense 2 player strategy game where the objective is to steal the other players Joker')
print()
print(''' INSTRUCTIONS:

      in this game, you have to try to steal the othr player's joker!''')

cpu_deck = ['A'] + [ str(x) for x in range(2, 11)] + [ 'J', 'Q', 'K', 'A'] + [str(x) for x in range(2, 11)] + [ 'J','Q','K', 'JOKER']  #['As', str(x) + 's' for x in range(2, 11), 'Js', 'Qs', 'Ks', 'Ac', str(x) + 'c' for x in range(2, 11), 'Jc', 'Qc', 'Kc']
player_deck = ['A'] + [ str(x) for x in range(2, 11)] + [ 'J', 'Q', 'K', 'A'] + [str(x) for x in range(2, 11)] + [ 'J','Q','K', 'JOKER']

print('Setup your defenses!!!!')
print()
#asks for firstline values
print(player_deck)
print('these are your available cards')
print()
yes = 1
while yes == 1:
    yes = 0
    
    player_firstline = list(input('What is your first line? (Please enter 8 cards that are included in the available cards. Put spaces to denote different cards.): ').split())
    if player_firstline == ['R']:
        player_firstline = ['K', 'J', '10', '2', '5', '4', '8', '9']
    for i in player_firstline:
        if i not in player_deck:
            print('Sorry, but', i, 'is not in your choices of cards. Try Again')
            print()
            yes = 1
    if len(player_firstline) != 8:
        print('Sorry, but you do not have 8 cards in this line. Try Again')
        print()
        yes = 1

print(player_firstline, 'is your first line')
#removes the cards put to the firstline from the deck
for i in player_firstline:
    player_deck.remove(i)

print()
print(player_deck, 'these are your remaining cards')
#gets secondline values
print()
yes = 1
while yes == 1:
    yes = 0
    player_secondline = list(input('What is your second line? ').split())
    if player_secondline == ['R']:
        player_secondline = ['3', '4', '7', '9', 'A', '10', 'K', 'Q']
    for i in player_secondline:
        if i not in player_deck:
            print('Sorry, but', i, 'is not in your choices of cards. Try Again')
            print()
            yes = 1
    if len(player_secondline) != 8:
        print('Sorry, but you do not have 8 cards in this line. Try Again')
        print()
        yes = 1

print(player_secondline, 'is your second line')
# removes cards put to second line from the deck
for i in player_secondline:
    player_deck.remove(i)

#gets third line values
print()
print(player_deck, 'these are your remaining cards')
print()
yes = 1
while yes == 1:
    yes = 0
    player_thirdline = list(input('What is your third line? ').split())
    if player_thirdline == ['R']:
        player_thirdline = ['5', '3', '7', '8', '2', 'A', 'J', 'Q']
    for i in player_thirdline:
        if i not in player_deck:
            print('Sorry, but', i, 'is not in your choices of cards. Try Again')
            print()
            yes = 1
    if len(player_thirdline) != 8:
        print('Sorry, but you do not have 8 cards in this line. Try Again')
        print()
        yes = 1
        
print(player_thirdline, 'is your third line')
print()
#removes thirdline values
for i in player_thirdline:
    player_deck.remove(i)

player_jokerline = player_deck[:]
print(player_jokerline, 'is your joker line')
print()
#shuffles the lines
random.shuffle(player_firstline)
random.shuffle(player_secondline)
random.shuffle(player_thirdline)
random.shuffle(player_jokerline)
#shows the player their setup
print('Your lines of defense')
print()
print('first:', player_firstline)
print('second:', player_secondline)
print('third:', player_thirdline)
print('jokerline:', player_jokerline)

cpu_deck_choice = 1#random.randint(1, 2)

if cpu_deck_choice == 1:
    cpu_firstline = ['K', 'J', '10', '2', '5', '4', '8', '9']
    cpu_secondline = ['3', '4', '7', '9', 'A', '10', 'K', 'Q']
    cpu_thirdline = ['5', '3', '7', '8', '2', 'A', 'J', 'Q']
    cpu_jokerline = ['6', 'JOKER', '6']
else:
    cpu_firstline = ['K', 'J', '10', '2', '5', '4', '8', '9']
    cpu_secondline = ['3', '4', '7', '9', 'A', '10', 'K', 'Q']
    cpu_thirdline = ['5', '3', '7', '8', '2', 'A', 'J', 'Q']
    cpu_jokerline = ['6', 'JOKER', '6']

cpu_currentline = cpu_firstline

#The beggining of the game

class player:
    def __init__(self, firstline, secondline, thirdline, jokerline):
        #eliminate all firstline secondline etc and only have currentline
        self.firstline = firstline
        self.secondline = secondline
        self.thirdline = thirdline
        #currentline = self.firstline
        #self.attackline = [i for i in currentline if i != 'J' and i != 'K' and i != 'Q' and i != 'JOKER']
    def attack(self, opp_line):

        if len(self.firstline) == 0 and len(self.secondline) == 0 and len(self.thirdline) == 0:
            currentline = self.jokerline
        elif len(self.firstline) == 0 and len(self.secondline) == 0:
            currentline = self.thirdline
        elif len(self.firstline) == 0:
            currentline = self.secondline
        else:
            currentline = self.firstline

        attackline = [i for i in currentline if i != 'J' and i != 'K' and i != 'Q' and i != 'JOKER' and i != '4']

        if int(len(currentline)) > int(len(opp_line)) + 1:
            winning == True
        else:
            winning == False
    def find_currentline(self):
        if len(self.firstline) == 0 and len(self.secondline) == 0 and len(self.thirdline) == 0:
            return self.jokerline
        elif len(self.firstline) == 0 and len(self.secondline) == 0:
            return self.thirdline
        elif len(self.firstline) == 0:
            return self.secondline
        else:
            return self.firstline

    def select_battlers(self, currentline):
        attackline = [i for i in currentline if i != 'J' and i != 'K' and i != 'Q' and i != 'JOKER' and i != '4']
        print(currentline, 'these are your cards')
        print()
        print(attackline, 'these are your choices to put into battle')
        print()
        yes = 1
        while yes == 1:
            yes = 0
            attackers = list(input('which card(s) is going into battle? ').split())
            for i in attackers:
                if i not in attackline:
                    print('Sorry, but', i, 'is not in your choices of cards. Try Again')
                    print()
                    yes = 1
                if len(attackers) == 0:
                    print('You have to enter a card ')
                    print()
                    yes = 1
        return attackers
    def choose_attacker(self, opp_line, attacker):
        print('[X] ' * len(opp_line), 'is the info on what you know on the cpu\'s cards')
        print()
        yes = 1
        #chooses card to attack
        while yes == 1:
            yes = 0
            try:
                chosencard = int(input('Which card number do you choose? '))
                if chosencard == 13585:
                    chosencard = 1
                    cheat = True
                    break
                elif chosencard == None:
                    print('enter a card')
                    print()
                    yes = 1
                if chosencard > len(opp_line):
                    print('that card does not exist')
                    print()
                    yes = 1
                if type(chosencard) == float:
                    print('you entered a decimal')
                    print()
                    yes = 1
                if chosencard <= 0:
                    print('your number is less than or equal to zero')
                    print()
                    yes = 1
            except:
                print('enter a number')
                print()
                yes = 1
        return chosencard    
            
    def manual_attack(self, opp_line):
        def find_currentline():
            if len(self.firstline) == 0 and len(self.secondline) == 0 and len(self.thirdline) == 0:
                return self.jokerline
            elif len(self.firstline) == 0 and len(self.secondline) == 0:
                return self.thirdline
            elif len(self.firstline) == 0:
                return self.secondline
            else:
                return self.firstline
        def select_battlers(currentline):
            attackline = [i for i in currentline if i != 'J' and i != 'K' and i != 'Q' and i != 'JOKER' and i != '4']
            print(currentline, 'these are your cards')
            print()
            print(attackline, 'these are your choices to put into battle')
            print()
            yes = 1
            while yes == 1:
                yes = 0
                attackers = list(input('which card(s) is going into battle? ').split())
                for i in attackers:
                    if i not in attackline:
                        print('Sorry, but', i, 'is not in your choices of cards. Try Again')
                        print()
                        yes = 1
                    if len(attackers) == 0:
                        print('You have to enter a card ')
                        print()
                        yes = 1
            return attackers
        def choose_attacker(opp_line, attacker):
            print('[X] ' * len(opp_line), 'is the info on what you know on the cpu\'s cards')
            print('FOR DEBUGGING: ', opp_line)
            print()
            yes = 1
            #chooses card to attack
            while yes == 1:
                yes = 0
                try:
                    chosencard = int(input('Which card number do you choose? '))
                    if chosencard == 13585:
                        chosencard = 1
                        cheat = True
                        break
                    elif chosencard == None:
                        print('enter a card')
                        print()
                        yes = 1
                    if chosencard > len(opp_line):
                        print('that card does not exist')
                        print()
                        yes = 1
                    if type(chosencard) == float:
                        print('you entered a decimal')
                        print()
                        yes = 1
                    if chosencard <= 0:
                        print('your number is less than or equal to zero')
                        print()
                        yes = 1
                except:
                    print('enter a number')
                    print()
                    yes = 1
            return chosencard    






        currentline = find_currentline()
        attackers = select_battlers(currentline)
        for attacker in attackers:
            chosencard = choose_attacker(opp_line, attacker)
            #fights
            print()
            opp_card = opp_line[chosencard - 1]
            print('the opponents card is', opp_card)
            print()
            try:
                if cheat == True:
                    del opp_line[:]
            except:
                
                if opp_card == 'J':# what happens if Jack is chosen(bomb)
                    if attacker == 'A' or attacker == '2':
                        print('You defused the bomb')
                        del opp_line[chosencard-1]
                    else:    
                        print('you set off a bomb. Your attacker(s) died')
                        for i in attackers:
                            try:
                                del currentline[currentline.index(i)]#ERROR
                                print('it deleted')#ERROR
                            except:
                                continue
                        break
                elif opp_card == 'Q':# what happens if Queen is chosen(abduction)
                    if attacker == 'A' or attacker == '2':
                        print('You killed the queen')
                        del opp_line[chosencard-1]
                    else:
                        print('The queen you chose abducted your attacker and made him a slave')
                        try:
                            del currentline[currentline.index(attacker)]
                        except:
                            continue
                        opp_line.append(attacker)
                        print(currentline)
                        print(opp_line)
                        break
                elif opp_card == 'K':# what happens if KIng is chosen(rage slaughter)
                    if attacker == 'A' or attacker == '2':
                        print('You killed the king')
                        del opp_line[chosencard-1]
                    else:
                        print('The king you chose slaughtered your attacker and also slaughtered another threat to him in your lineup because of his rage')
                        try:
                            del currentline[currentline.index(attacker)]
                        except:
                            continue
                        del currentline[random.randint(0, len(currentline))]
                        print(currentline)
                        break
                elif opp_card == 'JOKER':#what happens when joker is picked
                    print('Y   Y  OOO  U   U   W     W     W IIIII N  N  !!')
                    print(' Y Y  O   O U   U    W   W W   W    I   NN N  !!')
                    print('  Y   O   O U   U     W W   W W     I   N NN    ')
                    print('  Y    OOO   UUU       W     W    IIIII N  N  []')
                    break
                elif opp_card == 'A':# What happens if an A is picked up(kills 10)
                    if len(attackers) > 1:
                        if attacker == '10':
                            print('the opponent\'s immortal angel has killed your 10')
                            del currentline[currentline.index(attacker)]
                        elif attacker == 'A':
                            print('the opponent\'s immortal angel has taken your immortal angel')
                            del currentline[currentline.index(attacker)]
                            opp_line.append(attacker)
                            
                        else:
                            print('Your', attacker, 'has taken their immortal angel' )
                            del opp_line[chosencard - 1]
                            currentline.append(opp_card)
                    else:
                        if attacker == '10':
                            print('the immortal angel  has defended your 10')
                        elif attacker == 'A':
                            print('The immortal Angel has defended against your immortal angel')
                        else:
                            print('Your', attacker, 'has taken the immortal angel')
                            del opp_line[chosencard - 1]
                            currentline.append(opp_card)
                    break

                elif opp_card == '10': #(killed by ace)
                    if len(attackers) > 1:
                        if attacker == 'A':
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        else:
                            print('The opponent\'s', opp_card, 'has killed your', attacker)
                            del currentline[currentline.index(attacker)]
                            
                    else:
                        if attacker == 'A':
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        else:
                            print('The opponent\'s', opp_card, 'has defended your', attacker)
                elif opp_card == '9': # killed by 2
                    if len(attackers) > 1:
                        if attacker == 'A':
                            print('The opponent\'s', opp_card, 'has killed your', attacker)
                            del currentline[currentline.index(attacker)]
                        elif int(attacker) > int(opp_card) or attacker == '2':
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        else:
                            print('The opponent\'s', opp_card, 'has killed your', attacker)
                            del currentline[currentline.index(attacker)]
                            
                    else:
                        if attacker == 'A':
                            print('The opponent\'s', opp_card, 'has defended your', attacker)
                        elif int(attacker) > int(opp_card) or attacker == '2':
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        else:
                            print('The opponent\'s', opp_card, 'has defended your', attacker)
                

                
                else:
                    if len(attackers) > 1:
                        if attacker == 'A':
                            print('The opponent\'s', opp_card, 'has taken your', attacker)
                            del currentline[currentline.index(attacker)]
                            opp_line.append(attacker)
                        if attacker == '5':
                            if int(opp_card) >= 5:
                                print('The opponent\'s', opp_card, 'has killed your', attacker)
                                del currentline[currentline.index(attacker)]
                                currentline.append(opp_card)
                            else:
                                print('Your', attacker, 'has stolen the opponent\'s', opp_card)
                                del opp_line[chosencard - 1]
                        elif int(attacker) > int(opp_card):
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        else:
                            print('The opponent\'s', opp_card, 'has killed your', attacker)
                            del currentline[currentline.index(attacker)]
                            
                    else:
                        if attacker == 'A':
                            if len(attackers)> 1:
                                print('The opponent\'s', opp_card, 'has taken your', attacker)
                                del currentline[currentline.index(attacker)]
                                opp_line.append(attacker)
                            else:
                                print('The opponent\'s', opp_card, 'has defended your', attacker)
                        elif int(attacker) > int(opp_card):
                            print('Your', attacker, 'has killed the opponent\'s', opp_card)
                            del opp_line[chosencard - 1]
                        elif len(attackers) > 1:
                            print('The opponent\'s', opp_card, 'has killed your', attacker)
                            del currentline[currentline.index(attacker)]
                        else:
                            print('The opponent\'s', opp_card, 'has defended your', attacker)
                        
            



        print(currentline, 'these are your remaining cards')
        print('*******END TURN*******')
            
                
        
person = player(player_firstline, player_secondline, player_thirdline, player_jokerline)
cpu = player(cpu_firstline, cpu_secondline, cpu_thirdline, cpu_jokerline)

mode = input('which mode do you want to play? single sided siege(1) or capture the Joker(2)')
if mode == '2':
    while True:
    
        if len(cpu_firstline) == 0 and len(cpu_secondline) == 0 and len(cpu_thirdline) == 0:
            cpu_currentline = cpu_jokerline
        elif len(cpu_firstline) == 0 and len(cpu_secondline) == 0:
            cpu_currentline = cpu_thirdline
        elif len(cpu_firstline) == 0:
            cpu_currentline = cpu_secondline
        else:
            cpu_currentline = cpu_firstline

        if len(player_firstline) == 0 and len(player_secondline) == 0 and len(player_thirdline) == 0:
            player_currentline = player_jokerline
        elif len(player_firstline) == 0 and len(player_secondline) == 0:
            player_currentline = player_thirdline
        elif len(player_firstline) == 0:
            player_currentline = player_secondline
        else:
            player_currentline = player_firstline
        random.shuffle(cpu_currentline)
        random.shuffle(player_currentline)

        person.manual_attack(cpu_currentline)
        cpu.attack(player_currentline)

else:
    while True:

        if len(cpu_firstline) == 0 and len(cpu_secondline) == 0 and len(cpu_thirdline) == 0:
            cpu_currentline = cpu_jokerline
        elif len(cpu_firstline) == 0 and len(cpu_secondline) == 0:
            cpu_currentline = cpu_thirdline
        elif len(cpu_firstline) == 0:
            cpu_currentline = cpu_secondline
        else:
            cpu_currentline = cpu_firstline

        if len(person.firstline) == 0 and len(person.secondline) == 0 and len(person.thirdline) == 0:
            player_currentline = person.jokerline
        elif len(person.firstline) == 0 and len(person.secondline) == 0:
            player_currentline = person.thirdline
        elif len(person.firstline) == 0:
            player_currentline = person.secondline
        else:
            player_currentline = person.firstline

        random.shuffle(cpu_currentline)
        random.shuffle(player_currentline)
        print('for debugging only: currentline', cpu_currentline)
        person.manual_attack(cpu_currentline)
        del player_currentline[0]
        print('A ghost killed one of your cards')
        print()
        
            
        
        
    
    










    
        
            

        
            
    
    


