# -*- coding: utf-8 -*-

import random
import time
import csv

# Name of the files for each folder
CategoryNamesSpanish = (0, 
                 "Comunicacion", 
                 "Los_meses_y_las_estaciones",
                 "Los_numeros_y_las_fechas", 
                 "Colores",
                 "Chapter5-Cognados",
                 "Chapter5-Communication",
                 "Chapter5-Verbs",
                 "Chapter5-Vocabulary",
                 "Coloress")

#--------------------------------------------------------------------------------

def Startup():
    """
    User choses the categoies of words they want to study

    0 - Close
    1 - Comunicacion/Communication
    2 - Los meses y las estaciones/The months and the seasons
    3 - Los numeros y las fechas/Numbers and dates
    4 - Colores/Colors
    5 - Chapter 5 - Cognados
    6 - Chapter 5 - Communication
    7 - Chapter 5 - Verbs
    8 - Chapter 5 - Vocabulary
    """


    print(" \
    0 - Close\n \
    1 - Comunicacion/Communication\n \
    2 - Los meses y las estaciones/The months and the seasons\n \
    3 - Los numeros y las fechas/Numbers and dates\n \
    4 - Colores/Colors\n \
    5 - Chapter 5 - Cognados\n \
    6 - Chapter 5 - Communication\n \
    7 - Chapter 5 - Verbs\n \
    8 - Chapter 5 - Vocabulary\n \
    9 - Coloress\n"
          )

    # Gets user input and adds it to the list of categories
    category = int(input("Which categories would you like to study?\n"))
    Options = []

    while(True):

        if (category == 0 and len(Options) == 0):
            return
        
        elif (category == 0):
            break
        
        else:
            Options.append(category)

        category = int(input())

    # Adds all the words from the each category into one list
    AllWords = Setup(Options)
    
    # Prepares the test
    Pre_Test(AllWords)

#--------------------------------------------------------------------------------

def Setup(categorys: list) -> tuple:

    # Builds the string for the file name depending on the folder needing to be accessed
    for category in categorys:
        fileExtension = CategoryNamesSpanish[category]

        # Open the CSV file for reading
        with open("/Users/aprui/Side_Projects/Spanish_StudyGuide/" + fileExtension + ".csv", encoding='utf-8') as csvfile:
            # Create a CSV reader object
            csvreader = csv.reader(csvfile)

            rows = [row for row in csvreader]

            # sorted_data = sorted(rows, key=lambda x: int(x[-1]), reverse=True)

        return rows
    
def Pre_Test(AllWords: tuple):
    """
    SPANISHWORDS: the Spanish words to be tested on
    ENGLISHWORDS: the English words to be tested on

    Asks the user questions to make the test the way the user wants
    """
    
    amount_of_questions = int(input(f"How many words do you want to study out of {(len(AllWords))} words?\n"))

    while (amount_of_questions <= 0 or amount_of_questions > len(AllWords)):
        print("Not a valid response")
        print("Please choose again!\n")
        
        amount_of_questions = int(input())

    Type = int(input("Which would you like to be questioned in?\n" \
                "1 - English\n" \
                "2 - Spanish\n"))

    while (Type not in [1,2]):
        print("Not a valid response")
        print("Please choose again!\n")
        
        Type = int(input())
        
    print("\n\n\n")

    return Shuffle_Lists(AllWords, 1)


    # shuffles the two lists and choses the amount of questions the user asked for
    combined_lists = list(zip(SpanishWords, EnglishWords))
    random.shuffle(combined_lists)
    shuffled_Spanish, shuffled_English = zip(*combined_lists)

    shuffled_Spanish = list(shuffled_Spanish)
    shuffled_English = list(shuffled_English)

    del shuffled_Spanish[-((len(SpanishWords) - amount_of_questions)):]
    del shuffled_English[-((len(EnglishWords) - amount_of_questions)):]

    # Begins the test with the shuffled list
    Test(shuffled_Spanish, shuffled_English, Type, amount_of_questions)

def Shuffle_Lists(AllWords: list, Option: int):

    EnglishWords, SpanishWords, Correct, Attempts = zip(*AllWords)
    Correct = [int(x) for x in Correct]
    Attempts = [int(x) for x in Attempts]

    combined_lists = list(zip(EnglishWords, SpanishWords, Correct, Attempts))

    if (Option == 1):
        combined_lists = sorted(combined_lists, key=lambda x: x[3])
    
    elif (Option == 2):
        combined_lists = sorted(combined_lists, key=lambda x: x[2])

    elif (Option == 3):
        combined_lists = random.shuffle(combined_lists)

    # Unzip the sorted list back into separate lists
    EnglishWords, SpanishWords, Correct, Attempts = zip(*combined_lists)

    



    print("EnglishWords:", EnglishWords)
    print("SpanishWords:", SpanishWords)
    print("Correct:", Correct)
    print("Attempts:", Attempts)

    return 0

def Test(SpanishWords: list, EnglishWords: list, Type: int, amount_of_questions: int):
    """
    SPANISHWORDS: the Spanish words to be tested on
    ENGLISHWORDS: the English words to be tested on
    TYPE: determins what language the questions are in
    AMOUNT_OF_QUESTIONS: the amount of the questions the user is going to answer

    """

    questions = []
    answers = []
    answered = []
    wrong_questions = []
    amount_correct = 0

    if (Type == 1):
        questions = EnglishWords
        answers = SpanishWords

    elif (Type == 2):
        questions = SpanishWords
        answers = EnglishWords

    for i in range(3, 0, -1):
        print(f"Starting in {i}:")
        time.sleep(1)

    # print(EnglishWords)
    # print(SpanishWords)
    print("\n\n")

    if (len(questions) == 0):
        print("Empty list")
        print(EnglishWords)
        print(SpanishWords)
        print(questions)
        print(answers)
        print(Type)
    
    else:

        # Loops through the questions and accepts and compares the user aswer to the correct one
        for count, question in enumerate(questions, start=1):
            answer = input(f"{count}/{amount_of_questions}) {question}\n")

            if (answer.lower().strip() == str(answers[(count-1)]).lower().strip()):
                amount_correct += 1
            
            else:
                wrong_questions.append(count-1)

            answered.append(answer)

    # Tells the user their score 
    print(f"\n\nYou made a {amount_correct}/{amount_of_questions} - {'{:.2f}'.format(round(((amount_correct/amount_of_questions)*100), 2))}%")
    
    if (amount_correct == amount_of_questions):
        print("\n\nCongratulations!!! You got them all right!\n")

    # Displays the questions the user got wrong
    else:
        print("Here are the ones you missed\n\n")
            
        for i in wrong_questions:
            print(f"{(i+1)}. {questions[i]} / {answers[i]}\n You answered {answered[i]}\n\n")




Startup()

# # Open the file in read mode
# with open("/Users/aprui/Side_Projects/Spanish_StudyGuide/EnglishWords/The_months_and_the_seasons.txt", "r") as file:
#     # Read all lines from the file
#     lines = file.readlines()

# # Open the file in read mode
# with open("/Users/aprui/Side_Projects/Spanish_StudyGuide/SpanishWords/Los_meses_y_las_estaciones.txt", "r") as file:
#     # Read all lines from the file
#     Spanishlines = file.readlines()

# # Open the file in append mode
# with open("/Users/aprui/Side_Projects/Spanish_StudyGuide/EnglishWords/The_months_and_the_seasons.txt", "a") as file:
#     # Append each line to the file
#     file.write("\n\n")
#     for count, line in enumerate(lines):
#         line = line.strip()  # Remove any trailing newline character
#         line += " / "  # Append the desired character
#         line += Spanishlines[count].strip()
#         line += "\n"  # Add a newline character
#         file.write(line)
