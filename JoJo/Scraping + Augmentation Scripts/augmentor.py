# Image augmentation
import Augmentor

p = Augmentor.Pipeline("images", "images_pipe", save_format="PNG")
p.rotate(probability=1.0, max_left_rotation=12, max_right_rotation=12)
p.random_color(probability=1.0, min_factor=0.8, max_factor=1.2)
p.random_distortion(probability=1, grid_width=5, grid_height=5, magnitude=2)
p.sample(2500)
