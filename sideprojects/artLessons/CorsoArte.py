import random

def selectExercise():
    esercizi = [
        ["Tavole di quadrati", "www.nolink.com",  [1] ], 
        ["Tavole di ellissi", "https://drawabox.com/lesson/1/tablesofellipses", [1]],
        ["Cerchi concentrici", "www.nolink.com", [1] ],
        ["Foglio di reti", "www.nolink.com", [1]],
        ["Linee ondulate", "www.nolink.com", [1]]
    ]
    print(random.choice(esercizi))

selectExercise() 