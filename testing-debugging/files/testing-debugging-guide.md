# راهنمای کوتاه Testing و Debugging

این خلاصه جایگزین چند منبع بیرونی است تا دانشجو سریع‌تر به مسیر عملی برسد.

## GoogleTest

- برای منطق‌های non-UI مناسب است
- testها باید مستقل و repeatable باشند

## CTest

- اگر CMake دارید، `ctest` ساده‌ترین راه اجرای testهاست
- `--output-on-failure` برای دیباگ سریع مفید است

## AddressSanitizer

- برای memory bugهای C++ بسیار ارزشمند است
- use-after-free، out-of-bounds و بعضی leakها را خوب پیدا می‌کند

## برای این تمرین چه testهایی مهم‌اند؟

- register با username تکراری
- login با credential غلط
- create post با متن خالی
- reload داده بعد از save
- حذف post یا user بدون خراب‌شدن relationها

## منبع‌های اصلی برای نگهداری

- GoogleTest Primer
- CTest module
- AddressSanitizer docs
