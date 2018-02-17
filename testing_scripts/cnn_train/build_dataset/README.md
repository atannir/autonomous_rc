This script creates our dataset for use in training the network.

The script will create a list of all the image files in the subdirectories and create an array of flattened numpy image data and the direction from the filename. Strictly speaking, we don't need to keep the file path once we have the image data, but it makes things more convenient if we have to debug.
