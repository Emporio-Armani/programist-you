def filter_birds(birds, geese):
    filtered_birds = []
    for bird in birds:
        if bird not in geese:
            filtered_birds.append(bird)
    return filtered_birds