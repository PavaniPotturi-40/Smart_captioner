def generate_hashtags(caption):
    words = caption.split()
    hashtags = ["#" + word for word in words if len(word) > 3]
    return hashtags