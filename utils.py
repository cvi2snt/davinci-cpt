import io
import PIL.Image
import sketchgraphs.data as datalib
from sketchgraphs.data.sequence import sketch_from_sequence

import matplotlib.pyplot as plt

def show_cpts(imgs, rows, cols):

    # Create a figure with subplots
    fig, axs = plt.subplots(rows, cols, figsize=(20, 20))

    # Loop over the images and their corresponding subplot
    for i, ax in enumerate(axs.flat):
        ax.imshow(imgs[i])
        ax.axis('off')  # Hide the axes

    # Adjust the layout
    plt.tight_layout()

    plt.subplots_adjust(hspace=-0.8, wspace=-0.1)  # Adjust these values as needed

    # Display the grid
    plt.show()

def fig_to_img(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    # Convert the buffer to an image
    img = PIL.Image.open(buf)
    return img

def sketches_to_renderings(sequences):
    imgs = []
    for seq in sequences:
        sketch = sketch_from_sequence(seq)
        fig = datalib.render_sketch(sketch)
        plt.close()
        imgs.append(fig_to_img(fig))
    return imgs


