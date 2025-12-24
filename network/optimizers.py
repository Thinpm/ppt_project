"""
Các phương pháp tối ưu: Gradient Descent, BFGS
"""
import numpy as np
try:
    from scipy.optimize import minimize
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("Warning: scipy not available. BFGS optimizer will not work.")


class GradientDescent:
    """
    Gradient Descent optimizer đơn giản
    """
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
    
    def step(self, network, loss_fn, X, y):
        """
        Thực hiện một bước gradient descent
        """
        total_loss = 0
        n_samples = len(X)
        
        # Tính gradient cho từng mẫu và cộng dồn
        for i in range(n_samples):
            # Forward pass
            y_pred = network.forward(X[i])
            
            # Tính loss
            loss = loss_fn.forward(y_pred, y[i])
            total_loss += loss
            
            # Backward pass
            grad = loss_fn.backward()
            network.backward(grad, self.learning_rate)
        
        return total_loss / n_samples


class BFGSOptimizer:
    """
    BFGS Optimizer sử dụng scipy.optimize.minimize
    
    QUAN TRỌNG: Gradient vẫn được tính hoàn toàn bằng Backpropagation tự implement!
    scipy.optimize.minimize chỉ là wrapper để tối ưu, KHÔNG tính gradient tự động.
    Gradient được truyền vào qua tham số jac=gradient, và gradient đó được tính
    bằng backpropagation do chúng ta tự viết (không dùng automatic differentiation).
    
    BFGS là phương pháp quasi-Newton, không cần tính Hessian trực tiếp.
    """
    def __init__(self):
        if not SCIPY_AVAILABLE:
            raise ImportError("scipy is required for BFGS optimizer")
    
    def optimize(self, network, loss_fn, X, y, max_iter=100):
        """
        Tối ưu network bằng BFGS
        """
        # Hàm tính loss
        def objective(params):
            # Đặt lại tham số
            network.unflatten_params(params)
            
            # Tính loss
            total_loss = 0
            for i in range(len(X)):
                y_pred = network.forward(X[i])
                loss = loss_fn.forward(y_pred, y[i])
                total_loss += loss
            
            return total_loss / len(X)
        
        # Hàm tính gradient - QUAN TRỌNG: Gradient được tính bằng Backpropagation tự implement!
        def gradient(params):
            """
            Tính gradient bằng Backpropagation do chúng ta tự viết.
            KHÔNG dùng automatic differentiation của scipy.
            """
            # Đặt lại tham số
            network.unflatten_params(params)
            
            # Tính gradient cho tất cả mẫu và cộng dồn
            grad_flat = np.zeros_like(params)
            
            for i in range(len(X)):
                # Forward pass - tính output từ input
                y_pred = network.forward(X[i])
                loss_fn.forward(y_pred, y[i])
                
                # Backward pass - tính gradient bằng chain rule (tự implement)
                # lr=0 vì chỉ cần gradient, không cập nhật weights
                grad_loss = loss_fn.backward()
                network.backward(grad_loss, 0)  # Backpropagation tự viết!
                
                # Thu thập gradient từ các layer (đã được tính trong backward)
                grad_list = []
                for layer in network.layers:
                    if hasattr(layer, 'grad_W'):
                        grad_list.append(layer.grad_W.flatten())
                        grad_list.append(layer.grad_b.flatten())
                
                if grad_list:
                    grad_flat += np.concatenate(grad_list)
            
            return grad_flat / len(X)
        
        # Khởi tạo tham số
        initial_params = network.flatten_params()
        
        # Tối ưu bằng BFGS
        result = minimize(
            objective,
            initial_params,
            method='BFGS',
            jac=gradient,
            options={'maxiter': max_iter, 'disp': True}
        )
        
        # Đặt lại tham số tối ưu
        network.unflatten_params(result.x)
        
        return result
