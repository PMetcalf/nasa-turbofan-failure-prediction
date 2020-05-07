'''
NASA Turbofan Failure Prediction - PyTorch Neural Network Model

This file supports training and evalaution of a Neural Network Model, using PyTorch and Tensors. 

'''

###################################
# Module Importations (A - Z Format)
###################################
import torch

import src.ntfp_dataset_preprocessing as dataset_preprocessing

def create_pytorch_tensors(data_df):
    """
    Create and return PyTorch Tensors from input dataframe.
    ======================================

    Args:
        data_df (dataframe) - Dataframe with engine data to be modelled.

    Returns:
        X_tensor, y_tensor (Tensors) - PyTorch Tensors for use with NN models.
    """

    # Create numpy arrays of training and test data using helper method. 
    X_train_array, X_test_array, y_train_array, y_test_array = dataset_preprocessing.prepare_training_data(data_df, 'Cycles')

    print(X_train_array)

    # Convert each array into Tensor.
    X_train_tensor = torch.from_numpy(X_train_array)

    print(X_train_tensor)

    # Return Tensors.

def create_pytorch_NN():
    """
    Initialise and return PyTorch neural network.
    ======================================

    Args:
        None.

    Returns:
        nn (Neural Network) - PyTorch Neural Network.
    """

    pass

def train_pytorch_NN():
    """
    Train PyTorch neural network using Tensors.
    ======================================

    Args:
        tensors (Tensors) - PyTorch tensor training data.

    Returns:
        nn (Neural Network) - PyTorch Neural Network.
    """

    pass

def train_pytorch_NN():
    """
    Train PyTorch neural network using Tensors.
    ======================================

    Args:
        tensors (Tensors) - PyTorch tensor training data.

    Returns:
        nn (Neural Network) - PyTorch Neural Network.
    """

    pass

def evaluate_pytorch_NN():
    """
    Evaluate PyTorch neural network.
    ======================================

    Args:
        nn (Neural Network) - PyTorch neural network to undergo evaluation.
        test_data (Tensors) - PyTorch Tensors on which model is evaluated.

    Returns:
        evaluation_results (tuple) - Results of Neural Network evaluation.
    """

    pass