import tensorflow as tf
import tflearn 

model_path = "model.tflearn"
inference_graph = tf.Graph()
with tf.Session(graph= inference_graph) as sess:
   # Load the graph with the trained states
  loader = tf.train.import_meta_graph(model_path+'.meta')
  loader.restore(sess, model_path)


  _accuracy = inference_graph.get_tensor_by_name('accuracy:0')
  _x  = inference_graph.get_tensor_by_name('x:0')
  _y  = inference_graph.get_tensor_by_name('y:0')


print(categories[np.argmax(model.predict([get_tf_record(sent_1)]))])






