"""CarInsight AI - live demo (Gradio). Upload car photos -> estimated price + 80%/90% range."""
import functools
import gradio as gr
import joblib
import numpy as np
import torch
import torchvision.transforms as T
from PIL import Image

import image_to_price_v2 as m

BUNDLE = joblib.load("bundle.joblib")
NEED = sorted({b for c in BUNDLE["components"] for b in c["backbones"]})
DEV = "cuda" if torch.cuda.is_available() else "cpu"
MEANS = {"hub": ((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
         "clip": ((0.4815, 0.4578, 0.4082), (0.2686, 0.2613, 0.2758))}


@functools.lru_cache(maxsize=None)
def encoder(name):  # load each backbone once, keep it in memory
    kind, ident = m.BACKBONES[name]
    if kind == "hub":
        enc = torch.hub.load("facebookresearch/dinov2", ident)
        fwd = lambda x: enc(x)
    else:
        from transformers import CLIPModel
        enc = CLIPModel.from_pretrained(ident)
        fwd = lambda x: enc.vision_model(pixel_values=x).pooler_output
    mean, std = MEANS[kind]
    tf = T.Compose([T.Resize((224, 224), interpolation=T.InterpolationMode.BICUBIC), T.ToTensor(), T.Normalize(mean, std)])
    return enc.eval().to(DEV), fwd, tf


def embed(name, imgs):
    _, fwd, tf = encoder(name)
    x = torch.stack([tf(i) for i in imgs]).to(DEV)
    with torch.no_grad():
        E = fwd(x).float().cpu().numpy()
        Ef = fwd(torch.flip(x, dims=[3])).float().cpu().numpy()
    return m.l2norm(E), m.l2norm(Ef)


def predict(files):
    if not files:
        return "ارفع صورة واحدة على الأقل."
    paths = [f if isinstance(f, str) else f.name for f in files][:8]
    imgs = [Image.open(p).convert("RGB") for p in paths]
    emb = {n: embed(n, imgs) for n in NEED}
    lp = float(np.mean([m.comp_logpred(c, emb) for c in BUNDLE["components"]]))
    q = BUNDLE["q"]
    f = lambda v: f"{np.exp(v):,.0f}"
    return (f"## السعر المقدّر: {f(lp)} ر.س\n\n"
            f"- نطاق 80%: {f(lp + q['lo80'])} – {f(lp + q['hi80'])} ر.س\n"
            f"- نطاق 90%: {f(lp + q['lo90'])} – {f(lp + q['hi90'])} ر.س\n\n"
            f"(من {len(imgs)} صورة. التقدير من الصور فقط.)")


demo = gr.Interface(fn=predict,
                    inputs=gr.File(label="صور السيارة (من 1 إلى 8)", file_count="multiple", file_types=["image"]),
                    outputs=gr.Markdown(), title="CarInsight AI — تقدير السعر من الصورة",
                    description="ارفع صور سيارة وسيقدّر المودل سعرها بالريال مع نطاق محتمل.", flagging_mode="never")
if __name__ == "__main__":
    demo.launch()
