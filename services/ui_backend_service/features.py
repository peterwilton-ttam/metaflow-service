import os


FEATURE_PREFETCH_DISABLE = os.environ.get("FEATURE_PREFETCH_DISABLE", 0) == "1"
FEATURE_CACHE_DISABLE = os.environ.get("FEATURE_CACHE_DISABLE", 0) == "1"
FEATURE_S3_DISABLE = os.environ.get("FEATURE_S3_DISABLE", 0) == "1"
FEATURE_REFINE_DISABLE = os.environ.get("FEATURE_REFINE_DISABLE", 0) == "1"

FEATURE_PREFETCH_ENABLE = not FEATURE_PREFETCH_DISABLE
FEATURE_CACHE_ENABLE = not FEATURE_CACHE_DISABLE
FEATURE_S3_ENABLE = not FEATURE_S3_DISABLE
FEATURE_REFINE_ENABLE = not FEATURE_REFINE_DISABLE

FEATURE_WS_DISABLE = os.environ.get("FEATURE_WS_DISABLE", 0) == "1"
FEATURE_DB_LISTEN_DISABLE = os.environ.get("FEATURE_DB_LISTEN_DISABLE", 0) == "1"
FEATURE_HEARTBEAT_DISABLE = os.environ.get("FEATURE_HEARTBEAT_DISABLE", 0) == "1"

FEATURE_WS_ENABLE = not FEATURE_WS_DISABLE
FEATURE_DB_LISTEN_ENABLE = not FEATURE_DB_LISTEN_DISABLE
FEATURE_HEARTBEAT_ENABLE = not FEATURE_HEARTBEAT_DISABLE

if FEATURE_S3_DISABLE:
    os.environ["AWS_ACCESS_KEY_ID"] = "None"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "None"
    os.environ["AWS_DEFAULT_REGION"] = "None"
