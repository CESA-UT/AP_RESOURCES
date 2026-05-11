# مسیر شروع با Qt برای این تمرین

این خلاصه به‌جای چند صفحه بیرونی Qt نوشته شده تا داخل خود repo قابل‌استفاده باشد.

## آیا Qt برای این تمرین مناسب است؟

- اگر می‌خواهید app دسکتاپ با فرم، دکمه، input و window داشته باشید: بله
- اگر فقط یک prototype خیلی سریع می‌خواهید: شاید `ImGui` ساده‌تر باشد

## برای این تمرین بیشتر روی چه بخش Qt بایستیم؟

- `Qt Widgets`
- layoutها
- parent/child ownership
- signal/slotهای پایه

## مسیر پیشنهادی

1. اول هسته منطقی پروژه را بدون UI یا با UI خیلی کم بسازید.
2. بعد یک window ساده برای login یا profile viewer اضافه کنید.
3. هر feature جدید UI را به منطق آماده وصل کنید، نه برعکس.

## چند نکته مهم

- از parent-child ownership استفاده کنید تا objectها خودکار آزاد شوند.
- UI را با منطق domain قاطی نکنید.
- اول با widgetهای استاندارد شروع کنید؛ custom widget را دیرتر اضافه کنید.

## برای این تمرین چه exampleهایی مهم‌ترند؟

- فرم login
- نمایش profile
- نمایش feed با list یا card ساده
- edit کردن bio یا post text

## فایل‌های محلی این بخش

- [qt_fa.pdf](./qt_fa.pdf)

## منبع‌های اصلی برای نگهداری

- Qt Getting Started
- Getting Started Programming with Qt Widgets
- Widgets Tutorial
- Qt Widgets Examples
