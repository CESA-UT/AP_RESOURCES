# راهنمای SQLite برای این تمرین

این خلاصه برای گروه‌هایی است که persistence را جدی‌تر می‌خواهند.

## چه وقت SQLite منطقی‌تر می‌شود؟

- relationها بیشتر شده‌اند
- query دارید
- integrity برایتان مهم‌تر شده
- requirement اجرای همزمان ساده را می‌خواهید راحت‌تر پوشش بدهید

## چیزهایی که باید بدانید

- connection object
- prepared statement
- bind کردن پارامترها
- finalize و close

## چرا برای این تمرین جذاب است؟

- data model اجتماعی معمولاً relation زیاد دارد
- برای load/save کلی داده لازم نیست کل فایل JSON را rewrite کنید
- locking و atomic commit از قبل حل شده‌اند

## هشدار

- اگر هنوز تیم روی SQL و schema راحت نیست، ممکن است برای فاز اول زیادی سنگین شود
- schema ساده نگه دارید

## برای requirement همزمانی

- SQLite خودش locking و transaction دارد
- transactionها را کوتاه نگه دارید
- یک write path مشخص داشته باشید

## منبع‌های اصلی برای نگهداری

- SQLite C/C++ Interface intro
- SQLite locking and concurrency
- SQLite atomic commit
