def get_filename_without_extension(file_name):
    split_value = str(file_name).split(".")
    return ".".join(split_value[:-1])
