# فهرست منابع طراحی نرم‌افزار

فایل‌های واقعی این topic را داخل [files/](./files/) بگذارید. اگر منبع برای حل مستقیم این تمرین نیست، در توضیح آن برچسب `مطالعه اضافه` بزنید.

### DESIGN-001

- عنوان: note داخلی: مدل‌سازی موجودیت‌ها در `MinSocial`
- موضوع: domain modeling
- سطح: مقدماتی
- زمان تقریبی مطالعه: ۱۰ دقیقه
- پیش‌نیازها: class پایه
- چه زمانی باید این را بخوانیم؟ قبل از نوشتن کد زیاد
- خلاصه کوتاه: اول entityها، relationها و use caseهای اصلی را روی کاغذ مشخص کنید.
- مثال مرتبط با تمرین: `User`، `Profile`، `Post`، `Comment` و `SocialNetwork`
- لینک یا فایل منبع: [minsocial-modeling-note.md](./files/minsocial-modeling-note.md)
- نویسنده/اضافه‌کننده: curated
- وضعیت بررسی: بررسی شده

### DESIGN-002

- عنوان: note داخلی: چه چیزی داخل `SocialNetwork` باشد و چه چیزی نباشد؟
- موضوع: responsibility boundaries
- سطح: متوسط
- زمان تقریبی مطالعه: ۹ دقیقه
- پیش‌نیازها: class design
- چه زمانی باید این را بخوانیم؟ وقتی کلاس manager شروع به بادکردن می‌کند.
- خلاصه کوتاه: manager باید orchestration کند، نه این‌که همه جزئیات همه objectها را خودش مدیریت کند.
- مثال مرتبط با تمرین: login و search می‌تواند در manager باشد، ولی فرمت نمایش profile بهتر است جای دیگری بماند.
- لینک یا فایل منبع: [manager-boundaries.md](./files/manager-boundaries.md)
- نویسنده/اضافه‌کننده: curated
- وضعیت بررسی: بررسی شده
