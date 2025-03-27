from cellprofiler_library.functions.image_processing import find_maxima

from cellprofiler_library.functions.image_processing import find_maxima

def findmaxima(image, min_distance=1, threshold_abs=None, mask_image=None):
    return find_maxima(
        image=image,
        min_distance=min_distance,
        threshold_abs=threshold_abs,
        mask_image=mask_image,
    )
