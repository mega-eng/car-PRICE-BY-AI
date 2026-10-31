# 🚗 CarInsight AI
### A car's value is more than its name. Let AI see it.

**CarInsight AI** explores a different approach to vehicle price estimation: can AI estimate a car's value from its images alone?

Unlike approaches that require manually supplied vehicle details, **the core pricing model uses vehicle photos without make, model, year, or mileage as prediction inputs**. It applies computer vision to visual information and estimates a price in Saudi Riyals (SAR).

🌐 **[Launch CarInsight AI](https://reserved-justice-unified-brokers.trycloudflare.com/)** · **[View Source Code](https://github.com/mega-eng/car-PRICE-BY-AI)**

> **Demo availability:** The demo runs on a personal machine and may be slow or offline. The temporary hosting URL can change when the session restarts. Uploaded images are processed by the machine hosting the demo; avoid uploading private or sensitive images.

---

## 🔍 What Makes CarInsight AI Different?

### No Make. No Model. No Mileage. Just Images.

The core pricing model does not use the vehicle's make, model name, year, or mileage as prediction inputs. Instead, it analyzes visual patterns learned from vehicle images to estimate a price.

The project explores **image-based price estimation**: using computer vision to infer value from how a vehicle looks, rather than relying on its name or manually entered specifications.

- 🖼️ **Image-based estimation** — upload between **1 and 8 vehicle images**.
- 🧠 **Visual feature extraction** — uses DINOv2 at three model sizes and CLIP.
- 🔄 **Test-time augmentation** — evaluates original and horizontally flipped image views.
- 🧮 **Ensemble averaging** — predictions from multiple models are averaged in log-price space.
- 📊 **Prediction intervals** — returns an estimated price with 80% and 90% prediction intervals to communicate uncertainty.

---

## 📈 Evaluation Results

The project report presents evaluation results on **345 test vehicle listings**.

| Metric | Reported result |
|---|---:|
| Coefficient of determination (R²) | **0.848** |
| Median relative error | **10.7%** |
| Predictions within ±20% of actual price | **76%** |
| Predictions within ±30% of actual price | **88%** |
| Actual prices covered by the nominal 80% prediction interval | **80.9%** |
| Actual prices covered by the nominal 90% prediction interval | **92.2%** |

*These are reported evaluation results, not a guarantee for every vehicle. R² is a statistical performance metric and should not be interpreted as a percentage of predictions that are correct.*

---

## 🧠 How It Works

1. **Image input** — accepts 1–8 photos of a vehicle.
2. **Visual feature extraction** — extracts image features using DINOv2 at three model sizes and CLIP.
3. **Test-time augmentation** — processes original and flipped image views.
4. **Ensemble averaging** — averages model predictions in log-price space.
5. **Price and uncertainty** — returns an estimated price in SAR with 80% and 90% prediction intervals.

---

## 📁 Project Data

The project report describes a dataset of:

- **2,293** vehicle listings
- **11,199** vehicle images
- **345** test listings

The figures above describe the reported project dataset and evaluation. The README does not assume that the 345 test listings are additional to the 2,293 listings.

## 🛠️ Technologies

- Python
- PyTorch
- Cloudflare Tunnel
- DINOv2
- CLIP
- Gradio

## 🎯 Project Objectives

- Explore vehicle price estimation from images instead of manually entered vehicle specifications.
- Apply computer vision feature extraction and ensemble prediction.
- Evaluate performance on test listings.
- Communicate uncertainty with prediction intervals rather than presenting estimates as guaranteed prices.
- Provide an interactive interface for image-based price estimation.

## ⚠️ Limitations

CarInsight AI provides **estimates, not guaranteed market or selling prices**. Factors that may not be fully visible in photos—including mileage, mechanical condition, trim, accident history, location, and market demand—can affect a vehicle's actual value. The reported metrics describe the evaluated dataset and may not generalize to every market or vehicle type.

---

**CarInsight AI — Computer Vision · Deep Learning · Image-Based Price Estimation**
