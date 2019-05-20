import os

os.environ['TF_ENABLE_CONTROL_FLOW_V2'] = '1'

import tensorflow as tf


converter = tf.lite.TFLiteConverter.from_keras_model_file("cnn_best_model.h5")
tflite_model = converter.convert()
open("CNN.tflite", "wb").write(tflite_model)