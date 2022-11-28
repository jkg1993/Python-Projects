
def zoo():
    adj = ['amazing', 'huge', 'small', 'nice']
    noun = ['kangaroo', 'friend', 'rainbow']
    verb = ['hopped', 'skate', 'thanked']
    adverb = ['patiently', 'skillfully']

    adj = []
    noun = []
    verb = []
    adverb = []

    print("Hi there, I heard you want to tell me about your trip to the zoo today Madlib style. Let's start by choosing four adjectives.")
    for i in range(4):
        adj.append(input(f'Choose Adjective {i+1}: '))

    print("Now we should choose three nouns.")
    for i in range(3):
        noun.append(input(f'Choose Noun {i+1}: '))

    print("Now let's choose three verbs.")
    for i in range(3):
        verb.append(input(f'Choose Verb {i+1}: '))
    
    print("Finally we must choose three adverbs.")
    for i in range(3):
        adverb.append(input(f'Choose Adverb {i+1}: '))

    zoo_ML = f'Today I went to the zoo. I saw a(n) {adj[0]} {noun[0]} jumping up and down in its tree. He {verb[0]} {adverb[0]} \
through the large tunnel that led to its {adj[1]} {noun[1]}. I got some peanuts and passed them through the cage to a gigantic gray \
{noun[2]} towering above my head. Feeding that animal made me hungry. I went to get a {adj[2]} scoop of ice cream. It filled my \
stomach. Afterwards I had to {verb[1]} {adverb[1]} to catch our bus. When I got home I {verb[2]} my mom for a {adj[3]} day at the zoo.'

    print(zoo_ML)

zoo()