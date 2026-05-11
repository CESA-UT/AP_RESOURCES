# مسیر شروع با CMake

این فایل خلاصه‌ای از چند منبع بیرونی است تا CMake را برای همین تمرین سریع‌تر راه بیندازد.

## چرا CMake؟

- تعداد فایل‌ها در این پروژه زیاد می‌شود
- بعداً test، SQLite، Qt یا libraryهای دیگر ممکن است اضافه شوند
- build تکرارپذیر و قابل تحویل لازم دارید

## یک ساختار ساده خوب

```text
project-root/
├── CMakeLists.txt
├── src/
├── include/
├── tests/
└── data/
```

## حداقل چیزهایی که لازم دارید

- تعریف project
- تعیین استاندارد C++
- ساخت executable اصلی
- اضافه‌کردن include path
- اگر test دارید: `include(CTest)`

## پیشنهاد عملی

- از اول `src/` و `include/` را جدا نگه دارید
- اگر test دارید، آن را پشت `BUILD_TESTING` بگذارید
- اگر Qt استفاده می‌کنید، integration را بعد از پایدارشدن هسته پروژه اضافه کنید

## منبع‌های اصلی برای نگهداری

- CMake Tutorial
- CTest module
- Qt Creator CMake docs
