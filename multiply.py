#!/usr/bin/python3
def multiply_list(inputList):
    """
        #                multiply_list
        #
        #                this function will multiply all of the elements in an input list.
        #               parameter:
        #                ----------
        #                inputList: list
        #                A list which contain some numbers are ready to be multiply
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

    product = 1
    for i in inputList:
        try:
            i + 0
        except TypeError:
            return False
        else:
            product *= i

    return product

