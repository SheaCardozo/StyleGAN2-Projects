import Augmentor

# Image Augmentation:
p = Augmentor.Pipeline("faces_png", "faces_pipe", save_format="PNG")
p.rotate(probability=1.0, max_left_rotation=10, max_right_rotation=10)
p.random_color(probability=1.0,min_factor=0.7,max_factor=1.3)
p.random_distortion(probability=1, grid_width=5, grid_height=5, magnitude=2)
p.sample(300)