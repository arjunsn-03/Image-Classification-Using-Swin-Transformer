# Model Saving Script
# Run this after training your model in the notebook

import keras
import numpy as np
import tensorflow as tf
from keras import layers
from keras import ops

# Load your trained model (replace with your actual model variable name)
# model = your_trained_model  # Uncomment and replace with your model

def save_model_with_architecture(model, filename='swin_transformer_model.h5'):
    """
    Save the trained model with all its architecture and weights
    """
    try:
        # Save the entire model
        model.save(filename)
        print(f"✅ Model saved successfully as {filename}")
        
        # Also save model summary
        with open('model_summary.txt', 'w') as f:
            model.summary(print_fn=lambda x: f.write(x + '\n'))
        print("✅ Model summary saved as model_summary.txt")
        
    except Exception as e:
        print(f"❌ Error saving model: {e}")

def load_and_test_model(filename='swin_transformer_model.h5'):
    """
    Load the saved model and test it
    """
    try:
        # Load the model
        loaded_model = keras.models.load_model(filename)
        print(f"✅ Model loaded successfully from {filename}")
        
        # Print model summary
        print("\n📊 Model Summary:")
        loaded_model.summary()
        
        return loaded_model
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

# Example usage:
# After training your model in the notebook, run:
# save_model_with_architecture(model)

# To test loading:
# loaded_model = load_and_test_model()
