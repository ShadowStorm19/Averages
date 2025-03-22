from Num_Retrieve import numberRetriever, displayExplanation #type: ignore

info = """
In order to calculate the mean, we divide the sum of all numbers by how many numbers are there
E.G. The mean of the numbers 5, 3, 4 is 4 because 5 + 3 + 4 = 12. 12 / 3 = 4. """

programName = 'Mean'

def calculate_mean():
    sum = 0
    numberList = numberRetriever()
    for i in numberList:
        sum += i

    try:
        numberListLen =  len(numberList)
        meanNum = sum / numberListLen
        print(f"The mean is {meanNum}")
    except ZeroDivisionError:
        return 0
        
    def mean_ans_explanation():
        print(f'Your mean was {meanNum}. Here is the calculation for your answer.')
        print('First, we have to add all the number together.')
        print(numberList, sep=' + ')
        print(f'The sum of these numbers was {sum}')
        print(f'Then by dividing {sum} by{numberListLen} we get {meanNum}.')

    displayExplanation(mean_ans_explanation)
    