[app]
# قبول تراخيص أندرويد تلقائياً
android.accept_sdk_license = True
# (str) عنوان التطبيق الذي سيظهر على شاشة الهاتف
title = Solar Calculator

# (str) اسم حزمة التطبيق (يجب أن يكون باللغة الإنجليزية وبدون مسافات)
package.name = solarcalculator

# (str) نطاق الحزمة
package.domain = org.solar

# (list) الامتدادات والملفات المطلوبة ضمن التطبيق
source.include_exts = py,png,jpg,kv,atlas

# (list) المجلد الذي توجد فيه الملفات البرمجية (النقطة تعني المجلد الحالي)
source.dir = .

# (list) المكتبات المطلوبة لتشغيل التطبيق
requirements = python3,kivy

# (str) إصدار التطبيق
version = 1.0

# (str) اتجاه الشاشة المفضلة (portrait يعني عمودي)
orientation = portrait

# -------------------------------------------------------------------------
# إعدادات خاصة بنظام أندرويد (متوافقة ومستقرة لتجنب مشاكل التراخيص)
# -------------------------------------------------------------------------

# (list) الصلاحيات التي يحتاجها التطبيق على الهاتف
android.permissions = INTERNET

# (int) إصدار الأندرويد المستهدف (Target API)
android.api = 33

# (int) الحد الأدنى لإصدار أندرويد يدعم التطبيق (Minimum API)
android.min_api = 21

# (str) إصدار أدوات البناء لتجنب طلبات التراخيص المعلقة
android.build_tools_version = 33.0.0

# (str) المعمارية المدعومة للمعالجات (تدعم الهواتف الحديثة والقديمة)
android.archs = arm64-v8a, armeabi-v7a

# (str) مسار الأيقونة (اختياري، يمكنك تركها فارغة حالياً)
#icon.filename = %(source.dir)s/icon.png


[buildozer]

# (int) مستوى تفاصيل سجل الأخطاء (2 يعني وضع التصحيح المفصل debug)
log_level = 2

# (int) إظهار تحذير في حال تم تشغيل البناء بصلاحيات الـ Root
warn_on_root = 1

# (str) مسار تخزين بيئة أندرويد المؤقتة
# build_dir = ./.buildozer

# (str) مسار المخرجات (حيث سيتم حفظ ملف الـ APK النهائي)
# bin_dir = ./bin
