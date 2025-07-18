from ultralytics import YOLO

# Load the pretrained yolov11m-pose model
model = YOLO('yolo11m-pose.pt')

# Train the model on the Penn Action dataset
results = model.train(
    data='/home/alexis/Documentos/strike/YOLO-Training/pennaction.yaml',
    epochs=1,
    imgsz=640,
    batch=16,
    name='yolo11m-pose-pennaction'
)