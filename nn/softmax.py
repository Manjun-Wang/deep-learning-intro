# Softmax function
def softmax(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  
  return y


def softmax(a):
  c = np.max(a)
  exp_a = np.exp(a - c) # for over flow
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  
  return y
