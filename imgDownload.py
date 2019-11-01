from google_images_download import google_images_download

# Creates Image Object ->
imgObject = google_images_download.googleimagesdownload()

search_queries = [
    'juventus jersey',
    'juventus uniform',
    '''juventus players''',
    'juventus camiseta',
]


def downloadImages(query):
    # Keyword arguments is the query that we give the application to run
    # The image format goes on the format
    # We then set the limit of the images
    # We set print URL, can also be set to save in a csv
    # The size of the image we want
    # Can be specified like the Google Image Tool ("large, medium, icon")
    # Aspect Ratio of the images to download. ("tall, square, wide, panoramic")

    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 100,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": "panoramic"}
    try:
        imgObject.download(arguments)
    # Hadles if File is not Found:
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 100,
                     "print_urls": True,
                     "size": "medium"}
        # Providing arguments for the searched query
        try:
            # Downloads the photos based on given arguments
            imgObject.download(arguments)
        except:
            pass


# Driver Code  -> downloads images in a folder named downloads
for query in search_queries:
    downloadImages(query)
    print()
