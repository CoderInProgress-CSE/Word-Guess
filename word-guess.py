import random

name = input("What's your name ?")
print("Best Of Luck !" , name)

words= [
   # Computer Science
    'algorithm', 'binary', 'compiler', 'encryption', 'network', 'dataframe',
    'debugging', 'protocol', 'recursive', 'function',
    
    # Mathematics
     'equation', 'geometry', 'matrix', 'vector', 'calculus', 'probability',
    'theorem', 'derivative', 'integral', 'parabola',

    # Physics
    'gravity', 'quantum', 'velocity', 'photon', 'relativity', 'force',
    'thermodynamics', 'neutron', 'friction', 'entropy',

    # Biology
    'dna', 'photosynthesis', 'evolution', 'organism', 'ecosystem', 'chromosome',
    'mutation', 'enzyme', 'nucleus', 'cellulose',

    # Astronomy
    'galaxy', 'nebula', 'asteroid', 'eclipse', 'meteorite', 'orbit',
    'satellite', 'planetary', 'telescope', 'exoplanet'
]

word = random.choice(words)

print("Guess The Words based upon Computer Science, Mathematics, Physics, Biology, Astronomy")

guesses = ''
turns = 12

while turns > 0:

    failed = 0
    
    for char in word:
        if char in guesses:
          print(char, end=" ")
        
        else: 
          print("_")
          failed += 1
          
    if failed == 0:
          print("You Win")
          print("THe Word is: ", word)
          break
        
    guess = input("guess a character")
    guesses += guess[0]
        
    if guess not in word:
            turns -= 1
            print("wrong")
            print("You have" , + turns , 'more guesses')
            
    if turns == 0:
                print("You Loose") 