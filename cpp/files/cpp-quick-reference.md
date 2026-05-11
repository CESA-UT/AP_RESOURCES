# خلاصه سریع C++ برای این تمرین

این فایل جایگزین چند reference بیرونی است تا برای نیازهای اصلی همین تمرین، یک نسخه قابل‌خواندن داخل repo داشته باشید.

## Rule of Three/Five/Zero

- اگر class شما مالک resource خاصی نیست، تا جای ممکن به `Rule of Zero` نزدیک بمانید.
- اگر class شما raw pointer مالکانه، file handle یا resource مشابه دارد، کپی سطحی خطرناک است.
- در این حالت معمولاً باید destructor، copy constructor و copy assignment را با هم ببینید.

### برای این تمرین

- اگر `User`, `Post`, `Comment` را با `std::vector`, `std::string` و value typeها بسازید، خیلی وقت‌ها اصلاً لازم نیست Rule of Three دستی بنویسید.
- اگر از pointer خام برای ownership استفاده کنید، complexity سریع بالا می‌رود.

## `std::vector`

- برای لیست userها، postها، commentها و idها معمولاً بهترین نقطه شروع است.
- رشد پویا دارد و نسبت به آرایه دستی خطای کمتری تولید می‌کند.
- اگر به object واقعی اشاره می‌کنید، اول بررسی کنید آیا `vector<Id>` یا `vector<ValueType>` ساده‌تر نیست.

## `std::unique_ptr`

- اگر واقعاً نیاز به allocation پویا دارید و ownership فقط یک جاست، `unique_ptr` از `delete` دستی امن‌تر است.
- برای این تمرین معمولاً وقتی polymorphism یا object lifetime پیچیده می‌شود به کار می‌آید.
- اگر می‌توانید با value type جلو بروید، معمولاً ساده‌تر است.

## `ifstream`

- برای load کردن فایل، اول بازشدن فایل را چک کنید.
- parse ناموفق را از file-not-found جدا ببینید.
- format فایل را ثابت نگه دارید تا recovery ساده‌تر شود.

## Exceptions

- برای validation عادی user input لازم نیست همه‌چیز exception باشد.
- برای خطاهای جدی‌تر مثل خراب‌بودن فایل ذخیره‌سازی، parse failure یا resource failure می‌تواند مفید باشد.

## منبع‌های اصلی برای نگهداری

- cppreference: Rule of Three/Five/Zero
- cppreference: `std::vector`
- cppreference: `std::unique_ptr`
- cppreference: `std::basic_ifstream`
- cppreference: Exceptions
