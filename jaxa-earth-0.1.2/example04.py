
# Load module
from jaxa.earth import je

# Set query parameters
kw_d = ["ndvi","_monthly"]
kw_r = ["ndvi","_monthly","normal"]
dlim = ["2021-08-01T00:00:00","2021-08-01T00:00:00"]

# Get information of collections,bands for data
collections_d,bands_d = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_d)

# Get an image for data
data_d = je.ImageCollection(collection=collections_d[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution()\
           .filter_bounds()\
           .select(band=bands_d[0][0])\
           .get_images()

# Get information of collections,bands for reference
collections_r,bands_r = je.ImageCollectionList(ssl_verify=True)\
                          .filter_name(keywords=kw_r)

# Get an image for reference
data_r = je.ImageCollection(collection=collections_r[0],ssl_verify=True)\
           .filter_date(dlim=dlim)\
           .filter_resolution()\
           .filter_bounds()\
           .select(band=bands_r[0][0])\
           .get_images()

# Process and show an image
img = je.ImageProcess(data_d)\
        .diff_images(data_r)\
        .show_images()
