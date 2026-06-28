import inspect
from datetime import datetime
import os
from sqlalchemy import text
from functools import partial
from .Constants import ALL_LEVELS

ENV_LEVEL = ALL_LEVELS.get(os.getenv("LOG_LEVEL", "INFO"), 20)

def _log(engine, message, level="INFO"):
    """Centralized logging function that logs messages to both console and database."""

    if ALL_LEVELS.get(level, 20) < ENV_LEVEL:
        return

    frame = inspect.currentframe()
    frame = frame.f_back if frame is not None else None
        
    if frame:
        source = f"{os.path.basename(frame.f_code.co_filename)}::{frame.f_code.co_name}"
    else:
        source = "unknown"
    

    print(f"[{datetime.now().strftime('%H:%M:%S')}] [{level}] [{source}] {message}")

    try:
        with engine.begin() as conn:
            conn.execute(
                text("SELECT fnc.write_log(:level, :source, :message)"),
                {"level": level, "source": source, "message": message}
            )
    except Exception as e:
        print(f"Logging failed: {e}")

log_info = partial(_log, level="INFO")
log_warning = partial(_log, level="WARNING")
log_debug = partial(_log, level="DEBUG")
log_error = partial(_log, level="ERROR")
