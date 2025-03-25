# 概要

AI Searchでの数値での範囲指定方法について記載します。
数値の範囲指定は、`$filter`クエリパラメータを使用して行います。

## テストデータとフィールドの設定

テストフィールドは以下のように設定されています。

employee_countフィールドは数値型で、フィルタリング可能なフィールドとして設定されています。

```json
{
    "@odata.etag": "\"0x8DD6B654753EDE5\"",
  "name": "test-index",
  "fields": [
      {
          "name": "id",
      "type": "Edm.String",
      "searchable": true,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": true,
      "facetable": true,
      "key": true,
      "analyzer": "keyword",
      "synonymMaps": []
    },
    {
        "name": "company_name_lucene",
      "type": "Edm.String",
      "searchable": true,
      "filterable": false,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": false,
      "analyzer": "ja.lucene",
      "synonymMaps": []
    },
    {
        "name": "company_name_microsoft",
      "type": "Edm.String",
      "searchable": true,
      "filterable": false,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": false,
      "analyzer": "ja.microsoft",
      "synonymMaps": []
    },
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
    },
    {
        "name": "employee_count",
      "type": "Edm.Int32",
      "searchable": false,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": true,
      "facetable": true,
      "key": false,
      "synonymMaps": []
    }
  ],
  "scoringProfiles": [],
  "suggesters": [],
  "analyzers": [],
  "normalizers": [],
  "tokenizers": [],
  "tokenFilters": [],
  "charFilters": [],
  "similarity": {
      "@odata.type": "#Microsoft.Azure.Search.BM25Similarity"
  },
  "vectorSearch": {
      "algorithms": [],
    "profiles": [],
    "vectorizers": [],
    "compressions": []
  }
}
`````

テストデータ:

```json
{"id": "1", "company_name_lucene": "ワールドブリッジ株式会社", "company_name_microsoft": "ワールドブリッジ株式会社","company_name_keyword": "ワールドブリッジ株式会社", "employee_count": 100},
{"id": "2", "company_name_lucene": "有限会社コロンブス・ワールド", "company_name_microsoft": "有限会社コロンブス・ワールド","company_name_keyword": "有限会社コロンブス・ワールド", "employee_count": 50},
{"id": "3", "company_name_lucene": "株式会社ワールドスマイル", "company_name_microsoft": "株式会社ワールドスマイル","company_name_keyword": "株式会社ワールドスマイル", "employee_count": 200},
{"id": "4", "company_name_lucene": "ワールドミリョクセンター株式会社", "company_name_microsoft": "ワールドミリョクセンター株式会社","company_name_keyword": "ワールドミリョクセンター株式会社", "employee_count": 150},
{"id": "5", "company_name_lucene": "特定非営利活動法人ワールド会", "company_name_microsoft": "特定非営利活動法人ワールド会", "company_name_keyword": "特定非営利活動法人ワールド会", "employee_count": 75},
{"id": "6", "company_name_lucene": "ワールドワン有限会社", "company_name_microsoft": "ワールドワン有限会社", "company_name_keyword": "ワールドワン有限会社", "employee_count": 120},
{"id": "7", "company_name_lucene": "ワールド", "company_name_microsoft": "ワールド", "company_name_keyword": "ワールド", "employee_count": 80},
{"id": "8", "company_name_lucene": "1ワールド", "company_name_microsoft": "1ワールド", "company_name_keyword": "1ワールド", "employee_count": 60},
{"id": "9", "company_name_lucene": "しおワールド", "company_name_microsoft": "しおワールド", "company_name_keyword": "しおワールド", "employee_count": 90},
{"id": "10", "company_name_lucene": "株式会社ワールド", "company_name_microsoft": "株式会社ワールド", "company_name_keyword": "株式会社ワールド", "employee_count": 110},
```

## クエリの実行

数値の範囲指定は、`$filter`クエリパラメータを使用して行います。

クエリの例は以下の通りです。

```bash
api-version:2024-07-01
search:*
queryType:simple
$filter:employee_count ge 100 and employee_count le 200
top:10
$count:true
```

実行結果:

```json
{
    "@odata.context": "https://srch-guegkrklzq5jk.search.windows.net/indexes('test-index')/$metadata#docs(*)",
    "@odata.count": 5,
    "value": [
        {
            "@search.score": 1.0,
            "id": "3",
            "company_name_lucene": "株式会社ワールドスマイル",
            "company_name_microsoft": "株式会社ワールドスマイル",
            "company_name_keyword": "株式会社ワールドスマイル",
            "employee_count": 200
        },
        {
            "@search.score": 1.0,
            "id": "4",
            "company_name_lucene": "ワールドミリョクセンター株式会社",
            "company_name_microsoft": "ワールドミリョクセンター株式会社",
            "company_name_keyword": "ワールドミリョクセンター株式会社",
            "employee_count": 150
        },
        {
            "@search.score": 1.0,
            "id": "6",
            "company_name_lucene": "ワールドワン有限会社",
            "company_name_microsoft": "ワールドワン有限会社",
            "company_name_keyword": "ワールドワン有限会社",
            "employee_count": 120
        },
        {
            "@search.score": 1.0,
            "id": "1",
            "company_name_lucene": "ワールドブリッジ株式会社",
            "company_name_microsoft": "ワールドブリッジ株式会社",
            "company_name_keyword": "ワールドブリッジ株式会社",
            "employee_count": 100
        },
        {
            "@search.score": 1.0,
            "id": "10",
            "company_name_lucene": "株式会社ワールド",
            "company_name_microsoft": "株式会社ワールド",
            "company_name_keyword": "株式会社ワールド",
            "employee_count": 110
        }
    ]
}
```

今回の場合100以上200以下のデータが取得できています。
`$filter`クエリパラメータを使用することで、数値の範囲指定が可能です。

### 演算子

数値の範囲指定には、以下の演算子を使用します。
等価演算子:

`eq`: フィールドが定数値と等しいかどうかをテストします  
`ne`: フィールドが定数値と等しくないかどうかをテストします  

### 範囲演算子:

`gt`: フィールドが定数値より大きいかどうかをテストします  
`lt`: フィールドが定数値より小さいかどうかをテストします  
`ge`: フィールドが定数値以上であるかどうかをテストします  
`le`: フィールドが定数値以下であるかどうかをテストします  

## 参考

- [Azure AI Search - $filter](https://learn.microsoft.com/ja-jp/rest/api/searchservice/search-documents?tabs=rest-2024-07-01#filter)

- [Azure AI Search での OData $filter 構文](https://learn.microsoft.com/ja-jp/azure/search/search-query-odata-filter)

- [Azure AI Search の OData 比較演算子 - eq、 ne、 gt、 lt、ge、le](https://learn.microsoft.com/ja-jp/azure/search/search-query-odata-comparison-operators)

- [クエリの例](https://learn.microsoft.com/ja-jp/azure/search/search-query-simple-examples#example-5-range-filters)