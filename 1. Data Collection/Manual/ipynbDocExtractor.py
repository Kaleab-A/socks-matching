import json
import nbformat


def extract_markdown_and_code_outputs(ipynb_file_path):
    with open(ipynb_file_path, "r", encoding="utf-8") as file:
        nb = nbformat.read(file, as_version=4)

    extracted_data = []

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            extracted_data.append({"cell_type": "markdown", "content": cell.source})

        elif cell.cell_type == "code":
            # Extract only the outputs
            outputs = cell.outputs

            # Process each output
            for output in outputs:
                if "data" in output:
                    for mime_type, content in output["data"].items():
                        if mime_type.startswith("image/"):
                            # For images, content is usually base64-encoded
                            extracted_data.append(
                                {
                                    "cell_type": "code_output",
                                    "mime_type": mime_type,
                                    "content": content,
                                }
                            )

    return extracted_data


def render_to_markdown(extracted_data):
    initFile = open("README.md", "r", encoding="utf-8")
    initContent = ""

    startNow = False
    for line in initFile.readlines():
        if line == "---\n":
            startNow = True
        elif startNow:
            initContent += line
    initFile.close()

    with open("README.md", "w", encoding="utf-8") as md_file:
        # Iterate through the extracted data
        # for item in extracted_data:
        #     if item["cell_type"] == "markdown":
        #         # Write markdown content directly
        #         md_file.write(item["content"] + "\n\n")
        #     elif item["cell_type"] == "code_output":
        #         if item.get("mime_type", "").startswith("image/"):
        #             # Handle image output
        #             img_data = item["content"]
        #             # Embed image directly using a data URI
        #             md_file.write(
        #                 f"![Figure](data:{item['mime_type']};base64,{img_data})\n\n"
        #             )
        #         else:
        #             # Handle text output
        #             md_file.write(f"```\n{item['content']}\n```\n\n")
        md_file.write("---\n")
        md_file.write("---\n")
        md_file.write(initContent)


# Use the function with the path to your extracted data
render_to_markdown(
    extract_markdown_and_code_outputs("1. Data Collection/Manual/preprocess.ipynb")
)
