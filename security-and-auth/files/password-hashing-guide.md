# راهنمای کوتاه password hashing

این خلاصه برای همان requirement تمرین نوشته شده که می‌گوید password نباید plain text ذخیره شود.

## چه چیزی نکنیم؟

- ذخیره plain password
- hash خیلی ساده و سریع بدون salt

## چه چیزی بهتر است؟

- استفاده از password hashing function مناسب
- اگر library خارجی می‌خواهید: `libsodium`
- اگر فعلاً راه‌حل خیلی ساده‌تر می‌خواهید، حداقل روشن بنویسید که این بخش production-grade نیست

## برای این تمرین

- اگر گروه شما library خارجی اضافه نمی‌کند، باید در گزارش شفاف بگویید راه‌حل امنیتی شما محدود است
- اگر `libsodium` اضافه می‌کنید، مسیر قابل دفاع‌تری دارید

## ایده پیاده‌سازی

- هنگام register، خروجی hash را ذخیره کنید
- هنگام login، password ورودی را با همان API verify کنید
- password خام را در فایل یا database نگه ندارید

## منبع‌های اصلی برای نگهداری

- Libsodium password hashing
- Libsodium `pwhash*` API
