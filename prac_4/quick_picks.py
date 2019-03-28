import random

numbers_per_line = 6
maximum = 45
minimum = 1

def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        number_of_quick_picks = int(input("Please enter a number 0 or greater"))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()




