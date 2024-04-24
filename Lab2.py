def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    getVal = input()
    numbers = getVal.split(",")
    # convertedNums = []
    # for char in numbers:                      this is another way the strings / numbers in the list can be converted
    #     convertedNums.append(int(char))       into a list of floats  

    for i in range(len(numbers)):
        numbers.append(float(numbers[0]))
        numbers.pop(0)

    print(numbers)
    return numbers



def calc_average_temperature(valueList):
    total = sum(valueList)
    average = total / len(valueList)
    print(f"The average temperature value is {average}")
    return average


def calc_min_max_temperature(valueList):
    minVal = min(valueList)
    maxVal = max(valueList)
    return [minVal, maxVal]


   


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    print(f"The minimum and maximum temperature values are {calc_min_max_temperature(num_list)}")



if __name__ == "__main__":
    main()