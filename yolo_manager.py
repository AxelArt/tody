 
import argparse
import subprocess


# Define the command-line arguments
parser = argparse.ArgumentParser(description='YOLOv5 and YOLOv6 manager')
parser.add_argument('--version', type=str, choices=['v5', 'v6', 'v7', 'v8'], required=True,
                    help='The YOLO version to use')
parser.add_argument('--mode', type=str, choices=['train', 'test', 'validation'], required=True,
                    help='The mode to run')
parser.add_argument('--dataset', type=str, required=True,
                    help='The path to the custom dataset')

# Parse the command-line arguments
args = parser.parse_args()

# Define the YOLOv5 and YOLOv6 commands
if args.version == 'v5':
    if args.mode == 'train':
        command = f"python models/yolov5/train.py --img 640 --batch 16 --epochs 50 --data {args.dataset} --weights models/yolov5/yolov5s.pt --cache"
    elif args.mode == 'test':
        command = f"python models/yolov5/detect.py --weights models/yolov5/runs/train/exp/weights/best.pt --source {args.dataset}/test/images  --img 640 --conf 0.4"
    else:
        command = f"python models/yolov5/val.py --weights models/yolov5/runs/train/exp/weights/best.pt --data {args.dataset} --imgsz 640 --task val"
else
    print("Not yet implemented")

# Execute the corresponding YOLO command
subprocess.run(command, shell=True)
