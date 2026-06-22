import inspect
from datetime import datetime
import os
from sqlalchemy import text
from functools import partial

def _log(engine, message, level="INFO"):
    """Centralized logging function that logs messages to both console and database."""
    frame = inspect.currentframe()
    frame = frame.f_back if frame is not None else None
        
    if frame:
        filename = os.path.basename(frame.f_code.co_filename)
    else:
        filename = "unknown"
    

    print(f"[{datetime.now().strftime('%H:%M:%S')}] [{level}] [{filename}] {message}")

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO system_logs (timestamp, level, function, message) "
                 "VALUES (:ts, :lvl, :fnc, :msg)"),
            {"ts": datetime.now(), "lvl": level, "fnc": filename, "msg": message}
        )
        conn.commit()

log_info = partial(_log, level="INFO")
log_warning = partial(_log, level="WARNING")
log_debug = partial(_log, level="DEBUG")
log_error = partial(_log, level="ERROR")