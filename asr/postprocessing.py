def clean_text(text):
    if not text:
        return ""
    text = text.strip()
    text = " ".join(text.split()) # Remove extra spaces and newlines and joins words with single space, text.split() splits by any whitespace and joins with single space
    return text