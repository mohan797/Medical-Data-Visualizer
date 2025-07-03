import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertEqual(fig.axes[0].get_title(), 'cardio = 0')

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertTrue(len(fig.axes[0].images) > 0)

if _name_ == '_main_':
    unittest.main()
