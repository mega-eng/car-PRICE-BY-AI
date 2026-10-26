# 🚗 CarInsight AI
### A car's value is more than its name. Let AI see it.

**CarInsight AI** is an AI-powered vehicle price estimation project built around a simple question: *Can a model estimate a car's value from its images alone?*

Unlike conventional approaches that depend on manually supplied details such as make, model, year, or mileage, **CarInsight AI's core pricing model learns from visual information in vehicle photos**. It uses computer vision and a multi-model prediction pipeline to estimate a price in Saudi Riyals (SAR).

🌐 **[Launch CarInsight AI](https://kilometers-defined-conscious-routes.trycloudflare.com/)** · **[View Source Code](https://github.com/mega-eng/car-PRICE-BY-AI)**

> **Live demo note:** The demo uses a temporary hosting link, which may change or become unavailable when the hosting session restarts.

---

## 🔍 What Makes CarInsight AI Different?

### No Make. No Model. No Mileage. Just Images.

The core pricing model does not need the vehicle's make, model name, year, or mileage as prediction inputs. Instead, it analyzes visual patterns learned from vehicle images to estimate a price.

This makes the project an exploration of **image-based price estimation**: using computer vision to infer value from how a vehicle looks, rather than relying on its name or manually entered specifications.

- 🖼️ **Image-based estimation** — vehicle photos are the core input to the pricing model.
- 🧠 **Visual feature extraction** — uses DINOv2 at multiple model sizes alongside CLIP.
- 🗳️ **Multi-model voting** — combines predictions from three models.
- 📊 **Prediction intervals** — provides an estimated price with a range to communicate uncertainty.

---

## 📈 Evaluation Results

Evaluated on **345 vehicle listings the model had not seen during training**.

| Metric | Result |
|---|---:|
| Coefficient of determination (R²) | **0.848** |
| Median relative error | **10.7%** |
| Predictions within ±20% of actual price | **76%** |
| Predictions within ±30% of actual price | **88%** |
| Actual prices covered by the nominal 80% prediction interval | **80.9%** |
| Actual prices covered by the nominal 90% prediction interval | **92.2%** |

For comparison, a simple baseline estimate had a median relative error of **41.6%**, compared with **10.7%** for CarInsight AI on the reported evaluation.

*These figures describe the evaluated test set. R² is a statistical performance metric, not a claim of 84.8% prediction accuracy.*

---

## 🧠 How It Works

1. **Vehicle photos** — process images from a vehicle listing.
2. **Visual feature extraction** — extract image features using DINOv2 at three model sizes and CLIP.
3. **Image augmentation** — include flipped views to enrich the visual information.
4. **Model voting** — combine predictions from three models.
5. **Price and range** — return an estimated price in SAR and a prediction interval.

---

## 📁 Project Data & Model Pipeline

- **2,293** vehicle listings
- **11,199** vehicle images
- **345** unseen test listings
- **4** visual networks
- **3** models in the voting stage

## 🛠️ Technologies

- Python
- Machine Learning
- Computer Vision
- DINOv2
- CLIP
- Gradio

## 🎯 Project Objectives

- Explore vehicle price estimation from images rather than manually entered vehicle specifications.
- Evaluate visual feature extraction and multi-model prediction approaches.
- Test performance on listings not seen during training.
- Represent uncertainty with prediction intervals instead of presenting estimates as guaranteed prices.
- Deliver an interactive interface for experimenting with image-based price estimation.

## ⚠️ Limitations

CarInsight AI provides **estimates, not guaranteed market or selling prices**. Actual value can also depend on factors that may not be fully visible in images, including mileage, mechanical condition, trim, accident history, location, and current market demand. The reported results should not be interpreted as a guarantee for every vehicle.

---

**CarInsight AI — Computer Vision · Machine Learning · Image-Based Price Estimation**
