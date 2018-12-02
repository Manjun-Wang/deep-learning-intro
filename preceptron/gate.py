# simple implementation of preceptron gates
import numpy as np

# AND Gate
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7 // minus theta 
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

# NAND Gate
def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

# OR Gate
def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else: 
    return 1

# XOR Gate ===> the fundation of multi-layered perceptron 
def XOR(x1, x2):
  return AND(NAND(x1, x2), OR(x1, x2))
  
  
  
