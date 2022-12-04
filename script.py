#!python3
"""
Assumes we've defined:

- A directory for our working files to live in, CONTAINER_DIR
- an arbitrary integer VERSION_INT
- We have established local and S3 paths for our model and their labels as variables, particularly `modelLabel` and `modelPath`
"""
import os
import tensorflow as tf
import shutil

# Create a versioned path for the models to live in
# See https://stackoverflow.com/a/54014480/1877527
CONTAINER_DIR = 'feature-vector-with-serve'
VERSION_INT = '1.0'

exportDir = os.path.join(CONTAINER_DIR, VERSION_INT)
if os.path.exists(exportDir):
    shutil.rmtree(exportDir)
os.mkdir(exportDir)

def load_graph(model_file, returnElements= None):
    """
    Code from v1.6.0 of Tensorflow's label_image.py example
    """
    graph = tf.Graph()

    tf.saved_model.load(model_file, tags=[])

    # @tf.function
    # def f(x):
    #     return x

    # graph_def = f.get_concrete_function(1.).graph.as_graph_def()

    # returns = None
    # with graph.as_default():
    #     returns = tf.import_graph_def(graph_def, return_elements= returnElements)
    # if returnElements is None:
    #     return graph
    # return graph, returns
    return graph

# Add the serving metagraph tag
# We need the inputLayerName; in Inception we're feeding the resized tensor
# corresponding to resized_input_tensor_name
# May be able to get away with auto-determining this if not using Inception,
# but for Inception this is the 11th layer

modelPath = '/home/dhruft/development/school/gcloudTesting/efficientnet_lite0_feature-vector_2'

inputLayerName = None
# Load the graph
if inputLayerName is None:
    graph = load_graph(modelPath)
    inputTensor = None
else:
    graph, returns = load_graph(modelPath, returnElements= [inputLayerName])
    inputTensor = returns[0]
with tf.Session(graph= graph) as sess:
    # Read the layers
    from simplesave import *
    with graph.as_default():
        layers = [n.name for n in graph.as_graph_def().node]
        outName = layers.pop() + ":0"
        if inputLayerName is None:
            inputLayerName = layers.pop(0) + ":0"
    print("Checking outlayer", outName)
    outLayer = tf.get_default_graph().get_tensor_by_name(outName)
    if inputTensor is None:
        print("Checking inlayer", inputLayerName)
        inputTensor = tf.get_default_graph().get_tensor_by_name(inputLayerName)
    inputs = {
        inputLayerName: inputTensor
    }
    outputs = {
        outName: outLayer
    }
    simple_save(sess, exportDir, inputs, outputs)

print("Built a SavedModel")
# Put the model label into the artifact dir
modelLabelDest = os.path.join(exportDir, "saved_model.txt")
# !cp {modelLabel} {modelLabelDest}
# Prep for serving
import datetime as dt
modelArtifact = f"livemodel_{dt.datetime.now().timestamp()}.tar.gz"
# Copy the version directory here to package
# !cp -R {exportDir} ./
# # gziptar it
# !tar -czvf {modelArtifact} {VERSION_INT}
# Shove it back to S3 for serving
shutil.rmtree(VERSION_INT) # Cleanup
shutil.rmtree(exportDir) # Cleanup
