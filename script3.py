# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from tensorflow.python.platform import gfile

model_file = "./efficientnet_lite0_feature-vector_2/saved_model.pb"

with tf.Session() as sess:
    # tf.saved_model.load(model_file, tags=[])
    # with gfile.FastGFile(model_file,'rb') as f:
    #     graph_def = tf.GraphDef()
    #     graph_def.ParseFromString(f.read())
    # sess.graph.as_default()
    # tf.import_graph_def(graph_def, name='')

    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())

    tf.import_graph_def(graph_def)

# Export the model to /tmp/my-model.meta.
meta_graph_def = tf.serve.export_meta_graph(filename='./efficientnet_lite0_feature-vector_2/info.meta')