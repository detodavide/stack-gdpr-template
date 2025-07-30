from fastapi import FastAPI
from plugins.base_plugin import BasePlugin
import importlib
import logging

logger = logging.getLogger(__name__)

class PluginManager:
    def __init__(self, app: FastAPI):
        self.app = app
        self.plugins = []

    async def load_enabled_plugins(self):
        # Example: load plugins from settings.ENABLED_PLUGINS
        from core.config import settings
        for plugin_name in settings.ENABLED_PLUGINS:
            try:
                module = importlib.import_module(f"plugins.{plugin_name}.plugin")
                plugin_class = getattr(module, "GDPRPlugin", None) or getattr(module, "SecurityPlugin", None)
                if plugin_class:
                    plugin_instance = plugin_class(self.app)
                    plugin_instance.load()
                    plugin_instance.register_routes()
                    plugin_instance.security_checks()
                    self.plugins.append(plugin_instance)
                    logger.info(f"✅ Loaded plugin: {plugin_name}")
            except Exception as e:
                logger.error(f"❌ Failed to load plugin {plugin_name}: {e}")

    async def cleanup(self):
        for plugin in self.plugins:
            plugin.unload()
        logger.info("🔌 All plugins unloaded.")
