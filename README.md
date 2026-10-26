# CarInsight AI

واجهة لتقدير سعر السيارة من الصور فقط، مع خلفية Python تستخدم المودل المدرّب الموجود في المشروع.

## روابط المشروع

- **الموقع الثابت (GitHub Pages):** بعد تفعيل Pages من `Settings → Pages → Deploy from a branch → main → /docs` افتح `https://mega-eng.github.io/car-PRICE-BY-AI/`.
- **واجهة التقدير:** `https://mega-eng.github.io/car-PRICE-BY-AI/predict.html`.
- **كود المشروع:** [carinsight](./carinsight/README.md).

> إذا كان المستودع خاصًا، فقد يتطلب نشر GitHub Pages خطة مدفوعة. لا تغيّر المستودع إلى عام إلا إذا كنت موافقًا على نشر محتوياته.

## بنية النشر

- `docs/`: واجهة الموقع الثابتة التي تُنشر على GitHub Pages.
- `carinsight/api/`: خدمة FastAPI وDockerfile لتشغيل الخلفية.
- `carinsight/app/`: تطبيق Gradio الأصلي، كود التنبؤ، وملف المودل المدرّب.

## تشغيل الخلفية

اقرأ [دليل نشر API](./carinsight/api/README.md). الخيار المقترح للتشغيل المستمر ضمن موارد مجانية هو خادم Oracle Cloud Always Free عند توفر السعة المناسبة؛ لا يمكن ضمان توفر الخادم أو أن كل تكاليف الحساب ستكون صفرًا في كل الظروف.

بعد نشر الخلفية، عدّل `docs/api-config.js` وضع عنوانها الأساسي في `window.CARINSIGHT_API_URL`، ثم ادفع التغيير إلى GitHub. حافظ على عنوان API دون شرطة مائلة في النهاية.

**مهم:** GitHub Pages لا يشغّل Python أو المودل. الواجهة الثابتة لن تُجري تنبؤات فعلية حتى تنشر الخلفية وتضبط رابطها.
