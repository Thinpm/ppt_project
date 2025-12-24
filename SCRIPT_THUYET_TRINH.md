# SCRIPT THUYẾT TRÌNH CODE - NEURAL NETWORK

## 🎯 MỤC TIÊU THUYẾT TRÌNH

Thầy muốn thấy 3 điều:
1. ✅ **Tính được gradient** - Biết rõ loss phụ thuộc biến nào, tính gradient bằng chain rule
2. ✅ **Code chạy được** - Không nói suông, có kết quả thực tế
3. ✅ **Thiết kế adaptive** - Thêm/bớt layer không cần viết lại code

---

## 📋 CẤU TRÚC THUYẾT TRÌNH (10-15 phút)

### PHẦN 1: GIỚI THIỆU (1 phút)

**Nói:**
> "Em xin chào thầy. Hôm nay em sẽ trình bày về Neural Network từ đầu, tập trung vào 3 điểm chính:
> - Tính gradient bằng Backpropagation tự implement
> - Code chạy được với kết quả thực tế
> - Thiết kế adaptive, dễ mở rộng"

**Làm:**
- Mở terminal, cd vào thư mục project
- Giới thiệu cấu trúc project

---

### PHẦN 2: TÍNH GRADIENT - BACKPROPAGATION (4-5 phút)

**Đây là phần QUAN TRỌNG NHẤT!**

#### 2.1. Phát biểu bài toán tối ưu (1 phút)

**Nói:**
> "Đầu tiên, em phát biểu bài toán dưới dạng tối ưu.
> 
> Biến tối ưu là tất cả trọng số và bias: Θ = {W^(1), b^(1), ..., W^(L), b^(L)}
> 
> Hàm loss: L(Θ) = 0.5 × Σ(y_pred - y_true)²
> 
> Bài toán: Tìm Θ để L(Θ) đạt cực tiểu."

**Làm:**
- Chỉ vào công thức trong báo cáo/slide

#### 2.2. Tính gradient bằng Chain Rule (2-3 phút)

**Nói:**
> "Để tối ưu, em cần tính gradient. Em tính gradient bằng Chain Rule, không dùng automatic differentiation.
> 
> Gradient của loss theo output: δ^(L) = y_pred - y_true
> 
> Lan truyền ngược qua các layer:
> - Gradient của W: grad_W = δ @ a^T
> - Gradient của b: grad_b = δ
> - Gradient truyền về layer trước: grad_x = W^T @ δ"

**Làm:**
- Mở file `network/layers.py`
- Chỉ vào hàm `backward()` của `DenseLayer`

**Code cần chỉ:**
```python
def backward(self, grad_out, lr):
    # Gradient của W: grad_W = grad_out @ x^T (theo chain rule)
    grad_W = np.outer(grad_out, self.x)
    
    # Gradient của b: grad_b = grad_out (theo chain rule)
    grad_b = grad_out
    
    # Gradient truyền về layer trước: grad_x = W^T @ grad_out
    grad_x = self.W.T @ grad_out
    
    return grad_x
```

**Nói:**
> "Đây là công thức toán học, em tự implement, không dùng thư viện AI như PyTorch hay TensorFlow."

**Làm:**
- Mở file `network/loss.py`
- Chỉ vào hàm `backward()` của `MSELoss`

**Code cần chỉ:**
```python
def backward(self):
    # Đạo hàm của 0.5*(y_pred - y_true)^2 theo y_pred = y_pred - y_true
    return self.y_pred - self.y_true
```

**Nói:**
> "Gradient được tính hoàn toàn bằng công thức toán học, không dùng automatic differentiation."

---

### PHẦN 3: CODE CHẠY ĐƯỢC - DEMO (3-4 phút)

#### 3.1. Chạy demo chính (2 phút)

**Nói:**
> "Bây giờ em sẽ chạy code để chứng minh nó hoạt động."

**Làm:**
```bash
cd demos
python main.py
```

**Nói trong khi chạy:**
> "Code đang chạy. Em thấy:
> - Loss giảm dần từ ~0.1 xuống ~0.01
> - Network học được hàm sin(x)
> - Có so sánh giữa Gradient Descent và BFGS"

**Sau khi chạy xong:**
> "Kết quả:
> - Gradient Descent: Loss cuối = 0.006411 sau 1000 epochs
> - BFGS: Loss cuối = 0.003510 sau 100 iterations
> - BFGS hội tụ nhanh hơn và cho loss thấp hơn"

#### 3.2. Chứng minh gradient đúng (1-2 phút)

**Nói:**
> "Để chứng minh gradient được tính đúng, em chạy test backpropagation."

**Làm:**
```bash
python test_backprop.py
```

**Nói:**
> "Test này chứng minh:
> - Gradient được tính bằng Backpropagation tự implement
> - Loss giảm dần khi train (chứng minh gradient đúng)
> - Không dùng thư viện AI"

---

### PHẦN 4: THIẾT KẾ ADAPTIVE (2-3 phút)

**Nói:**
> "Yêu cầu thứ 3 là thiết kế adaptive. Em thiết kế theo hướng OOP + danh sách layer."

**Làm:**
- Mở file `network/network.py`
- Chỉ vào class `NeuralNetwork`

**Code cần chỉ:**
```python
class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
    
    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def backward(self, grad, lr):
        for layer in reversed(self.layers):
            grad = layer.backward(grad, lr)
        return grad
```

**Nói:**
> "Thiết kế này cho phép thêm/bớt layer mà không cần sửa code training."

**Làm:**
- Mở file `demos/test_adaptive.py`
- Chỉ vào ví dụ

**Nói:**
> "Ví dụ: Network đơn giản 1->5->1 và network phức tạp 1->10->5->1 đều dùng cùng một hàm train.
> Chỉ cần thay đổi khởi tạo network, code training tự động thích nghi."

**Làm:**
```bash
python test_adaptive.py
```

**Nói:**
> "Test này chứng minh 3 network khác nhau đều train được với cùng một hàm, không cần viết lại code."

---

### PHẦN 5: SO SÁNH OPTIMIZER (1-2 phút)

**Nói:**
> "Em đã so sánh Gradient Descent và BFGS. Cả hai đều dùng gradient tính bằng Backpropagation tự implement."

**Làm:**
- Mở file `network/optimizers.py`
- Chỉ vào `BFGSOptimizer`

**Nói:**
> "QUAN TRỌNG: Trong BFGS, gradient vẫn được tính bằng Backpropagation tự viết, không dùng automatic differentiation của scipy.
> scipy.optimize.minimize chỉ là wrapper để tối ưu, gradient được truyền vào qua tham số jac=gradient."

**Chỉ code:**
```python
def gradient(params):
    # Forward pass
    y_pred = network.forward(X[i])
    loss_fn.forward(y_pred, y[i])
    
    # Backward pass - tính gradient bằng chain rule (tự implement)
    grad_loss = loss_fn.backward()
    network.backward(grad_loss, 0)  # Backpropagation tự viết!
    
    return grad_flat
```

---

### PHẦN 6: ỨNG DỤNG (1 phút)

**Nói:**
> "Em đã làm 3 ứng dụng:
> 1. Function Approximation: sin(x)
> 2. XOR Problem
> 3. Classification: Circle
> 
> Tất cả đều chạy được và cho kết quả tốt."

---

### PHẦN 7: KẾT LUẬN (1 phút)

**Nói:**
> "Tóm lại, em đã:
> 1. ✅ Tính gradient bằng Backpropagation tự implement, không dùng thư viện AI
> 2. ✅ Code chạy được, có kết quả và visualization
> 3. ✅ Thiết kế adaptive, thêm/bớt layer không cần viết lại code
> 
> Em xin cảm ơn thầy!"

---

## ⚠️ LƯU Ý QUAN TRỌNG KHI THUYẾT TRÌNH

### ✅ NÊN LÀM:
1. **Chỉ code trực tiếp** - Mở file và chỉ vào dòng code cụ thể
2. **Nhấn mạnh "tự implement"** - Nói rõ không dùng automatic differentiation
3. **Chạy code live** - Chứng minh code thực sự chạy được
4. **Giải thích công thức** - Nói rõ gradient được tính như thế nào
5. **So sánh kết quả** - Chỉ ra GD vs BFGS

### ❌ KHÔNG NÊN:
1. ❌ Chỉ nói suông, không mở code
2. ❌ Nói "dùng thư viện" - Phải nhấn mạnh "tự implement"
3. ❌ Bỏ qua phần gradient - Đây là phần quan trọng nhất
4. ❌ Không chạy code - Phải chứng minh code chạy được

---

## 🎯 CÂU TRẢ LỜI CHO CÁC CÂU HỎI THƯỜNG GẶP

### Q: "Gradient được tính như thế nào?"
**A:** "Em tính gradient bằng Chain Rule. Với mỗi layer, em tính:
- grad_W = δ @ a^T (gradient của trọng số)
- grad_b = δ (gradient của bias)
- grad_x = W^T @ δ (gradient truyền về layer trước)
Tất cả đều theo công thức toán học, em tự implement trong hàm backward() của DenseLayer."

### Q: "Có dùng automatic differentiation không?"
**A:** "Không ạ. Em tính gradient hoàn toàn bằng công thức toán học. Em không dùng PyTorch's autograd hay TensorFlow's gradient tape. Em tự viết công thức đạo hàm trong code."

### Q: "Làm sao chứng minh gradient đúng?"
**A:** "Em chứng minh bằng cách:
1. Loss giảm dần khi train (nếu gradient sai, loss sẽ không giảm)
2. Network học được pattern từ dữ liệu
3. Có test file test_backprop.py chứng minh gradient được tính"

### Q: "Thiết kế adaptive là gì?"
**A:** "Thiết kế adaptive nghĩa là khi thêm/bớt layer hoặc thay đổi số neuron, code training không cần viết lại. Em dùng OOP + danh sách layer, mỗi layer tự quản lý forward và backward. Có file test_adaptive.py chứng minh điều này."

### Q: "BFGS có dùng gradient tự tính không?"
**A:** "Có ạ. Trong BFGS, em vẫn tính gradient bằng Backpropagation tự implement. scipy.optimize.minimize chỉ là wrapper để tối ưu, gradient được truyền vào qua tham số jac=gradient. Em có thể chỉ code trong BFGSOptimizer để chứng minh."

---

## 📝 CHECKLIST TRƯỚC KHI THUYẾT TRÌNH

- [ ] Đã test code chạy được
- [ ] Đã chuẩn bị terminal sẵn sàng
- [ ] Đã mở sẵn các file code quan trọng (layers.py, loss.py, network.py)
- [ ] Đã chuẩn bị câu trả lời cho các câu hỏi thường gặp
- [ ] Đã nhớ các điểm quan trọng cần nhấn mạnh
- [ ] Đã test thời gian thuyết trình (10-15 phút)

---

## 🚀 LỆNH CẦN CHUẨN BỊ

```bash
# Terminal 1: Chạy demo chính
cd /home/thuypm/Desktop/ttu/pptinh/final/demos
python main.py

# Terminal 2: Test backprop
cd /home/thuypm/Desktop/ttu/pptinh/final/demos
python test_backprop.py

# Terminal 3: Test adaptive
cd /home/thuypm/Desktop/ttu/pptinh/final/demos
python test_adaptive.py
```

---

## 💡 TIPS THUYẾT TRÌNH

1. **Tự tin** - Bạn đã làm đúng, code chạy được
2. **Chỉ code cụ thể** - Đừng nói chung chung, chỉ vào dòng code
3. **Nhấn mạnh "tự implement"** - Đây là điểm mạnh của bạn
4. **Chạy code live** - Chứng minh code thực sự hoạt động
5. **Giải thích rõ ràng** - Nói chậm, rõ ràng, dễ hiểu

---

**CHÚC BẠN THUYẾT TRÌNH THÀNH CÔNG! 🎉**

