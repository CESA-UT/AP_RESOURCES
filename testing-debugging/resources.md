# فهرست منابع Testing و Debugging

فایل‌های واقعی این topic را داخل [files/](./files/) بگذارید. اگر منبع برای حل مستقیم این تمرین نیست، در توضیح آن برچسب `مطالعه اضافه` بزنید.

### TEST-101

- عنوان: GoogleTest Primer
- موضوع: unit testing
- سطح: مقدماتی
- زمان تقریبی مطالعه: ۱۲ دقیقه
- پیش‌نیازها: CMake یا build پایه
- چه زمانی باید این را بخوانیم؟ وقتی می‌خواهید برای منطق‌های non-UI چند تست واقعی بنویسید.
- خلاصه کوتاه: سریع‌ترین شروع برای testهای مستقل و repeatable در C++.
- مثال مرتبط با تمرین: تست register، search و serialization بدون درگیرشدن با UI.
- لینک یا فایل منبع: [testing-debugging-guide.md](./files/testing-debugging-guide.md)
- نویسنده/اضافه‌کننده: curated
- وضعیت بررسی: بررسی شده

### TEST-102

- عنوان: CTest module
- موضوع: test runner
- سطح: مقدماتی
- زمان تقریبی مطالعه: ۸ دقیقه
- پیش‌نیازها: CMake
- چه زمانی باید این را بخوانیم؟ وقتی می‌خواهید testها را در workflow build جا بدهید.
- خلاصه کوتاه: اگر از CMake استفاده می‌کنید، `include(CTest)` و `ctest` مسیر ساده‌ای برای اجرای testها می‌دهد.
- مثال مرتبط با تمرین: قبل از merge فازها، testهای پایه را با `ctest --output-on-failure` اجرا کنید.
- لینک یا فایل منبع: [testing-debugging-guide.md](./files/testing-debugging-guide.md)
- نویسنده/اضافه‌کننده: curated
- وضعیت بررسی: بررسی شده

### TEST-103

- عنوان: AddressSanitizer
- موضوع: memory debugging
- سطح: متوسط
- زمان تقریبی مطالعه: ۱۰ دقیقه
- پیش‌نیازها: Clang یا compiler سازگار
- چه زمانی باید این را بخوانیم؟ وقتی نگران use-after-free، out-of-bounds و memory bug هستید.
- خلاصه کوتاه: برای پروژه‌ای که روی مدیریت حافظه نمره دارد، یکی از مفیدترین ابزارهای عملی است.
- مثال مرتبط با تمرین: حذف کاربر یا پست باعث خراب‌شدن حافظه شده و نمی‌دانید کجا.
- لینک یا فایل منبع: [testing-debugging-guide.md](./files/testing-debugging-guide.md)
- نویسنده/اضافه‌کننده: curated
- وضعیت بررسی: بررسی شده
