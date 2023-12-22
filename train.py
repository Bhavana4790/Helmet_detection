from ultralytics import YOLO

# the results will be saved in runs/detect/train folder while you run the code
# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from scratch
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Use the model
results = model.train(data='data.yaml', epochs=90)  # train the model
results = model.val()  # evaluate model performance on the validation set
