import random

def generate_random_poem():
    lines = [
        "The sun sets in the west,",
        "Birds return to their nest.",
        "The moon rises high,",
        "Stars light up the sky.",
        "The night is calm and still,",
        "Nature's beauty gives a thrill."
    ]
    poem = "\n".join(random.sample(lines, len(lines)))
    return poem

def display_poem(poem):
    print(poem)

if __name__ == "__main__":
    poem = generate_random_poem()
    display_poem(poem)
