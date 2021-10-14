
def tripler(func):
    """
    #                tripler
    #
    #                This decorator will call the function that this function is used on three times.
    #                Parameters
    #                ----------
    #                   func: function
    #             a function will be called three times
    #
    #                Returns
    #                -------
    #                None
    #
    #                Examples
    #                --------
    #                hello world
    #                hello world
    #                hello world
    #                """

    def wrapper():
        # firstname calling
        func()
        # secondTime calling
        func()
        # thridTime calling
        func()

    return wrapper


def printH():
    print("hello world")


tripler(printH)
