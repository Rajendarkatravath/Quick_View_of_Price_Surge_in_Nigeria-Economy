import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import os

# Function to convert Jupyter Notebook to HTML
def convert_notebook_to_html(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = False  # Include input cells
    body, _ = html_exporter.from_notebook_node(nb)
    return body

st.title("Jupyter Notebooks Viewer & Downloader")

st.sidebar.title("Actions")
choice = st.sidebar.selectbox("Choose Action:", ["View Local Notebooks"])

if choice == "View Notebooks":
    # List all notebooks in the specified directory
    notebooks_dir = 'Notebooks'
    if not os.path.exists(notebooks_dir):
        st.error(f"The directory {notebooks_dir} does not exist.")
    else:
        notebook_files = [f for f in os.listdir(notebooks_dir) if f.endswith('.ipynb')]
        selected_notebook = st.selectbox("Select a notebook to display", notebook_files)

        if selected_notebook:
            notebook_path = os.path.join(notebooks_dir, selected_notebook)
            try:
                notebook_html = convert_notebook_to_html(notebook_path)
                st.components.v1.html(notebook_html, height=1000, scrolling=True)
                st.download_button(
                    label="Download Notebook",
                    data=open(notebook_path, "rb").read(),
                    file_name=selected_notebook,
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"An error occurred while displaying the notebook: {e}")
