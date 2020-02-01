from bs4 import BeautifulSoup
from bs4.element import Tag
from copy import deepcopy
from urllib.request import urlopen
from dataclasses import dataclass
from typing import Collection
from http.client import HTTPResponse


def get_glasses_urls(url: str) -> Collection[str]:
    glasses = []
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('div', {'class': 'product-name-wrapper desktop'}):
            glasses.append(anchor.find('a')['href'])
    return glasses


@dataclass
class GlassesDimensions:
    width: int = None
    arm_length: int = None
    bridge_width: int = None
    lens_width: int = None
    lens_height: int = None


class Glasses:
    def __init__(self, url: str, parser='html.parser'):
        self._url = url
        self._glasses_page: HTTPResponse = urlopen(self.url).read()
        self._parser = parser
        self._name: str = None
        self._dimensions: GlassesDimensions = None
        self._price: float = None
        self._frame_shape: str = None

    @property
    def url(self):
        return self._url

    @property
    def name(self):
        if self._name is None:
            self._name = self._get_name(self._glasses_page, self._parser)
        return self._name

    @property
    def dimensions(self):
        if self._dimensions is None:
            self._dimensions = self._get_dimensions(self._glasses_page, self._parser)
        return self._dimensions

    @property
    def price(self):
        if self._price is None:
            self._price = self._get_price(self._glasses_page, self._parser)
        return self._price

    @property
    def frame_shape(self):
        if self._frame_shape is None:
            self._frame_shape = self._get_frame_shape(self._glasses_page, self._parser)
        return self._frame_shape

    @staticmethod
    def _get_name(page: HTTPResponse, parser: str):
        soup = BeautifulSoup(page, parser)
        product_name: Tag = soup.find('h1', {'class': 'product-name'})
        name = product_name.contents[0].strip()
        return name

    @staticmethod
    def _get_price(page: HTTPResponse, parser: str) -> float:
        soup = BeautifulSoup(page, parser)
        anchor = soup.find('div', {'class': 'product-main-price-wrapper'})
        anchor = anchor.find('span')
        anchor = anchor.find('span')
        price = float(anchor.contents[0].replace(' ', ''))
        return price

    @staticmethod
    def _get_frame_shape(page: HTTPResponse, parser: str) -> str:
        soup = BeautifulSoup(page, parser)
        anchor = soup.find('table', {'class': 'product-properties-table'})
        anchor = anchor.find_all('tr')

        for tr in anchor:
            header = tr.find('th').contents[0]
            if header == 'Oblik okvira:':
                wanted_row = tr
                break

        frame_shape = wanted_row.find('td').find('a').contents[0]

        return frame_shape

    @staticmethod
    def _get_dimensions(page: HTTPResponse, parser: str) -> GlassesDimensions:
        return GlassesDimensions(
            width=Glasses._get_dim_width(page, parser),
            bridge_width=Glasses._get_dim_bridge_width(page, parser),
            arm_length=Glasses._get_dim_arm_length(page, parser),
            lens_width=Glasses._get_dim_lens_width(page, parser),
            lens_height=Glasses._get_dim_lens_height(page, parser),
        )

    @staticmethod
    def _get_dim_width(page: HTTPResponse, parser: str) -> int:
        soup = BeautifulSoup(page, parser)

        if soup.find_all('div', {'class': 'dimensions dim-4'}):
            anchor = soup.find('div', {'class': 'dimensions dim-4'})
            anchor = anchor.find('span')
            width = int(anchor.contents[0].split()[0])
        else:
            width = None

        return width

    @staticmethod
    def _get_dim_bridge_width(page: HTTPResponse, parser: str) -> int:
        soup = BeautifulSoup(page, parser)

        if soup.find_all('div', {'class': 'dimensions dim-2'}):
            anchor = soup.find('div', {'class': 'dimensions dim-2'})
            anchor = anchor.find('span')
            bridge_width = int(anchor.contents[0].split()[0])
        else:
            bridge_width = None

        return bridge_width

    @staticmethod
    def _get_dim_arm_length(page: HTTPResponse, parser: str) -> int:
        soup = BeautifulSoup(page, parser)

        if soup.find_all('div', {'class': 'dimensions dim-1'}):
            anchor = soup.find('div', {'class': 'dimensions dim-1'})
            anchor = anchor.find('span')
            arm_length = int(anchor.contents[0].split()[0])
        else:
            arm_length = None

        return arm_length

    @staticmethod
    def _get_dim_lens_width(page: HTTPResponse, parser: str) -> int:
        soup = BeautifulSoup(page, parser)

        if soup.find_all('div', {'class': 'dimensions dim-3'}):
            anchor = soup.find('div', {'class': 'dimensions dim-3'})
            anchor = anchor.find_all('span')
            try:
                lens_width = int(anchor[1].contents[0].split()[0])
            except IndexError:
                lens_width = None
        else:
            lens_width = None

        return lens_width

    @staticmethod
    def _get_dim_lens_height(page: HTTPResponse, parser: str) -> int:
        soup = BeautifulSoup(page, parser)

        if soup.find_all('div', {'class': 'dimensions dim-3'}):
            anchor = soup.find('div', {'class': 'dimensions dim-3'})
            anchor = anchor.find_all('span')
            try:
                lens_height = int(anchor[0].contents[0].split()[0])
            except IndexError:
                lens_height = None
        else:
            lens_height = None

        return lens_height

