"""
TEST TÍNH THÍCH NGHI - CHỨNG MINH CODE KHÔNG CẦN VIẾT LẠI
Test này chứng minh:
1. Thêm/bớt layer → code training KHÔNG ĐỔI
2. Thay đổi số neuron → code training KHÔNG ĐỔI
3. Thiết kế adaptive - chỉ cần thay đổi khởi tạo network
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))

import numpy as np
from layers import DenseLayer, Tanh, Sigmoid
from network import NeuralNetwork
from loss import MSELoss
from optimizers import GradientDescent

print("=" * 80)
print("TEST TÍNH THÍCH NGHI - THÊM/BỚT LAYER, THAY ĐỔI SỐ NEURON")
print("=" * 80)

# Dữ liệu test chung
X = np.array([[0.5], [1.0], [-0.5], [0.0]])
y = np.array([[0.5], [1.0], [-0.5], [0.0]])

# Hàm train chung - KHÔNG THAY ĐỔI cho tất cả test
def train_network(network, X, y, epochs=20, lr=0.1):
    """Hàm train chung - dùng cho MỌI network"""
    loss_fn = MSELoss()
    optimizer = GradientDescent(learning_rate=lr)
    losses = []
    
    for epoch in range(epochs):
        loss = optimizer.step(network, loss_fn, X, y)
        losses.append(loss)
    
    return losses

print("\n" + "=" * 80)
print("TEST 1: Network đơn giản - 1 hidden layer (1 -> 5 -> 1)")
print("=" * 80)
network1 = NeuralNetwork([
    DenseLayer(1, 5),
    Tanh(),
    DenseLayer(5, 1)
])
print(f"Cấu trúc: 1 input -> 5 hidden -> 1 output")
print(f"Số layer: {len(network1.layers)}")

losses1 = train_network(network1, X, y, epochs=20)
print(f"Loss ban đầu: {losses1[0]:.6f}")
print(f"Loss cuối:    {losses1[-1]:.6f}")
print(f"✅ Train thành công với hàm train_network() chung!")

print("\n" + "=" * 80)
print("TEST 2: Network phức tạp hơn - 2 hidden layers (1 -> 10 -> 5 -> 1)")
print("=" * 80)
print("⚠️  THÊM LAYER - Code training KHÔNG ĐỔI!")
network2 = NeuralNetwork([
    DenseLayer(1, 10),   # Layer 1: 1 -> 10
    Tanh(),
    DenseLayer(10, 5),   # Layer 2: 10 -> 5 (THÊM LAYER NÀY)
    Tanh(),
    DenseLayer(5, 1)     # Layer 3: 5 -> 1
])
print(f"Cấu trúc: 1 input -> 10 hidden -> 5 hidden -> 1 output")
print(f"Số layer: {len(network2.layers)}")

losses2 = train_network(network2, X, y, epochs=20)  # DÙNG CÙNG HÀM TRAIN!
print(f"Loss ban đầu: {losses2[0]:.6f}")
print(f"Loss cuối:    {losses2[-1]:.6f}")
print(f"✅ Train thành công - KHÔNG CẦN VIẾT LẠI CODE TRAINING!")

print("\n" + "=" * 80)
print("TEST 3: Thay đổi số neuron (1 -> 3 -> 1)")
print("=" * 80)
print("⚠️  THAY ĐỔI SỐ NEURON - Code training KHÔNG ĐỔI!")
network3 = NeuralNetwork([
    DenseLayer(1, 3),    # Thay đổi từ 5 -> 3 neuron
    Tanh(),
    DenseLayer(3, 1)
])
print(f"Cấu trúc: 1 input -> 3 hidden -> 1 output")
print(f"Số layer: {len(network3.layers)}")

losses3 = train_network(network3, X, y, epochs=20)  # DÙNG CÙNG HÀM TRAIN!
print(f"Loss ban đầu: {losses3[0]:.6f}")
print(f"Loss cuối:    {losses3[-1]:.6f}")
print(f"✅ Train thành công - KHÔNG CẦN VIẾT LẠI CODE!")

print("\n" + "=" * 80)
print("TÓM TẮT - CHỨNG MINH TÍNH THÍCH NGHI")
print("=" * 80)
print("""
✅ ĐÃ TEST 3 NETWORK KHÁC NHAU:
   1. Network đơn giản (1 -> 5 -> 1)
   2. Network phức tạp (1 -> 10 -> 5 -> 1) - THÊM LAYER
   3. Network khác số neuron (1 -> 3 -> 1) - THAY ĐỔI SỐ NEURON

✅ TẤT CẢ ĐỀU DÙNG CÙNG MỘT HÀM TRAIN:
   - train_network(network, X, y, epochs=20, lr=0.1)
   - KHÔNG CẦN VIẾT LẠI CODE TRAINING!
   - KHÔNG CẦN VIẾT LẠI BACKPROPAGATION!

✅ THIẾT KẾ ADAPTIVE:
   - Chỉ cần thay đổi khởi tạo network
   - Code training tự động thích nghi
   - Mỗi layer tự quản lý forward và backward

✅ ĐÁP ỨNG YÊU CẦU CỦA THẦY:
   "thiết kế code có tính thích nghi, tức là khi thêm bớt layer 
   hoặc số lượng tham số thì code vẫn chạy được mà không phải viết lại"
""")
print("=" * 80)



