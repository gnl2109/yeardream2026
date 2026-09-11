import os
import shutil
import traceback

from transformers import pipeline

# window 경고메세지 지우기(선택사항)
os.environ["HF_HUB_DISABLE_SYMLINK_WARNING"] = "1"

# 이미지 분류
# uv pip install pillow torchvision
vision = pipeline(model="google/vit-base-patch16-224")

def fileUpload(file,path):
    success = -1
    try:
        with open(path,'wb') as file_obj:
            shutil.copyfileobj(file,file_obj)
        success = 1
    except Exception as e:
        print(e) # 에러 메세지
        print(traceback.format_exc()) # 에러내용 상세 출력(개발용)
    return success

def class_img(img_path):
    result = vision(img_path)
    print(result)
    if os.path.exists(img_path):
        os.remove(img_path)

    return result[0]