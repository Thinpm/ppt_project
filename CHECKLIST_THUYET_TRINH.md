# ✅ CHECKLIST THUYẾT TRÌNH CODE

## 📋 TRƯỚC KHI THUYẾT TRÌNH

### Chuẩn bị môi trường
- [ ] Test code chạy được trên máy thuyết trình
- [ ] Chuẩn bị terminal sẵn sàng (cd vào thư mục project)
- [ ] Mở sẵn các file code quan trọng:
  - [ ] `network/layers.py` (DenseLayer.backward)
  - [ ] `network/loss.py` (MSELoss.backward)
  - [ ] `network/network.py` (NeuralNetwork class)
  - [ ] `network/optimizers.py` (BFGSOptimizer)
- [ ] Test các lệnh chạy:
  - [ ] `python demos/main.py`
  - [ ] `python demos/test_backprop.py`
  - [ ] `python demos/test_adaptive.py`

### Chuẩn bị nội dung
- [ ] Đọc lại script thuyết trình
- [ ] Nhớ các điểm quan trọng cần nhấn mạnh
- [ ] Chuẩn bị câu trả lời cho câu hỏi thường gặp
- [ ] Test thời gian thuyết trình (10-15 phút)

### Chuẩn bị slides (nếu có)
- [ ] Compile slides LaTeX thành công
- [ ] Test trình chiếu slides
- [ ] Chuẩn bị backup (PDF)

---

## 🎯 TRONG KHI THUYẾT TRÌNH

### Phần 1: Giới thiệu
- [ ] Giới thiệu 3 điểm chính
- [ ] Giới thiệu cấu trúc project

### Phần 2: Tính gradient (QUAN TRỌNG NHẤT!)
- [ ] Phát biểu bài toán tối ưu
- [ ] Giải thích công thức Backpropagation
- [ ] **Mở file `network/layers.py`** - Chỉ vào `backward()`
- [ ] **Mở file `network/loss.py`** - Chỉ vào `backward()`
- [ ] Nhấn mạnh "tự implement", không dùng automatic differentiation

### Phần 3: Code chạy được
- [ ] **Chạy `python demos/main.py`** - Chứng minh code hoạt động
- [ ] Giải thích kết quả (loss giảm, network học được)
- [ ] So sánh GD vs BFGS
- [ ] **Chạy `python demos/test_backprop.py`** - Chứng minh gradient đúng

### Phần 4: Thiết kế adaptive
- [ ] **Mở file `network/network.py`** - Chỉ vào class NeuralNetwork
- [ ] Giải thích OOP + danh sách layer
- [ ] **Chạy `python demos/test_adaptive.py`** - Chứng minh adaptive
- [ ] Giải thích ví dụ thêm layer

### Phần 5: So sánh optimizer
- [ ] Giải thích GD vs BFGS
- [ ] **Mở file `network/optimizers.py`** - Chỉ vào BFGSOptimizer
- [ ] Nhấn mạnh gradient vẫn tự tính

### Phần 6: Ứng dụng
- [ ] Liệt kê 3 ứng dụng
- [ ] Nói về kết quả

### Phần 7: Kết luận
- [ ] Tóm tắt 3 điểm chính
- [ ] Cảm ơn

---

## ⚠️ LƯU Ý QUAN TRỌNG

### ✅ PHẢI LÀM:
1. **Chỉ code trực tiếp** - Mở file và chỉ vào dòng code cụ thể
2. **Nhấn mạnh "tự implement"** - Nói rõ không dùng automatic differentiation
3. **Chạy code live** - Chứng minh code thực sự chạy được
4. **Giải thích công thức** - Nói rõ gradient được tính như thế nào
5. **Tự tin** - Bạn đã làm đúng, code chạy được

### ❌ KHÔNG ĐƯỢC:
1. ❌ Chỉ nói suông, không mở code
2. ❌ Nói "dùng thư viện" - Phải nhấn mạnh "tự implement"
3. ❌ Bỏ qua phần gradient - Đây là phần quan trọng nhất
4. ❌ Không chạy code - Phải chứng minh code chạy được
5. ❌ Nói quá nhanh - Nói chậm, rõ ràng, dễ hiểu

---

## 💬 CÂU TRẢ LỜI CẦN NHỚ

### Q: "Gradient được tính như thế nào?"
**A:** "Em tính gradient bằng Chain Rule. Với mỗi layer:
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

## 📝 GHI CHÚ THÊM

- Thời gian: 10-15 phút
- Tập trung vào: Gradient, Code chạy được, Adaptive
- Tự tin: Bạn đã làm đúng, code chạy được
- Chỉ code cụ thể: Đừng nói chung chung

---

**CHÚC BẠN THUYẾT TRÌNH THÀNH CÔNG! 🎉**

