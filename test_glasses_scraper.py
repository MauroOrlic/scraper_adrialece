import pytest
from scraper import Glasses, GlassesDimensions

glasses_objects = [
    Glasses('https://www.adrialece.hr/crulle-odyssey-c4'),
    Glasses('https://www.adrialece.hr/crulle-titanium-1124-c1'),
]
expected = {
    'name': [
        'Crullé Odyssey C4',
        'Crullé Titanium 1124 C1'
    ],
    'dimensions': [
        GlassesDimensions(
            width=137,
            bridge_width=18,
            lens_height=42,
            lens_width=51,
            arm_length=145
        ),
        GlassesDimensions(
            width=135,
            bridge_width=17,
            lens_height=46,
            lens_width=52,
            arm_length=146
        ),

    ],
    'price': [
        9.9,
        25.94
    ],
    'frame_shape': [
        'Četvrtasti',
        'Pilot'
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
