# CarInsight AI — تقدير سعر السيارة من الصورة

مودل يقدّر سعر السيارة من صورها فقط (بدون ماركة أو سنة أو ممشى)، ويعطي نطاقاً محتملاً 80% و90%.

**نتائج الاختبار (345 إعلان):** الخطأ النسبي الوسيط 10.7%، R² = 0.848، متوسط الخطأ 15,908 ر.س.

## محتويات المستودع
| المسار | الوصف |
|---|---|
| `docs/` | لوحة النتائج (GitHub Pages) |
| `app/` | تطبيق التجربة الحيّة (Gradio، يُنشر على Hugging Face Spaces) |
| `src/image_to_price_v2.py` | كود التدريب والتقييم |
| `notebooks/` | دفتر Colab لإعادة التدريب |

## النشر (ثلاث خطوات)
1. **GitHub:** أنشئ مستودعاً فارغاً ثم:
```bash
git init && git add . && git commit -m "CarInsight AI"
git branch -M main && git remote add origin https://github.com/USERNAME/REPO.git && git push -u origin main
```
2. **GitHub Pages:** Settings ← Pages ← Branch `main` ← Folder `/docs` ← Save. تظهر اللوحة على `https://USERNAME.github.io/REPO/`
3. **التجربة الحيّة:** أنشئ Space جديد على huggingface.co/spaces (نوع Gradio) وارفع محتويات مجلد `app/` كلها. بعد ما يشتغل، انسخ رابطه وضعه في `docs/index.html` في المتغير `DEMO_URL` ثم ادفع التعديل.

> ملاحظة: الداتا والصور الكاملة غير مرفوعة عمداً (`.gitignore`). تأكد من صلاحية نشر أي صور أمثلة قبل جعل المستودع عاماً.
