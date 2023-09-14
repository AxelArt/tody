# TODY

A tool for object detection using YOLO models

---

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

```commandline
pip install -qr models/yolov5/requirements.txt roboflow 
```

Start training process using YOLOv5

```commandline
python yolo_manager.py --help
usage: python yolo_manager.py [-h] --dataset DATASET [--mode {train,test,validation}] [--img {generic,apk}] [-p PERCENTAGE] [-v]

Tool for Object Detection using YOLO

optional arguments:
  -h, --help            show this help message and exit

Arguments:
  --dataset DATASET
                    The dataset path
                        
  --version {'v5', 'v6', 'v7', 'v8'}
  --mode {train,test,validation}
  --img IMAGE_SIZE
                    FORMAT ACCEPTED = S
  --batch BATCH_SIZE
  --epochs EPOCHS
                number of epochs
  
```
Example:
```
python yolo_manager.py --version v5 --mode train --dataset /content/tody/yolov5/data/coco.yaml --epochs 30 --img 640
```

### Acknowledgements

The authors would like to thank the 'Trust, Security and Privacy' research group within the 
[Institute of Informatics and Telematics](https://www.iit.cnr.it/) (CNR - Pisa, Italy), which support their research.

 
