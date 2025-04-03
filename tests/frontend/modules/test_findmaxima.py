import numpy.testing
import skimage.filters

import cellprofiler.modules.findmaxima

instance = cellprofiler.modules.findmaxima.FindMaxima()

# three tests for each mode: labels, mask, threshold
# copy math from image_processing
def test_run(image, module, image_set, workspace):
    module.x_name.value = "example"

    module.y_name.value = "FindMaxima"

    module.run(workspace)

    actual = image_set.get_image("FindMaxima")

    if image.multichannel:
        channel_axis = -1
    else:
        channel_axis = None

    maxima_coords = skimage.feature.peak_local_max(
        image,
        min_distance=min_distance, 
        threshold_abs=threshold_abs
    ) # test threshold and mask

    desired = numpy.zeros(image.shape, dtype=bool)
    desired[tuple(maxima_coords.T)] = True

    numpy.testing.assert_array_almost_equal(actual.pixel_data, desired)


