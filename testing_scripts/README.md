This is the directory of all experiments that led to the current state. As scripts are shown to be successful, they will be moved to the final_versions directory.

easycap_ffmpeg was created to ensure that the video4linux2 device was accessible through the Linux OS.

ocv_test was an exploration into using OpenCV for the convenience of opening the capture device and saving the images. Later, more sophisticated features of OpenCV will be explored.

control_test demonstrated that the Pi can be used to directly trigger the buttons on the remote. Due to the design, pulling the pin to ground will complete the circuit. Additionally, there is a minimum amount of time for the signal to be sent to the car, otherwise I assume the button debounce circuitry does not register the change. These facts were not immediately apparent.

training_data_capture forms the basis of our dataset collection. It is recommended to view a live feed through another device since every frame is not displayed in real time, only the frames that are captured and saved.

cnn_train is the current area of work. Inside the folder are successful test scripts to build the dataset suitable for training. However, currently there are some strange filesystem behaviors that need to be overcome. The network structure will be a few convolutional layers followed by two or more fully connected layers resulting in the output of a direction and steering command pair. Once trained, the model will be saved and loaded into the next phase, which will process an image and output a direction, continuously.
