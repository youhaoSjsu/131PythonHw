import time


def calculate_time(timingFunc):
    """
               timer

               This function calculate the time of running a function. And print the time
               Parameters
               ----------
               timingFunc: function
            function to be test running time
            
               Returns
               -------
               None

               Examples
               --------
               Total time 2.0081357955932617
               """
    b_time = time.time()
    timingFunc()
    e_time = time.time()
    result = e_time - b_time
    print("Total time " + str(result))

