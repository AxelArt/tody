import argparse
import subprocess

# Define the command-line arguments
parser = argparse.ArgumentParser(prog="python yolo_manager.py", description='A Tool for Object Detection using YOLO')
# REQUIRED Arguments
parser.add_argument('--version', type=str, choices=['v5', 'v6', 'v7', 'v8'], required=True,
                    help='The YOLO version to use')
parser.add_argument('--mode', type=str, choices=['train', 'test', 'val'], required=True,
                    help='The mode to run')
parser.add_argument('--img', '--image_size', type=int, required=True,
                    help='Image size')
# OPTIONAL Arguments
parser.add_argument('--dataset', type=str, required=False, default='datasets',
                    help='The path to the custom dataset')
parser.add_argument('--batch', type=int, required=False, default=16,
                    help='The batch size')
parser.add_argument('--epochs', type=int, required=False, default=50,
                    help='Number of epochs')
parser.add_argument('--conf', type=float, required=False, default=0.2,
                    help='')
parser.add_argument('--source', type=str, required=False,
                    help='')
parser.add_argument('--weights', type=str, required=False,
                    help='')
parser.add_argument('--yaml', type=str, required=False,
                    help='')
# Parse the command-line arguments
args = parser.parse_args()

# Define the YOLOv5 and YOLOv6 commands
if args.version == 'v5':
    if args.mode == 'train':
        command = f"python models/yolov5/train.py --img {args.img} --batch {args.batch} --epochs {args.epochs} --data {args.dataset} --weights models/yolov5/yolov5s.pt --cache"
    elif args.mode == 'test':
        command = f"python models/yolov5/detect.py --weights {args.weights} --source {args.dataset} --img {args.img} --conf {args.conf}"
    else:
        command = f"python models/yolov5/val.py --weights {args.weights} --data {args.dataset} --imgsz {args.img} --task val"
elif args.version == 'v6':
    if args.mode == 'train':
        command = f"python models/yolov6/tools/train.py --img-size {args.img} --batch {args.batch} --epochs {args.epochs} --data {args.dataset} --conf models/yolov6/configs/yolov6s.py"
    elif args.mode == 'test':
        command = f"python models/yolov6/tools/infer.py --yaml {args.dataset} --weights {args.weights} --source {args.source}  --img-size {args.img} --yaml {args.yaml}"
    else:
        command = f"python models/yolov6/tools/eval.py --weights {args.weights} --data {args.dataset} --img-size {args.img}"
elif args.version == 'v7':
    if args.mode == 'train':
        command = f"python models/yolov7/train.py --img-size {args.img} --batch-size {args.batch} --epochs {args.epochs} --data {args.dataset} --weights models/yolov7/yolov7_training.pt"
    elif args.mode == 'test':
        command = f"python models/yolov7/test.py --weights {args.weights} --data {args.source} --conf {args.conf}"
    else:
        command = f"python models/yolov7/detect.py --weights {args.weights} --source {args.source} --conf {args.conf}"
elif args.version == 'v8':
    if args.mode == 'train':
        command = f"yolo task=detect mode=train model=yolov8s.pt data={args.dataset} epochs={args.epochs} imgsz={args.img} plots=True"
    elif args.mode == 'test':
        command = f"yolo task=detect mode=predict model={args.weights} conf={args.conf} source={args.source}"
    else:
        command = f"yolo task=detect mode=val model={args.weights} data={args.dataset}"
else:
    print("Please choose among v5, v6, v7 and v8")

# Execute the corresponding YOLO command
subprocess.run(command, shell=True)
