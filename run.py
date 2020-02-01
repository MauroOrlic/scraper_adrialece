from scraper import get_glasses_urls, Glasses
from constants import GLASSES_CORRECTIONAL_MALE_URL
from csv import writer, QUOTE_ALL
from logging import getLogger, INFO, StreamHandler
import sys

logger = getLogger('scraper_adrialece')
logger.setLevel(INFO)
logger.addHandler(StreamHandler(sys.stdout))

# =======================================================================
glasses_category_url = GLASSES_CORRECTIONAL_MALE_URL

# =======================================================================
logger.info(f"Getting glasses URLs for page '{glasses_category_url}'")
glasses_urls = get_glasses_urls(glasses_category_url)

with open('naocale.csv', mode='w') as file:
    writer = writer(file, delimiter=',', quotechar='"', quoting=QUOTE_ALL)
    writer.writerow([
        'Ime',
        'Cijena',
        'Oblik okvira',
        'Ukupna širina',
        'Širina nosa',
        'Dužina ruke',
        'Širina leća',
        'Visina leća',
        'Url'
    ])
    total = len(glasses_urls)
    for i, url in enumerate(glasses_urls):
        i += 1
        logger.info(f"({i: 4d}/{total: 4d})  Getting glasses page for url '{url}'")
        glasses = Glasses(url)
        logger.info(f"({i: 4d}/{total: 4d})  Writing info for glasses '{glasses.name}'")
        writer.writerow([
            glasses.name,
            glasses.price,
            glasses.frame_shape,
            glasses.dimensions.width,
            glasses.dimensions.bridge_width,
            glasses.dimensions.arm_length,
            glasses.dimensions.lens_width,
            glasses.dimensions.lens_height,
            glasses.url
        ])

logger.info(f"Done.")


