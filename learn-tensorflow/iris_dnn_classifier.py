'''
Getting started with Tensorflow using IRIS dataset.
References:

https://github.com/tensorflow/models/tree/master/samples/core/get_started
https://www.commonlounge.com/discussion/b2e6d04be44d4ca79e6b8434b762db3c
'''

import tensorflow as tf
import pandas as pd
import os

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--batch_size', default=100, type=int, help='Batch Size')
# parser.add_argument('--train_steps', default=1000, type=int, help='No. of training steps')

BATCH_SIZE=100
STEPS=1000


TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

'''
load_data - Function to load dataset from the given url.
The file is obtained from given url using Keras util. The downloaded csv is read using Pandas.
The function then returns the content separately as features and labels.

Note: Written suitably for IRIS dataset, may require modification for others.
'''
def load_data(data_url, columns, label_name='Species'):
    
    data_file = os.path.join('', data_url.split('/')[-1])
    data_path = tf.keras.utils.get_file(fname=data_file, origin=data_url)

    data = pd.read_csv(filepath_or_buffer=data_path, names=columns, header=0)

    features, label = data, data.pop(label_name)

    return (features, label)

'''
train_input_function - Function to create tf-Dataset object from the input tensors
'''
def train_input_function(features, labels, batch_size):
    # converts input dataset into tensor slices
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    # shuffle the data ; larger the number, the better
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    return dataset

'''
eval_input_function - Function to evaluate input function.
'''
def eval_input_function(features, labels=None, batch_size=None):
    
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    # return dataset.make_one_shot_iterator().get_next()
    return dataset

(train_feature, train_label) = load_data(TRAIN_URL, CSV_COLUMN_NAMES)
(test_feature, test_label) = load_data(TEST_URL, CSV_COLUMN_NAMES)

# Iterating through the column names to map them to tf.feature_columns
feature_columns = []

for column in train_feature.keys():
    feature_columns.append(tf.feature_column.numeric_column(key=column))

'''
hidden_units=[10, 10]:

each element of the list represents number of neuron in a layer
and the length of the list represents the number of hidden layers. 
'''
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns, n_classes=len(SPECIES), hidden_units=[10, 10])
classifier.train(input_fn=lambda:train_input_function(train_feature, train_label, BATCH_SIZE), steps=STEPS)

eval_result = classifier.evaluate(input_fn=lambda:eval_input_function(test_feature, test_label, BATCH_SIZE))
print(eval_result)



predict_x = {'SepalLength': [5.1, 5.9, 6.9], 'SepalWidth': [3.3, 3.0, 3.1], 'PetalLength': [1.7, 4.2, 5.4], 'PetalWidth': [0.5, 1.5, 2.1]}
predictions = classifier.predict(input_fn=lambda:eval_input_function(predict_x, batch_size=BATCH_SIZE))
