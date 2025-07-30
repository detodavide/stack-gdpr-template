from plugins.base_plugin import BasePlugin
from fastapi import FastAPI
from .api.router import router as gdpr_router

class GDPRPlugin(BasePlugin):
    name = "gdpr"
    version = "2.0.0"

    def load(self):
        # GDPR-specific startup logic
        pass

    def register_routes(self):
        self.app.include_router(gdpr_router, prefix="/gdpr", tags=["GDPR"])

    def security_checks(self):
        # Run GDPR compliance checks
        pass

    def unload(self):
        # GDPR-specific cleanup
        pass
