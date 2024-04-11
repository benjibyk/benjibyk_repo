import hashlib

def generate_short_url(original_url):
    # Generate a unique hash for the original URL
    hash_object = hashlib.md5(original_url.encode())
    hash_digest = hash_object.hexdigest()

    # Take the first 8 characters of the hash to create the short URL
    short_url = hash_digest[:8]

    return short_url
