import os

os.environ["DATASET_DIRECTORY"] = "/content/tody/datasets"

git submodule init
git submodule update

#git clone https://github.com/ultralytics/yolov5.git
#cd yolov5
git checkout tags/v5.0
pip install -r models/yolov5/requirements.txt

# YOLOv6
# git clone https://github.com/WongKinYiu/yolov6.git
#cd yolov6
pip install -r models/yolov6/requirements.txt

# YOLOv7
# git clone https://github.com/ultralytics/yolov7.git
# cd yolov7
git checkout fix problems_associated_with_the_latest_versions_of_pytorch_and_numpy
pip install -r models/yolov7/requirements.txt
wget -P /content/tody/models/yolov7 https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt



# YOLOv8
# git clone https://github.com/your-username/yolov8.git
# cd yolov8
pip install -r models/yolov8/requirements.txt
