import collections

import tensorflow as tf


tfrecord_writer = tf.io.TFRecordWriter(output_file)
tfrecord_features = collections.OrederDict()

for name, val in zip(
        ['inut_ids', 'input_mask', 'segment_ids', 'label_ids'],
        [input_ids, input_mask, segment_ids, lable_ids]):
    tfrecord_features[name] = tf.train.Feature(
        int64_list=tf.train.Int64List(value=val))
tfrecord = tf.train.Example(
    feature=tf.train.Features(feature=tfrecord_features))
tfrecord_writer.write(tfrecord.SerializeToString())
tf_record_writer.close()

