#initializing functions
def zoo():
    #intializing lists to hold user input with helpful information
    adj = ['regular', 'regular', 'regular', 'regular']
    noun = ['singular', 'singular', 'singular']
    verb = ['past tense', 'regular', 'past tense']
    adverb = ['regular', 'regular']

    #Main program to interface with user.
    intro = f"""    Hi there, I heard you want to tell me about your trip to the zoo today Madlib style.
Together we will choose {len(adj)} adjective(s), {len(noun)} noun(s), {len(verb)} verb(s), and {len(adverb)} adverb(s)\n\n"""
    print(intro)

    for i in range(len(adj)):
        adj[i] = input(f'Choose a(n) {adj[i]} Adjective: ')

    for i in range(len(noun)):
        noun[i] = input(f'Choose a(n) {noun[i]} Noun: ')
        
    for i in range(len(verb)):
        verb [i] = input(f'Choose a(n) {verb[i]} Verb: ')
    
    for i in range(len(adverb)):
        adverb [i] = input(f'Choose a(n) {adverb[i]} Adverb: ')

    print("\nGreat! Now let's hear all about your day at the zoo!\n")

    #Full Returned Paragraph
    zoo_ML = f"""   Today I went to the zoo. I saw a(n) {adj[0]} {noun[0]} jumping up and down in its tree. He {verb[0]} {adverb[0]}
through the large tunnel that led to its {adj[1]} {noun[1]}. I got some peanuts and passed them through the cage to a gigantic gray
{noun[2]} towering above my head. Feeding that animal made me hungry. I went to get a {adj[2]} scoop of ice cream. It filled my
stomach. Afterwards I had to {verb[1]} {adverb[1]} to catch our bus. When I got home I {verb[2]} my mom for a {adj[3]} day at the zoo."""

    print(zoo_ML)

def arcade():
    #intializing lists to hold user input with helpful information
    noun = ['plural', 'plural', 'singular', 'plural', 'singular', 'plural']
    verb = ['regular', '-ing']

    #Main program to interface with user
    intro = f"""  Hi there, I heard you want to tell me about your trip to the arcade today Madlib style.
Together we will choose {len(noun)} nouns and {len(verb)} verbs.\n\n"""
    print(intro)

    for i in range(len(noun)):
        noun[i] = input(f'Choose a(n) {noun[i]} Noun: ')
        
    for i in range(len(verb)):
        verb [i] = input(f'Choose a(n) {verb[i]} Verb: ')
    
    print("\nAwesome! Now let's here all about your trip to the arcade!\n")
    
    #Full text paragraph
    arcade_ML = f"""    When I go to the arcade with my {noun[0]} there are lots of games to play.
I spend lots of time there with my friends. In the game X-Men you can be different {noun[1]}. The point
of the game is to {verb[0]} every robot. You also need to save people. Then you can go to the next level.

    In the game Star Wars you are Luke Skywalker and you try to destroy every {noun[2]}. In a car
racing/motorcycle racing game you need to beat every computerized vehicle that you are {verb[1]} against.

    There are a whole lot of other cool games. When you play some games you win {noun[3]} for
certain scores. Once you're done you can cash in your tickets to get a big {noun[4]}. You can save your
{noun[5]} for another time. When I went to this arcade I didn't believe how much fun it would be.
So far I have had a lot of fun every time I've been to this great arcade!"""

    print(arcade_ML)

#debugging
#zoo()
#arcade()

def play_again():
    print("\n\nThat was so much fun, I'm glad that we got to play madlibs together :)\n")
    invalid_input = True
    while invalid_input:
        replay = input('Do you want to play again y/n?').lower()

        #Data validation
        if replay in ['y', 'n']:
            invalid_input = False
        else:
            print("\n\nYou're answer must either be 'y' or 'n'. Please try again.\n\n")
    
    #Replay or end game based on user input
    if replay == 'y':
        print('\nYay!\n\n')
        madlibs()
    else:
        print('\n\nOkay! Well I had a lot of fun, and I hope you did to. I\'ll see you next time!')

#Main Program
def madlibs():
    print("Thank you for choosing to play Madlibs with me, i cant't wait to see what kind of silly stories you come up with!\n")
    invalid_input = True
    while invalid_input:
        choice = input('Would you rather tell me about the zoo or the arcade?').lower()

        #data validation
        if choice in ['zoo', 'arcade']:
            invalid_input = False
        else:
            print("\n\nWhoops, I don't recognize your answer.\nAre you sure you spelled 'arcade' or 'zoo' correctly?\n\
Please try again.\n\n")

    #Running chosen situation
    if choice == 'zoo':
        zoo()
    else:
        arcade()

    play_again()

#Running the program
madlibs()