# GIẢI THÍCH CHI TIẾT FILE `demos/main.py` (Dòng 1-78)

## PHẦN 1: IMPORT VÀ SETUP (Dòng 1-13)

### Dòng 1-4: Docstring
```python
"""
Demo Neural Network với giao diện terminal đẹp
Sử dụng box drawing và màu sắc để hiển thị rõ ràng
"""
```
- **Mục đích**: Mô tả ngắn gọn về file này
- **Nội dung**: File này tạo demo Neural Network với giao diện terminal đẹp, sử dụng ký tự box drawing (╔╗║═) và màu sắc ANSI

### Dòng 5: `import numpy as np`
- **Mục đích**: Import thư viện NumPy để tính toán số học
- **Sử dụng**: Tạo mảng, tính toán ma trận, tạo dữ liệu sin(x)

### Dòng 6: `import matplotlib.pyplot as plt`
- **Mục đích**: Import matplotlib để vẽ đồ thị
- **Sử dụng**: Vẽ đồ thị so sánh sin(x) thật vs network dự đoán

### Dòng 7: `import sys`
- **Mục đích**: Import module hệ thống
- **Sử dụng**: Dùng `sys.path.insert()` để thêm đường dẫn import

### Dòng 8: `import os`
- **Mục đích**: Import module hệ điều hành
- **Sử dụng**: Dùng `os.path.join()` và `os.path.dirname()` để xây dựng đường dẫn

### Dòng 9: `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))`
- **Mục đích**: Thêm thư mục `network/` vào Python path để import các module
- **Giải thích chi tiết**:
  - `__file__`: Đường dẫn file hiện tại (`demos/main.py`)
  - `os.path.dirname(__file__)`: Lấy thư mục chứa file (`demos/`)
  - `os.path.join(..., '..', 'network')`: Đi lên 1 cấp (`final/`) rồi vào `network/`
  - `sys.path.insert(0, ...)`: Thêm vào đầu danh sách đường dẫn (ưu tiên cao nhất)
- **Kết quả**: Có thể import `from layers import ...` thay vì `from network.layers import ...`

### Dòng 10: `from layers import DenseLayer, Tanh`
- **Mục đích**: Import lớp DenseLayer (fully connected) và hàm activation Tanh
- **Sử dụng**: Xây dựng network: `DenseLayer(1, 10)` và `Tanh()`

### Dòng 11: `from network import NeuralNetwork`
- **Mục đích**: Import class NeuralNetwork để quản lý các layers
- **Sử dụng**: Tạo network: `NeuralNetwork([...])`

### Dòng 12: `from loss import MSELoss`
- **Mục đích**: Import hàm loss Mean Squared Error
- **Sử dụng**: Tính loss giữa output network và giá trị thật

### Dòng 13: `from optimizers import GradientDescent, BFGSOptimizer`
- **Mục đích**: Import 2 optimizer: Gradient Descent và BFGS
- **Sử dụng**: So sánh hiệu quả của 2 thuật toán tối ưu

---

## PHẦN 2: CLASS COLORS - MÀU SẮC TERMINAL (Dòng 15-25)

### Dòng 15: `# Màu sắc cho terminal (ANSI codes)`
- **Mục đích**: Comment giải thích
- **ANSI codes**: Mã escape để đổi màu text trong terminal

### Dòng 16: `class Colors:`
- **Mục đích**: Định nghĩa class chứa các mã màu ANSI
- **Lý do**: Tập trung tất cả mã màu vào 1 chỗ, dễ quản lý

### Dòng 17: `HEADER = '\033[95m'`
- **Mục đích**: Màu hồng/tím nhạt cho header
- **Giải thích**: `\033[95m` là ANSI escape code
- **Sử dụng**: In tiêu đề chính của demo

### Dòng 18: `BLUE = '\033[94m'`
- **Mục đích**: Màu xanh dương
- **Sử dụng**: In label trong `print_info()`

### Dòng 19: `CYAN = '\033[96m'`
- **Mục đích**: Màu xanh lơ
- **Sử dụng**: In khung section (`print_section()`)

### Dòng 20: `GREEN = '\033[92m'`
- **Mục đích**: Màu xanh lá
- **Sử dụng**: In giá trị trong `print_info()`

### Dòng 21: `YELLOW = '\033[93m'`
- **Mục đích**: Màu vàng
- **Sử dụng**: In giá trị loss trong progress bar

### Dòng 22: `RED = '\033[91m'`
- **Mục đích**: Màu đỏ
- **Sử dụng**: (Có thể dùng cho cảnh báo/error)

### Dòng 23: `END = '\033[0m'`
- **Mục đích**: Reset màu về mặc định
- **Quan trọng**: PHẢI dùng sau mỗi đoạn text có màu, nếu không màu sẽ áp dụng cho toàn bộ text sau đó

### Dòng 24: `BOLD = '\033[1m'`
- **Mục đích**: In đậm
- **Sử dụng**: Làm nổi bật tiêu đề

### Dòng 25: `UNDERLINE = '\033[4m'`
- **Mục đích**: Gạch chân
- **Sử dụng**: (Có thể dùng cho nhấn mạnh)

---

## PHẦN 3: HÀM IN KHUNG (Dòng 27-39)

### Dòng 27: `def print_box(title, content, width=70):`
- **Mục đích**: In khung đẹp với tiêu đề và nội dung
- **Tham số**:
  - `title`: Tiêu đề (string)
  - `content`: Danh sách các dòng nội dung (list)
  - `width`: Độ rộng khung (mặc định 70 ký tự)

### Dòng 28: `"""In khung đẹp với title và content"""`
- **Mục đích**: Docstring mô tả hàm

### Dòng 29: `print()`
- **Mục đích**: In dòng trống để tạo khoảng cách

### Dòng 30: `print("╔" + "═" * (width - 2) + "╗")`
- **Mục đích**: In cạnh trên của khung
- **Giải thích**:
  - `╔`: Góc trên bên trái (box drawing character)
  - `"═" * (width - 2)`: Lặp ký tự `═` (width-2) lần (trừ 2 vì có 2 góc)
  - `╗`: Góc trên bên phải
- **Ví dụ**: `width=70` → `╔════════════════════════════════════════════════════════════════╗`

### Dòng 31: `print("║" + f"{title:^{width-2}}" + "║")`
- **Mục đích**: In tiêu đề căn giữa trong khung
- **Giải thích**:
  - `║`: Cạnh dọc bên trái
  - `f"{title:^{width-2}}"`: Format string, `^` = căn giữa, `width-2` = độ rộng
  - `║`: Cạnh dọc bên phải

### Dòng 32: `print("╠" + "═" * (width - 2) + "╣")`
- **Mục đích**: In đường phân cách giữa tiêu đề và nội dung
- **Giải thích**:
  - `╠`: Nối dọc-trái
  - `╣`: Nối dọc-phải

### Dòng 33: `for line in content:`
- **Mục đích**: Duyệt từng dòng trong nội dung

### Dòng 34: `if isinstance(line, list):`
- **Mục đích**: Kiểm tra nếu dòng là list (nested content)
- **Lý do**: Cho phép nội dung lồng nhau (ví dụ: danh sách có sub-items)

### Dòng 35: `for subline in line:`
- **Mục đích**: Duyệt các dòng con nếu là list

### Dòng 36: `print("║" + f"{subline:<{width-2}}" + "║")`
- **Mục đích**: In dòng con căn trái
- **Giải thích**: `{subline:<{width-2}}` - `<` = căn trái

### Dòng 37: `else:`
- **Mục đích**: Nếu không phải list, xử lý như string thông thường

### Dòng 38: `print("║" + f"{line:<{width-2}}" + "║")`
- **Mục đích**: In dòng nội dung căn trái

### Dòng 39: `print("╚" + "═" * (width - 2) + "╝")`
- **Mục đích**: In cạnh dưới của khung
- **Giải thích**:
  - `╚`: Góc dưới bên trái
  - `╝`: Góc dưới bên phải

---

## PHẦN 4: HÀM IN SECTION (Dòng 41-46)

### Dòng 41: `def print_section(title, width=70):`
- **Mục đích**: In tiêu đề section với khung đơn giản hơn
- **Tham số**: Tương tự `print_box()` nhưng chỉ có title

### Dòng 42: `"""In tiêu đề section"""`
- **Mục đích**: Docstring

### Dòng 43: `print()`
- **Mục đích**: Dòng trống

### Dòng 44: `print(Colors.BOLD + Colors.CYAN + "┌" + "─" * (width - 2) + "┐" + Colors.END)`
- **Mục đích**: In cạnh trên của section (màu xanh lơ, in đậm)
- **Giải thích**:
  - `Colors.BOLD`: Bật in đậm
  - `Colors.CYAN`: Đổi màu xanh lơ
  - `┌`: Góc trên trái (box drawing, nhẹ hơn `╔`)
  - `─`: Đường ngang (nhẹ hơn `═`)
  - `┐`: Góc trên phải
  - `Colors.END`: Tắt màu

### Dòng 45: `print(Colors.BOLD + Colors.CYAN + "│" + f"{title:^{width-2}}" + "│" + Colors.END)`
- **Mục đích**: In tiêu đề căn giữa
- **Giải thích**: Tương tự dòng 44, nhưng có tiêu đề ở giữa

### Dòng 46: `print(Colors.BOLD + Colors.CYAN + "└" + "─" * (width - 2) + "┘" + Colors.END)`
- **Mục đích**: In cạnh dưới của section
- **Giải thích**: `└` và `┘` là góc dưới

---

## PHẦN 5: HÀM IN THÔNG TIN (Dòng 48-50)

### Dòng 48: `def print_info(label, value, width=70):`
- **Mục đích**: In thông tin dạng "Label: Value" với màu sắc
- **Tham số**:
  - `label`: Nhãn (ví dụ: "Số mẫu:")
  - `value`: Giá trị (ví dụ: "50")
  - `width`: Độ rộng (mặc định 70)

### Dòng 49: `"""In thông tin với format đẹp"""`
- **Mục đích**: Docstring

### Dòng 50: `print(Colors.BLUE + f"  {label:<25}" + Colors.END + Colors.GREEN + f"{value:>40}" + Colors.END)`
- **Mục đích**: In label màu xanh dương (căn trái) và value màu xanh lá (căn phải)
- **Giải thích chi tiết**:
  - `Colors.BLUE`: Bật màu xanh dương
  - `f"  {label:<25}"`: Label căn trái, độ rộng 25 ký tự, có 2 space đầu
  - `Colors.END`: Tắt màu xanh dương
  - `Colors.GREEN`: Bật màu xanh lá
  - `f"{value:>40}"`: Value căn phải, độ rộng 40 ký tự
  - `Colors.END`: Tắt màu xanh lá
- **Ví dụ output**: `  Số mẫu:                                         50`

---

## PHẦN 6: HÀM PROGRESS BAR (Dòng 52-57)

### Dòng 52: `def print_progress_bar(epoch, total, loss, width=50):`
- **Mục đích**: In thanh tiến trình khi training
- **Tham số**:
  - `epoch`: Epoch hiện tại
  - `total`: Tổng số epoch
  - `loss`: Giá trị loss hiện tại
  - `width`: Độ rộng thanh (mặc định 50 ký tự)

### Dòng 53: `"""In progress bar đẹp"""`
- **Mục đích**: Docstring

### Dòng 54: `filled = int(width * epoch / total)`
- **Mục đích**: Tính số ký tự đã điền trong thanh
- **Giải thích**:
  - `epoch / total`: Tỷ lệ hoàn thành (0.0 → 1.0)
  - `width * ...`: Nhân với độ rộng để ra số ký tự
  - `int(...)`: Làm tròn xuống
- **Ví dụ**: `epoch=500, total=1000, width=50` → `filled = 25`

### Dòng 55: `bar = "█" * filled + "░" * (width - filled)`
- **Mục đích**: Tạo chuỗi thanh tiến trình
- **Giải thích**:
  - `"█" * filled`: Ký tự đầy (filled) lặp `filled` lần
  - `"░" * (width - filled)`: Ký tự rỗng lặp phần còn lại
- **Ví dụ**: `[████████████░░░░░░░░]` (50% hoàn thành)

### Dòng 56: `percent = epoch / total * 100`
- **Mục đích**: Tính phần trăm hoàn thành
- **Ví dụ**: `500/1000*100 = 50.0%`

### Dòng 57: `print(f"\r  [{bar}] {percent:5.1f}% | Epoch {epoch:4d} | Loss: {Colors.YELLOW}{loss:.6f}{Colors.END}", end="")`
- **Mục đích**: In progress bar với thông tin chi tiết
- **Giải thích chi tiết**:
  - `\r`: Carriage return - quay về đầu dòng (ghi đè dòng cũ)
  - `  `: 2 space đầu
  - `[{bar}]`: Thanh tiến trình
  - `{percent:5.1f}%`: Phần trăm, 5 ký tự, 1 chữ số thập phân
  - `| Epoch {epoch:4d} |`: Epoch hiện tại, 4 chữ số
  - `Loss: {Colors.YELLOW}{loss:.6f}{Colors.END}`: Loss màu vàng, 6 chữ số thập phân
  - `end=""`: Không xuống dòng (để `\r` hoạt động)
- **Ví dụ output**: `  [████████████░░░░░░░░]  50.0% | Epoch  500 | Loss: 0.012345`

---

## PHẦN 7: HÀM TẠO DỮ LIỆU (Dòng 59-64)

### Dòng 59: `def generate_data(n_samples=50):`
- **Mục đích**: Tạo dữ liệu training: y = sin(x) với nhiễu
- **Tham số**: `n_samples`: Số mẫu (mặc định 50)

### Dòng 60: `"""Tạo dữ liệu: y = sin(x) với nhiễu"""`
- **Mục đích**: Docstring

### Dòng 61: `np.random.seed(42)`
- **Mục đích**: Set seed cho random generator
- **Lý do**: Đảm bảo kết quả có thể tái tạo (reproducible)
- **Giải thích**: Mỗi lần chạy sẽ tạo cùng 1 bộ dữ liệu

### Dòng 62: `X = np.linspace(-np.pi, np.pi, n_samples)`
- **Mục đích**: Tạo mảng X từ -π đến π với `n_samples` điểm đều nhau
- **Giải thích**:
  - `np.linspace(start, stop, num)`: Tạo mảng từ start đến stop với num điểm
  - `-np.pi` đến `np.pi`: Khoảng [-3.14, 3.14]
  - Kết quả: `X = [-3.14, -2.95, ..., 2.95, 3.14]` (50 điểm)
- **Shape**: `(50,)` - 1D array

### Dòng 63: `y = np.sin(X) + 0.1 * np.random.randn(n_samples)`
- **Mục đích**: Tạo y = sin(x) + nhiễu ngẫu nhiên
- **Giải thích chi tiết**:
  - `np.sin(X)`: Tính sin của từng phần tử trong X → `[sin(-π), sin(-2.95), ...]`
  - `np.random.randn(n_samples)`: Tạo nhiễu Gaussian (mean=0, std=1)
  - `0.1 * ...`: Giảm độ lớn nhiễu xuống 0.1 (10% so với amplitude của sin)
  - `+`: Cộng nhiễu vào sin(x)
- **Kết quả**: y gần bằng sin(x) nhưng có nhiễu nhỏ

### Dòng 64: `return X.reshape(-1, 1), y.reshape(-1, 1)`
- **Mục đích**: Reshape từ 1D sang 2D (cột vector)
- **Giải thích**:
  - `X.reshape(-1, 1)`: Chuyển từ `(50,)` → `(50, 1)`
  - `-1`: Tự động tính số hàng (50)
  - `1`: 1 cột
  - **Lý do**: Neural network cần input dạng `(n_samples, n_features)`
- **Kết quả**: 
  - `X.shape = (50, 1)`
  - `y.shape = (50, 1)`

---

## PHẦN 8: HÀM MAIN - PHẦN ĐẦU (Dòng 66-78)

### Dòng 66: `def main():`
- **Mục đích**: Hàm chính chạy toàn bộ demo
- **Lưu ý**: Tất cả logic chính nằm trong hàm này

### Dòng 67: `# Clear screen`
- **Mục đích**: Comment giải thích

### Dòng 68: `print("\033[2J\033[H", end="")`
- **Mục đích**: Xóa màn hình terminal
- **Giải thích**:
  - `\033[2J`: ANSI escape code - xóa toàn bộ màn hình
  - `\033[H`: Di chuyển con trỏ về góc trên trái
  - `end=""`: Không xuống dòng
- **Kết quả**: Terminal sạch sẽ trước khi in nội dung mới

### Dòng 69: (Trống)
- **Mục đích**: Dòng trống để dễ đọc code

### Dòng 70: `# Header`
- **Mục đích**: Comment đánh dấu phần header

### Dòng 71: `print(Colors.BOLD + Colors.HEADER + "=" * 70 + Colors.END)`
- **Mục đích**: In dòng phân cách trên cùng (màu hồng, in đậm)
- **Giải thích**:
  - `Colors.BOLD`: In đậm
  - `Colors.HEADER`: Màu hồng/tím
  - `"=" * 70`: 70 dấu `=`
  - `Colors.END`: Tắt màu
- **Output**: `======================================================================` (màu hồng, đậm)

### Dòng 72: `print(Colors.BOLD + Colors.HEADER + " " * 15 + "NEURAL NETWORK DEMO" + " " * 15 + Colors.END)`
- **Mục đích**: In tiêu đề chính căn giữa
- **Giải thích**:
  - `" " * 15`: 15 space bên trái
  - `"NEURAL NETWORK DEMO"`: Tiêu đề
  - `" " * 15`: 15 space bên phải
  - Tổng: 15 + 19 + 15 = 49 ký tự (trong 70, tự căn giữa)
- **Output**: `               NEURAL NETWORK DEMO               ` (màu hồng, đậm)

### Dòng 73: `print(Colors.BOLD + Colors.HEADER + " " * 10 + "Function Approximation: sin(x)" + " " * 10 + Colors.END)`
- **Mục đích**: In mô tả phụ căn giữa
- **Giải thích**: Tương tự dòng 72, nhưng với text khác
- **Output**: `          Function Approximation: sin(x)          ` (màu hồng, đậm)

### Dòng 74: `print(Colors.BOLD + Colors.HEADER + "=" * 70 + Colors.END)`
- **Mục đích**: In dòng phân cách dưới cùng (giống dòng 71)
- **Output**: `======================================================================` (màu hồng, đậm)

### Dòng 75: (Trống)
- **Mục đích**: Dòng trống

### Dòng 76: `# Section 1: Tạo dữ liệu`
- **Mục đích**: Comment đánh dấu section 1

### Dòng 77: `print_section("1. TẠO DỮ LIỆU TRAINING")`
- **Mục đích**: In tiêu đề section 1
- **Giải thích**: Gọi hàm `print_section()` đã định nghĩa ở dòng 41
- **Output**: 
  ```
  ┌────────────────────────────────────────────────────────────────────┐
  │                      1. TẠO DỮ LIỆU TRAINING                       │
  └────────────────────────────────────────────────────────────────────┘
  ```
  (màu xanh lơ, đậm)

### Dòng 78: `X, y = generate_data(n_samples=50)`
- **Mục đích**: Tạo dữ liệu training
- **Giải thích**:
  - Gọi hàm `generate_data()` với 50 mẫu
  - Nhận về `X` (input) và `y` (target)
  - `X.shape = (50, 1)` - 50 điểm x từ -π đến π
  - `y.shape = (50, 1)` - 50 giá trị sin(x) + nhiễu

---

## TÓM TẮT

**Dòng 1-13**: Import các thư viện và module cần thiết
**Dòng 15-25**: Định nghĩa class Colors chứa mã màu ANSI
**Dòng 27-39**: Hàm `print_box()` - in khung đẹp với box drawing
**Dòng 41-46**: Hàm `print_section()` - in tiêu đề section
**Dòng 48-50**: Hàm `print_info()` - in thông tin label:value
**Dòng 52-57**: Hàm `print_progress_bar()` - in thanh tiến trình training
**Dòng 59-64**: Hàm `generate_data()` - tạo dữ liệu sin(x) với nhiễu
**Dòng 66-78**: Hàm `main()` - phần đầu: clear screen, in header, tạo dữ liệu

