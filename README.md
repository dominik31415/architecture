# Classifying buildings by architectural style using Keras/InceptionV3 

### Summary:
I trained (transfer learning + fine-tuning) the InceptionV3 using Keras to classify buildings by their architectural style (I picked 10 styles, see below). The training images were harvested from Bing using a script. The NN eventually achieves about **65% accuracy**. Most errors are due to either low quality training images (especially in the Ottoman architecture) or styles that are difficult to discern in general (modern, postmodern, brutalist).

Trained styles:
{0: 'artdeco',  1: 'brutalist',  2: 'classical',  3: 'colonial',  4: 'gothic',  5: 'modern',  6: 'ottoman',  7: 'postmodern',  8: 'romanesque',  9: 'tudor'}


### Description of files:
- batch.py , script that starts downloading the sample images 
- bbid.py , (forked, not mine) interfaces with Bing 
- train_test_split.py , divides data set about 80/20 
- downsize.py , rescales all images to 500px along long axis 
- training.ipynb , main script for training the NN 
- results.ipynb , generates some graphs/metrics of the trained NN 
- weights-xx.hdf5 , my weights after fine-tuning
- ImageDataGeneratorExtended.py , a modified Keras image generator. it adds the option to crop images randomly



### Data collection and pre-processing:

- The images were scarped from Bing using the scripts batch.py and bbid.py. Latter downloaded about 400 images for each specified architecture style, using searches like “modern architecture", or “classical architecture”

- I found the downloaded images to be of somewhat mixed quality. So I sifted through them quickly by hand and discarded all “wrong” images, e.g. interior images, ottoman chairs, textbook images that compare two styles, and ruins. All in all I threw away about 10% of all images, and ended up with about 3700 images

- I found it necessary to strip the images of their metadata.

- Those images were randomly split into a train/test set (80-20 split), using the script train_test_split.py

-  Some of the images were quite large, which slowed down training. But the used NN always downsizes to 299x299pixels anyways, and does not actually use the extra resolution. At the same time I did not want to just throw away all this information. As a compromise, I decided to shrink all images to 500x500 pixels (using the script downsize.py) and then use the Keras image generator to take subsets of downsample further. I also discarded images too small (less than 400pixels in both directions).


### Training and results:
The "result.jpynb" file generates and describes a few figures of merit. "examples.png" shows some images, which were either classified correctly (first column) or incorrectly (second and third column). Arguably, many mis-classified images are tough cases even for human eyes (e.g. interoir images, images with overlayed text, images with multiple buildings). It would be interesting to see how this NN performs on a more curated data set.

The confusion matrix is given here:
![here](https://github.com/dominik31415/architecture/blob/master/confusionMatrix.png)

Three obvervations:
- for most categories the accuracy is actually higher than 65%
- the second worst category is the 'ottoman architecture', which also was the data set with the lowest quality of sample images
- the NN struggles to discern modern-postmodern (not really surprising IMHO)
