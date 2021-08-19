from __future__ import annotations

import json
import os
from typing import Dict, List

from monkey_island.cc.environment.user_creds import UserCreds
from monkey_island.cc.resources.auth.auth_user import User
from monkey_island.cc.resources.auth.user_store import UserStore


class EnvironmentConfig:
    def __init__(self, file_path):
        self._server_config_path = os.path.expanduser(file_path)  # SUC-7
        self.server_config = None
        self.deployment = None
        self.user_creds = None
        self.aws = None

        self._load_from_file(self._server_config_path)

    def _load_from_file(self, file_path):
        # SUC-14: dict_data in SUC-13 is obtained from here which is the server config path (SUC-7 to SUC-10)
        file_path = os.path.expanduser(file_path)

        with open(file_path, "r") as f:
            config_content = f.read()

        self._load_from_json(config_content)

    def _load_from_json(self, config_json: str) -> EnvironmentConfig:
        data = json.loads(config_json)
        self._load_from_dict(data["environment"])

    def _load_from_dict(self, dict_data: Dict):
        aws = dict_data["aws"] if "aws" in dict_data else None

        self.server_config = dict_data["server_config"]
        self.deployment = dict_data["deployment"]
        self.user_creds = _get_user_credentials_from_config(dict_data)  # SUC-13
        self.aws = aws

    def save_to_file(self):
        with open(self._server_config_path, "r") as f:
            config = json.load(f)

        config["environment"] = self.to_dict()  # SUC-4

        with open(self._server_config_path, "w") as f:  # SUC-6: opens server config file path
            f.write(json.dumps(config, indent=2))  # SUC-11: saves config to server config file

    def to_dict(self) -> Dict:
        config_dict = {
            "server_config": self.server_config,
            "deployment": self.deployment,
        }
        if self.aws:
            config_dict.update({"aws": self.aws})
        config_dict.update(self.user_creds.to_dict())  # SUC-5: creds added to config
        return config_dict

    def add_user(self, credentials: UserCreds):
        self.user_creds = credentials
        self.save_to_file()  # SUC-3
        UserStore.set_users(self.get_users())

    def get_users(self) -> List[User]:
        auth_user = self.user_creds.to_auth_user()
        return [auth_user] if auth_user else []


def _get_user_credentials_from_config(dict_data: Dict):
    # SUC-12: and every time the island is started, the config is set up
    username = dict_data.get("user", "")
    password_hash = dict_data.get("password_hash", "")

    return UserCreds(username, password_hash)
