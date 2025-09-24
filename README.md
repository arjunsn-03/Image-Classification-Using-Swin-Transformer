# README.md

# Swin Transformer Image Classification - Interactive Web App

This project implements a Swin Transformer for image classification on CIFAR-100 dataset with an interactive web interface.

## 🚀 Features

- **Interactive Web Interface**: Upload images and get instant predictions
- **Swin Transformer Architecture**: Efficient window-based attention mechanism
- **Real-time Predictions**: See top 5 predictions with confidence scores
- **Beautiful Visualization**: Confidence bars and intuitive UI
- **CIFAR-100 Support**: Classify images into 100 different categories

## 📁 Project Structure

```
IMG_CLS_SwingTransformer/
├── model.ipynb          # Jupyter notebook with model training
├── app.py               # Streamlit web application
├── save_model.py        # Script to save trained model
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🛠️ Installation

1. **Clone or download the project**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Step 1: Train the Model
1. Open `model.ipynb` in Jupyter Notebook
2. Run all cells to train the Swin Transformer model
3. After training, save the model by running:
   ```python
   # In the notebook, after training
   model.save('swin_transformer_model.h5')
   ```

### Step 2: Launch the Web App
1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
2. **Open your browser** and go to `http://localhost:8501`
3. **Upload an image** and click "Classify Image"
4. **View predictions** with confidence scores

## 🖼️ How to Use the Web App

1. **Upload Image**: Click "Choose an image file" and select a PNG, JPG, or JPEG image
2. **Classify**: Click the "🔍 Classify Image" button
3. **View Results**: See the top prediction and top 5 predictions with confidence bars
4. **Sample Classes**: Check the sidebar for CIFAR-100 class examples

## 📊 Model Performance

- **Test Accuracy**: 43.71%
- **Top-5 Accuracy**: 74.51%
- **Architecture**: Swin Transformer with window-based attention
- **Input Size**: 32×32×3 (CIFAR-100 standard)

## 🔧 Technical Details

### Swin Transformer Architecture
- **Patch Size**: 2×2
- **Window Size**: 2×2
- **Shift Size**: 1 (for cross-window communication)
- **Embedding Dimension**: 64
- **Attention Heads**: 8
- **MLP Size**: 256

### Key Features
- **Window-based Attention**: Reduces computational complexity from O(n²) to O(n)
- **Shifted Windows**: Enables information flow between non-overlapping windows
- **Hierarchical Structure**: Uses patch merging for multi-scale representations
- **Relative Position Bias**: Learns spatial relationships within windows

## 🎨 Web App Features

- **Responsive Design**: Works on desktop and mobile
- **Real-time Processing**: Instant image classification
- **Confidence Visualization**: Beautiful confidence bars
- **Top 5 Predictions**: See multiple possible classifications
- **Model Information**: Sidebar with performance metrics
- **Sample Classes**: Reference for CIFAR-100 categories

## 📝 Notes

- The model was trained on CIFAR-100 dataset (32×32 images)
- For best results, upload images containing objects similar to CIFAR-100 classes
- The model automatically resizes uploaded images to 32×32 pixels
- Training requires significant computational resources (GPU recommended)

## 🚀 Quick Start

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Train model**: Run `model.ipynb` and save the model
3. **Launch app**: `streamlit run app.py`
4. **Upload image**: Use the web interface to classify images

## 🔍 Troubleshooting

- **Model not found**: Make sure to train and save the model first
- **Import errors**: Install all requirements with `pip install -r requirements.txt`
- **Slow predictions**: The model processes images in real-time, some delay is normal
- **Poor accuracy**: Upload images similar to CIFAR-100 classes for best results

## 📚 References

- [Swin Transformer Paper](https://arxiv.org/abs/2103.14030)
- [CIFAR-100 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Happy Classifying! 🎉**
