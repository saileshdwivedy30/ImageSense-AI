import streamlit as st
from query_expansion import expand_query
from search_engine import search_images
import os
from config import IMAGE_FOLDER

st.title("🔍 ImageSense AI - Image Search Quality Optimization")

query = st.text_input("Enter an image search query:")

if query:
    st.write("🔄 Expanding Query...")
    expanded_query = expand_query(query)
    st.write(f"**Expanded Query:** {expanded_query}")

    st.write("🔍 Searching Images...")
    results = search_images(expanded_query)

    st.write("### 🎯 Top Results")
    for img in results:
        st.image(os.path.join(IMAGE_FOLDER, img), caption=img)
