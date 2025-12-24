# Neural Network từ đầu - Bài tập Computational Methods

## Mô tả
Implement Neural Network từ đầu bằng **"Hard-coding the Backpropagation"** - Code tay thuật toán lan truyền ngược.

**Nguyên tắc:**
- ✅ **ĐƯỢC DÙNG:** NumPy (tính toán ma trận), matplotlib (vẽ biểu đồ), scipy.optimize (chỉ wrapper cho BFGS)
- ❌ **CẤM TUYỆT ĐỐI:** TensorFlow, PyTorch, Keras, sklearn
- ⚠️ **Scipy.optimize:** Chỉ dùng như wrapper, gradient vẫn tính bằng Backpropagation tự implement

**Điểm quan trọng:** Tự viết công thức đạo hàm, tự implement chain rule, không dùng automatic differentiation.

## Cấu trúc project

```
final/
├── network/          (Backend - Core modules)
│   ├── layers.py     (DenseLayer, Tanh, Sigmoid, ReLU)
│   ├── network.py    (NeuralNetwork class)
│   ├── loss.py       (MSELoss)
│   └── optimizers.py  (GradientDescent, BFGSOptimizer)
│
├── demos/            (Demos - Main demo files)
│   ├── main.py       (Demo chính: GD + BFGS, giao diện đẹp)
│   └── demo_menu.py  (Menu chọn ứng dụng)
│
└── apps/             (Applications - Real-world apps)
    ├── app_xor.py           (XOR Problem)
    ├── app_regression.py     (Dự đoán giá nhà)
    ├── app_classification.py (Phân loại circle)
    └── app_list.py          (Danh sách apps)
```

## Cài đặt

```bash
pip install numpy matplotlib scipy
```

## Chạy demo

### 1. Demo chính (GD + BFGS):
```bash
cd demos
python main.py
```

**Kết quả:**
- So sánh Gradient Descent vs BFGS
- Function Approximation: sin(x)
- Visualization với 2 đồ thị
- Giao diện terminal đẹp với màu sắc

### 2. Menu chọn ứng dụng:
```bash
cd demos
python demo_menu.py
```

### 3. Ứng dụng riêng lẻ:
```bash
cd apps
python app_xor.py          # XOR Problem
python app_regression.py   # Dự đoán giá nhà
python app_classification.py  # Phân loại circle
```

## Tính năng

1. ✅ **Tính gradient bằng Backpropagation** (không dùng thư viện AI)
   - Tự implement chain rule
   - Gradient được tính tay theo công thức toán học
   - Không dùng automatic differentiation

2. ✅ **Code chạy được, có visualization**
   - Console output rõ ràng
   - Plot matplotlib minh họa kết quả
   - Giao diện terminal đẹp

3. ✅ **Thiết kế adaptive**
   - Dễ thêm/bớt layer
   - Thay đổi số neuron không cần viết lại code
   - Code training tự động thích nghi

4. ✅ **So sánh Gradient Descent vs BFGS**
   - Cùng dữ liệu, cùng network ban đầu
   - So sánh loss cuối và số iterations
   - Visualization so sánh dự đoán

5. ✅ **Demo ứng dụng thực tế**
   - Function Approximation: sin(x) (demos/main.py)
   - XOR Problem (apps/app_xor.py)
   - Regression: Dự đoán giá nhà (apps/app_regression.py)
   - Classification: Phân loại circle (apps/app_classification.py)

## Yêu cầu đã hoàn thành

- [x] **Yêu cầu 1:** Phát biểu bài toán tối ưu
- [x] **Yêu cầu 2:** Trình bày Backpropagation chi tiết
- [x] **Yêu cầu 3:** Code Simple Network (không dùng thư viện AI)
- [x] **Yêu cầu 4:** So sánh optimizer (GD vs BFGS)
- [x] **Yêu cầu 5:** Ứng dụng thực tế với demo

## Kết quả

### Function Approximation (sin(x))
- Network học được hàm sin(x) từ dữ liệu có nhiễu
- Loss giảm từ ~0.1 xuống ~0.01
- Cả GD và BFGS đều cho kết quả tốt
- Visualization rõ ràng, dễ hiểu

### Chứng minh Backpropagation
- Loss giảm dần → Gradient được tính đúng
- Network học được → Backpropagation hoạt động tốt
- Không dùng thư viện AI → Tự implement hoàn toàn

## Tài liệu

- `demos/GIAI_THICH_KET_QUA.md`: Giải thích chi tiết kết quả
- `THUYET_TRINH.md`: Script thuyết trình
# ppt_project
