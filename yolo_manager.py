 
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
parser.add_argument('--img', type=int, required=True,
                    help='Image size')
parser.add_argument('--batch', type=int, required=True,
                    help='The batch size')
parser.add_argument('--epochs', type=int, required=True,
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
