import torch
from torchvision import models, transforms
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os
import numpy as np
import pickle
from config import IMAGE_FOLDER, EMBEDDING_FOLDER

# Load CLIP Model
print("Loading CLIP model...")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
print("CLIP model loaded!")

# Load ResNet50 Model for Image Classification
#print("Loading ResNet50 model...")
#resnet_model = models.resnet50(pretrained=True)
#resnet_model.eval()
#print("ResNet50 model loaded!")

# Image Preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


def get_image_embedding(image_path):
    """ Extracts embedding using CLIP """
    image = Image.open(image_path)
    inputs = clip_processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        embedding = clip_model.get_image_features(**inputs)
    return embedding.numpy()


# def classify_image(image_path):
#     """ Classifies an image using ResNet50 """
#     image = Image.open(image_path).convert("RGB")
#     image = transform(image).unsqueeze(0)
#     with torch.no_grad():
#         output = resnet_model(image)
#     return output.argmax().item()  # Return predicted class


def process_images():
    """ Processes all images and saves embeddings """
    os.makedirs(EMBEDDING_FOLDER, exist_ok=True)
    image_embeddings = []

    for img_name in os.listdir(IMAGE_FOLDER):
        img_path = os.path.join(IMAGE_FOLDER, img_name)
        embedding = get_image_embedding(img_path)
        image_embeddings.append(embedding)

    # Save embeddings
    with open(f"{EMBEDDING_FOLDER}/image_embeddings.pkl", "wb") as f:
        pickle.dump(image_embeddings, f)


if __name__ == "__main__":
    print("Processing images...")
    process_images()
    print("Image processing complete!")