from Num_Retrieve import numberRetriever, displayExplanation #type: ignore

info = """
In order to calculate the range of any set of numbers, all we have to do is to take away the
smallest number from the largest number.
E.G. 12 - 3 = 9. This simply means that there are 9 numbers in between 3 and 12.

Note: Range is not actually an average but a measure of spread.

Note: Negative numbers can also be used in calculating range.
      E.G. 12-(-3). The plus cancel out to make a plus which would be 12 + 3 = 15.
      Meaning that there are 15 numbers in betwwen 12 and -3
"""

programName = "Range"

def calculate_range():
    RangeList = numberRetriever()
    RangeList.append(0)
    RangeList.sort()
    try:
        largest = RangeList[-1]
        smallest = RangeList[0]
        NumRange = largest - smallest
    except IndexError:
        return 0

    print(f"The range of your numbers is {NumRange}")

    def range_ans_explanation():
        print(f'Your range was {NumRange}.')
        print(f'In order to find this number we first subtracted the largest number from the smallest number')
        print(f'In this case, {largest} - {smallest} = {NumRange}')
    
    displayExplanation(range_ans_explanation)