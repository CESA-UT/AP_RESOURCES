# مسیر شروع با Make

اگر گروه شما `Makefile` را ترجیح می‌دهد، این خلاصه برای شروع کافی است.

## ساختار پایه

- یک target پیش‌فرض مثل `all`
- target اجرایی
- targetهای object
- target `clean`
- استفاده از `.PHONY` برای `all`, `clean`, `run`

## برای این تمرین

- پروژه را بی‌دلیل پیچیده نکنید
- اگر Makefile خیلی بزرگ شد، احتمالاً وقت CMake است

## یک الگوی ساده

```make
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra

.PHONY: all clean

all: app

app: main.o user.o post.o
	$(CXX) $(CXXFLAGS) -o app main.o user.o post.o

clean:
	rm -f app *.o
```

## منبع‌های اصلی برای نگهداری

- GNU Make: Simple Makefile
- GNU Make: Rule Syntax
- GNU Make: Phony Targets
