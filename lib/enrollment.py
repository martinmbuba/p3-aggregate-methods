from datetime import datetime
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # Dictionary to store grades: {enrollment: grade}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        """Count the number of courses this student is enrolled in."""
        return len(self._enrollments)

    def add_grade(self, enrollment, grade):
        """Add a grade for a specific enrollment."""
        if enrollment in self._enrollments:
            self._grades[enrollment] = grade
        else:
            raise ValueError("Student is not enrolled in this course")

    def aggregate_average_grade(self):
        """Calculate the average grade across all enrolled courses."""
        if not self._grades:
            return 0.0
        
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses

    def get_enrolled_courses(self):
        """Get all courses this student is enrolled in."""
        return [enrollment.course for enrollment in self._enrollments]

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def student_count(self):
        """Count the number of students enrolled in this course."""
        return len(self._enrollments)

    def get_enrolled_students(self):
        """Get all students enrolled in this course."""
        return [enrollment.student for enrollment in self._enrollments]


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Aggregate and count enrollments by enrollment date."""
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
