 
import argparse
import subprocess
from models/yolov5.train import train, val, test
from models/yolov6.train import train, val, test

# Define the command-line arguments
parser = argparse.ArgumentParser(description='YOLOv5 and YOLOv6 manager')
parser.add_argument('--version', type=str, choices=['v5', 'v6'], required=True,
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
        command = f"python models/yolov5/train.py --img 640 --batch 16 --epochs 50 --data {args.dataset} --cfg models/yolov5/custom_yolov5s.yaml --weights models/yolov5/yolov5s.pt --name custom_yolov5s_results --cache"
    elif args.mode == 'test':
        command = f"python models/yolov5/test.py --weights models/yolov5/custom_yolov5s_results/weights/best.pt --data {args.dataset} --img 640 --conf 0.4"
    else:
        command = f"python models/yolov5/val.py --weights models/yolov5/custom_yolov5s_results/weights/best.pt --data {args.dataset} --img 640 --conf 0.4"
else:
    if args.mode == 'train':
        command = f"python models/yolov6/train.py --img 640 --batch 16 --epochs 50 --data {args.dataset} --cfg models/yolov6/custom_yolov6s.yaml --weights models/syolov6/yolov6s.pt --name custom_yolov6s_results --cache"
    elif args.mode == 'test':
        command = f"python models/yolov6/test.py --weights models/yolov6/custom_yolov6s_results/weights/best.pt --data {args.dataset} --img 640 --conf 0.4"
    else:
        command = f"python models/yolov6/val.py --weights models/yolov6/custom_yolov6s_results/weights/best.pt --data {args.dataset} --img 640 --conf 0.4"

# Execute the corresponding YOLO command
subprocess.run(command, shell=True)
