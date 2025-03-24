# 形態素解析調査

各アナライザーの形態素解析の結果は下記です。
`ja.microsoft`と`ja.lucene`は形態素解析を行うため、トークン単位での検索が行われます。
`keyword`はトークン単位での検索が行われないため、全文を使った前方一致や部分一致の検索ができます。

## ja.lucene

```json
{
 "text": "株式会社ワールドスマイル",
 "analyzer": "ja.lucene"
}
```

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/$metadata#Microsoft.Azure.Search.V2024_07_01.AnalyzeResult",
    "tokens": [
        {
            "token": "株式",
            "startOffset": 0,
            "endOffset": 2,
            "position": 0
        },
        {
            "token": "株式会社",
            "startOffset": 0,
            "endOffset": 4,
            "position": 0
        },
        {
            "token": "会社",
            "startOffset": 2,
            "endOffset": 4,
            "position": 1
        },
        {
            "token": "ワールド",
            "startOffset": 4,
            "endOffset": 8,
            "position": 2
        },
        {
            "token": "スマイル",
            "startOffset": 8,
            "endOffset": 12,
            "position": 3
        }
    ]
}
```

## ja.microsoft

```json
{
 "text": "株式会社ワールドスマイル",
 "analyzer": "ja.microsoft"
}
```

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/$metadata#Microsoft.Azure.Search.V2024_07_01.AnalyzeResult",
    "tokens": [
        {
            "token": "株式",
            "startOffset": 0,
            "endOffset": 2,
            "position": 0
        },
        {
            "token": "会社",
            "startOffset": 2,
            "endOffset": 4,
            "position": 1
        },
        {
            "token": "ワールド",
            "startOffset": 4,
            "endOffset": 8,
            "position": 2
        },
        {
            "token": "スマイル",
            "startOffset": 8,
            "endOffset": 12,
            "position": 3
        }
    ]
}
```

## keyword

```json
{
 "text": "株式会社ワールドスマイル",
 "analyzer": "keyword"
}
```

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/$metadata#Microsoft.Azure.Search.V2024_07_01.AnalyzeResult",
    "tokens": [
        {
            "token": "株式会社ワールドスマイル",
            "startOffset": 0,
            "endOffset": 12,
            "position": 0
        }
    ]
}
```

## クエリと結果

前提条件: ja.microsoftやja.luceneを使用すると形態素解析が行われるため、トークン単位での検索が行われます。

もし文章を前方一致検索したい場合は、keywordを使用する必要があります。

今回はkeywordで設定したフィールドを`company_name_keyword`とします。

フィールドの設定例

```json
{
    "name": "company_name_keyword",
    "type": "Edm.String",
    "searchable": true,
    "filterable": false,
    "retrievable": true,
    "stored": true,
    "sortable": false,
    "facetable": false,
    "key": false,
    "analyzer": "keyword",
    "synonymMaps": []
}
```

検索条件を絞らない場合の検索結果は下記の通り

```json
{
  "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
  "@odata.count": 10,
  "value": [
    {
      "@search.score": 1,
      "id": "3",
      "company_name_lucene": "株式会社ワールドスマイル",
      "company_name_microsoft": "株式会社ワールドスマイル",
      "company_name_keyword": "株式会社ワールドスマイル"
    },
    {
      "@search.score": 1,
      "id": "9",
      "company_name_lucene": "しおワールド",
      "company_name_microsoft": "しおワールド",
      "company_name_keyword": "しおワールド"
    },
    {
      "@search.score": 1,
      "id": "2",
      "company_name_lucene": "有限会社コロンブス・ワールド",
      "company_name_microsoft": "有限会社コロンブス・ワールド",
      "company_name_keyword": "有限会社コロンブス・ワールド"
    },
    {
      "@search.score": 1,
      "id": "4",
      "company_name_lucene": "ワールドミリョクセンター株式会社",
      "company_name_microsoft": "ワールドミリョクセンター株式会社",
      "company_name_keyword": "ワールドミリョクセンター株式会社"
    },
    {
      "@search.score": 1,
      "id": "5",
      "company_name_lucene": "特定非営利活動法人ワールド会",
      "company_name_microsoft": "特定非営利活動法人ワールド会",
      "company_name_keyword": "特定非営利活動法人ワールド会"
    },
    {
      "@search.score": 1,
      "id": "7",
      "company_name_lucene": "ワールド",
      "company_name_microsoft": "ワールド",
      "company_name_keyword": "ワールド"
    },
    {
      "@search.score": 1,
      "id": "6",
      "company_name_lucene": "ワールドワン有限会社",
      "company_name_microsoft": "ワールドワン有限会社",
      "company_name_keyword": "ワールドワン有限会社"
    },
    {
      "@search.score": 1,
      "id": "8",
      "company_name_lucene": "1ワールド",
      "company_name_microsoft": "1ワールド",
      "company_name_keyword": "1ワールド"
    },
    {
      "@search.score": 1,
      "id": "1",
      "company_name_lucene": "ワールドブリッジ株式会社",
      "company_name_microsoft": "ワールドブリッジ株式会社",
      "company_name_keyword": "ワールドブリッジ株式会社"
    },
    {
      "@search.score": 1,
      "id": "10",
      "company_name_lucene": "株式会社ワールド",
      "company_name_microsoft": "株式会社ワールド",
      "company_name_keyword": "株式会社ワールド"
    }
  ]
}
```

その上で、以下のようなクエリを実行する。

1. 実現したいこと1：「ワールド～～」（前方一致）だけ抽出したいパターン ※正規表現

検索parameters:

```json
api-version:2024-07-01
search:company_name_keyword:/ワールド.*/
queryType:full
top:10
```

結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "value": [
        {
            "@search.score": 1.0,
            "id": "4",
            "company_name_lucene": "ワールドミリョクセンター株式会社",
            "company_name_microsoft": "ワールドミリョクセンター株式会社",
            "company_name_keyword": "ワールドミリョクセンター株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "7",
            "company_name_lucene": "ワールド",
            "company_name_microsoft": "ワールド",
            "company_name_keyword": "ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "6",
            "company_name_lucene": "ワールドワン有限会社",
            "company_name_microsoft": "ワールドワン有限会社",
            "company_name_keyword": "ワールドワン有限会社"
        },
        {
            "@search.score": 1.0,
            "id": "1",
            "company_name_lucene": "ワールドブリッジ株式会社",
            "company_name_microsoft": "ワールドブリッジ株式会社",
            "company_name_keyword": "ワールドブリッジ株式会社"
        }
    ]
}
```

2. 実現したいこと2：「ワールド～～」（前方一致）だけ抽出したいパターン

検索parameters:

```json
api-version:2024-07-01
search:company_name_keyword:ワールド*
queryType:full
top:10
```

結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "value": [
        {
            "@search.score": 1.0,
            "id": "4",
            "company_name_lucene": "ワールドミリョクセンター株式会社",
            "company_name_microsoft": "ワールドミリョクセンター株式会社",
            "company_name_keyword": "ワールドミリョクセンター株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "7",
            "company_name_lucene": "ワールド",
            "company_name_microsoft": "ワールド",
            "company_name_keyword": "ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "6",
            "company_name_lucene": "ワールドワン有限会社",
            "company_name_microsoft": "ワールドワン有限会社",
            "company_name_keyword": "ワールドワン有限会社"
        },
        {
            "@search.score": 1.0,
            "id": "1",
            "company_name_lucene": "ワールドブリッジ株式会社",
            "company_name_microsoft": "ワールドブリッジ株式会社",
            "company_name_keyword": "ワールドブリッジ株式会社"
        }
    ]
}
```


3. 実現したいこと3：「ワールド～～」、「～～ワールド」（部分一致）だけ抽出したいパターン

検索parameters:

```json
api-version:2024-07-01
search:company_name_keyword:/.*ワールド.*/
queryType:full
top:10
```

結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "value": [
        {
            "@search.score": 1.0,
            "id": "3",
            "company_name_lucene": "株式会社ワールドスマイル",
            "company_name_microsoft": "株式会社ワールドスマイル",
            "company_name_keyword": "株式会社ワールドスマイル"
        },
        {
            "@search.score": 1.0,
            "id": "9",
            "company_name_lucene": "しおワールド",
            "company_name_microsoft": "しおワールド",
            "company_name_keyword": "しおワールド"
        },
        {
            "@search.score": 1.0,
            "id": "2",
            "company_name_lucene": "有限会社コロンブス・ワールド",
            "company_name_microsoft": "有限会社コロンブス・ワールド",
            "company_name_keyword": "有限会社コロンブス・ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "4",
            "company_name_lucene": "ワールドミリョクセンター株式会社",
            "company_name_microsoft": "ワールドミリョクセンター株式会社",
            "company_name_keyword": "ワールドミリョクセンター株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "5",
            "company_name_lucene": "特定非営利活動法人ワールド会",
            "company_name_microsoft": "特定非営利活動法人ワールド会",
            "company_name_keyword": "特定非営利活動法人ワールド会"
        },
        {
            "@search.score": 1.0,
            "id": "7",
            "company_name_lucene": "ワールド",
            "company_name_microsoft": "ワールド",
            "company_name_keyword": "ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "6",
            "company_name_lucene": "ワールドワン有限会社",
            "company_name_microsoft": "ワールドワン有限会社",
            "company_name_keyword": "ワールドワン有限会社"
        },
        {
            "@search.score": 1.0,
            "id": "8",
            "company_name_lucene": "1ワールド",
            "company_name_microsoft": "1ワールド",
            "company_name_keyword": "1ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "1",
            "company_name_lucene": "ワールドブリッジ株式会社",
            "company_name_microsoft": "ワールドブリッジ株式会社",
            "company_name_keyword": "ワールドブリッジ株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "10",
            "company_name_lucene": "株式会社ワールド",
            "company_name_microsoft": "株式会社ワールド",
            "company_name_keyword": "株式会社ワールド"
        }
    ]
}
```


4. 実現したいこと4：「ワールド」「ワイルド」などの「ワ*ルド」だけ抽出したいパターン

検索parameters:

```json
api-version:2024-07-01
search:company_name_keyword:ワ?ルド
queryType:full
top:10
```

結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "value": [
        {
            "@search.score": 1.0,
            "id": "7",
            "company_name_lucene": "ワールド",
            "company_name_microsoft": "ワールド",
            "company_name_keyword": "ワールド"
        }
    ]
}
```

逆に本クエリーをja.luceneで行うと下記のようになる。

検索parameters:

```json
api-version:2024-07-01
search:company_name_lucene:ワ?ルド
queryType:full
top:10
```

結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "value": [
        {
            "@search.score": 1.0,
            "id": "3",
            "company_name_lucene": "株式会社ワールドスマイル",
            "company_name_microsoft": "株式会社ワールドスマイル",
            "company_name_keyword": "株式会社ワールドスマイル"
        },
        {
            "@search.score": 1.0,
            "id": "9",
            "company_name_lucene": "しおワールド",
            "company_name_microsoft": "しおワールド",
            "company_name_keyword": "しおワールド"
        },
        {
            "@search.score": 1.0,
            "id": "2",
            "company_name_lucene": "有限会社コロンブス・ワールド",
            "company_name_microsoft": "有限会社コロンブス・ワールド",
            "company_name_keyword": "有限会社コロンブス・ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "4",
            "company_name_lucene": "ワールドミリョクセンター株式会社",
            "company_name_microsoft": "ワールドミリョクセンター株式会社",
            "company_name_keyword": "ワールドミリョクセンター株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "5",
            "company_name_lucene": "特定非営利活動法人ワールド会",
            "company_name_microsoft": "特定非営利活動法人ワールド会",
            "company_name_keyword": "特定非営利活動法人ワールド会"
        },
        {
            "@search.score": 1.0,
            "id": "7",
            "company_name_lucene": "ワールド",
            "company_name_microsoft": "ワールド",
            "company_name_keyword": "ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "6",
            "company_name_lucene": "ワールドワン有限会社",
            "company_name_microsoft": "ワールドワン有限会社",
            "company_name_keyword": "ワールドワン有限会社"
        },
        {
            "@search.score": 1.0,
            "id": "8",
            "company_name_lucene": "1ワールド",
            "company_name_microsoft": "1ワールド",
            "company_name_keyword": "1ワールド"
        },
        {
            "@search.score": 1.0,
            "id": "1",
            "company_name_lucene": "ワールドブリッジ株式会社",
            "company_name_microsoft": "ワールドブリッジ株式会社",
            "company_name_keyword": "ワールドブリッジ株式会社"
        },
        {
            "@search.score": 1.0,
            "id": "10",
            "company_name_lucene": "株式会社ワールド",
            "company_name_microsoft": "株式会社ワールド",
            "company_name_keyword": "株式会社ワールド"
        }
    ]
}
```

この結果により検索の絞り込みがトークン単位で行われていることがわかります。

ja.microsoftやja.luceneを使用すると、トークン単位での検索が行われるため、形態素解析されたトークンに`ワ?ルド`(ワールド,ワイルド等)が含まれていれば検索にヒットします。

一方、keywordを使用すると、トークン単位での検索が行われないため、`ワ?ルド`(ワールド,ワイルド等)のような合計４文字の文章でかつ上記の条件に合致するものがあれば検索にヒットします。

## まとめ

- アナライザーkeywordを使用すると、トークン単位での検索が行われないため、全文を使った前方一致や部分一致の検索ができます。
- 文章の前方一致などしたい場合はアナライザーをkeywordにする。もし全文一致検索をしたい場合はja.microsoftやja.luceneを使用する使い分けをすることが望ましいと言えます。
