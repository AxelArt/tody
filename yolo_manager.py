 
import argparse
import subprocess


# Define the command-line arguments
parser = argparse.ArgumentParser(prog="python yolo_manager.py", description='A Tool for Object Detection using YOLO')
# REQUIRED Arguments
parser.add_argument('--v', '--version', type=int, choices=['5', '6', '7', '8'], required=True,
                    help='The YOLO version to use')
parser.add_argument('--mode', type=str, choices=['train', 'test', 'validation'], required=True,
                    help='The mode to run')
parser.add_argument('--img','--image_size', type=int, required=True,
                    help='Image size')
# OPTIONAL Arguments
parser.add_argument('--d', '--dataset', type=str, required=False, default='datasets',
                    help='The path to the custom dataset')
parser.add_argument('--b', '--batch', type=int, required=False, default=16,
                    help='The batch size')
parser.add_argument('--e', '--epochs', type=int, required=False, default=50,
                    help='Number of epochs')

# Parse the command-line arguments
args = parser.parse_args()

# Define the YOLOv5 and YOLOv6 commands
if args.version == 'v5':
    if args.mode == 'train':
        command = f"python models/yolov5/train.py --img {args.img} --batch {args.batch} --epochs {args.epochs} --data {args.dataset} --weights models/yolov5/yolov5s.pt --cache"
    elif args.mode == 'test':
        command = f"python models/yolov5/detect.py --weights models/yolov5/runs/train/exp/weights/best.pt --source {args.dataset}/test/images  --img {args.img} --conf 0.4"
    else:
        command = f"python models/yolov5/val.py --weights models/yolov5/runs/train/exp/weights/best.pt --data {args.dataset} --imgsz {args.img} --task val"
elif args.version == 'v6':
    if args.mode == 'train':
        command = f"python models/yolov6/tools/train.py --img-size {args.img} --batch {args.batch} --epochs {args.epochs} --data {args.dataset} --weights models/yolov6/yolov5s.pt --cache"
    elif args.mode == 'test':
        command = f"python models/yolov6/tools/infer.py --weights models/yolov6/runs/train/exp/weights/best.pt --source {args.dataset}/images/test  --img-size {args.img} --conf 0.4"
    else:
        command = f"python models/yolov6/tools/eval.py --weights models/yolov6/runs/train/exp/weights/best.pt --data {args.dataset} --img-size {args.img} --task val"        
else:
    print("Not yet implemented")

# Execute the corresponding YOLO command
subprocess.run(command, shell=True)
