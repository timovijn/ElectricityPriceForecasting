	F����@q@F����@q@!F����@q@	�3�u��?�3�u��?!�3�u��?"h
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails'�F����@q@��"���p@A��n�@@Y1�Zd�?*	     @@2F
Iterator::Model�������?!      T@)���Mb�?1������R@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap+�����?!333333/@)�p=
ף�?1      *@:Preprocessing2S
Iterator::Model::ParallelMap�~j�t��?!333333@)�~j�t��?1333333@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat�I+��?!������@)/�$��?1������@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate9��v���?!������@)����Mb�?1�������?:Preprocessing2�
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice{�G�zt?!      �?){�G�zt?1      �?:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor����MbP?!�������?)����MbP?1�������?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B97.7 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	��"���p@��"���p@!��"���p@      ��!       "      ��!       *      ��!       2	��n�@@��n�@@!��n�@@:      ��!       B      ��!       J	1�Zd�?1�Zd�?!1�Zd�?R      ��!       Z	1�Zd�?1�Zd�?!1�Zd�?JCPU_ONLY