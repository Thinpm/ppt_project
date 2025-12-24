# GIẢI THÍCH CHI TIẾT KẾT QUẢ CHẠY `demos/main.py`

## PHẦN 1: HEADER (Dòng 1-4)

```
======================================================================
               NEURAL NETWORK DEMO               
          Function Approximation: sin(x)          
======================================================================
```

### Dòng 1: `======================================================================`
- **Ý nghĩa**: Đường phân cách trên cùng (70 ký tự `=`)
- **Mục đích**: Tạo khung đẹp, phân tách phần header
- **Màu sắc**: Màu hồng/tím, in đậm (từ code: `Colors.BOLD + Colors.HEADER`)

### Dòng 2: `               NEURAL NETWORK DEMO               `
- **Ý nghĩa**: Tiêu đề chính của demo
- **Nội dung**: "NEURAL NETWORK DEMO" - Demo về Neural Network
- **Căn chỉnh**: Căn giữa (15 space mỗi bên)
- **Màu sắc**: Màu hồng/tím, in đậm

### Dòng 3: `          Function Approximation: sin(x)          `
- **Ý nghĩa**: Mô tả ứng dụng cụ thể
- **Nội dung**: "Function Approximation: sin(x)" - Xấp xỉ hàm sin(x)
- **Giải thích**: Network sẽ học để xấp xỉ hàm sin(x) từ dữ liệu training
- **Căn chỉnh**: Căn giữa (10 space mỗi bên)
- **Màu sắc**: Màu hồng/tím, in đậm

### Dòng 4: `======================================================================`
- **Ý nghĩa**: Đường phân cách dưới cùng (giống dòng 1)
- **Mục đích**: Đóng khung header

---

## PHẦN 2: SECTION 1 - TẠO DỮ LIỆU (Dòng 6-11)

```
┌────────────────────────────────────────────────────────────────────┐
│                      1. TẠO DỮ LIỆU TRAINING                       │
└────────────────────────────────────────────────────────────────────┘
  Số mẫu:                                                        50
  Input range:                                        [-3.14, 3.14]
  Output range:                                       [-1.19, 1.02]
```

### Dòng 6: `┌────────────────────────────────────────────────────────────────────┐`
- **Ý nghĩa**: Cạnh trên của khung section (box drawing character)
- **Ký tự**: `┌` = góc trên trái, `─` = đường ngang, `┐` = góc trên phải
- **Màu sắc**: Xanh lơ (cyan), in đậm
- **Độ rộng**: 70 ký tự

### Dòng 7: `│                      1. TẠO DỮ LIỆU TRAINING                       │`
- **Ý nghĩa**: Tiêu đề section 1
- **Nội dung**: "1. TẠO DỮ LIỆU TRAINING" - Tạo dữ liệu để training
- **Căn chỉnh**: Căn giữa trong khung
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 8: `└────────────────────────────────────────────────────────────────────┘`
- **Ý nghĩa**: Cạnh dưới của khung section
- **Ký tự**: `└` = góc dưới trái, `┘` = góc dưới phải
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 9: `  Số mẫu:                                                        50`
- **Ý nghĩa**: Hiển thị số lượng mẫu dữ liệu training
- **Giải thích**:
  - **Label** (màu xanh dương): "Số mẫu:" - Số lượng điểm dữ liệu
  - **Value** (màu xanh lá): `50` - Có 50 điểm dữ liệu
- **Căn chỉnh**: Label căn trái (25 ký tự), Value căn phải (40 ký tự)
- **Nguồn gốc**: Từ code `generate_data(n_samples=50)`

### Dòng 10: `  Input range:                                        [-3.14, 3.14]`
- **Ý nghĩa**: Hiển thị khoảng giá trị của input (X)
- **Giải thích**:
  - **Label**: "Input range:" - Khoảng giá trị đầu vào
  - **Value**: `[-3.14, 3.14]` - X chạy từ -π đến π
- **Nguồn gốc**: Từ code `X = np.linspace(-np.pi, np.pi, 50)`
- **Lý do**: π ≈ 3.14159, nên hiển thị là 3.14

### Dòng 11: `  Output range:                                       [-1.19, 1.02]`
- **Ý nghĩa**: Hiển thị khoảng giá trị của output (y)
- **Giải thích**:
  - **Label**: "Output range:" - Khoảng giá trị đầu ra
  - **Value**: `[-1.19, 1.02]` - y chạy từ -1.19 đến 1.02
- **Nguồn gốc**: Từ code `y = np.sin(X) + 0.1 * np.random.randn(n_samples)`
- **Lý do**: 
  - sin(x) có giá trị từ -1 đến 1
  - Cộng thêm nhiễu 0.1 nên có thể vượt quá [-1, 1] một chút
  - -1.19 và 1.02 là giá trị min/max thực tế của 50 điểm dữ liệu

---

## PHẦN 3: SECTION 2 - KHỞI TẠO NETWORK (Dòng 13-23)

```
┌────────────────────────────────────────────────────────────────────┐
│                     2. KHỞI TẠO NEURAL NETWORK                     │
└────────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
╠════════════════════════════════════════════════════════════════════╣
║Cấu trúc: 1 input → 10 hidden → 1 output                            ║
║Activation: Tanh                                                    ║
║Tổng số tham số: 31                                                 ║
╚════════════════════════════════════════════════════════════════════╝
```

### Dòng 13-15: Khung section 2
- **Tương tự** section 1, nhưng tiêu đề là "2. KHỞI TẠO NEURAL NETWORK"
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 16: (Dòng trống)
- **Mục đích**: Tạo khoảng cách giữa section header và box thông tin

### Dòng 17: `╔════════════════════════════════════════════════════════════════════╗`
- **Ý nghĩa**: Cạnh trên của box thông tin (box drawing nặng hơn)
- **Ký tự**: `╔` = góc trên trái (double line), `═` = đường ngang (double line)
- **Độ rộng**: 70 ký tự

### Dòng 18: `║                                                                    ║`
- **Ý nghĩa**: Dòng trống trong box (tạo khoảng cách)
- **Ký tự**: `║` = cạnh dọc (double line)

### Dòng 19: `╠════════════════════════════════════════════════════════════════════╣`
- **Ý nghĩa**: Đường phân cách giữa phần trống và nội dung
- **Ký tự**: `╠` = nối dọc-trái, `╣` = nối dọc-phải

### Dòng 20: `║Cấu trúc: 1 input → 10 hidden → 1 output                            ║`
- **Ý nghĩa**: Mô tả cấu trúc của neural network
- **Giải thích chi tiết**:
  - **1 input**: 1 neuron đầu vào (nhận giá trị x)
  - **→ 10 hidden**: 10 neuron trong lớp ẩn (hidden layer)
  - **→ 1 output**: 1 neuron đầu ra (trả về giá trị dự đoán)
- **Tổng cộng**: 3 layers (1 input layer, 1 hidden layer, 1 output layer)
- **Nguồn gốc**: Từ code `NeuralNetwork([DenseLayer(1, 10), Tanh(), DenseLayer(10, 1)])`

### Dòng 21: `║Activation: Tanh                                                    ║`
- **Ý nghĩa**: Hàm kích hoạt (activation function) được sử dụng
- **Giải thích**:
  - **Tanh**: Hyperbolic tangent
  - **Công thức**: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
  - **Khoảng giá trị**: [-1, 1]
  - **Vị trí**: Áp dụng sau hidden layer
- **Nguồn gốc**: Từ code `Tanh()` trong danh sách layers

### Dòng 22: `║Tổng số tham số: 31                                                 ║`
- **Ý nghĩa**: Tổng số tham số (parameters) cần học trong network
- **Giải thích chi tiết**:
  - **Layer 1** (DenseLayer 1→10):
    - Weight matrix: 1 × 10 = 10 tham số
    - Bias vector: 10 tham số
    - Tổng: 20 tham số
  - **Layer 2** (DenseLayer 10→1):
    - Weight matrix: 10 × 1 = 10 tham số
    - Bias vector: 1 tham số
    - Tổng: 11 tham số
  - **Tổng cộng**: 20 + 11 = 31 tham số
- **Lưu ý**: Tanh không có tham số (chỉ là hàm toán học)

### Dòng 23: `╚════════════════════════════════════════════════════════════════════╝`
- **Ý nghĩa**: Cạnh dưới của box thông tin
- **Ký tự**: `╚` = góc dưới trái, `╝` = góc dưới phải

---

## PHẦN 4: SECTION 3 - TRAINING GRADIENT DESCENT (Dòng 25-29)

```
┌────────────────────────────────────────────────────────────────────┐
│                  3. HUẤN LUYỆN - GRADIENT DESCENT                  │
└────────────────────────────────────────────────────────────────────┘
  Training progress:
  [██████████████████████████████████████████████████] 100.0% | Epoch 1000 | Loss: 0.006411
```

### Dòng 25-27: Khung section 3
- **Tiêu đề**: "3. HUẤN LUYỆN - GRADIENT DESCENT"
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 28: `  Training progress:`
- **Ý nghĩa**: Nhãn cho thanh tiến trình
- **Màu sắc**: Màu vàng (từ code: `Colors.YELLOW`)
- **Mục đích**: Báo hiệu đang hiển thị quá trình training

### Dòng 29: `  [██████████████████████████████████████████████████] 100.0% | Epoch 1000 | Loss: 0.006411`
- **Ý nghĩa**: Thanh tiến trình và thông tin training
- **Giải thích chi tiết từng phần**:
  
  **1. Thanh tiến trình**: `[██████████████████████████████████████████████████]`
  - `█`: Ký tự đầy (filled) - phần đã hoàn thành
  - `░`: Ký tự rỗng (empty) - phần chưa hoàn thành
  - **Trong ví dụ này**: Tất cả đều là `█` vì đã 100% hoàn thành
  - **Độ rộng**: 50 ký tự
  
  **2. Phần trăm**: `100.0%`
  - **Ý nghĩa**: Đã hoàn thành 100% số epoch
  - **Format**: 5 ký tự, 1 chữ số thập phân
  
  **3. Epoch**: `Epoch 1000`
  - **Ý nghĩa**: Đang ở epoch thứ 1000 (epoch cuối cùng)
  - **Format**: 4 chữ số
  
  **4. Loss**: `Loss: 0.006411`
  - **Ý nghĩa**: Giá trị loss tại epoch 1000
  - **Giải thích**: 
    - Loss = 0.006411 (rất nhỏ, gần 0)
    - Càng nhỏ càng tốt (network học tốt)
    - So với loss ban đầu (0.214744), đã giảm rất nhiều
  - **Màu sắc**: Màu vàng (từ code: `Colors.YELLOW`)
  - **Format**: 6 chữ số thập phân

- **Lưu ý**: Dòng này được in bằng `\r` (carriage return), nên nó ghi đè lên dòng cũ mỗi lần update

---

## PHẦN 5: SECTION 4 - TRAINING BFGS (Dòng 31-42)

```
┌────────────────────────────────────────────────────────────────────┐
│                        4. HUẤN LUYỆN - BFGS                        │
└────────────────────────────────────────────────────────────────────┘
  BFGS Optimization...
/home/thuypm/Desktop/ttu/pptinh/final/.venv/lib/python3.10/site-packages/scipy/optimize/_minimize.py:733: OptimizeWarning: Maximum number of iterations has been exceeded.
  res = _minimize_bfgs(fun, x0, args, jac, callback, **options)
         Current function value: 0.003510
         Iterations: 100
         Function evaluations: 110
         Gradient evaluations: 110
  Final loss: 0.003510
  Iterations: 100
```

### Dòng 31-33: Khung section 4
- **Tiêu đề**: "4. HUẤN LUYỆN - BFGS"
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 34: `  BFGS Optimization...`
- **Ý nghĩa**: Thông báo đang chạy thuật toán BFGS
- **Màu sắc**: Màu vàng
- **BFGS**: Broyden-Fletcher-Goldfarb-Shanno - thuật toán tối ưu bậc 2

### Dòng 35: `/home/thuypm/Desktop/ttu/pptinh/final/.venv/lib/python3.10/site-packages/scipy/optimize/_minimize.py:733: OptimizeWarning: Maximum number of iterations has been exceeded.`
- **Ý nghĩa**: Cảnh báo từ thư viện scipy
- **Giải thích**:
  - **OptimizeWarning**: Cảnh báo về quá trình tối ưu
  - **"Maximum number of iterations has been exceeded"**: Đã vượt quá số lần lặp tối đa
  - **Lý do**: BFGS đặt `max_iter=100`, nhưng có thể chưa hội tụ hoàn toàn
  - **Ảnh hưởng**: Không nghiêm trọng, chỉ là cảnh báo

### Dòng 36: `  res = _minimize_bfgs(fun, x0, args, jac, callback, **options)`
- **Ý nghĩa**: Dòng code trong scipy gây ra cảnh báo
- **Mục đích**: Giúp debug nếu cần (thường không cần quan tâm)

### Dòng 37: `         Current function value: 0.003510`
- **Ý nghĩa**: Giá trị hàm mục tiêu (loss) hiện tại
- **Giải thích**: 
  - Loss = 0.003510 (rất nhỏ)
  - Tốt hơn Gradient Descent (0.006411)
- **Format**: Từ scipy tự động in ra

### Dòng 38: `         Iterations: 100`
- **Ý nghĩa**: Số lần lặp đã thực hiện
- **Giải thích**: Đã chạy đủ 100 iterations (đạt max_iter)
- **Format**: Từ scipy tự động in ra

### Dòng 39: `         Function evaluations: 110`
- **Ý nghĩa**: Số lần gọi hàm loss (evaluate loss function)
- **Giải thích**: 
  - BFGS cần đánh giá hàm nhiều lần để tìm hướng tối ưu
  - 110 lần > 100 iterations vì có thể cần thêm đánh giá để tính gradient

### Dòng 40: `         Gradient evaluations: 110`
- **Ý nghĩa**: Số lần tính gradient
- **Giải thích**: Mỗi lần đánh giá hàm có thể kèm theo tính gradient
- **So sánh**: Gradient Descent tính gradient mỗi epoch (1000 lần), BFGS chỉ 110 lần

### Dòng 41: `  Final loss: 0.003510`
- **Ý nghĩa**: Loss cuối cùng sau khi training với BFGS
- **Màu sắc**: Màu xanh lá (từ code: `Colors.GREEN`)
- **So sánh**: 
  - BFGS: 0.003510
  - Gradient Descent: 0.006411
  - **BFGS tốt hơn** (loss nhỏ hơn)

### Dòng 42: `  Iterations: 100`
- **Ý nghĩa**: Số iterations đã chạy
- **Màu sắc**: Màu xanh lá
- **So sánh**: 
  - BFGS: 100 iterations
  - Gradient Descent: 1000 epochs
  - **BFGS hiệu quả hơn** (ít iterations hơn nhưng loss tốt hơn)

---

## PHẦN 6: SECTION 5 - KẾT QUẢ VÀ SO SÁNH (Dòng 44-63)

```
┌────────────────────────────────────────────────────────────────────┐
│                       5. KẾT QUẢ VÀ SO SÁNH                        │
└────────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
╠════════════════════════════════════════════════════════════════════╣
║Gradient Descent:                                                   ║
║  Loss ban đầu:     0.214744                               ║
║  Loss cuối:        0.006411                               ║
║  Giảm loss:        97.0%                                  ║
║  MSE trên test:    0.006884                               ║
║                                                                    ║
║BFGS:                                                               ║
║  Loss cuối:        0.003510                               ║
║  MSE trên test:    0.001914                               ║
║  Iterations:       100                                    ║
║                                                                    ║
║So sánh: BFGS tốt hơn Gradient Descent                              ║
╚════════════════════════════════════════════════════════════════════╝
```

### Dòng 44-46: Khung section 5
- **Tiêu đề**: "5. KẾT QUẢ VÀ SO SÁNH"
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 47-48: Box thông tin (cạnh trên và dòng trống)
- **Tương tự** box ở section 2

### Dòng 49: `║Gradient Descent:                                                   ║`
- **Ý nghĩa**: Tiêu đề cho phần kết quả Gradient Descent
- **Mục đích**: Phân tách rõ ràng giữa 2 thuật toán

### Dòng 50: `║  Loss ban đầu:     0.214744                               ║`
- **Ý nghĩa**: Loss tại epoch đầu tiên (epoch 0)
- **Giải thích**:
  - **Loss ban đầu**: Giá trị loss trước khi training
  - **0.214744**: Loss khá lớn (network chưa học gì)
  - **Màu sắc**: Màu đỏ (từ code: `Colors.RED`) - thể hiện giá trị cao/bad

### Dòng 51: `║  Loss cuối:        0.006411                               ║`
- **Ý nghĩa**: Loss tại epoch cuối cùng (epoch 1000)
- **Giải thích**:
  - **0.006411**: Loss rất nhỏ (network đã học tốt)
  - **Màu sắc**: Màu xanh lá (từ code: `Colors.GREEN`) - thể hiện giá trị tốt
  - **So sánh**: Giảm từ 0.214744 → 0.006411 (giảm rất nhiều!)

### Dòng 52: `║  Giảm loss:        97.0%                                  ║`
- **Ý nghĩa**: Phần trăm loss đã giảm
- **Công thức**: `((loss_ban_dau - loss_cuoi) / loss_ban_dau) × 100%`
- **Tính toán**: `((0.214744 - 0.006411) / 0.214744) × 100% = 97.0%`
- **Giải thích**: Loss đã giảm 97% - network học rất tốt!
- **Màu sắc**: Màu xanh lá

### Dòng 53: `║  MSE trên test:    0.006884                               ║`
- **Ý nghĩa**: Mean Squared Error trên tập test
- **Giải thích**:
  - **Test set**: 200 điểm mới (không dùng để training)
  - **MSE**: Đo độ lệch giữa dự đoán và giá trị thật
  - **0.006884**: MSE nhỏ → dự đoán chính xác
  - **Công thức**: `MSE = mean((y_pred - y_true)²)`
- **Màu sắc**: Màu xanh lơ (từ code: `Colors.CYAN`)

### Dòng 54: `║                                                                    ║`
- **Ý nghĩa**: Dòng trống để phân tách

### Dòng 55: `║BFGS:                                                               ║`
- **Ý nghĩa**: Tiêu đề cho phần kết quả BFGS

### Dòng 56: `║  Loss cuối:        0.003510                               ║`
- **Ý nghĩa**: Loss cuối cùng của BFGS
- **So sánh**: 
  - BFGS: 0.003510
  - Gradient Descent: 0.006411
  - **BFGS tốt hơn** (loss nhỏ hơn ~2 lần)
- **Màu sắc**: Màu xanh lá

### Dòng 57: `║  MSE trên test:    0.001914                               ║`
- **Ý nghĩa**: MSE trên test set của BFGS
- **So sánh**:
  - BFGS: 0.001914
  - Gradient Descent: 0.006884
  - **BFGS tốt hơn** (MSE nhỏ hơn ~3.6 lần)
- **Màu sắc**: Màu xanh lơ

### Dòng 58: `║  Iterations:       100                                    ║`
- **Ý nghĩa**: Số iterations của BFGS
- **So sánh**:
  - BFGS: 100 iterations
  - Gradient Descent: 1000 epochs
  - **BFGS hiệu quả hơn** (ít iterations hơn 10 lần nhưng kết quả tốt hơn)
- **Màu sắc**: Màu xanh lơ

### Dòng 59: `║                                                                    ║`
- **Ý nghĩa**: Dòng trống để phân tách

### Dòng 60: `║So sánh: BFGS tốt hơn Gradient Descent                              ║`
- **Ý nghĩa**: Kết luận so sánh 2 thuật toán
- **Giải thích**: 
  - Dựa trên loss cuối: BFGS (0.003510) < GD (0.006411)
  - Dựa trên MSE test: BFGS (0.001914) < GD (0.006884)
  - Dựa trên số iterations: BFGS (100) < GD (1000)
  - **→ BFGS tốt hơn về mọi mặt!**

### Dòng 61-63: Box thông tin (cạnh dưới)
- **Tương tự** box ở section 2

---

## PHẦN 7: SECTION 6 - VISUALIZATION (Dòng 65-68)

```
┌────────────────────────────────────────────────────────────────────┐
│                          6. VISUALIZATION                          │
└────────────────────────────────────────────────────────────────────┘
  Đã lưu đồ thị:                             results_comparison.png
```

### Dòng 65-67: Khung section 6
- **Tiêu đề**: "6. VISUALIZATION"
- **Màu sắc**: Xanh lơ, in đậm

### Dòng 68: `  Đã lưu đồ thị:                             results_comparison.png`
- **Ý nghĩa**: Thông báo đã lưu file đồ thị
- **Giải thích**:
  - **Label** (màu xanh dương): "Đã lưu đồ thị:"
  - **Value** (màu xanh lá): `results_comparison.png`
- **Nội dung file**: 
  - **Plot 1**: So sánh sin(x) thật vs dự đoán của GD và BFGS
  - **Plot 2**: Đồ thị loss theo epoch (Gradient Descent)
- **Vị trí**: File được lưu trong thư mục `demos/`

---

## PHẦN 8: FOOTER (Dòng 70-72)

```
======================================================================
                         HOÀN THÀNH!                         
======================================================================
```

### Dòng 70: `======================================================================`
- **Ý nghĩa**: Đường phân cách trên cùng của footer
- **Màu sắc**: Màu xanh lá, in đậm (từ code: `Colors.BOLD + Colors.GREEN`)

### Dòng 71: `                         HOÀN THÀNH!                         `
- **Ý nghĩa**: Thông báo hoàn thành demo
- **Căn chỉnh**: Căn giữa (25 space mỗi bên)
- **Màu sắc**: Màu xanh lá, in đậm

### Dòng 72: `======================================================================`
- **Ý nghĩa**: Đường phân cách dưới cùng của footer
- **Màu sắc**: Màu xanh lá, in đậm

---

## PHẦN 9: WARNING (Dòng 74-75)

```
/home/thuypm/Desktop/ttu/pptinh/final/demos/main.py:211: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
  plt.show()
```

### Dòng 74: `/home/thuypm/Desktop/ttu/pptinh/final/demos/main.py:211: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown`
- **Ý nghĩa**: Cảnh báo từ matplotlib
- **Giải thích**:
  - **UserWarning**: Cảnh báo cho người dùng (không phải lỗi)
  - **"FigureCanvasAgg is non-interactive"**: Backend của matplotlib không tương tác được
  - **"cannot be shown"**: Không thể hiển thị cửa sổ đồ thị
  - **Lý do**: Chạy trên terminal/server không có GUI
- **Ảnh hưởng**: Không nghiêm trọng, đồ thị vẫn được lưu vào file PNG

### Dòng 75: `  plt.show()`
- **Ý nghĩa**: Dòng code gây ra cảnh báo
- **Giải thích**: Code cố gắng hiển thị đồ thị, nhưng không có GUI nên chỉ cảnh báo
- **Xử lý**: Code đã có `try-except` để bỏ qua lỗi này

---

## TÓM TẮT Ý NGHĨA CÁC CON SỐ QUAN TRỌNG

### Loss Values:
- **GD Loss ban đầu**: 0.214744 → Network chưa học
- **GD Loss cuối**: 0.006411 → Network đã học tốt (giảm 97%)
- **BFGS Loss cuối**: 0.003510 → Tốt hơn GD ~2 lần

### MSE Test:
- **GD MSE**: 0.006884 → Dự đoán khá chính xác
- **BFGS MSE**: 0.001914 → Dự đoán rất chính xác (tốt hơn GD ~3.6 lần)

### Iterations:
- **GD**: 1000 epochs → Cần nhiều lần lặp
- **BFGS**: 100 iterations → Hiệu quả hơn 10 lần

### Kết luận:
- **BFGS tốt hơn Gradient Descent** về mọi mặt: loss thấp hơn, MSE thấp hơn, ít iterations hơn

