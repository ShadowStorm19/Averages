from Range_Calc import calculate_range, info as range_info, programName as r_name
from Mode_calc import calculate_mode, info as mode_info, programName as mode_name
from Median_Calc import calculate_median, info as median_info, programName as med_name
from Mean_Calc import calculate_mean, info as mean_info, programName as mean_name
from time import sleep
import sys

def displayInfo(info, stringCalcName):
    print(f"\nDo you want to see some information about {stringCalcName}s before you procced?: ")
    infoQuestion = input("Y / (any other key for no): ").lower()
    if infoQuestion == 'y' or infoQuestion == 'yes':
        infoBox = 'Info box'.center(80,'-')
        print(infoBox)
        print(info)

def name_display(program_name, space_num):
    print()
    program_name = program_name + ' Calculator'
    name = program_name.center(space_num,"-")
    print(name)

def runPrograms(program):
    program()

def run_Calculations():

    rangeDef = [calculate_range, range_info, r_name]
    modeDef = [calculate_mode, mode_info, mode_name]
    meanDef = [calculate_mean,  mean_info, mean_name]
    medianDef = [calculate_median, median_info, med_name]
    choosenSpaceNum = 80

    
    def program_Body(selection):
        entirety = {'range': rangeDef, 'mode' : modeDef, 'mean': meanDef, 'median' : medianDef}
        choosenList = entirety[selection]
        program, info, name = choosenList
        displayInfo(info, name) # displays info about average type
        name_display(name, choosenSpaceNum) # displays average type name
        runPrograms(program)    # runs average type program

    options = 'Range, Mean, Median or Mode'
    optionsList = ['range', 'mean', 'median', 'mode']

    name = input('Hello, what is your name? ')
    print(f'\nHello {name}, welcome to my Maths program.')
    print(f"It can calculate {options}.")
    code_continue = input("\nWill you be using this program today? (Y / (any other key for no)): ").lower() 

    if code_continue != 'y' and code_continue != 'yes':
        sys.exit(f"Well, bye bye for now {name}, hope you play the program again next time.")


    while True:
        userWantedCalculation = input(f"\nWhat do you want to calculate: {options} or (q to quit): ").lower()
        if userWantedCalculation == 'q':
            sys.exit(f"Bye bye {name}")
        if userWantedCalculation not in optionsList:
            print('Invalid input. Try again please.\n')
            continue
        else:
            program_Body(userWantedCalculation)
        
        playAgain = input('Do you want to do another calculation? (Y / (any other key for no)): ').lower()
        if playAgain != 'y' and playAgain not in optionsList:
            sys.exit(f"Bye ,Bye, see you next time {name}")

run_Calculations()
