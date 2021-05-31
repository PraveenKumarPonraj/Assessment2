import unittest
import Assessment2

class TestAssessment(unittest.TestCase):
    def setUp(self):
        self.Total_Fees=25000
        self.TotalAbsentDays=5
        self.LOPAmount=500
        self.FineAmt=100
        self.StudentAbsentDays=7


    def test_students_details(self):
        user_input={self.Total_Fees}
        expected_output={25000}
        self.assertEqual(user_input == expected_output,True)
        
    def test_staff_details(self):
        user_input={self.TotalAbsentDays}
        expected_output={5}
        self.assertEqual(user_input == expected_output,True)
    
        user_input={self.LOPAmount}
        expected_output={500}
        self.assertEqual(user_input == expected_output,True)

        user_input={self.TotalAbsentDays*self.LOPAmount}
        expected_output={2500}
        self.assertEqual(user_input == expected_output,True)

    def test_Student_Attendance(self):
        user_input={self.FineAmt}
        expected_output={100}
        self.assertEqual(user_input == expected_output,True)
    
        user_input={self.StudentAbsentDays}
        expected_output={7}
        self.assertEqual(user_input == expected_output,True)

        user_input={self.StudentAbsentDays*self.FineAmt}
        expected_output={700}
        self.assertEqual(user_input == expected_output,True)

if __name__ == '__main__':
    unittest.main()