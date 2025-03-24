import json
import os
import requests

from load_azd_env import load_azd_env

def create_index(index_name:str, ai_search_endpoint:str, ai_search_key:str):
    index_payload = {
    "name": index_name,
    "defaultScoringProfile": None,
    "fields": [
      { "name": "id", "type": "Edm.String", "searchable": True, "filterable": True, "retrievable": True, "stored": True, "sortable": True, "facetable": True, "key": True, "indexAnalyzer": None, "searchAnalyzer": None, "analyzer": "keyword", "dimensions": None, "vectorSearchProfile": None, "vectorEncoding": None, "synonymMaps": []    },
      { "name": "company_name_lucene", "type": "Edm.String", "searchable": True, "filterable": False, "retrievable": True, "stored": True, "sortable": False, "facetable": False, "key": False, "indexAnalyzer": None, "searchAnalyzer": None, "analyzer": "ja.lucene", "dimensions": None, "vectorSearchProfile": None, "vectorEncoding": None, "synonymMaps": []    },
      { "name": "company_name_microsoft", "type": "Edm.String", "searchable": True, "filterable": False, "retrievable": True, "stored": True, "sortable": False, "facetable": False, "key": False, "indexAnalyzer": None, "searchAnalyzer": None, "analyzer": "ja.microsoft", "dimensions": None, "vectorSearchProfile": None, "vectorEncoding": None, "synonymMaps": []    },
      { "name": "company_name_keyword", "type": "Edm.String", "searchable": True, "filterable": False, "retrievable": True, "stored": True, "sortable": False, "facetable": False, "key": False, "indexAnalyzer": None, "searchAnalyzer": None, "analyzer": "keyword", "dimensions": None, "vectorSearchProfile": None, "vectorEncoding": None, "synonymMaps": []    },
    ],
    "scoringProfiles": [],
    "corsOptions": None,
    "suggesters": [],
    "analyzers": [],
    "tokenizers": [],
    "tokenFilters": [],
    "charFilters": [],
    "encryptionKey": None,
    "similarity": {
      "@odata.type": "#Microsoft.Azure.Search.BM25Similarity",
      "k1": None,
      "b": None
    },
    "semantic": None,
    "vectorSearch": {
      "algorithms": [],
      "profiles": [],
      "vectorizers": [],
      "compressions": []
    }
  }
    
    headers = {'Content-Type': 'application/json', 'api-key': ai_search_key}
    params = {'api-version': '2024-07-01'}

    print("Creating index...")

    r = requests.put(ai_search_endpoint + "/indexes/" + index_name,
                    data=json.dumps(index_payload), headers=headers, params=params)
    print(r.status_code)
    print(r.ok)
    print(r.text)

def add_documents(index_name:str, ai_search_endpoint:str, ai_search_key:str, documents:list):
    headers = {'Content-Type': 'application/json', 'api-key': ai_search_key}
    params = {'api-version': '2024-07-01'}
    document_payload = {
        "value": documents
    }

    print("Adding documents...")
    r = requests.post(ai_search_endpoint + "/indexes/" + index_name + "/docs/index",
                      data=json.dumps(document_payload), headers=headers, params=params)
    
    print(r.status_code)
    print(r.ok)
    print(r.text)

if __name__ == "__main__":
    # Load the environment variables from the azd env file
    load_azd_env()

    # Get the environment variables
    ai_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    ai_search_key = os.getenv("AZURE_SEARCH_KEY")

    # Create index
    create_index("test-index", ai_search_endpoint, ai_search_key,)

        # Add sample documents
    sample_documents = [
    {"id": "1", "company_name_lucene": "ワールドブリッジ株式会社", "company_name_microsoft": "ワールドブリッジ株式会社","company_name_keyword": "ワールドブリッジ株式会社"},
    {"id": "2", "company_name_lucene": "有限会社コロンブス・ワールド", "company_name_microsoft": "有限会社コロンブス・ワールド","company_name_keyword": "有限会社コロンブス・ワールド"},
    {"id": "3", "company_name_lucene": "株式会社ワールドスマイル", "company_name_microsoft": "株式会社ワールドスマイル","company_name_keyword": "株式会社ワールドスマイル"},
    {"id": "4", "company_name_lucene": "ワールドミリョクセンター株式会社", "company_name_microsoft": "ワールドミリョクセンター株式会社","company_name_keyword": "ワールドミリョクセンター株式会社"},
    {"id": "5", "company_name_lucene": "特定非営利活動法人ワールド会", "company_name_microsoft": "特定非営利活動法人ワールド会", "company_name_keyword": "特定非営利活動法人ワールド会"},
    {"id": "6", "company_name_lucene": "ワールドワン有限会社", "company_name_microsoft": "ワールドワン有限会社", "company_name_keyword": "ワールドワン有限会社"},
    {"id": "7", "company_name_lucene": "ワールド", "company_name_microsoft": "ワールド", "company_name_keyword": "ワールド"},
    {"id": "8", "company_name_lucene": "1ワールド", "company_name_microsoft": "1ワールド", "company_name_keyword": "1ワールド"},
    {"id": "9", "company_name_lucene": "しおワールド", "company_name_microsoft": "しおワールド", "company_name_keyword": "しおワールド"},
    {"id": "10", "company_name_lucene": "株式会社ワールド", "company_name_microsoft": "株式会社ワールド", "company_name_keyword": "株式会社ワールド"},
    ]
    add_documents("test-index", ai_search_endpoint, ai_search_key, sample_documents)