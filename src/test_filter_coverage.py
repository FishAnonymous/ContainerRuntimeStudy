# # python 3.10-4

# Analyze research question: if the current bugs appears in the current testing oracles and why can they be detected?
# 1. Oracle not covered (designed too simple) 2. Driver performance not promising
# Unit Tests: 6120
# Integration Tests: 1730

import json
import time
import re
import subprocess

root_dir = "{SourceCodeDir}"

mode = "read" # analysis / read

if __name__ == '__main__':
    
    Version = "1.1.4"

    code_dir = f"{root_dir}/Source_Code/runc-{Version}"
    log_dir = f"{root_dir}/Test"
    log_file_path = f"{log_dir}/runc-{Version}-unittest.log"

    function_names = []

    with open(log_file_path, 'r') as lf:
        log_data = lf.readlines()

    for log in log_data:
        if "PASS:" in log:
            function_name = re.search('PASS: (.*) (.*)', log)[1]
            function_names.append(function_name)


        