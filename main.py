from app.captioner import generate_caption
from app.self_corrector import refine_caption
from app.scorer import choose_best
from app.hashtag import generate_hashtags

def run_pipeline(image_path):
    print("\nProcessing Image...\n")

    c1 = generate_caption(image_path)
    c2 = refine_caption(image_path)

    best = choose_best(c1, c2)
    hashtags = generate_hashtags(best)

    print("Caption 1:", c1)
    print("Caption 2:", c2)
    print("Best Caption:", best)
    print("Hashtags:", hashtags)


if __name__ == "__main__":
    image_path = "data/test_images/sample.jpg"  # Put your image here
    run_pipeline(image_path)