# ddm501-assignment-1-telco-churn-system-design

**Trịnh Đức Dương - 25ms13290 | DDM501**

Project độc lập cho bài 1: báo cáo thiết kế hệ thống dự đoán khách hàng rời bỏ viễn thông, baseline ML, API và test chạy thật.

## Nội dung nộp

- `DDM501_Assignment1_25ms13290_TrinhDucDuong.pdf`: báo cáo tiếng Anh theo đề.
- `report/report.md`: nội dung có thể chỉnh sửa; script trong `report/` dựng lại PDF từ kết quả thật.
- `churn/`, `tests/`, `data/`: mã nguồn, test, dữ liệu mẫu IBM kèm nguồn và checksum.
- `evidence/verification.json`, `evidence/pytest.txt`, `evidence/pipeline.txt`: bằng chứng thực thi.

## Chạy độc lập trên Windows

Yêu cầu Python 3.10 hoặc 3.11. Mở PowerShell tại thư mục **ddm501-assignment-1-telco-churn-system-design**:

```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
./.venv/Scripts/python.exe -m churn
./.venv/Scripts/python.exe -m pytest -q
./.venv/Scripts/python.exe scripts/verify.py
```

Môi trường `.venv` nằm ngay trong project, không dùng môi trường của bài 2 hay thư mục cha. `scripts/verify.py` chạy kiểm tra dependency, lint, test, train toàn bộ dữ liệu và dựng API tạm để gửi request HTTP thật; tiến trình API được đóng sau kiểm tra.

Chạy API để tự thao tác:

```powershell
./.venv/Scripts/python.exe -m uvicorn churn.api:create_app --factory --host 127.0.0.1 --port 8011
```

Mở http://127.0.0.1:8011/docs. GET `/health`; POST `/predict` với payload theo `examples/request.json`. Dừng bằng Ctrl+C. Phải chạy train trước để tạo `artifacts/model.joblib`.

## Linux/macOS hoặc Docker

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m churn
.venv/bin/python -m pytest -q
docker build -t ddm501-assignment1 .
docker run --rm -p 127.0.0.1:8011:8000 ddm501-assignment1
```

Dockerfile train mô hình trong image, do đó không cần artifact được tạo trên máy khác. Lệnh Docker cần Docker Engine đang chạy.

## Cấu hình, dữ liệu và giới hạn

`config.yaml` chứa seed=42, tỷ lệ liên hệ=20%, đường dẫn dữ liệu và output. Có thể override bằng `CHURN_DATA_PATH`, `CHURN_OUTPUT_DIR`; API dùng `CHURN_MODEL_PATH` nếu cần. Dữ liệu đã nằm trong `data/telco.csv`, không cần tải lại.

Dữ liệu IBM là mẫu giả lập, không có thời gian quan sát hay hiệu quả chiến dịch. Kết quả offline không chứng minh tăng doanh thu hoặc giữ chân khách hàng thực tế. API là demo cục bộ, không triển khai trực tiếp công khai. Chỉ nạp file joblib tin cậy.

## Chuẩn bị Git repo riêng

Dựng lại PDF bằng môi trường riêng của project:

```powershell
./.venv/Scripts/python.exe -m pip install -r requirements-report.txt
./.venv/Scripts/python.exe report/build_report.py
```

Chạy pipeline trước để báo cáo lấy đúng kết quả mới. Font Unicode và giấy phép font đã nằm trong `report/fonts/`.

Có thể di chuyển nguyên thư mục này tới vị trí bất kỳ. Không có import hay đường dẫn phụ thuộc project đồng cấp. `.gitignore` bỏ `.venv`, cache, runtime artifacts và database; **báo cáo, dữ liệu mẫu, mã nguồn, cấu hình và evidence vẫn được giữ để commit**. Tạo lại `.venv` bằng `setup.ps1` sau khi di chuyển hoặc clone. `requirements-lock-windows.txt` ghi đủ phiên bản của môi trường Windows đã kiểm tra; `requirements.txt` là bộ dependency trực tiếp dùng được đa nền tảng.

Repository: https://github.com/TrinhDucDuong/ddm501-assignment-1-telco-churn-system-design

Project dùng Git repository riêng, nhánh `main`, remote `origin` trỏ tới địa chỉ trên.

`setup.ps1` uses `requirements-lock-windows.txt` when present to restore the tested full environment; otherwise it uses `requirements.txt`.
