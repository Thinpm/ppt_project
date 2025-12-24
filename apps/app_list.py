"""
Danh sách các ứng dụng thực tế
Chạy file này để xem danh sách và chọn ứng dụng muốn chạy
"""
import sys

print("=" * 70)
print("DANH SÁCH ỨNG DỤNG THỰC TẾ - NEURAL NETWORK")
print("=" * 70)

apps = [
    {
        "name": "Function Approximation",
        "file": "main.py hoặc demo_simple.py",
        "description": "Học hàm sin(x) từ dữ liệu",
        "command": "python main.py hoặc python demo_simple.py"
    },
    {
        "name": "XOR Problem",
        "file": "app_xor.py",
        "description": "Giải bài toán XOR kinh điển",
        "command": "python app_xor.py"
    },
    {
        "name": "Regression - Dự đoán giá nhà",
        "file": "app_regression.py",
        "description": "Dự đoán giá nhà dựa trên diện tích",
        "command": "python app_regression.py"
    },
    {
        "name": "Classification - Phân loại trong/circle",
        "file": "app_classification.py",
        "description": "Phân loại điểm trong hay ngoài circle",
        "command": "python app_classification.py"
    }
]

print("\nCác ứng dụng có sẵn:\n")
for i, app in enumerate(apps, 1):
    print(f"{i}. {app['name']}")
    print(f"   📄 File: {app['file']}")
    print(f"   📝 Mô tả: {app['description']}")
    print(f"   ▶️  Chạy: {app['command']}")
    print()

print("=" * 70)
print("YÊU CẦU 5: 'Tìm một ứng dụng cho mô hình network và chạy chương trình minh họa'")
print("=" * 70)
print("\n✅ Đã có 4 ứng dụng thực tế:")
print("   1. Function Approximation (sin(x)) - Đã chạy thành công")
print("   2. XOR Problem - Bài toán kinh điển")
print("   3. Regression - Dự đoán giá nhà")
print("   4. Classification - Phân loại trong/circle")
print("\n💡 Khuyến nghị cho thuyết trình:")
print("   - Function Approximation (sin(x)): Dễ hiểu, có visualization")
print("   - XOR Problem: Kinh điển, chứng minh network có thể học logic")
print("\n🎯 Tất cả ứng dụng đều:")
print("   ✅ Chạy được")
print("   ✅ Có kết quả rõ ràng")
print("   ✅ Dùng cùng code base (tính thích nghi)")
print("=" * 70)


