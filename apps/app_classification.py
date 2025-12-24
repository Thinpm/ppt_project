"""
Ứng dụng 3: Classification - Phân loại đơn giản
Ví dụ: Phân loại điểm dựa trên tọa độ (trong/circle)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))

import numpy as np
import matplotlib.pyplot as plt
from layers import DenseLayer, Tanh, Sigmoid
from network import NeuralNetwork
from loss import MSELoss
from optimizers import GradientDescent


def generate_circle_data(n_samples=100):
    """Tạo dữ liệu: điểm trong/circle dựa trên khoảng cách từ gốc"""
    np.random.seed(42)
    X = np.random.uniform(-2, 2, (n_samples, 2))
    # Label: 1 nếu trong circle (r < 1), 0 nếu ngoài
    y = ((X[:, 0]**2 + X[:, 1]**2) < 1).astype(float).reshape(-1, 1)
    return X, y


def main():
    print("=" * 70)
    print("ỨNG DỤNG 3: Classification - Phân loại điểm trong/circle")
    print("=" * 70)
    
    # Tạo dữ liệu
    print("\n1. Tạo dữ liệu training...")
    X, y = generate_circle_data(n_samples=100)
    print(f"   Số mẫu: {len(X)}")
    print(f"   Số điểm trong circle: {int(y.sum())}")
    print(f"   Số điểm ngoài circle: {int(len(y) - y.sum())}")
    
    # Tạo network: 2 input -> 6 hidden -> 1 output
    print("\n2. Khởi tạo Neural Network...")
    print("   Cấu trúc: 2 -> 6 -> 1 (với Tanh + Sigmoid)")
    network = NeuralNetwork([
        DenseLayer(2, 6),
        Tanh(),
        DenseLayer(6, 1),
        Sigmoid()  # Sigmoid để output trong [0, 1]
    ])
    
    # Train
    print("\n3. Huấn luyện...")
    loss_fn = MSELoss()
    optimizer = GradientDescent(learning_rate=0.1)
    
    losses = []
    epochs = 1000
    for epoch in range(epochs):
        loss = optimizer.step(network, loss_fn, X, y)
        losses.append(loss)
        if epoch % 200 == 0:
            print(f"   Epoch {epoch:4d}, Loss: {loss:.6f}")
    
    print(f"   Loss cuối: {losses[-1]:.6f}")
    
    # Test
    print("\n4. Đánh giá độ chính xác...")
    correct = 0
    for i in range(len(X)):
        pred = network.forward(X[i])
        pred_class = 1 if pred[0] > 0.5 else 0
        if pred_class == y[i][0]:
            correct += 1
    
    accuracy = correct / len(X) * 100
    print(f"   Độ chính xác: {correct}/{len(X)} = {accuracy:.1f}%")
    
    # Vẽ kết quả
    print("\n5. Vẽ kết quả...")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Dữ liệu thực tế
    axes[0].scatter(X[y.flatten() == 1, 0], X[y.flatten() == 1, 1], 
                    c='blue', label='Trong circle', alpha=0.6, s=30)
    axes[0].scatter(X[y.flatten() == 0, 0], X[y.flatten() == 0, 1], 
                    c='red', label='Ngoài circle', alpha=0.6, s=30)
    circle = plt.Circle((0, 0), 1, fill=False, color='green', linestyle='--', linewidth=2)
    axes[0].add_patch(circle)
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].set_title('Dữ liệu thực tế')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_aspect('equal')
    
    # Plot 2: Dự đoán của network
    X_test = np.random.uniform(-2, 2, (1000, 2))
    y_pred = []
    for x in X_test:
        pred = network.forward(x)
        y_pred.append(1 if pred[0] > 0.5 else 0)
    y_pred = np.array(y_pred)
    
    axes[1].scatter(X_test[y_pred == 1, 0], X_test[y_pred == 1, 1], 
                    c='blue', label='Dự đoán: Trong', alpha=0.3, s=10)
    axes[1].scatter(X_test[y_pred == 0, 0], X_test[y_pred == 0, 1], 
                    c='red', label='Dự đoán: Ngoài', alpha=0.3, s=10)
    circle = plt.Circle((0, 0), 1, fill=False, color='green', linestyle='--', linewidth=2)
    axes[1].add_patch(circle)
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    axes[1].set_title(f'Dự đoán của Network (Accuracy: {accuracy:.1f}%)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('app_classification.png', dpi=150, bbox_inches='tight')
    print("   ✅ Đã lưu vào 'app_classification.png'")
    
    print("\n" + "=" * 70)
    print("✅ Network đã học được phân loại trong/circle!")
    print("=" * 70)
    
    try:
        plt.show()
    except:
        pass


if __name__ == "__main__":
    main()


