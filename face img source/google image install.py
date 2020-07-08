from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
 
arguments = {"keywords" : "고양이", "limit" : 10, "print_urls" : True, "chromedriver": "chromedriver.exe"}

paths = response.donwload(arguments)
print(paths)