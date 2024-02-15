# TODY

A tool for object detection using YOLO models

---

## Preliminary steps

Clone the project

```commandline
git clone https://github.com/AxelArt/tody.git
```

Run the following command on your Colab notebook to start the submodules and install all depedencies

```commandline
bash setup.sh
```

Or install dependencies only for a specific model ex: YOLOv5

```commandline
pip install -qr models/yolov5/requirements.txt roboflow 
```

Type yolo_manager.py --help

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
   --weights WEIGHTS
                the path to the saved weights
  
```
Start training process using YOLOv5 and a custom ataset as an example:
```
python yolo_manager.py --version v5 --mode train --dataset {dataset.location}/data.yaml 
--epochs 30 --img 100
```

For validation process using YOLOv5 as an example

```
python yolo_manager.py --version v5 --mode val --img 100 --dataset {dataset.location}/data.yaml 
--weights <path_to_weights>
```

To run test process using YOLOv5 as an example

```
python yolo_manager.py --version v5 --mode test --img 100 --conf 0.25 --dataset {dataset.location}/test/images --weights <path_to_weights>
```
Before start training be sure that you have updated the path on data.yaml. An exammle bellow for yolov6

```commandline
test: /content/tody/models/yolov6/utility-meter-reading-dataset-for-automatic-reading-yolo-1/images/test
train: /content/tody/models/yolov6/utility-meter-reading-dataset-for-automatic-reading-yolo-1/images/train
val: /content/tody/models/yolov6/utility-meter-reading-dataset-for-automatic-reading-yolo-1/images/valid
```


### Acknowledgements

This work has been carried out within the Italian National Doctorate on Artificial Intelligence run by the Sapienza University of Rome in collaboration with the Institute of Informatics and Telematics (IIT), the National Research Council of Italy (CNR).


 
