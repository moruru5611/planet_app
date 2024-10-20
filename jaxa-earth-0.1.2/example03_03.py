
# Load module
from jaxa.earth import je

# Set query parameters
kw   = ["AW3D"]
dlim = ["2019-01-01T00:00:00","2021-02-01T00:00:00"]
ppu  = 360
bbox = [139.5, 35, 140.5, 36]
mq   = "bits_equal"
val  = [0,0,0,0,0,0,0,0]

# Get information of collections,bands for data
collections,bands = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw)

# Get an image for data
data_d = je.ImageCollection(collection=collections[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution(ppu=ppu)\
           .filter_bounds(bbox=bbox)\
           .select(band="DSM")\
           .get_images()

# Get an image for mask
data_m = je.ImageCollection(collection=collections[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution(ppu=ppu)\
           .filter_bounds(bbox=bbox)\
           .select(band="MSK")\
           .get_images()

# Process and show an image
img = je.ImageProcess(data_d)\
        .mask_images(data_m,method_query=mq, values=val)\
        .show_images()
