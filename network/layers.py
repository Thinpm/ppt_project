"""
Module định nghĩa các layer cho Neural Network
Thiết kế theo hướng module hóa, dễ mở rộng
"""
import numpy as np


class DenseLayer:
    """
    Dense Layer (Fully Connected Layer)
    Thực hiện: output = W @ input + b
    """
    def __init__(self, n_in, n_out):
        """
        n_in: số neuron đầu vào
        n_out: số neuron đầu ra
        """
        # Khởi tạo trọng số ngẫu nhiên nhỏ
        self.W = np.random.randn(n_out, n_in) * 0.1
        self.b = np.zeros(n_out)
        
    def forward(self, x):
        """
        Forward pass: tính output từ input
        Lưu input để dùng trong backward
        """
        self.x = x  # Lưu để tính gradient sau
        # output = W @ x + b
        return self.W @ x + self.b
    
    def backward(self, grad_out, lr):
        """
        Backward pass: tính gradient và cập nhật trọng số
        
        QUAN TRỌNG: Gradient được tính TỰ TAY theo công thức toán học,
        không dùng automatic differentiation (như PyTorch's autograd).
        Đây là "Hard-coding the Backpropagation" - code tay thuật toán.
        
        grad_out: gradient từ layer sau
        lr: learning rate
        """
        # Gradient của W: grad_W = grad_out @ x^T (theo chain rule)
        # Đây là công thức toán học, tự implement, không dùng thư viện AI
        grad_W = np.outer(grad_out, self.x)
        
        # Gradient của b: grad_b = grad_out (theo chain rule)
        grad_b = grad_out
        
        # Lưu gradient để dùng với optimizer (như BFGS)
        self.grad_W = grad_W
        self.grad_b = grad_b
        
        # Gradient truyền về layer trước: grad_x = W^T @ grad_out
        grad_x = self.W.T @ grad_out
        
        # Cập nhật trọng số (Gradient Descent)
        self.W -= lr * grad_W
        self.b -= lr * grad_b
        
        return grad_x
    
    def get_params(self):
        """Trả về tất cả tham số (để dùng với optimizer)"""
        return {'W': self.W, 'b': self.b}
    
    def set_params(self, params):
        """Đặt lại tham số (để dùng với optimizer)"""
        self.W = params['W']
        self.b = params['b']


class ActivationLayer:
    """
    Base class cho activation function
    """
    def forward(self, x):
        raise NotImplementedError
    
    def backward(self, grad_out, lr):
        """
        grad_out: gradient từ layer sau
        lr: không dùng ở đây nhưng giữ để interface nhất quán
        """
        return grad_out * self.derivative(self.x)
    
    def derivative(self, x):
        raise NotImplementedError


class Tanh(ActivationLayer):
    """
    Tanh activation: tanh(x)
    """
    def forward(self, x):
        self.x = x
        return np.tanh(x)
    
    def derivative(self, x):
        # Đạo hàm của tanh: 1 - tanh^2(x)
        return 1 - np.tanh(x)**2


class Sigmoid(ActivationLayer):
    """
    Sigmoid activation: 1/(1 + exp(-x))
    """
    def forward(self, x):
        self.x = x
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip để tránh overflow
    
    def derivative(self, x):
        s = self.forward(x)
        return s * (1 - s)


class ReLU(ActivationLayer):
    """
    ReLU activation: max(0, x)
    """
    def forward(self, x):
        self.x = x
        return np.maximum(0, x)
    
    def derivative(self, x):
        return (x > 0).astype(float)

