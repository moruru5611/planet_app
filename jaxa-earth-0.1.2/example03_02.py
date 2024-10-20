
# Load module
from jaxa.earth import je

# Set query parameters
kw_d = ["AW3D"]
kw_m = ["LCCS"]
dlim = ["2019-01-01T00:00:00","2021-02-01T00:00:00"]
ppu  = 360
bbox = [139.5, 35, 140.5, 36]
mq   = "values_equal"
val  = [190]

# Get information of collections,bands for data
collections_d,bands_d = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_d)

# Get an image for data
data_d = je.ImageCollection(collection=collections_d[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution(ppu=ppu)\
           .filter_bounds(bbox=bbox)\
           .select(band=bands_d[0][0])\
           .get_images()

# Get information of collections,bands for mask
collections_m,bands_m = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_m)

# Get an image for mask
data_m = je.ImageCollection(collection=collections_m[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution(ppu=ppu)\
           .filter_bounds(bbox=bbox)\
           .select(band=bands_m[0][0])\
           .get_images()

# Process and show an image
img = je.ImageProcess(data_d)\
        .mask_images(data_m,method_query=mq, values=val)\
        .show_images()
