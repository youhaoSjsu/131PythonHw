def triple(func):
    """
    #                triple
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
    # firstname calling
    func()
    # secondTime calling
    func()
    # thridTime calling
    func()