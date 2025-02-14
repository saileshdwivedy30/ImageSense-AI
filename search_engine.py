import torch
import faiss
import numpy as np
import pickle
import os
from image_processing import get_image_embedding
from config import EMBEDDING_FOLDER, IMAGE_FOLDER
from transformers import CLIPProcessor, CLIPModel

# Load CLIP model for text embeddings
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_text_embedding(text_query):
    """ Converts a text query into a CLIP embedding """
    inputs = clip_processor(text=[text_query], return_tensors="pt")
    with torch.no_grad():
        text_embedding = clip_model.get_text_features(**inputs)
    return text_embedding.numpy()


def load_embeddings():
    """ Loads saved image embeddings """
    with open(f"{EMBEDDING_FOLDER}/image_embeddings.pkl", "rb") as f:
        return pickle.load(f)


def build_faiss_index():
    """ Builds a FAISS index for fast image retrieval """
    embeddings = load_embeddings()
    embeddings = np.vstack(embeddings)  # Convert list to NumPy array

    index = faiss.IndexFlatL2(512)  # 512-dim vector
    index.add(embeddings)

    return index


def search_images(query, top_k=5):
    """ Searches for the most relevant images using text-to-image similarity """
    query_embedding = get_text_embedding(query)  # Convert query text to embedding
    index = build_faiss_index()

    distances, indices = index.search(query_embedding, top_k)  # Find similar images

    image_files = os.listdir(IMAGE_FOLDER)
    results = [image_files[i] for i in indices[0]]

    return results


# if __name__ == "__main__":
#    print(search_images("sunset beach"))
