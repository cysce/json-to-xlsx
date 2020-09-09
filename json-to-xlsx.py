import pandas as pd
import sys

if len(sys.argv) != 3:
    print ("\nUsage: python json-to-xls.py <json_in_file_path> <xls_out_file_path>\n")
else:
    #Reading arguments
    json_file_path = sys.argv[1]
    xlsx_file_path = sys.argv[2]
    sheetname = "sheet1"
    
    #checking if the output has extension with it
    if ".xlsx" not in xlsx_file_path:
        xlsx_file_path = xlsx_file_path+".xlsx"
    
    #normalize the json
    df = pd.read_json(json_file_path)   
    df.to_excel(xlsx_file_path)

    print ("File XLSX created")
