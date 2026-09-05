# بسيطة README بالعربية

مشروع: لعبة رعب بسيطة مبنية بـ Kivy (Python)

محتويات:
- main.py: الكود الرئيسي للتطبيق
- buildozer.spec: إعدادات Buildozer لبناء APK
- sounds/: مجلد مخصص لوضع ملفات الأصوات (اختياري)

تعليمات لبناء APK محليًا:
1) ثبت Buildozer وبيئة Android على جهاز Linux أو استخدم Docker.
2) من داخل مجلد المشروع شغّل:
   buildozer android debug
3) ستجد الـAPK داخل مجلد bin/ بعد انتهاء البناء.

في CI تم إعداد GitHub Actions لبناء APK تلقائياً (قد تتطلب مدة أطول وسيتم رفع الـAPK كـ artifact).

ملاحظة: الـAPK موقّع بتوقيع debug — مناسب للاختبار، ليس للنشر.
