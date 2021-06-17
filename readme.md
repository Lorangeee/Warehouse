# Dog Classifier
This is my first neural network model, a dog classifier. Here in this file I will record how I develop it and improve it's performance step by step.

## Neural Network Structure
Start it from a simple version.
L = 2, there are 2 hidden layers in the neural network.
Input layer, X --(10000,1)
Layer1, A1 -- (10,1)
Layer2, A2 -- (1,1), also the predict y_hat
Use sigmoid as activation function between layers.

Input --> linear forward --> sigmoid --> linear forward --> sigmoid --> output
Loss --> cost --> back propagation1 --> back propagation2 --> simultaneously update parameters

## Data Set
'Kaggle Cats and Dogs Dataset' is the data set I will use to train and test my model. It has 12497 cat images and 12499 dog images.
    I will choose 24000 pictures from that data sets for training, and the rest for testing.  

##### Feed Back

###### Why my costs increased instead decrease after every iteration?

- Recheck my backpropagation algorithm.
- Recheck the calculate form of costs.



