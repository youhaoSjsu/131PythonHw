#!/usr/bin/python3
def multiply_list():
    """
        #                multiply_list
        #
        #                this function will multiply all of the elements in an input list.
        #               parameter:
        #                ----------
        #               none
        #
        #                Returns
        #                -------
        #                product: product of numbers in inputList
        #
        #                Examples
        #                --------
        #                inputList: [1, 2, 3, 7]
        #                return: 42
        #
        #                """
    inputStr = input()
    inputList = inputStr.split(",")

    product = 1.0
    for i in inputList:
        try:
            float(i) + 0
        except TypeError:
            return False
        else:
            product *= float(i)
    print(product)
    return product
