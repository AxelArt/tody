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

This work has been carried out within the Italian National Doctorate on Artificial Intelligence run by the Sapienza University of Rome in collaboration with the Institute of Informatics and Telematics (IIT), the National Research Council of Italy (CNR).


 
