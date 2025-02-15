import unittest

"""
DivePlanner Class:
This class provides functionality to determine a diver's pressure group based on depth and time,
adjust the pressure group according to surface interval, and check if the diver can safely dive again.
It utilizes predefined tables for pressure groups and surface intervals.
"""

class DivePlanner:
    def __init__(self):
        # Pressure group lookup table based on depth (meters) and dive time (minutes)
        self.table = {
            10.7: {3: 'A', 6: 'C', 7.6: 'E', 9.1: 'F', 12.2: 'I', 15.2: 'K'},
            15.2: {3: 'B', 6: 'D', 7.6: 'F', 9.1: 'G', 12.2: 'J', 15.2: 'L'},
            18.3: {3: 'C', 6: 'E', 7.6: 'G', 9.1: 'H', 12.2: 'K', 15.2: 'M'},
            21.3: {3: 'D', 6: 'F', 7.6: 'H', 9.1: 'I', 12.2: 'L', 15.2: 'N'},
            24.4: {3: 'E', 6: 'G', 7.6: 'I', 9.1: 'J', 12.2: 'M', 15.2: 'O'},
            27.4: {3: 'F', 6: 'H', 7.6: 'J', 9.1: 'K', 12.2: 'N', 15.2: 'P'},
            30.5: {3: 'G', 6: 'I', 7.6: 'K', 9.1: 'L', 12.2: 'O', 15.2: 'Q'},
            33.5: {3: 'H', 6: 'J', 7.6: 'L', 9.1: 'M', 12.2: 'P', 15.2: 'R'},
            36.6: {3: 'I', 6: 'K', 7.6: 'M', 9.1: 'N', 12.2: 'Q', 15.2: 'S'},
            39.6: {3: 'J', 6: 'L', 7.6: 'N', 9.1: 'O', 12.2: 'R', 15.2: 'T'},
            42.7: {3: 'K', 6: 'M', 7.6: 'O', 9.1: 'P', 12.2: 'S', 15.2: 'U'}
        }
        
        # Surface interval lookup table based on pressure group
        self.surface_interval_table = {
            'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50, 'F': 60, 'G': 70, 'H': 80,
            'I': 90, 'J': 100, 'K': 110, 'L': 120, 'M': 130, 'N': 140, 'O': 150, 'P': 160,
            'Q': 170, 'R': 180, 'S': 190, 'T': 200, 'U': 210
        }
    
    def get_pressure_group(self, depth, time):
        """Returns the pressure group based on depth and time"""
        return self.table.get(depth, {}).get(time, "No data available for given depth/time")
    
    def adjust_for_surface_interval(self, pressure_group, interval):
        """Adjusts the pressure group based on surface interval"""
        return self.surface_interval_table.get(pressure_group, "No data available for given surface interval")
    
    def can_dive_again(self, new_pressure_group):
        """Determines if the diver can safely dive again"""
        if new_pressure_group in ['A', 'B']:
            return "You are cleared to dive again."
        elif new_pressure_group in self.surface_interval_table:
            return f"You should wait at least {self.surface_interval_table[new_pressure_group]} minutes before diving again."
        else:
            return "You should wait a significant amount of time before diving again."

"""
Unit tests for DivePlanner
"""
class TestDivePlanner(unittest.TestCase):
    def setUp(self):
        self.dive_planner = DivePlanner()
    
    def test_get_pressure_group(self):
        self.assertEqual(self.dive_planner.get_pressure_group(18.3, 9.1), 'H')
        self.assertEqual(self.dive_planner.get_pressure_group(10.7, 3), 'A')
        self.assertEqual(self.dive_planner.get_pressure_group(42.7, 15.2), 'U')
        self.assertEqual(self.dive_planner.get_pressure_group(50, 10), "No data available for given depth/time")
    
    def test_adjust_for_surface_interval(self):
        self.assertEqual(self.dive_planner.adjust_for_surface_interval('H', 80), 80)
        self.assertEqual(self.dive_planner.adjust_for_surface_interval('A', 10), 10)
        self.assertEqual(self.dive_planner.adjust_for_surface_interval('Z', 20), "No data available for given surface interval")
    
    def test_can_dive_again(self):
        self.assertEqual(self.dive_planner.can_dive_again('A'), "You are cleared to dive again.")
        self.assertEqual(self.dive_planner.can_dive_again('D'), "You should wait at least 40 minutes before diving again.")
        self.assertEqual(self.dive_planner.can_dive_again('Z'), "You should wait a significant amount of time before diving again.")

if __name__ == "__main__":
    unittest.main()
