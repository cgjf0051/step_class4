# step_class4

## 課題内容

実行時間がかなりかかるのと、課題内容をきちんと理解できていないのか必要なものが出力できてないような気がします、、、


## 準備

[wikipedia_data.zip](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view?usp=sharing) をダウンロードして解凍し、以下のようなディレクトリ構成にしてください。

```
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── .gitignore
├── README.md
└── wiki_search.py
```

## 注意
・pages/linksの読み込みに時間がかかります．
・出力はTrue/Falseが返されるようになっています.
・pathに通った経路のidが格納されています

### 実行方法

#### Python

テスト環境: Python 3.9.2

```shell
python3 wiki_search.py
```
