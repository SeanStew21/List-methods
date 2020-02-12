#High scores

scores = []

choice = None

while choice != 0:
    print(
    """
    High scores
    0- exit
    1- show scores
    2- add a score
    3- delete a score
    4-sort scores
    """)

    choice = input("Choice: ")
    print()

    #exit
    if choice == 0:
        print('Good-bye.')
    elif choice == 1: #list high score table
        print('High Scores')
        for score in scores:
            print(score)
    elif choice == 2: #add a score
        score = int(input('What score did you get?: '))
        scores.append(score)
    elif choice == 3: #remove a score
        score = int(input('Remove which score?: '))
        if score in scores:
            scores.remove(score)
        else:
            print(score, 'isn\'t in the high scores list.')
    elif choice == 4: #sort scores
        scores.sort(reverse=True)
    else: #some unknown choice
        print('Sorry but', choice, 'isn\'t a valid choice.')
    print('Scores: 'scores)
