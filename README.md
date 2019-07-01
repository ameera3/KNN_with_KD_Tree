# kNN_with_KD_Tree

We implement a kNN (k Nearest Neighbor) Classifier using a KD tree. For any query point, a kNN Classifier outputs the most 
frequent label of its k nearest neighbors in the training data. A KD Tree is used to make searching for the k nearest 
neighbors more efficient.  

This is the Python partial solution to this CSE 100 [assignment](https://sites.google.com/eng.ucsd.edu/cao100/programming-assignments/pa1-bst-and-kd-tree-in-c/part-2-kd-tree-in-c). I coded this in C++ too, but the C++ repo remains private for academic integrity reasons.

## Usage 
The KNNClassifier.py program takes in 4 command line arguments and outputs a file called "result.txt". The first 
command line argument is the choice of k in KNN (number of nearest neighbors). The second is the name of the training 
data file. The third is the name of input data file. The fourth is the mode, which is either "validation" or "test".

python3 KNNClassifier.py -k 3 -t ./iris_train -i ./iris_test -m test

## Training data file

Each line of the training data file is a data point. Each line should have d features (in type float) followed by a 
label (in type int). Numbers in each line are separated by spaces.

For example, if d = 3, each line of training data file should have the format:

7.27 6.25 6.12 1

where "7.27 6.25 6.12" are the 3 features of the training point, and "1" is the label of this point.

## Input data file

The input data file has different formats depending on whether the mode is "validation" or "test."

### Validation mode

In validation mode, the input data file should have the same format as training data file. We are trying to use the input 
data file as a validation set (with labels) to find the validation error. This is done by counting the number of times 
our classifier has made a label mismatch mistake. A label mismatch mistake means that, after training the classifier 
using the training data file, our predicted label for a point in the validation set differs from its true label. The 
validation error percentage is the number of label mismatch mistakes divided by the size of data input. We can then choose 
the k with the lowest validation error.

### Test mode

In test mode, each line of the input data file should contain only the features of this data with no label following. In 
this case we are trying to use the input data file as a test set. For each test point, we first find its k nearest neighbors 
in the training data. We then predict a label for the test point by outputting the most frequent label of its k nearest 
neighbors in the training data.

## Output file

The output file, result.txt, has different formats depending on whether the mode is "validation" or "test."

### Validation mode
In validation mode, the output file contains the value of k and its corresponding validation error. For example, if we 
choose k = 3 and the validation error is 0.1, then the output file contains a single line with:

K: 3, Validation Error: 0.1

The string above is appended to the output file, result.txt, which means that the output file may contain multiple 
lines of information if you run your classifier repeatedly.

### Test mode

In test mode, each line of the output file, result.txt, contains the predicted label for the data in the corresponding 
line of the input data file. For example, if the input file has two data points, and the kNN classifier predicts that the 
label for both of those data points is 1, then the output file contains:

1

1
