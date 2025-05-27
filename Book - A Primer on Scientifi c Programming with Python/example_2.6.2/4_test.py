import unittest
import ast  # For parsing the data file
from analysis_2 import analyze_decade  # Import your analysis function

class TestDecadeAnalysis(unittest.TestCase):
    """"Test cases for the sun hours analysis functions
    """
    def setUp(self):
        """Set up test data"""
        self.data = [
            [43.8, 60.5, 190.2, 144.7, 240.9, 210.3, 219.7, 176.3, 199.1, 109.2, 78.7, 67.0],  # Year 1929
            [49.9, 54.3, 109.7, 102.0, 134.5, 211.2, 174.1, 207.5, 108.2, 113.5, 68.7, 23.3],  # Year 1930
            [63.7, 72.0, 142.3, 93.5, 150.1, 158.7, 127.9, 135.5, 92.3, 102.5, 62.4, 38.5],  # Year 1931
        ]

    def test_analyze_decade_output_format(self):
        """Test the output format of the analyze_decade function"""
        result = analyze_decade(self.data)

        # Check if the result is a list of tuples
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        # Check if each item in the result is a tuple with two elements
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], float)
            
    def test_analyze_decade_calculations(self):
        """Test that analyze_decade calculates averages correctly"""
        # For the test data (1929-1931), we can manually calculate the expected result
        # For the 1930s decade:
        # Dec 1929 = 67.0, Jan 1930 = 49.9, Dec 1930 = 23.3, Jan 1931 = 63.7
        expected_sum = 67.0 + 49.9 + 23.3 + 63.7
        expected_avg = expected_sum / (4 * 30 * 2)      # Average per day for Jan and Dec (2 months, 30 days each, 4 vals )
        print("Expected sum:", expected_sum)
        print("Expected average:", expected_avg)

        # Get the results - THIS LINE IS MISSING
        results = analyze_decade(self.data)

        # Find the 1930s result
        for decade, avg in results:
            if decade == "1930s":
                # Note: Your calculation might be different (you divide by len*2*30)
                # Adjust this test to match your exact calculation method
                self.assertAlmostEqual(avg, expected_avg, delta=0.05)  # Allow a small margin of error
            print(f"Actual average for {decade}: {avg}")
            print(f"Ratio: {expected_avg/avg}")
    
    def test_empty_data(self):
        """Test that the function handles empty data gracefully"""
        results = analyze_decade([])
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
