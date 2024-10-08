from .languages import get_file_extension

# Conversion Prompt
def conversion_prompt(source_file_data, source_language, target_language):
    target_ext = get_file_extension(target_language)
    prompt = f"""
You are an advanced AI specializing in code conversion. Your task is to convert multiple {source_language} source files to the {target_language} language while preserving their functionality and structure. The source files are provided in a dictionary format where the 'code' key contains the {source_language} source files, and each key represents a filename with its corresponding code.

**Instructions:**
1. Convert all the {source_language} source files provided in the 'code' dictionary to {target_language}.
2. Merge the converted code into a single output file.
3. Ensure that all functionalities from the input source files are available and preserved in the converted target file.
4. Maintain correct syntax, indentation, and code structure in the converted code.
5. Handle `.DAT` files and other external files correctly based on their format. If the file is binary or has a specific encoding, ensure the converted code reads and processes the file using the correct methods.
6. Initialize all variables, properties, and fields appropriately to avoid any nullability warnings (such as CS8618 or CS8600 in C#) or runtime errors. If a property or field is non-nullable, ensure it is initialized with a default value or through a constructor.
7. Do not include any functionality in the converted code that requires user input to terminate the execution unless that functionality is explicitly present in the source code.
8. If certain legacy COBOL functionalities cannot be directly converted due to limitations or differences in the target language, adapt the code appropriately while maintaining the original intent and functionality. Provide a working solution rather than changing the entire functionality unnecessarily.
9. Return only the final converted code as the output, with no additional explanations or metadata.
10. Dont add Readkey() for .NET in the end of the execution.

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