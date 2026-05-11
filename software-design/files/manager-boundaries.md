# مرزهای `SocialNetwork`

این فایل کمک می‌کند `SocialNetwork` یا `SystemManager` به کلاس همه‌کاره تبدیل نشود.

## داخل manager چه چیزهایی خوب است؟

- register و login
- lookup بر اساس `id` یا `username`
- هماهنگ‌کردن چند object برای یک use case
- load و save سطح بالا

## چه چیزهایی بهتر است داخل manager نرود؟

- جزئیات نمایش متن profile یا post
- validation خیلی محلی که خود object بهتر می‌فهمد
- parse و serialize ریز همه fieldها اگر لایه جدا دارید

## یک rule ساده

اگر یک operation بیشتر شبیه «هماهنگ‌کردن چند موجودیت» است، manager جای خوبی است.

اگر یک operation بیشتر شبیه «منطق داخلی خود object» است، آن را نزدیک همان object نگه دارید.
