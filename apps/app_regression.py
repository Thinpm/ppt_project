"""
Ứng dụng 2: Regression - Dự đoán giá trị liên tục
Ví dụ: Dự đoán giá nhà dựa trên diện tích
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))

import numpy as np
import matplotlib.pyplot as plt
from layers import DenseLayer, Tanh
from network import NeuralNetwork
from loss import MSELoss
from optimizers import GradientDescent


def generate_house_data(n_samples=30):
    """Tạo dữ liệu giả: giá nhà = 50 * diện tích + nhiễu"""
    np.random.seed(42)
    area = np.random.uniform(20, 200, n_samples)  # Diện tích (m²)
    price = 50 * area + np.random.normal(0, 200, n_samples)  # Giá (triệu VNĐ)
    return area.reshape(-1, 1), price.reshape(-1, 1)


def main():
    print("=" * 70)
    print("ỨNG DỤNG 2: Regression - Dự đoán giá nhà")
    print("=" * 70)
    
    # Tạo dữ liệu
    print("\n1. Tạo dữ liệu training...")
    X, y = generate_house_data(n_samples=30)
    print(f"   Số mẫu: {len(X)}")
    print(f"   Diện tích: {X.min():.1f} - {X.max():.1f} m²")
    print(f"   Giá: {y.min():.1f} - {y.max():.1f} triệu VNĐ")
    
    # Tạo network: 1 input -> 8 hidden -> 1 output
    print("\n2. Khởi tạo Neural Network...")
    print("   Cấu trúc: 1 -> 8 -> 1 (với Tanh activation)")
    network = NeuralNetwork([
        DenseLayer(1, 8),
        Tanh(),
        DenseLayer(8, 1)
    ])
    
    # Train
    print("\n3. Huấn luyện...")
    loss_fn = MSELoss()
    optimizer = GradientDescent(learning_rate=0.001)
    
    losses = []
    epochs = 1000
    for epoch in range(epochs):
        loss = optimizer.step(network, loss_fn, X, y)
        losses.append(loss)
        if epoch % 200 == 0:
            print(f"   Epoch {epoch:4d}, Loss: {loss:.2f}")
    
    print(f"   Loss cuối: {losses[-1]:.2f}")
    
    # Dự đoán
    print("\n4. Dự đoán trên dữ liệu test...")
    X_test = np.linspace(20, 200, 100).reshape(-1, 1)
    y_pred = network.predict(X_test)
    
    # Tính error
    mse = np.mean((network.predict(X) - y)**2)
    print(f"   Mean Squared Error: {mse:.2f}")
    
    # Vẽ kết quả
    print("\n5. Vẽ kết quả...")
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.6, label='Training data', s=50, color='blue')
    plt.plot(X_test, y_pred, 'r-', label='Network Prediction', linewidth=2)
    plt.xlabel('Diện tích (m²)')
    plt.ylabel('Giá (triệu VNĐ)')
    plt.title('Dự đoán giá nhà dựa trên diện tích')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('app_regression.png', dpi=150, bbox_inches='tight')
    print("   ✅ Đã lưu vào 'app_regression.png'")
    
    # Ví dụ dự đoán
    print("\n6. Ví dụ dự đoán:")
    test_areas = [50, 100, 150]
    for area in test_areas:
        pred = network.forward(np.array([[area]]))
        print(f"   Diện tích {area:3d} m² → Giá dự đoán: {pred[0]:.0f} triệu VNĐ")
    
    print("\n" + "=" * 70)
    print("✅ Network đã học được mối quan hệ giữa diện tích và giá!")
    print("=" * 70)
    
    try:
        plt.show()
    except:
        pass


if __name__ == "__main__":
    main()


