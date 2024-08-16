from .languages import get_file_extension

# Conversion Prompt
def conversion_prompt(source_file_data, source_language, target_language):
    print("source_file_data /prompt.py : ",source_file_data)
    print("source_language /prompt.py : ",source_language)
    print("target_language /prompt.py : ",target_language)
    target_ext = get_file_extension(target_language)
    prompt = f"""
You are an advanced AI specializing in code conversion. Your task is to convert multiple {source_language} source files to the {target_language} language while preserving their functionality and structure. The source files are provided in a dictionary format where the 'code' key contains the COBOL source files, and each key represents a filename with its corresponding code. The 'external_files' key lists the associated external files such as datasets and database files, but you do not need to include these in your output.

**Instructions:**
1. Convert each COBOL source file within the 'code' dictionary to {target_language}.
2. Ensure that the functionality is fully preserved in the converted code.
3. Maintain correct syntax, indentation, and code structure in the converted code.
4. Escape all strings in the output to be JSON-compliant. Specifically, ensure that all double quotes (`"`) inside strings are properly escaped with a backslash (`\\`).
5. Validate that the output is a well-formed JSON object before returning it.
6. If any external references (datasets, database files) are present in the source code, ensure equivalent handling in the target code. However, do not include the 'external_files' key in your response.
7. If certain legacy COBOL functionalities cannot be directly converted due to the limitations or differences in the target language, adapt the code appropriately while maintaining the original intent and functionality. Provide a working solution rather than changing the entire functionality unnecessarily.
8. Return the converted files in the same dictionary format with a 'code' key. Each key should represent the filename with the {target_ext} extension and its corresponding converted code as the value.

**Example Response Format:**
{{
    'code': {{
        'main.{target_ext}': 'code for main.{target_ext} file',
        'subprogram1.{target_ext}': 'code for subprogram1.{target_ext} file',
        'subprogram2.{target_ext}': 'code for subprogram2.{target_ext} file'
    }}
}}

Here is the source file data for conversion:

{source_file_data}
"""

    return prompt


# Accuracy Prompt
def accuracy_prompt(source_language, source_output, target_language, target_output):
    prompt = f"""Evaluate and compare the outputs generated by {source_language} and {target_language} code, focusing solely on the accuracy of the data values. Ensure there are no alterations, and return the accuracy as a percentage out of 100. The accuracy is based on the values present in output 1 and output 2. The accuracy is not based on the trailing spaces within the output.

    \nFor example, "Accuracy : 90.42%"

Below is the output of {source_language} code:

{source_output}

Below is the output of {target_language} code:

{target_output}

"""
    return prompt