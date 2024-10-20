
# Load module
from jaxa.earth import je

# Set query parameters
kw   = ["Aqua","LST","half-monthly"]
dlim = ["2021-01-01T00:00:00","2021-01-01T00:00:00"]
ppu  = 5
bbox = [110, 20, 160, 50]

# Get information of collections,bands
collections,bands = je.ImageCollectionList(ssl_verify=True)\
                      .filter_name(keywords=kw)

# Get an image
data = je.ImageCollection(collection=collections[0],ssl_verify=True)\
         .filter_date(dlim=dlim)\
         .filter_resolution(ppu=ppu)\
         .filter_bounds(bbox=bbox)\
         .select(band=bands[0][0])\
         .get_images()

# Process and show an image
img = je.ImageProcess(data)\
        .show_images()

