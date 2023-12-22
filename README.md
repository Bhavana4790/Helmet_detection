# Bicycle Helmet Detection
Collected data on helmet images and annotated them for training the object detection model using yolov8.
This repository contains train, test and valid data. I am also providing data.yaml file which can be used for training the model using yolov8.

For prediction, use the code below:

```bash
from ultralytics import YOLO

model = YOLO('best.pt') # your pretrained model
results = model(source = "video.mp4", save=True)
```
