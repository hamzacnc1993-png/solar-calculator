[app]
# عنوان التطبيق واسم الحزمة
title = Solar Calculator
package.name = solarcalculator
package.domain = org.solar

# الملفات المراد تضمينها
source.include_exts = py,png,jpg,kv,atlas
source.dir = .

# الإصدار والمكتبات المطلوبة
version = 1.0
requirements = python3,kivy

# اتجاه الشاشة (عمودي)
orientation = portrait

# إعدادات أندرويد
android.permissions = INTERNET
android.api = 33
android.min_api = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
