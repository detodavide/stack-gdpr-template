from plugins.base_plugin import BasePlugin
from fastapi import FastAPI

class SecurityPlugin(BasePlugin):
    name = "security"
    version = "1.0.0"

    def load(self):
        pass

    def register_routes(self):
        pass

    def security_checks(self):
        pass

    def unload(self):
        pass
