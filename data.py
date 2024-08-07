# data.py

def get_kit_body(name):
    return {"name": name}

# Test data
KIT_BODY_MIN_CHAR = get_kit_body("a")
KIT_BODY_MAX_CHAR = get_kit_body("A" * 511)
KIT_BODY_EMPTY = get_kit_body("")
KIT_BODY_TOO_LONG = get_kit_body("A" * 512)
KIT_BODY_SPECIAL_CHARS = get_kit_body("!@#$%^&*()")
KIT_BODY_SPACES = get_kit_body("  A Aaa  ")
KIT_BODY_NUMBERS = get_kit_body("123")
KIT_BODY_MISSING_NAME = {}
KIT_BODY_INVALID_TYPE = {"name": 123}
