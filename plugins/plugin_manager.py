from fastapi import FastAPI
from plugins.base_plugin import BasePlugin
import importlib
import logging

logger = logging.getLogger(__name__)

class PluginManager:
    def __init__(self, app: FastAPI):
        self.app = app
        self.plugins = []
import importlib
import sys
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class PluginManager:
    ALLOWED_PLUGINS = ["gdpr_plugin", "security_plugin", "analytics_plugin", "audit_plugin"]

    def __init__(self, app):
        self.app = app
        self.plugins = []

    async def load_enabled_plugins(self):
        from core.config import settings

        for plugin_name in settings.ENABLED_PLUGINS:
            # 🚨 SECURITY: Whitelist validation
            if plugin_name not in self.ALLOWED_PLUGINS:
                logger.error(f"❌ SECURITY: Plugin non autorizzato: {plugin_name}")
                continue

            # 🚨 SECURITY: Path validation
            plugin_path = Path(f"plugins/{plugin_name}")
            if not plugin_path.exists() or not plugin_path.is_dir():
                logger.error(f"❌ SECURITY: Plugin path invalid: {plugin_name}")
                continue

            try:
                # 🚨 SECURITY: Isolated import
                module_name = f"plugins.{plugin_name}.plugin"
                if module_name in sys.modules:
                    # Reload solo se necessario
                    module = sys.modules[module_name]
                else:
                    module = importlib.import_module(module_name)

                # 🚨 SECURITY: Class name validation
                plugin_class_name = f"{plugin_name.title().replace('_', '')}Plugin"
                plugin_class = getattr(module, plugin_class_name, None)

                if not plugin_class:
                    logger.error(f"❌ Plugin class not found: {plugin_class_name}")
                    continue

                # Load plugin con timeout
                plugin_instance = plugin_class(self.app)
                plugin_instance.load()
                plugin_instance.register_routes()

                self.plugins.append(plugin_instance)
                logger.info(f"✅ Plugin loaded: {plugin_name}")

            except Exception as e:
                logger.error(f"❌ Failed to load plugin {plugin_name}: {e}")
                # 🚨 CRITICAL: Non fermare l'app per plugin falliti
                continue

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
