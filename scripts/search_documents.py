import os
import requests
import json
import re

from load_azd_env import load_azd_env

# function to sanitize filenames
def sanitize_filename(filename):
    # Remove invalid characters for filenames
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def search_documents(index_name:str, ai_search_endpoint:str, ai_search_key:str, search_text:str,analyzer_name:str,search_type:str):
    headers = {'Content-Type': 'application/json', 'api-key': ai_search_key}
    params = {
        'api-version': '2024-07-01',
        'search': search_text,
        'queryType': 'full',
    }

    # Sanitize the search text to create a valid directory name
    if search_type is not None:
        sanitized_search_text = sanitize_filename(search_type)
        directory = f"samples/{analyzer_name}/{sanitized_search_text}"
    else:
        sanitized_search_text = sanitize_filename(search_text)
        directory = f"samples/{analyzer_name}/{sanitized_search_text}"
    os.makedirs(directory, exist_ok=True)

    # Save input parameters to input.json
    with open(f'{directory}/input.json', 'w') as input_file:
        json.dump(params, input_file, ensure_ascii=False, indent=4)

    print(f"Searching for '{search_text}'...")
    r = requests.get(ai_search_endpoint + "/indexes/" + index_name + "/docs", headers=headers, params=params)
    
    print(r.status_code)
    print(r.ok)
    response_json = r.json()
    print(response_json)

    # Save output JSON to output.json
    with open(f'{directory}/output.json', 'w') as output_file:
        json.dump(response_json, output_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Load the environment variables from the azd env file
    load_azd_env()

    # Get the environment variables
    ai_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    ai_search_key = os.getenv("AZURE_SEARCH_KEY")

    # Search for documents
    print("Searching for documents...")
    print("analyzer keyword:")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_keyword:/ワールド.*/", "keyword","前方一致_正規表現")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_keyword:ワールド*", "keyword","前方一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_keyword:/.*ワールド.*/", "keyword","部分一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_keyword:ワ?ルド", "keyword","部分抽出_ワ?ルド")
    print("analyzer ja.lucene:")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_lucene:/ワールド.*/", "ja.lucene", "前方一致_正規表現")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_lucene:ワールド*", "ja.lucene", "前方一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_lucene:/.*ワールド.*/", "ja.lucene", "部分一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_lucene:ワ?ルド", "ja.lucene", "部分抽出_ワ?ルド")
    print("analyzer ja.microsoft:")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_microsoft:/ワールド.*/", "ja.microsoft", "前方一致_正規表現")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_microsoft:ワールド*", "ja.microsoft", "前方一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_microsoft:/.*ワールド.*/", "ja.microsoft", "部分一致")
    search_documents("test-index", ai_search_endpoint, ai_search_key, "company_name_microsoft:ワ?ルド", "ja.microsoft", "部分抽出_ワ?ルド")