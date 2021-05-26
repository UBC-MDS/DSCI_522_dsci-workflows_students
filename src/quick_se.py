# author: Tiffany Timbers
# date: 2020-01-15

'''This script calculates the standard error for any numerical vector
from a csv file. This script takes an unquoted column name and a data file path.

Usage: quick_titanic_fare_se.py --file_path=<file_path> --var=<var>

Options:
--file_path=<file_path>   Path to the data file
--var=<var>               Unquoted column name of the numerical vector for which to calculate the se
'''

import pandas as pd
import numpy as np
from docopt import docopt

opt = docopt(__doc__)

def main(file_path, var):
  # read in data
  data = pd.read_csv(file_path)

  # print out statistic of variable of interest
  out = sterror(data[var])
  print(out)

# standard error function

def sterror(x):
  """
  calculate standard error
    
  Parameters
  ----------
  numpy.ndarray : x
    A numpy array of numeric values.
        
  Returns
  -------
  se
    The standard error of x. 
        
  Examples
  --------
  >>> sterror(numpy.array([2, 2, 2]))
  0
  """
  se = x.std()/np.sqrt(x.size)
  return se
  
def test_sterror():
  assert sterror(np.array([1, 1, 1])) == 0, "sterror should return 0 if vector values are all the same"

test_sterror()
  
if __name__ == "__main__":
    main(opt["--file_path"], opt["--var"])
