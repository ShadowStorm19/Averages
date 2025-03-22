def numberRetriever():
    numList = []

    while True:
        number = input("Enter a number(blank to stop): ")

        try:
            numList.append(int(number))
        except ValueError:
            if number == '':
                break
            else:
                print('Invalid input \n')
                continue
    
    return numList

def displayExplanation(ans_explanation):
    display_exp = input('\nDo you want to view the explanation of this calculation? (Y/any other key) :').lower()
    if display_exp == 'y':
        ans_explanation()
        print()