import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import time

root_dir = "{SourceCodeDir}"

mode = "Sample"

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

key_words = ["fix", "defect", "error", "bug", "issue", "mistake", "incorrect", "fault",  "flaw"]

if __name__ == '__main__':

    with open(f'{root_dir}/config.json', 'r') as jf:
        config_data = json.load(jf)

    project_name = config_data['project_name']
    query_type = config_data['query_type']

    # Read filtered json 
    with open(f"{root_dir}/{mode}/{query_type}_{project_name}_filter.json", 'r') as rf:
        data = json.load(rf)

    # Read Google doc excel
    credentials = ServiceAccountCredentials.from_json_keyfile_name(f"{root_dir}/google_api.json", scopes)
    file = gspread.authorize(credentials)

    sheet = file.open("Container_Study_Results_Revised")
    
    #########################################
    #### Remember to Change this Config #####
    sheet_id = config_data['google_doc_sheet']
    worksheet = sheet.get_worksheet(sheet_id-1)
    
    # time.sleep(19999)

    # selectedsheet = sheet.sheet1 # For runc #
    # print(f'Read Google Doc Sheet {sheet_id} Successful')
    #########################################

    # Process with each commit  
    
    for idx, commit_data in enumerate(data):
        sha_to_update = commit_data['sha']
        change_to_update = commit_data['changed_files']

        # sha column
        doc_sha_pos = f"B{idx+2}"
        doc_changed_pos = f"G{idx+2}"
        worksheet.update(doc_sha_pos, sha_to_update)
        worksheet.update(doc_changed_pos, str(change_to_update))
        print(f"update commit {idx} OK")
        time.sleep(1.5)