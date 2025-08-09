import numpy as np

"""
Custom functions for color processing and array operations.

This module contains utility functions for color name identification
and array manipulation. It is designed to be imported into Jupyter 
notebooks or other Python scripts.

Functions:
    rgb_to_color_name(r, g, b): Identifies the closest named color for given RGB values.
    head(arr, n=5): Returns the first n elements of an array.

Usage:
    To use this module in a Jupyter notebook or Python script, ensure 
    that the directory containing this file is in your Python path. 
    You can do this by adding the following code at the beginning of 
    your notebook or script:

    import sys
    import os
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if module_path not in sys.path:
        sys.path.append(module_path)
for me=====
import sys
import os

myfun_path = os.path.join(os.path.expanduser('~'), 'projects/py4sci/my_package')
sys.path.append(myfun_path)

=====
    Then import the module:
    import my_fun

    You can now use the functions:
    color = my_fun.rgb_to_color_name(0.2, 0.3, 0.4)
    first_five = my_fun.head(some_array)

Note:
    If you make changes to this file while a Jupyter notebook is running,
    you may need to restart the kernel or use importlib.reload() to see 
    the changes take effect in the notebook.
"""



def head1D(arr, n=5):
    return arr[:n]
import numpy as np

def head(arr, n=5, axis=0):
    """
    Return the first n elements along the specified axis of an array.
    
    Parameters:
    arr : array-like
        The input array.
    n : int, optional
        Number of elements to return (default is 5).
    axis : int, optional
        The axis along which to return the elements (default is 0).
    
    Returns:
    numpy.ndarray
        A slice of the input array containing the first n elements along the specified axis.
    Sample use:
        result = head(my_array, n=3, axis=1)  # Get first 3 elements along axis 1

    """
    arr = np.asarray(arr)
    slc = [slice(None)] * arr.ndim
    slc[axis] = slice(n)
    return arr[tuple(slc)]


def rgb2name(r, g, b):
    """reb2name will take r(red), g(green) and B(blue) values as positional arguments on a scale of 0 to 1.0
    and return the color they form when mixed
    """
    # Define color ranges and names
    color_ranges = {
        "Red": np.array([1, 0, 0]),
        "Green": np.array([0, 1, 0]),
        "Blue": np.array([0, 0, 1]),
        "Yellow": np.array([1, 1, 0]),
        "Magenta": np.array([1, 0, 1]),
        "Cyan": np.array([0, 1, 1]),
        "White": np.array([1, 1, 1]),
        "Black": np.array([0, 0, 0]),
        "Gray": np.array([0.5, 0.5, 0.5]),
        "Orange": np.array([1, 0.5, 0]),
        "Purple": np.array([0.5, 0, 0.5]),
        "Brown": np.array([0.6, 0.4, 0.2])
    }

    input_color = np.array([r, g, b])  # Changed this line
    
    # Calculate Euclidean distances
    distances = {name: np.linalg.norm(color - input_color) for name, color in color_ranges.items()}
    
    # Find the color with the minimum distance
    closest_color = min(distances, key=distances.get)
    
    return closest_color
# add more functions as needed