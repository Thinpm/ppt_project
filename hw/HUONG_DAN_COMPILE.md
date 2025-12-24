# Hướng dẫn compile báo cáo LaTeX

## Yêu cầu

Cần cài đặt LaTeX distribution:
- **Ubuntu/Debian:** `sudo apt-get install texlive-full`
- **Windows:** MiKTeX hoặc TeX Live
- **macOS:** MacTeX

## Cách compile

### Cách 1: Sử dụng pdflatex (command line)

```bash
cd /home/thuypm/Desktop/ttu/pptinh/final
pdflatex bao_cao.tex
pdflatex bao_cao.tex  # Chạy 2 lần để cập nhật references
```

### Cách 2: Sử dụng Overleaf (Khuyến nghị)

1. Truy cập [Overleaf.com](https://www.overleaf.com)
2. Tạo project mới → Upload Project
3. Upload file `bao_cao.tex`
4. Overleaf sẽ tự động compile

## Lưu ý

- File `bao_cao.tex` đã được thiết kế để code **không bị ngắt giữa trang**
- Sử dụng `tcolorbox` với `breakable=false` để đảm bảo code nằm trọn trong một trang
- Nếu code quá dài, có thể cần điều chỉnh font size trong `\lstset`

## Packages cần thiết

File đã include các packages sau:
- `amsmath, amssymb, amsthm` - Toán học
- `geometry` - Cấu hình trang
- `graphicx` - Hình ảnh
- `listings` - Code formatting
- `xcolor` - Màu sắc
- `tcolorbox` - Box cho code (quan trọng để không ngắt trang)
- `hyperref` - Links
- `babel` - Hỗ trợ tiếng Việt

## Nếu thiếu package

Nếu compile báo lỗi thiếu package, cài thêm:

```bash
# Ubuntu/Debian
sudo apt-get install texlive-lang-other  # Cho babel vietnamese
sudo apt-get install texlive-latex-extra  # Cho các package khác
```

## Output

Sau khi compile thành công, sẽ có file `bao_cao.pdf` trong cùng thư mục.

