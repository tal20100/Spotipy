def config_read_path():
    filename = "paths.config"
    contents = open(filename).read()
    config = eval(contents)
    return config['loggers_path']
