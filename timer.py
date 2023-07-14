# Created with reference from https://www.learndatasci.com/solutions/python-timer/

# Import required packages
from contextlib import contextmanager
import time
import numpy as np

# The timer function is implemented as a context manager using the @context manager decorator
@contextmanager

def print_time():
    """
    =======
    PURPOSE
    =======
    This function is used as a WITH statement to measure the time of any function(s) within the WITH statement.
    Time measured in seconds with 4 decimal places.

    ======
    INPUTS
    ======
    Any function can be timed within the WITH statement, even if the function fails

    =======
    OUTPUTS
    =======
    Printout of time taken for function or operation.
    Returns the time taken for storage.

    =======
    EXAMPLE
    =======
    with print_time():
        {insert function here}

    >>> Time taken: {time_taken} seconds.
    """




    # Initiate the timer
    start_time = time.perf_counter()
    
    # a yield was added inside a try-finally code block to ensure that the context manager can still calculate end time even if framed code throws error
    try:
        yield
        
    finally:
        # End the timer
        end_time = time.perf_counter()
        
        # Calculate time taken, then print out time taken
        time_taken = np.round(end_time - start_time,4)
        print(f"Time taken: {time_taken} seconds.")