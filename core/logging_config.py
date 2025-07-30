import logging
import json
import sys
from datetime import datetime
from core.config import settings

class StructuredFormatter(logging.Formatter):
    """HOTFIX: Logging strutturato per monitoring."""
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        if hasattr(record, 'request_id'):
            log_entry["request_id"] = record.request_id
        if hasattr(record, 'user_id'):
            log_entry["user_id"] = record.user_id
        if hasattr(record, 'plugin'):
            log_entry["plugin"] = record.plugin
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)

def setup_logging():
    """HOTFIX: Setup logging sicuro."""
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredFormatter())
    if settings.ENVIRONMENT == "production":
        logging.basicConfig(level=logging.WARNING, handlers=[handler])
    else:
        logging.basicConfig(level=logging.INFO, handlers=[handler])
    logging.getLogger("plugins.gdpr_plugin").setLevel(logging.INFO)
    logging.getLogger("plugins.security_plugin").setLevel(logging.WARNING)
    return logging.getLogger(__name__)
