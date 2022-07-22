from flask import Flask, render_template, request
import torch
from torchvision import models, transforms
from PIL import Image
from torch import nn


app = Flask(__name__)
# model = pickle.load(open('model_state.pth'))

@app.route('/', methods=['GET'])

def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def predict():
    imagefile= request.files['imagefile']
    image_path= './images/' + imagefile.filename
    imagefile.save(image_path)

    model = models.resnext50_32x4d(pretrained=True)
    inputs = model.fc.in_features
    outputs = 6
    clf = nn.Linear(inputs, outputs)


    model.fc = clf
    model.load_state_dict(torch.load('model_state.pth'))
    image = Image.open(image_path)
    # convert_tensor = transforms.ToTensor()
    # image_tensor = convert_tensor(image)
    classes = torch.load('classes.pth')


    transform = transforms.Compose([
        transforms.Resize((150, 150)),
        transforms.CenterCrop(124),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225])

    ])

    processed_image = transform(image).unsqueeze(0)

    model.eval()
    with torch.no_grad():
        pred = torch.argmax(model(processed_image), dim=1).item()

    # return classes[pred]


    return render_template('index.html', prediction = classes[pred])

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
