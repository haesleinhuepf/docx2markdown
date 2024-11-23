def command_line_interface():
    import sys
    from ._docx_to_markdown import docx_to_markdown
    from ._markdown_to_docx import markdown_to_docx

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    if filename1.lower().endswith(".docx") and filename2.lower().endswith(".md"):
        docx_to_markdown(filename1, filename2)
    elif filename1.lower().endswith(".md") and filename2.lower().endswith(".docx"):
        markdown_to_docx(filename1, filename2)
    else:
        print("Conversion not supported. Please provide a .md and a .docx file, or a .docx and a .md file.")
