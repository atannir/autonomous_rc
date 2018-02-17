This is the location of the script that will read all our image data, flatten it, and provide it to our network to be trained. I opted to use Keras with a TensorFlow backend because it is easier to create standard networks and there are a number of portability functions for convenience.

The network seen here will be trained on a more powerful computer, preferably one with Nvidia CUDA capabilities. Once trained, the Keras model and weights will be saved and transferred to the Raspberry Pi to control the car. The current approach assumes that every frame is sufficient to make a prediction on the next action to be taken.

The network will be a convolutional neural network, likely with similar convolution stride values as the DAVE-2 architecture from Nvidia and others. Performance testing will determine if this needs to be scaled back for realtime operation on the Raspberry Pi.

Currently, some strange filesystem behavior is stalling development at this stage.
