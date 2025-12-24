"""
Module định nghĩa hàm loss và cách tính gradient
"""
import numpy as np


class MSELoss:
    """
    Mean Squared Error Loss
    Loss = 0.5 * sum((y_pred - y_true)^2)
    """
    def __init__(self):
        pass
    
    def forward(self, y_pred, y_true):
        """
        Tính loss
        y_pred: dự đoán của network
        y_true: giá trị thực tế
        """
        self.y_pred = y_pred
        self.y_true = y_true
        # Loss = 0.5 * ||y_pred - y_true||^2
        error = y_pred - y_true
        return 0.5 * np.sum(error ** 2)
    
    def backward(self):
        """
        Tính gradient của loss theo y_pred
        
        QUAN TRỌNG: Gradient được tính TỰ TAY theo công thức toán học.
        Đạo hàm của 0.5*(y_pred - y_true)^2 theo y_pred = y_pred - y_true
        
        Không dùng automatic differentiation, tự implement theo công thức.
        """
        # Đạo hàm của 0.5*(y_pred - y_true)^2 theo y_pred
        return self.y_pred - self.y_true

