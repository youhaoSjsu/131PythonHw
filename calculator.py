import math


def calculator(number1, number2, operator):
    """
            make calculation

            This function make calculation according given numbers and operators
            Parameters
            ----------
            number1: float number
                    first operation number
            number2: float number
                    second operation number
            operator: string
                    operator string
            Returns
            -------
            false if operator can't be recognized

            Examples
            --------
            >>10,11,"+"
            21.0
            """
    result = 0.0
    # judge the operator to do right operation
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number1 == 0:
            return False
        else:
            result = number1 / number2
    elif operator == "//":
        if number1 == 0:
            return False
        else:
            result = int(number1) / int(number2)
            result = int(result)
    elif operator == "**":
        result = math.pow(number1, number2)
    else:
        return False
    print(result)
    return result


def parse_input():
    """
        get the text of user input and parse the text.

        This function simply split user's input into 3 parts: number1, number2, and operator.
        pass these variables to next function.
        Parameters
        ----------
        Returns
        -------
        false if number1 or number2 or not numbers

        Examples
        --------
        >> 10 + 11
        number1: 10 ,number2: 11, operator: +
        """
    number1 = 0.0
    number2 = 0.0
    print("Enter equation: ")
    text = input()
    # split text into three variables by " ", So that we can get the data
    strList = text.split(" ")
    # prevent system get error when user input wrong text
    try:
        number1 = float(strList[0])
        number2 = float(strList[2])
    except ValueError:
        return False
    calculator(number1, number2, strList[1])

