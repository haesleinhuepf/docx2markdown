def command_line_interface():
    import sys
    from ._convert import convert
    docx_filename = sys.argv[1]
    md_filename = sys.argv[2]

    convert(docx_filename, md_filename)
