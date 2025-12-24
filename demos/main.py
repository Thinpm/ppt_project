"""
Demo Neural Network với giao diện terminal đẹp
Sử dụng box drawing và màu sắc để hiển thị rõ ràng
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'network'))
from layers import DenseLayer, Tanh
from network import NeuralNetwork
from loss import MSELoss
from optimizers import GradientDescent, BFGSOptimizer

# Màu sắc cho terminal (ANSI codes)
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

def print_box(title, content, width=70):
    """In khung đẹp với title và content"""
    print()
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + f"{title:^{width-2}}" + "║")
    print("╠" + "═" * (width - 2) + "╣")
    for line in content:
        if isinstance(line, list):
            for subline in line:
                print("║" + f"{subline:<{width-2}}" + "║")
        else:
            print("║" + f"{line:<{width-2}}" + "║")
    print("╚" + "═" * (width - 2) + "╝")

def print_section(title, width=70):
    """In tiêu đề section"""
    print()
    print(Colors.BOLD + Colors.CYAN + "┌" + "─" * (width - 2) + "┐" + Colors.END)
    print(Colors.BOLD + Colors.CYAN + "│" + f"{title:^{width-2}}" + "│" + Colors.END)
    print(Colors.BOLD + Colors.CYAN + "└" + "─" * (width - 2) + "┘" + Colors.END)

def print_info(label, value, width=70):
    """In thông tin với format đẹp"""
    print(Colors.BLUE + f"  {label:<25}" + Colors.END + Colors.GREEN + f"{value:>40}" + Colors.END)

def print_progress_bar(epoch, total, loss, width=50):
    """In progress bar đẹp"""
    filled = int(width * epoch / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = epoch / total * 100
    print(f"\r  [{bar}] {percent:5.1f}% | Epoch {epoch:4d} | Loss: {Colors.YELLOW}{loss:.6f}{Colors.END}", end="")

def generate_data(n_samples=50):
    """Tạo dữ liệu: y = sin(x) với nhiễu"""
    np.random.seed(42)
    X = np.linspace(-np.pi, np.pi, n_samples)
    y = np.sin(X) + 0.1 * np.random.randn(n_samples)
    return X.reshape(-1, 1), y.reshape(-1, 1)

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Header
    print(Colors.BOLD + Colors.HEADER + "=" * 70 + Colors.END)
    print(Colors.BOLD + Colors.HEADER + " " * 15 + "NEURAL NETWORK DEMO" + " " * 15 + Colors.END)
    print(Colors.BOLD + Colors.HEADER + " " * 10 + "Function Approximation: sin(x)" + " " * 10 + Colors.END)
    print(Colors.BOLD + Colors.HEADER + "=" * 70 + Colors.END)
    
    # Section 1: Tạo dữ liệu
    print_section("1. TẠO DỮ LIỆU TRAINING")
    X, y = generate_data(n_samples=50)
    print_info("Số mẫu:", f"{len(X)}")
    print_info("Input range:", f"[{X.min():.2f}, {X.max():.2f}]")
    print_info("Output range:", f"[{y.min():.2f}, {y.max():.2f}]")
    
    # Section 2: Khởi tạo Network
    print_section("2. KHỞI TẠO NEURAL NETWORK")
    network_gd = NeuralNetwork([
        DenseLayer(1, 10),
        Tanh(),
        DenseLayer(10, 1)
    ])
    
    content = [
        "Cấu trúc: 1 input → 10 hidden → 1 output",
        "Activation: Tanh",
        f"Tổng số tham số: {sum(layer.W.size + layer.b.size for layer in network_gd.layers if hasattr(layer, 'W'))}"
    ]
    print_box("", content, width=70)
    
    # Network cho BFGS (copy để so sánh công bằng)
    network_bfgs = NeuralNetwork([
        DenseLayer(1, 10),
        Tanh(),
        DenseLayer(10, 1)
    ])
    # Copy tham số ban đầu
    params_gd = network_gd.get_all_params()
    network_bfgs.set_all_params(params_gd)
    
    # Section 3: Training với Gradient Descent
    print_section("3. HUẤN LUYỆN - GRADIENT DESCENT")
    loss_fn = MSELoss()
    optimizer_gd = GradientDescent(learning_rate=0.01)
    
    losses_gd = []
    epochs = 1000
    
    print(Colors.YELLOW + "  Training progress:" + Colors.END)
    for epoch in range(epochs):
        loss = optimizer_gd.step(network_gd, loss_fn, X, y)
        losses_gd.append(loss)
        
        if epoch % 100 == 0 or epoch == epochs - 1:
            print_progress_bar(epoch + 1, epochs, loss)
    
    print()  # New line after progress bar
    
    # Section 3b: Training với BFGS
    print_section("4. HUẤN LUYỆN - BFGS")
    optimizer_bfgs = BFGSOptimizer()
    
    print(Colors.YELLOW + "  BFGS Optimization..." + Colors.END)
    result = optimizer_bfgs.optimize(network_bfgs, loss_fn, X, y, max_iter=100)
    
    # Tính loss sau khi tối ưu
    final_loss_bfgs = 0
    for i in range(len(X)):
        y_pred = network_bfgs.forward(X[i])
        loss = loss_fn.forward(y_pred, y[i])
        final_loss_bfgs += loss
    final_loss_bfgs /= len(X)
    
    print(Colors.GREEN + f"  Final loss: {final_loss_bfgs:.6f}" + Colors.END)
    print(Colors.GREEN + f"  Iterations: {result.nit}" + Colors.END)
    
    # Section 5: Kết quả và So sánh
    print_section("5. KẾT QUẢ VÀ SO SÁNH")
    
    # Tính toán thêm
    X_test = np.linspace(-np.pi, np.pi, 200).reshape(-1, 1)
    y_true = np.sin(X_test)
    y_pred_gd = network_gd.predict(X_test)
    y_pred_bfgs = network_bfgs.predict(X_test)
    mse_gd = np.mean((y_pred_gd - y_true)**2)
    mse_bfgs = np.mean((y_pred_bfgs - y_true)**2)
    
    content = [
        f"Gradient Descent:",
        f"  Loss ban đầu:     {Colors.RED}{losses_gd[0]:.6f}{Colors.END}",
        f"  Loss cuối:        {Colors.GREEN}{losses_gd[-1]:.6f}{Colors.END}",
        f"  Giảm loss:        {Colors.GREEN}{((losses_gd[0]-losses_gd[-1])/losses_gd[0]*100):.1f}%{Colors.END}",
        f"  MSE trên test:    {Colors.CYAN}{mse_gd:.6f}{Colors.END}",
        "",
        f"BFGS:",
        f"  Loss cuối:        {Colors.GREEN}{final_loss_bfgs:.6f}{Colors.END}",
        f"  MSE trên test:    {Colors.CYAN}{mse_bfgs:.6f}{Colors.END}",
        f"  Iterations:       {Colors.CYAN}{result.nit}{Colors.END}",
        "",
        f"So sánh: BFGS {'tốt hơn' if final_loss_bfgs < losses_gd[-1] else 'kém hơn'} Gradient Descent"
    ]
    print_box("", content, width=70)
    
    # Section 6: Visualization
    print_section("6. VISUALIZATION")
    
    plt.figure(figsize=(14, 5))
    
    # Plot 1: So sánh dự đoán
    plt.subplot(1, 2, 1)
    plt.scatter(X, y, alpha=0.5, label='Training data', s=20, color='gray')
    plt.plot(X_test, y_true, 'g-', label='True: sin(x)', linewidth=2)
    plt.plot(X_test, y_pred_gd, 'r--', label='GD Prediction', linewidth=2)
    plt.plot(X_test, y_pred_bfgs, 'b--', label='BFGS Prediction', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function Approximation: sin(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Loss curve
    plt.subplot(1, 2, 2)
    plt.plot(losses_gd, 'r-', label='Gradient Descent', linewidth=2)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss (Gradient Descent)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    
    plt.tight_layout()
    plt.savefig('results_comparison.png', dpi=150, bbox_inches='tight')
    
    print_info("Đã lưu đồ thị:", "results_comparison.png")
    
    # Footer
    print()
    print(Colors.BOLD + Colors.GREEN + "=" * 70 + Colors.END)
    print(Colors.BOLD + Colors.GREEN + " " * 25 + "HOÀN THÀNH!" + " " * 25 + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "=" * 70 + Colors.END)
    print()
    
    try:
        plt.show()
    except:
        pass

if __name__ == "__main__":
    main()


