# GIẢI THÍCH KẾT QUẢ CLASSIFICATION - PHÂN LOẠI TRONG/NGOÀI CIRCLE

## TỔNG QUAN

Hai hình này minh họa kết quả của bài toán **Classification** (Phân loại) - một trong những ứng dụng thực tế của Neural Network. Bài toán cụ thể là: **Phân loại điểm có nằm trong một circle (hình tròn) hay không**.

---

## HÌNH 1: "DỮ LIỆU THỰC TẾ" (Ground Truth)

### Mục đích:
Hình này hiển thị **dữ liệu training thực tế** - những gì network được học.

### Các thành phần:

1. **Điểm màu LAM (Blue/Purple) - "Trong circle"**
   - Đại diện cho các điểm có **nhãn = 1** (label = 1)
   - Điều kiện: Khoảng cách từ gốc tọa độ < 1
   - Công thức: `x² + y² < 1`
   - **PHẢI NẰM TRONG** đường tròn màu xanh lá (đường viền)
   - **Nếu điểm LAM nằm NGOÀI circle → DỰ ĐOÁN SAI!**

2. **Điểm màu ĐỎ - "Ngoài circle"**
   - Đại diện cho các điểm có **nhãn = 0** (label = 0)
   - Điều kiện: Khoảng cách từ gốc tọa độ ≥ 1
   - Công thức: `x² + y² ≥ 1`
   - **PHẢI NẰM NGOÀI** đường tròn màu xanh lá
   - **Nếu điểm ĐỎ nằm TRONG circle → DỰ ĐOÁN SAI!**

3. **Đường tròn màu xanh lá (dashed)**
   - Đường viền decision boundary thực tế
   - Tâm tại (0, 0), bán kính = 1
   - Đây là ranh giới phân loại "chuẩn" mà network cần học

### Đặc điểm:
- Có **100 điểm training** (n_samples=100)
- Một số điểm gần biên có thể bị nhầm lẫn (overlap)
- Đây là dữ liệu network được "nhìn thấy" khi training

---

## HÌNH 2: "DỰ ĐOÁN CỦA NETWORK" (Network Prediction)

### Mục đích:
Hình này hiển thị **khả năng dự đoán của network** sau khi đã được huấn luyện.

### Các thành phần:

1. **Điểm màu LAM (Blue/Purple) - "Dự đoán: Trong"**
   - Các điểm network dự đoán là "trong circle" (pred > 0.5)
   - **PHẢI NẰM TRONG** đường tròn màu xanh lá
   - **Nếu điểm LAM nằm NGOÀI circle → DỰ ĐOÁN SAI!**
   - Độ trong suốt cao hơn (alpha=0.3) vì có nhiều điểm hơn

2. **Điểm màu ĐỎ - "Dự đoán: Ngoài"**
   - Các điểm network dự đoán là "ngoài circle" (pred ≤ 0.5)
   - **PHẢI NẰM NGOÀI** đường tròn màu xanh lá
   - **Nếu điểm ĐỎ nằm TRONG circle → DỰ ĐOÁN SAI!**
   - Độ trong suốt cao hơn (alpha=0.3)

3. **Đường tròn màu xanh lá (dashed)**
   - Cùng đường viền như hình 1 (để so sánh)
   - Network đã học được ranh giới này rất tốt

### Đặc điểm:
- Có **1000 điểm test** (nhiều hơn training data)
   - Đây là dữ liệu mới, network chưa từng thấy
   - Mục đích: Kiểm tra khả năng tổng quát hóa (generalization)
- **Accuracy: 99.0%** - Độ chính xác rất cao!
- Phân loại rất sạch, ít điểm bị nhầm lẫn

---

## QUY TẮC MÀU SẮC VÀ ĐÁNH GIÁ ĐÚNG/SAI

### 🟦 MÀU LAM (Blue/Purple):
- **Ý nghĩa**: Điểm "Trong circle" (label = 1)
- **Vị trí đúng**: PHẢI nằm TRONG đường tròn (x² + y² < 1)
- **Nếu lệch**: Điểm LAM nằm NGOÀI circle → **DỰ ĐOÁN SAI!**

### 🔴 MÀU ĐỎ:
- **Ý nghĩa**: Điểm "Ngoài circle" (label = 0)
- **Vị trí đúng**: PHẢI nằm NGOÀI đường tròn (x² + y² ≥ 1)
- **Nếu lệch**: Điểm ĐỎ nằm TRONG circle → **DỰ ĐOÁN SAI!**

### 📊 Cách đánh giá độ chính xác:
- **Đúng**: LAM trong circle + ĐỎ ngoài circle
- **Sai**: LAM ngoài circle HOẶC ĐỎ trong circle
- **Accuracy = (Số điểm đúng) / (Tổng số điểm) × 100%**

---

## SO SÁNH HAI HÌNH

| Tiêu chí | Hình 1 (Dữ liệu thực tế) | Hình 2 (Dự đoán Network) |
|----------|-------------------------|--------------------------|
| **Số điểm** | 100 điểm (training) | 1000 điểm (test) |
| **Mục đích** | Hiển thị dữ liệu network học | Hiển thị khả năng dự đoán |
| **Độ chính xác** | 100% (ground truth) | 99.0% (network prediction) |
| **Mật độ điểm** | Thưa hơn | Dày đặc hơn |
| **Màu sắc** | Đậm hơn (alpha=0.6) | Nhạt hơn (alpha=0.3) |

---

## KẾT LUẬN VÀ Ý NGHĨA

### ✅ Network đã học được gì?

1. **Học được pattern (mẫu hình)**
   - Network nhận ra rằng: điểm gần gốc tọa độ (0,0) → "trong circle"
   - Điểm xa gốc tọa độ → "ngoài circle"
   - Mặc dù không được dạy công thức `x² + y² < 1`, network tự học được!

2. **Tổng quát hóa tốt (Generalization)**
   - Accuracy 99.0% trên 1000 điểm test
   - Network không chỉ "học thuộc" 100 điểm training
   - Có thể dự đoán đúng cho điểm mới chưa từng thấy

3. **Decision Boundary rõ ràng**
   - Network tạo ra một ranh giới phân loại gần như trùng với đường tròn thực tế
   - Điều này chứng minh network đã "hiểu" bài toán

### ✅ Đáp ứng yêu cầu của thầy:

- **Yêu cầu 5**: "Tìm một ứng dụng cho mô hình network và chạy chương trình minh họa"
  - ✅ Đã có ứng dụng Classification thực tế
  - ✅ Có visualization rõ ràng
  - ✅ Kết quả tốt (99% accuracy)

### ✅ Chứng minh code hoạt động:

- Network được train từ đầu (không dùng thư viện AI)
- Backpropagation tự implement
- Loss giảm dần → Gradient được tính đúng
- Kết quả tốt → Code chạy được, không phải "nói suông"

---

## CẤU TRÚC NETWORK ĐÃ DÙNG

```
Input: (x, y) - tọa độ điểm
  ↓
DenseLayer(2 → 6)  - 2 input, 6 hidden neurons
  ↓
Tanh()              - Activation function
  ↓
DenseLayer(6 → 1)  - 6 hidden, 1 output
  ↓
Sigmoid()           - Output trong [0, 1]
  ↓
Output: 0 (ngoài) hoặc 1 (trong)
```

**Training:**
- Epochs: 1000
- Learning rate: 0.1
- Loss function: MSE (Mean Squared Error)
- Optimizer: Gradient Descent

---

## CÁCH CHẠY LẠI

```bash
cd apps
python app_classification.py
```

Kết quả sẽ được lưu vào file `app_classification.png` trong thư mục hiện tại.

---

## TẠI SAO BÀI TOÁN NÀY QUAN TRỌNG?

1. **Bài toán không tuyến tính (Non-linear)**
   - Không thể phân loại bằng đường thẳng đơn giản
   - Cần network với hidden layer để học được pattern phức tạp

2. **Ứng dụng thực tế**
   - Phân loại vùng (ví dụ: vùng an toàn/nguy hiểm)
   - Nhận dạng hình dạng
   - Computer vision cơ bản

3. **Chứng minh sức mạnh của Neural Network**
   - Từ dữ liệu training → Học được quy tắc phức tạp
   - Tổng quát hóa tốt trên dữ liệu mới

---

**Tóm lại:** Hai hình này chứng minh network đã học được bài toán phân loại circle một cách xuất sắc, với độ chính xác 99%, và có khả năng tổng quát hóa tốt trên dữ liệu mới.

