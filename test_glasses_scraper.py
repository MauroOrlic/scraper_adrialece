import pytest
from scraper import Glasses, GlassesDimensions

glasses_objects = [
    Glasses('https://www.adrialece.hr/crulle-fort-c6'),
    Glasses('https://www.adrialece.hr/crulle-artsy-c1'),
    Glasses('https://www.adrialece.hr/ray-ban-rb4181-601-87'),
    Glasses('https://www.adrialece.hr/ray-ban-rb4171-622-t3')
]
expected = {
    'name': [
        'Crullé Fort C6',
        'Crullé Artsy C1',
        'Ray-Ban RB4181 601/87',
        'Ray-Ban RB4171 622/T3'

    ],
    'dimensions': [
        GlassesDimensions(
            width=138,
            bridge_width=18,
            lens_height=42,
            lens_width=53,
            arm_length=138
        ),
        GlassesDimensions(
            width=138,
            bridge_width=20,
            lens_height=44,
            lens_width=53,
            arm_length=142
        ),
        GlassesDimensions(
            width=143,
            bridge_width=16,
            lens_height=42,
            lens_width=57,
            arm_length=145
        ),
        GlassesDimensions(
            width=None,
            bridge_width=18,
            lens_height=46,
            lens_width=54,
            arm_length=145
        ),

    ],
    'price': [
        28.90,
        33.90,
        136.90,
        132.00
    ],
    'frame_shape': [
        'Četvrtasti',
        'Šesterokutan',
        'Pravokutan',
        'Oval / Elipse'
    ]
}


class TestGlasses:

    @pytest.mark.parametrize(
        'glasses,attribute,expected_value',
        [
            (glasses_objects[i], attribute_name, expected_values[i])
            for attribute_name, expected_values in expected.items()
            for i in range(len(glasses_objects))
        ],
        ids=[
            f"{attribute_name}-{i+1}"
            for attribute_name in expected.keys()
            for i in range(len(glasses_objects))
        ]
    )
    def test_glasses(self, glasses, attribute, expected_value):
        assert glasses.__getattribute__(attribute) == expected_value
