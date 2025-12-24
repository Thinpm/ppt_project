"""
Menu chính với giao diện đẹp
Cho phép chọn các ứng dụng khác nhau
"""
import sys
import os

# Thêm path để import từ network/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))

# Màu sắc cho terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Xóa màn hình"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_header():
    """In header đẹp"""
    print(Colors.BOLD + Colors.HEADER + "╔" + "═" * 68 + "╗" + Colors.END)
    print(Colors.BOLD + Colors.HEADER + "║" + " " * 15 + "NEURAL NETWORK PROJECT" + " " * 30 + "║" + Colors.END)
    print(Colors.BOLD + Colors.HEADER + "║" + " " * 20 + "Computational Methods" + " " * 25 + "║" + Colors.END)
    print(Colors.BOLD + Colors.HEADER + "╚" + "═" * 68 + "╝" + Colors.END)
    print()

def print_menu():
    """In menu chính"""
    print(Colors.BOLD + Colors.CYAN + "┌" + "─" * 66 + "┐" + Colors.END)
    print(Colors.BOLD + Colors.CYAN + "│" + " " * 20 + "MENU CHÍNH" + " " * 35 + "│" + Colors.END)
    print(Colors.BOLD + Colors.CYAN + "├" + "─" * 66 + "┤" + Colors.END)
    
    menu_items = [
        ("1", "Function Approximation", "Học hàm sin(x) - Demo chính"),
        ("2", "XOR Problem", "Giải bài toán XOR kinh điển"),
        ("3", "Regression", "Dự đoán giá nhà dựa trên diện tích"),
        ("4", "Classification", "Phân loại điểm trong/circle"),
        ("5", "Test Tính Thích Nghi", "Chứng minh code adaptive"),
        ("6", "Test Backpropagation", "Chứng minh gradient đúng"),
        ("0", "Thoát", "Exit program")
    ]
    
    for num, title, desc in menu_items:
        print(Colors.BOLD + Colors.CYAN + "│" + Colors.END, end="")
        print(Colors.YELLOW + f"  {num}. " + Colors.END, end="")
        print(Colors.BOLD + f"{title:<25}" + Colors.END, end="")
        print(Colors.BLUE + f" - {desc}" + Colors.END)
    
    print(Colors.BOLD + Colors.CYAN + "└" + "─" * 66 + "┘" + Colors.END)
    print()

def print_info_box(title, items):
    """In box thông tin"""
    print()
    print(Colors.BOLD + Colors.GREEN + "┌" + "─" * 66 + "┐" + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "│" + f"{title:^66}" + "│" + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "├" + "─" * 66 + "┤" + Colors.END)
    for item in items:
        print(Colors.BOLD + Colors.GREEN + "│" + Colors.END + f"  {item:<64}" + Colors.BOLD + Colors.GREEN + "│" + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "└" + "─" * 66 + "┘" + Colors.END)
    print()

def main():
    clear_screen()
    print_header()
    
    while True:
        print_menu()
        
        choice = input(Colors.BOLD + Colors.YELLOW + "Chọn chức năng (0-6): " + Colors.END).strip()
        
        if choice == "0":
            print_info_box("THOÁT", ["Cảm ơn bạn đã sử dụng!", "Goodbye!"])
            break
        
        elif choice == "1":
            clear_screen()
            print_header()
            print_info_box("FUNCTION APPROXIMATION", [
                "Ứng dụng: Học hàm sin(x) từ dữ liệu có nhiễu",
                "File: main.py",
                "Đang chạy..."
            ])
            os.chdir(os.path.dirname(__file__))
            os.system("python main.py")
            os.chdir(os.path.dirname(os.path.dirname(__file__)))
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        elif choice == "2":
            clear_screen()
            print_header()
            print_info_box("XOR PROBLEM", [
                "Bài toán: Giải bài toán XOR kinh điển",
                "File: app_xor.py",
                "Đang chạy..."
            ])
            app_path = os.path.join(os.path.dirname(__file__), '..', 'apps', 'app_xor.py')
            os.system(f"python {app_path}")
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        elif choice == "3":
            clear_screen()
            print_header()
            print_info_box("REGRESSION", [
                "Ứng dụng: Dự đoán giá nhà dựa trên diện tích",
                "File: app_regression.py",
                "Đang chạy..."
            ])
            app_path = os.path.join(os.path.dirname(__file__), '..', 'apps', 'app_regression.py')
            os.system(f"python {app_path}")
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        elif choice == "4":
            clear_screen()
            print_header()
            print_info_box("CLASSIFICATION", [
                "Ứng dụng: Phân loại điểm trong/circle",
                "File: app_classification.py",
                "Đang chạy..."
            ])
            app_path = os.path.join(os.path.dirname(__file__), '..', 'apps', 'app_classification.py')
            os.system(f"python {app_path}")
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        elif choice == "5":
            clear_screen()
            print_header()
            print_info_box("TEST TÍNH THÍCH NGHI", [
                "Chứng minh: Thêm/bớt layer không cần viết lại code",
                "File: test_adaptive.py",
                "Đang chạy..."
            ])
            test_path = os.path.join(os.path.dirname(__file__), 'test_adaptive.py')
            os.system(f"python {test_path}")
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        elif choice == "6":
            clear_screen()
            print_header()
            print_info_box("TEST BACKPROPAGATION", [
                "Chứng minh: Gradient được tính đúng",
                "File: test_backprop.py",
                "Đang chạy..."
            ])
            test_path = os.path.join(os.path.dirname(__file__), 'test_backprop.py')
            os.system(f"python {test_path}")
            input(Colors.CYAN + "\nNhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()
        
        else:
            print(Colors.RED + "Lựa chọn không hợp lệ! Vui lòng chọn lại." + Colors.END)
            input(Colors.CYAN + "Nhấn Enter để tiếp tục..." + Colors.END)
            clear_screen()
            print_header()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_info_box("THOÁT", ["Đã dừng chương trình", "Goodbye!"])
        sys.exit(0)


