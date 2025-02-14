# ImageSense AI - Image Search Quality Optimization

An AI-powered image search engine that uses advanced Large Language Models (LLMs) to enhance search capabilities by understanding user intent with greater effectiveness.

precision, FAISS for similarity search, and Streamlit for a user-friendly interface.

## 🌟 Demo

Live Demo: https://www.youtube.com/watch?v=ufqe0eF5GxM


## 🚀 Features

- **LLM Integration**: Incorporates Large Language Models to refine image search by better understanding user queries and context, resulting in more relevant and accurate search outcomes.
- **CLIP-based Image Embeddings**: Extracts embeddings from images using OpenAI's CLIP model.
- **Text-to-Image Search**: Converts text queries into embeddings to find the most relevant images.
- **Query Expansion**: Uses LLaMA 3.2 3b model (locally hosted via Ollama API) to improve search queries.
- **Efficient Search with FAISS**: Enables fast similarity search among images.
- **User-Friendly Web Interface**: Built with Streamlit.

---
## 🛠 Tools Used

- **Python**: Core programming language used for development.
- **OpenAI CLIP Model**: For extracting image and text embeddings.
- **FAISS (Facebook AI Similarity Search)**: For fast image retrieval.
- **LLaMA Model**: Hosted locally through Ollama API for query expansion.
- **Streamlit**: For creating the web interface.
- **PIL (Pillow)**: For image processing.

![Tools Overview](ImageSense%20AI%20diagram.png)
---


## 🛠️ Setup & Installation

🛠️ Setup & Installation

📊 Dataset Used

This project utilizes the Flickr8k dataset.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saileshdwivedy30/ImageSense-AI
cd ImageSense-AI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Paths

Modify `config.py` with your image and embedding folder paths:

```python
IMAGE_FOLDER = "path/to/your/images"
EMBEDDING_FOLDER = "path/to/store/embeddings"
```

### 4️⃣ Process Images

Extract embeddings for all images in the dataset:

```bash
python image_processing.py
```

### 5️⃣ Run the Web App

```bash
streamlit run app.py
```

---

## 🔍 How It Works

### 1️⃣ Image Processing

- Extracts embeddings from all images in `IMAGE_FOLDER`.
- Saves embeddings in `EMBEDDING_FOLDER` for fast retrieval.

### 2️⃣ Query Expansion

- The **query\_expansion.py** script refines user search queries using an LLaMA model (via Ollama API).

### 3️⃣ Image Search

- Converts the expanded text query into an embedding using CLIP.
- Searches for the closest matching images using **FAISS**.
- Returns the top relevant images.

### 4️⃣ Web Interface

- Users enter a search query via Streamlit UI.
- Expanded query is displayed.
- Matching images are shown as search results.

---

## 📷 Example Usage

1. Run the app with `streamlit run app.py`.
2. Enter a query like **"snow capped mountains"**.
3. The system expands the query and searches for the most relevant images.
4. The top-matching images are displayed.

---

## 📌 Future Enhancements

- Deep learning models for image classification to improve search result accuracy by categorizing and ranking images.
- Integration with cloud storage.
---

## 📜 License

This project is licensed under the **MIT License**.

