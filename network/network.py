"""
Neural Network class - thiết kế adaptive, dễ mở rộng
"""
import numpy as np


class NeuralNetwork:
    """
    Neural Network với thiết kế module hóa
    Có thể thêm/bớt layer mà không cần sửa code training
    """
    def __init__(self, layers):
        """
        layers: danh sách các layer (DenseLayer, ActivationLayer, ...)
        """
        self.layers = layers
    
    def forward(self, x):
        """
        Forward pass: truyền dữ liệu qua tất cả các layer
        """
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def backward(self, grad, lr):
        """
        Backward pass: lan truyền gradient ngược từ output về input
        grad: gradient từ loss function
        lr: learning rate
        """
        # Đi ngược từ layer cuối về layer đầu
        for layer in reversed(self.layers):
            grad = layer.backward(grad, lr)
        return grad
    
    def predict(self, X):
        """
        Dự đoán cho nhiều mẫu
        X: mảng các input (mỗi hàng là một mẫu)
        """
        predictions = []
        for x in X:
            pred = self.forward(x)
            predictions.append(pred)
        return np.array(predictions)
    
    def get_all_params(self):
        """
        Lấy tất cả tham số của network (để dùng với optimizer)
        Trả về: danh sách các tham số
        """
        params = []
        for layer in self.layers:
            if hasattr(layer, 'get_params'):
                params.append(layer.get_params())
        return params
    
    def set_all_params(self, params_list):
        """
        Đặt lại tất cả tham số (để dùng với optimizer)
        """
        param_idx = 0
        for layer in self.layers:
            if hasattr(layer, 'set_params'):
                layer.set_params(params_list[param_idx])
                param_idx += 1
    
    def flatten_params(self):
        """
        Chuyển tất cả tham số thành vector 1 chiều (để dùng với BFGS)
        """
        params = []
        for layer in self.layers:
            if hasattr(layer, 'W'):
                params.append(layer.W.flatten())
                params.append(layer.b.flatten())
        return np.concatenate(params) if params else np.array([])
    
    def unflatten_params(self, flat_params):
        """
        Chuyển vector 1 chiều về lại thành tham số của các layer
        """
        idx = 0
        for layer in self.layers:
            if hasattr(layer, 'W'):
                W_size = layer.W.size
                b_size = layer.b.size
                
                layer.W = flat_params[idx:idx+W_size].reshape(layer.W.shape)
                idx += W_size
                
                layer.b = flat_params[idx:idx+b_size].reshape(layer.b.shape)
                idx += b_size

