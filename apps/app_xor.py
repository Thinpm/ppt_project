"""
Ứng dụng 1: Giải bài toán XOR
XOR là bài toán kinh điển trong Neural Network
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))

import numpy as np
from layers import DenseLayer, Tanh, Sigmoid
from network import NeuralNetwork
from loss import MSELoss
from optimizers import GradientDescent


def main():
    print("=" * 70)
    print("ỨNG DỤNG 1: Giải bài toán XOR")
    print("=" * 70)
    
    # Dữ liệu XOR
    print("\n1. Dữ liệu XOR:")
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])  # XOR: khác nhau = 1, giống nhau = 0
    
    print("   Input | Output")
    print("   " + "-" * 20)
    for i in range(len(X)):
        print(f"   {X[i]} | {y[i][0]}")
    
    # Tạo network: 2 input -> 5 hidden -> 1 output
    print("\n2. Khởi tạo Neural Network...")
    print("   Cấu trúc: 2 -> 5 -> 1 (với Tanh activation)")
    network = NeuralNetwork([
        DenseLayer(2, 5),
        Tanh(),
        DenseLayer(5, 1),
        Sigmoid()  # Sigmoid để output trong [0, 1]
    ])
    
    # Khởi tạo lại weights tốt hơn
    for layer in network.layers:
        if hasattr(layer, 'W'):
            layer.W = np.random.randn(*layer.W.shape) * 0.5
            layer.b = np.random.randn(*layer.b.shape) * 0.1
    
    # Train
    print("\n3. Huấn luyện...")
    loss_fn = MSELoss()
    optimizer = GradientDescent(learning_rate=0.8)
    
    losses = []
    for epoch in range(3000):
        loss = optimizer.step(network, loss_fn, X, y)
        losses.append(loss)
        if epoch % 600 == 0:
            print(f"   Epoch {epoch:4d}, Loss: {loss:.6f}")
    
    print(f"   Loss cuối: {losses[-1]:.6f}")
    
    # Test
    print("\n4. Kết quả dự đoán:")
    print("   Input | Target | Dự đoán | Đúng?")
    print("   " + "-" * 40)
    correct = 0
    for i in range(len(X)):
        pred = network.forward(X[i])
        pred_binary = 1 if pred[0] > 0.5 else 0
        is_correct = "✅" if pred_binary == y[i][0] else "❌"
        if pred_binary == y[i][0]:
            correct += 1
        print(f"   {X[i]} |   {y[i][0]}    |  {pred[0]:.3f} ({pred_binary}) | {is_correct}")
    
    print(f"\n   Độ chính xác: {correct}/{len(X)} = {correct/len(X)*100:.1f}%")
    
    print("\n" + "=" * 70)
    print("✅ Network đã học được bài toán XOR!")
    print("=" * 70)


if __name__ == "__main__":
    main()

