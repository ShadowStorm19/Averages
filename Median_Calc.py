from Num_Retrieve import numberRetriever, displayExplanation #type: ignore

info = """
To calculate the median of a certain list of numbers, the numbers are first
listed in ascending order. Then by finding the middle number, often done by dividing
the amount of numbers by 2 and rounding up e.g. 5 numbers / 2 = number 2.5 rounded
up to the number 3, you can find the 3rd number in your list of numbers and that is the median.
For example take this list of numbers, 6, 8, 4, 6, 9. To find the median we first put them in 
ascending order: 4, 6, 6, 8, 9. Then by finding the middle number we get the number 6.

If there is an even amount of numbers, e.g. only 8, 4, 6, 9; We find the number in between the
supposed middle number (in this case, 6 since 4/ 2 = 2 and the second number is 6) and the next
number(in this case is 8). Then to find the number in the middle of 6 and 8, we add the two 
numbers together (6 + 8 = 14) and the sum by 2. In this case, 6 + 8 is 14 and 14 / 2 = 7

Note: Sometimes adding the middle and nest number after it will give you an odd number.
      E.G. 6 + 5 = 11. By dividing 11 by 2 we get 5.5 
      Be careful not to round up this decimal median you have gotten, as it is very possible to 
      get a median with a .5 after the number.
      
In any case, chances are that you are here to have the program to do the calculations for you so
might just be reading this for the fun of it :) """

programName = 'Median'

def calculate_median():
    NumberList = numberRetriever()
    NumberList.sort()
    
    listLen = len(NumberList)
    length = listLen % 2
    middle = listLen // 2

    if length == 1 :    # if list is odd
        listOdd = True
        medianNumber = NumberList[middle]

    else:   
        listOdd = False  # list is even
        try:
            dividedmedianNumber = NumberList[middle]
            oddMedianSecNumber = NumberList[middle - 1]
            addition = dividedmedianNumber + oddMedianSecNumber
            medianNumber = addition / 2
        except IndexError:
            return 0

    print(f"The median is {medianNumber}")

    def median_ans_explanation():
        if listOdd == True:
            print(f'The length of the list of numbers is {listLen}')
            print(f'Therefore the middle number is {medianNumber}')
        else:
            print(f'The median of your list of numbers is {medianNumber}')
            print(f'To find the middle number, we get the two numbers in the middle, {dividedmedianNumber} and {oddMedianSecNumber}')
            print(f'Then we add these two numbers to get {addition}')
            print(f'Then we divide {addition} by 2 to get a median of {medianNumber}')

    displayExplanation(median_ans_explanation)