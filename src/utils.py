from matplotlib import pyplot as plt
import numpy as np

## Function taken from Udacity course.
## Modified to change tick colots to white
## (Personally prefer working with black background)
def view_classify(img, ps, version="MNIST"):
    ''' Function for viewing an image and it's predicted classes.
    '''
    ps = ps.data.numpy().squeeze()
    
    with plt.rc_context({'xtick.color':'white', 'ytick.color':'white'}):
        fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
        ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
        ax1.axis('off')
        ax2.barh(np.arange(10), ps)
        ax2.set_aspect(0.1)
        ax2.set_yticks(np.arange(10))
        if version == "MNIST":
            ax2.set_yticklabels(np.arange(10))
    #         ax2.set_xticklabels
        elif version == "Fashion":
            ax2.set_yticklabels(['T-shirt/top',
                                'Trouser',
                                'Pullover',
                                'Dress',
                                'Coat',
                                'Sandal',
                                'Shirt',
                                'Sneaker',
                                'Bag',
                                'Ankle Boot'], size='small');
        ax2.set_title('Class Probability', color='white')
        ax2.xaxis.label.set_color('white')
        ax2.set_xlim(0, 1.1)


plt.tight_layout()