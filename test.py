import os

k = os.environ.get("ANTHROPIC_API_KEY", "")
if k.startswith("op://"):
    raise ValueError("ANTHROPIC_API_KEY should not start with op://")
