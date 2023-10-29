import os
import yaml


class CreateSampleConfig:
    @staticmethod
    def get_config_path():
        home_dir = os.path.expanduser("~")
        config_dir = os.path.join(home_dir, "sample", "configs")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        return config_dir


    @staticmethod
    def create_default_config(db_type):
        default_configs = {
            "mysql": {
                "host": "localhost",
                "user": "test_user",
                "password": "test_password",
                "database": "test_db",
            },
            "postgresql": {
                "host": "localhost",
                "user": "test_user",
                "password": "test_password",
                "database": "test_db",
            },
            "mssql": {
                "host": "localhost",
                "user": "test_user",
                "password": "test_password",
                "database": "test_db",
            },
        }
        config = default_configs.get(db_type)
        if config:
            config_path = os.path.join(
                CreateSampleConfig.get_config_path(), f"{db_type}_config.yaml"
            )
            with open(config_path, "w") as f:
                yaml.dump(config, f)


    @staticmethod
    def get_config(db_type):
        config_dir = CreateSampleConfig.get_config_path()
        config_path = os.path.join(config_dir, f"{db_type}_config.yaml")
        if not os.path.exists(config_path):
            CreateSampleConfig.create_default_config(db_type)
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return config
