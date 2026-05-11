# راهنمای کوتاه Git

این خلاصه برای کار روزمره گروهی روی همین تمرین است.

## `clone`

- repository گروه را clone می‌کنید
- remote اصلی معمولاً `origin` است

## branch

- هر feature را روی branch جدا جلو ببرید
- branch اصلی را stable نگه دارید

## merge

- وقتی feature آماده شد، آن را merge کنید یا PR بزنید
- conflict طبیعی است و باید intent دو تغییر را بفهمید

## `restore`

- برای برگرداندن تغییرات محلی خیلی مفید است
- آن را با reset قاطی نکنید

## workflow پیشنهادی برای این تمرین

1. `main` یا `master` فقط نسخه قابل اجرا
2. هر feature روی branch جدا
3. merge بعد از build و test

## منبع‌های اصلی برای نگهداری

- git-clone docs
- Git Book: Basic Branching and Merging
- git-restore docs
