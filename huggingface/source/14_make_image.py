# pip uninstall -y diffusers transformers huggingface-hub
# uv pip install --no-cache-dir -U huggingface-hub transformers diffusers
# uv pip install diffusers transformers accelerate torch

from diffusers import StableDiffusionPipeline
import torch
from diffusers.pipelines.stable_diffusion import safety_checker

model_id = "sd-legacy/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    dtype=torch.float16,
    safety_checker=None # NSFW 필터 제거(유해 이미지를 판단하는 필터)
).to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("image.png")