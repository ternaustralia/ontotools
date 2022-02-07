def get_filename_without_extension(file_name):
    split_value = file_name.split(".")
    return ".".join(split_value[:-1])
