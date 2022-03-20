from yaml import load, FullLoader


class Configuration:

    @staticmethod
    def read():
        path = "resources/configuration/server_configuration.yaml"
        with open(path) as configuration_file:
            configuration = load(configuration_file, Loader=FullLoader)
        return configuration
