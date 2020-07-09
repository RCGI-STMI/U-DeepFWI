# DNN with Keras and Tensorflow

This project has a convolutional neural network, more specifically a U-net implemented with the aid of the Tensorflow / Keras framework. This network aims to predict the speed models present in the subsurface, having as input to the network a set of 4 equidistant seismograms.


# Process of shots generation
To generate the shots we used the software Devito [https://www.devitoproject.org/] 


## Network Structure 
The network structure is shown below.
  
<img src="./figures/unet.png">



# Obtained Results

After running the experiments, we were able to obtain good prediction results. Below, we present 6 examples of predictions.

<img src="./figures/predict.png">