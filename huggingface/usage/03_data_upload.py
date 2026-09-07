from datasets import load_dataset
# split='train[:200]' : train 의 0~199 까지만 가져와라
dataset = load_dataset('cornell-movie-review-data/rotten_tomatoes',split='train[:200]')
# label, text
# 1. label = 0,1 -> negative, positive
"""
def add_label_text(item):
    if item['label'] == 1:
        item['label_text'] = 'positive'
    else:
        item['label_text'] = 'negative'

    # return item['label_text'] = 'positive' if item['label'] == 1 else 'negative'
    return item
"""
ds = dataset.map(
    lambda item: {'label_text': 'positive' if item['label'] == 1 else 'negative'}
)

# 2. text -> review 컬럼만 변경
ds = ds.rename_column('text','review')

# 3. 10자 미만의 리뷰는 거른다.
# (item) => len(item['review']) >= 10
df = ds.filter(lambda item: len(item['review']) >= 10)

print(f'columns : {ds.column_names}')
print(f'data : {ds[0]}')

# HF 에 업로드
# HF auth login --force (업로드 토큰변경 로그인)
REPO_ID = 'gnl2109/upload_test_ds'
ds.push_to_hub(REPO_ID,split="train")
print(f'업로드 완료 : https://huggingface.co/datasets/{REPO_ID}')

# DOWNLOAD
# dataset = load_dataset(REPO_ID,split='train')
# print(dataset)