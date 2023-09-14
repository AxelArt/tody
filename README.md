# TODY

A tool for object detection using YOLO models

## Preliminary steps

Clone the project

```commandline
git clone https://github.com/AxelArt/tody.git
```

Run the following commands on your Colab notebook

```commandline
git submodule init
git submodule update
```

Install dependencies for YOLOv5

<<<<<<< HEAD
```commandline
=======
Install dependencies for YOLOv5
>>>>>>> 0738cb1c15cb3e68b6d43efd4964e2496c9b4af7
pip install -qr models/yolov5/requirements.txt roboflow 
```

Start training process using YOLOv5

```commandline
python yolo_manager.py --version v5 --mode train --dataset /content/tody/yolov5/data/coco.yaml --epochs 30 --img 640
```

 
