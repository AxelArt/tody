A tool for object detection using YOLO models

Clone the project
git clone https://github.com/AxelArt/tody.git

Run the following commands on your Colab notebook
git submodule init
git submodule update

Install dependenciesfor YOLOv5
pip install -qr models/yolov5/requirements.txt roboflow 

Run the train using YOLOv5
python yolo_manager.py --version v5 --mode train --dataset /content/tody/yolov5/data/coco.yaml

 
