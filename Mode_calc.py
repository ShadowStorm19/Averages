from Num_Retrieve import numberRetriever, displayExplanation #type: ignore

info = """
In order to calculate the mode, the occurence of each number is counted. 
The number with the most amount of  occurences is said to be the mode.
E.G. The mode of the numbers 10, 5, 64, 10, 6, 86, 10 is 10 as it occurs 3 times throughout the list of numbers. """


programName = 'Mode'

def calculate_mode():
    NumCounter = {}
    ModeList = numberRetriever()

    for i in ModeList:
        NumCounter.setdefault(i, 0)
        NumCounter[i] += 1
    
    HighestNumber = 0
    HighestOccuring = 0

    for number, repetition in NumCounter.items():
        if repetition > HighestOccuring:
            HighestOccuring = repetition
            HighestNumber = number
    
    print(f"The number with the most occurences is {HighestNumber} with an occurence of {HighestOccuring}")
    
    def mode_ans_explanation():
        print(f"The mode of the given numbers was {HighestNumber}.")
        print("These are how many times each number occured in your inputs.")
        for k, v in NumCounter.items():
            print(f"The number {k} appears {v} times throughout the given list of numbers.")
        print(f'The number {HighestNumber} appears more times than any others in the list.')
        print(f'Therefore {HighestNumber} is the mode.')

    displayExplanation(mode_ans_explanation)
    
    

    
