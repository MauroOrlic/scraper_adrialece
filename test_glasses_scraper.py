import pytest
from scraper import Glasses, GlassesDimensions

glasses_objects = [
    Glasses('https://www.adrialece.hr/crulle-s1725-c4'),
    Glasses('https://www.adrialece.hr/boss-orange-bo-0324-2w7'),
    Glasses('https://www.adrialece.hr/carrera-ca6623-8fx')
]
expected = {'name': ['Crullé S1725 C4',
                     'Boss Orange BO 0324/2W7',
                     'Carrera CA6623 8FX'],
            'dimensions': [GlassesDimensions(width=137,
                                             bridge_width=16,
                                             lens_height=38,
                                             lens_width=54,
                                             arm_length=140),
                           GlassesDimensions(bridge_width=19,
                                             lens_width=57,
                                             arm_length=145),
                           GlassesDimensions(width=140,
                                             bridge_width=19,
                                             lens_height=35,
                                             lens_width=54,
                                             arm_length=145),
                           ],
            'price': [189.0,
                      639.0,
                      599.0],
            'frame_shape': ['Četvrtasti',
                            'Pravokutan',
                            'Pravokutan']
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
