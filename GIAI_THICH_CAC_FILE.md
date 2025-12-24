# 📚 GIẢI THÍCH CÁC FILE - TÁC DỤNG VÀ CÁCH DÙNG

## 🎯 FILE CHO THUYẾT TRÌNH

### 1. `SCRIPT_THUYET_TRINH.md` ⭐ QUAN TRỌNG NHẤT
**Tác dụng:** Script chi tiết để bạn đọc khi thuyết trình

**Nội dung:**
- Từng phần cần nói gì
- Câu nói cụ thể cho từng phần
- Hướng dẫn mở file nào, chỉ code ở đâu
- Câu trả lời cho câu hỏi thường gặp

**Cách dùng:**
- Đọc trước khi thuyết trình để nhớ nội dung
- In ra hoặc mở trên điện thoại để tham khảo khi thuyết trình
- Làm theo từng bước trong script

**Ví dụ:**
```
PHẦN 2: TÍNH GRADIENT
- Nói: "Em tính gradient bằng Chain Rule..."
- Làm: Mở file network/layers.py, chỉ vào hàm backward()
```

---

### 2. `CHECKLIST_THUYET_TRINH.md` ✅
**Tác dụng:** Checklist để chuẩn bị và kiểm tra khi thuyết trình

**Nội dung:**
- Checklist trước khi thuyết trình (test code, mở file, ...)
- Checklist trong khi thuyết trình (đã nói phần nào chưa)
- Lưu ý quan trọng
- Câu trả lời cần nhớ

**Cách dùng:**
- Đọc trước khi thuyết trình
- Đánh dấu ✓ các mục đã làm
- Đảm bảo không bỏ sót phần nào

**Ví dụ:**
```
- [ ] Test code chạy được
- [ ] Mở sẵn file network/layers.py
- [ ] Chuẩn bị câu trả lời cho câu hỏi
```

---

### 3. `slides_thuyet_trinh.tex` 📊
**Tác dụng:** Slides LaTeX để trình chiếu (nếu cần)

**Nội dung:**
- 13 slides với công thức, code, kết quả
- Có thể compile thành PDF để trình chiếu

**Cách dùng:**
- Upload lên Overleaf.com → Compile → Download PDF
- Hoặc compile local: `pdflatex slides_thuyet_trinh.tex`
- Trình chiếu PDF khi thuyết trình (nếu cần)

**Lưu ý:** 
- File này là TÙY CHỌN - không bắt buộc
- Có thể thuyết trình không cần slides, chỉ cần mở code

---

## 📝 FILE CHO BÁO CÁO

### 4. `hw/bao_cao.tex` 📄
**Tác dụng:** Báo cáo LaTeX chuyên nghiệp để nộp thầy

**Nội dung:**
- Báo cáo đầy đủ theo 5 yêu cầu
- Công thức toán học
- Code được format đẹp
- So sánh GD vs BFGS
- Ứng dụng

**Cách dùng:**
- Upload lên Overleaf.com
- Compile thành PDF
- Nộp PDF cho thầy

**Lưu ý:** File này trong thư mục `hw/`, có thể đã có sẵn

---

## 💻 FILE CODE - CẦN MỞ KHI THUYẾT TRÌNH

### 5. `network/layers.py` 🔴 QUAN TRỌNG
**Tác dụng:** File chứa code tính gradient trong DenseLayer

**Phần cần chỉ:**
- Hàm `backward()` của class `DenseLayer` (dòng 31-60)
- Đây là nơi tính gradient bằng Chain Rule

**Khi thuyết trình:**
- Mở file này
- Chỉ vào dòng code tính `grad_W = np.outer(grad_out, self.x)`
- Nói: "Đây là gradient được tính bằng công thức toán học"

---

### 6. `network/loss.py` 🔴 QUAN TRỌNG
**Tác dụng:** File chứa code tính gradient của Loss

**Phần cần chỉ:**
- Hàm `backward()` của class `MSELoss` (dòng 27-37)
- Đây là nơi tính gradient của loss theo output

**Khi thuyết trình:**
- Mở file này
- Chỉ vào dòng `return self.y_pred - self.y_true`
- Nói: "Gradient của loss = y_pred - y_true, theo công thức toán học"

---

### 7. `network/network.py` 🔴 QUAN TRỌNG
**Tác dụng:** File chứa class NeuralNetwork - thiết kế adaptive

**Phần cần chỉ:**
- Class `NeuralNetwork` (dòng 7-95)
- Hàm `forward()` và `backward()` dùng vòng lặp qua danh sách layer

**Khi thuyết trình:**
- Mở file này
- Chỉ vào vòng lặp `for layer in self.layers:`
- Nói: "Thiết kế này cho phép thêm/bớt layer mà không cần sửa code"

---

### 8. `network/optimizers.py` 🟡 QUAN TRỌNG
**Tác dụng:** File chứa GradientDescent và BFGSOptimizer

**Phần cần chỉ:**
- Class `BFGSOptimizer` (dòng 43-125)
- Hàm `gradient()` trong BFGS - chứng minh gradient vẫn tự tính

**Khi thuyết trình:**
- Mở file này
- Chỉ vào hàm `gradient()` trong BFGS
- Nói: "Trong BFGS, gradient vẫn được tính bằng Backpropagation tự implement"

---

## 🚀 FILE DEMO - CẦN CHẠY KHI THUYẾT TRÌNH

### 9. `demos/main.py` 🔴 QUAN TRỌNG NHẤT
**Tác dụng:** Demo chính - chạy để chứng minh code hoạt động

**Nội dung:**
- Function Approximation: sin(x)
- So sánh Gradient Descent vs BFGS
- In kết quả và vẽ đồ thị

**Cách dùng:**
```bash
cd demos
python main.py
```

**Khi thuyết trình:**
- Chạy lệnh này để chứng minh code chạy được
- Chỉ vào kết quả: Loss giảm dần → Gradient đúng
- So sánh GD vs BFGS

---

### 10. `test/test_backprop.py` 🟡 QUAN TRỌNG
**Tác dụng:** Test chứng minh gradient được tính đúng

**Nội dung:**
- Test forward pass
- Test backward pass
- Chứng minh gradient được tính
- Chứng minh loss giảm dần

**Cách dùng:**
```bash
cd test
python test_backprop.py
```

**Khi thuyết trình:**
- Chạy lệnh này để chứng minh gradient đúng
- Nói: "Test này chứng minh gradient được tính bằng Backpropagation tự implement"

---

### 11. `test/test_adaptive.py` 🟡 QUAN TRỌNG
**Tác dụng:** Test chứng minh thiết kế adaptive

**Nội dung:**
- Test 3 network khác nhau
- Tất cả dùng cùng một hàm train
- Chứng minh thêm/bớt layer không cần viết lại code

**Cách dùng:**
```bash
cd test
python test_adaptive.py
```

**Khi thuyết trình:**
- Chạy lệnh này để chứng minh thiết kế adaptive
- Nói: "3 network khác nhau đều train được với cùng một hàm"

---

## 📖 FILE TÀI LIỆU

### 12. `hw/GIAI_THICH_KET_QUA.md` 📚
**Tác dụng:** Giải thích chi tiết kết quả khi chạy `demos/main.py`

**Nội dung:**
- Giải thích từng dòng output
- Ý nghĩa của các con số
- So sánh GD vs BFGS

**Cách dùng:**
- Đọc để hiểu kết quả
- Tham khảo khi thuyết trình nếu cần giải thích kết quả

---

### 13. `hw/GIAI_THICH_MAIN.md` 📚
**Tác dụng:** Giải thích code trong `demos/main.py`

**Nội dung:**
- Giải thích từng phần code
- Ý nghĩa của các biến
- Cách hoạt động

**Cách dùng:**
- Đọc để hiểu code
- Tham khảo khi cần giải thích code

---

### 14. `README.md` 📚
**Tác dụng:** Hướng dẫn tổng quan về project

**Nội dung:**
- Mô tả project
- Cấu trúc thư mục
- Cách chạy
- Tính năng

**Cách dùng:**
- Đọc để hiểu tổng quan
- Tham khảo khi cần giải thích cấu trúc project

---

## 🎯 TÓM TẮT - FILE NÀO DÙNG KHI NÀO?

### Khi CHUẨN BỊ thuyết trình:
1. ✅ Đọc `SCRIPT_THUYET_TRINH.md` - Nhớ nội dung cần nói
2. ✅ Đọc `CHECKLIST_THUYET_TRINH.md` - Kiểm tra đã chuẩn bị đủ chưa
3. ✅ Test code: `demos/main.py`, `test/test_backprop.py`, `test/test_adaptive.py`

### Khi THUYẾT TRÌNH:
1. 🔴 Mở `network/layers.py` - Chỉ vào hàm `backward()` (tính gradient)
2. 🔴 Mở `network/loss.py` - Chỉ vào hàm `backward()` (gradient của loss)
3. 🔴 Mở `network/network.py` - Chỉ vào class NeuralNetwork (thiết kế adaptive)
4. 🔴 Chạy `demos/main.py` - Chứng minh code chạy được
5. 🟡 Chạy `test/test_backprop.py` - Chứng minh gradient đúng
6. 🟡 Chạy `test/test_adaptive.py` - Chứng minh adaptive

### Khi NỘP BÁO CÁO:
1. 📄 Compile `hw/bao_cao.tex` → PDF → Nộp thầy

---

## ❓ CÂU HỎI THƯỜNG GẶP

### Q: File nào quan trọng nhất?
**A:** 
- `SCRIPT_THUYET_TRINH.md` - Để biết nói gì
- `network/layers.py` - Để chỉ code tính gradient
- `demos/main.py` - Để chạy demo

### Q: Có cần slides không?
**A:** Không bắt buộc. Có thể thuyết trình chỉ bằng cách mở code và chạy demo.

### Q: File nào cần mở khi thuyết trình?
**A:** 
- `network/layers.py` (QUAN TRỌNG)
- `network/loss.py` (QUAN TRỌNG)
- `network/network.py` (QUAN TRỌNG)
- Terminal để chạy `demos/main.py`

### Q: File nào chỉ để đọc tham khảo?
**A:**
- `hw/GIAI_THICH_KET_QUA.md`
- `hw/GIAI_THICH_MAIN.md`
- `README.md`

---

## 🚀 HƯỚNG DẪN NHANH

### Bước 1: Chuẩn bị (trước khi thuyết trình)
```bash
# 1. Đọc script
cat SCRIPT_THUYET_TRINH.md

# 2. Đọc checklist
cat CHECKLIST_THUYET_TRINH.md

# 3. Test code
cd demos && python main.py
cd ../test && python test_backprop.py && python test_adaptive.py
```

### Bước 2: Thuyết trình
1. Mở `network/layers.py` → Chỉ vào `backward()`
2. Mở `network/loss.py` → Chỉ vào `backward()`
3. Mở `network/network.py` → Chỉ vào class NeuralNetwork
4. Chạy `python demos/main.py`
5. Chạy `python test/test_backprop.py`
6. Chạy `python test/test_adaptive.py`

### Bước 3: Nộp báo cáo
- Upload `hw/bao_cao.tex` lên Overleaf
- Compile → Download PDF → Nộp

---

**Tóm lại:**
- **Script** = Biết nói gì
- **Checklist** = Không quên gì
- **Code files** = Chỉ vào khi thuyết trình
- **Demo files** = Chạy để chứng minh
- **Báo cáo** = Nộp thầy

