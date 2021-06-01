# -*- coding: utf-8 -*-
"""optimize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aU9GOFZQORwmQmMm24FGraIIQM9zvOXW
"""

import 

def optimize(X,Y,W,B,num_Iterations,learning_Rate):
  ''' optimize func use forward_Back_Propagation func to calculate dW and dB and cost, then update this parameters
  
  Arguments:
  X -- data of size(750000,number_of_examples)
  Y -- true label vector (1,number_of_examples)
  W -- dictionary of Weights for layer1 and layer2
  B -- dictionary of Bias for layer1 and layer2
  num_Iteration -- a scalar
  learning_Rate -- a scalar

  Return:
  W -- dictionary of weights
  B -- dictionary of bias
  costs -- list of costs after evry iteration
  '''
  
  costs = []
  W1 = W['W1']
  W2 = W['W2']
  B1 = B['B1']
  B2 = B['B2']

  for i in range(num_Iterations):
    #use forward_back_propagation 
    gradW, gradB, cost = forward_back_propagation(X,W,B,Y)
    
    #Append costs
    costs.append(cost) 
    dW1 = gradW['dW1']
    dW2 = gradW['dW2']
    dB1 = gradB['dB1']
    dB2 = gradB['dB2']

    #simutaneously update W and B
    W['W1'] = W1 - learning_Rate*dW1
    W['W2'] = W2 - learning_Rate*dW2
    B['B1'] = B1 - learning_Rate*dB1
    B['B2'] = B2 - learning_rate*dB2

  return W,B,costs