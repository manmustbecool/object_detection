
# opencv

install opencv

`
pip install opencv-python
`

# Object detection

tensorflow models APIs:

https://github.com/tensorflow/models

'Object detection' model is inside the research folder

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

#### protobuf

Download Google Protobuf https://github.com/google/protobuf Windows  release “protoc-3.x.x-win32.zip”

Extract the Protobuf download to local, for example:

C:\protoc-3.x.0-win32

Now cd into models\research.

cd path\to\models\research

Execute the protobuf compile

`
“C:\protoc-3.x.0-win32\bin\protoc.exe” object_detection/protos/*.proto --python_out=.
`

.py files will be generated in the object_detection/protos/ folder


The *. may not work in the windows. A good way to solve this problem is to use bash. We can run above command in git bash.



# Tutorials


https://pythonprogramming.net/video-tensorflow-object-detection-api-tutorial/