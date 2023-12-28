import pandas as pd

df = pd.read_csv('conf.csv')

# DataFrame을 마크다운 문자열로 변환합니다.
markdown_str = df.to_markdown(index=False)

print(markdown_str)

