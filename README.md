# Steel Defect Detection

This project focuses on detecting surface defects in steel using deep learning techniques. It utilizes image-based classification to identify common flaws such as scratches, rolled-in scales, and patches.

The codebase is written in Python and organized into modular components including training scripts, configuration files, and utility functions. The main workflow is managed through the notebook `main.ipynb`, which handles model training and evaluation.

### Dataset  
We use the NEU Surface Defect Dataset, available for download here:  
🔗 [NEU Surface Defect Dataset on Kaggle](https://www.kaggle.com/datasets/zy12345/neudet)

After downloading, place the dataset inside a folder named `NEU-DET` within the project directory.

### How to Run

1. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   
2. Launch Jupyter Notebook and open main.ipynb

3. Run the notebook cells sequentially to train and evaluate the model
   
### Model Architecture

The model is built on a **Swin Transformer Backbone** that extracts rich features from steel surface images. It includes three heads:

- **Contrastive Projection Head:** Learns robust feature embeddings using supervised contrastive loss.
- **Classification Head:** Classifies images into defect categories.
- **Detection Head:** Detects and localizes defects with bounding boxes and objectness scores.

The model supports three modes — contrastive learning, classification, and detection — allowing flexible training strategies.

### Training Pipeline

The project implements a **K-Fold Cross-Validation** training pipeline, which splits the dataset into multiple folds. The model trains on K-1 folds and validates on the remaining fold in each iteration. This approach improves generalization and reduces overfitting by using all data for training and validation across folds.

The pipeline supports all model modes and adapts loss functions and data processing accordingly.
