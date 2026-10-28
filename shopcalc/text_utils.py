import re
""" remove capital letters and slugify text """


def slugify_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


""" cut text and add ... if it is too long"""

def truncate_text(text:str, max_length: int) -> str:
    if(len(text) > max_length):
        return text[:max_length - 3] + "..."
    return text


