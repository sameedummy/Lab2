def display_main_menu():
    print("display_main_menu")	
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    getVal = input()
    numbers = getVal.split(",")
    # convertedNums = []
    # for char in numbers:                      this is another way the strings / numbers in the list can be converted
    #     convertedNums.append(int(char))       into a list of floats  

    for i in range(len(numbers)):
        numbers.append(float(numbers[0]))
        numbers.pop(0)

    return numbers


def calc_average_temperature(valueList):
    print("calc_average_temperature")  
    total = sum(valueList)
    average = total / len(valueList)
    print(f"The average temperature value is {average}")
    return average


def calc_min_max_temperature(valueList):
    print("calc_min_max_temperature")
    minVal = min(valueList)
    maxVal = max(valueList)
    return [minVal, maxVal]   


def sort_temperature(valueList):
    print("sort_temperature")
    return sorted(valueList)


def calc_median_temperature(valueList):
    sortedValueList = sorted(valueList)
    print("calc_median_temperature")
    amount = len(sortedValueList)
    if amount % 2 == 0:
        halfAmount = int(amount / 2)
        median = (sortedValueList[halfAmount - 1] + sortedValueList[halfAmount]) / 2
        print(f"The median temperature value is {median}")
    else:
        positionalNum = int(amount / 2)
        median = (sortedValueList[positionalNum])
        print(f"The median temperature value is {median}")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    print(f"The minimum and maximum temperature values are {calc_min_max_temperature(num_list)}")
    calc_median_temperature(num_list)



if __name__ == "__main__":
    main()