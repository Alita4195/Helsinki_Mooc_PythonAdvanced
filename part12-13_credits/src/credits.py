from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


# Write your solution
def sum_of_all_credits(attempts):
    # return sum(attempt.credits for attempt in attempts)
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)


def sum_of_passed_credits(attempts):
    return reduce(
        lambda total, attempt: total + attempt.credits if attempt.grade > 0 else total,
        attempts,
        0,
    )
    # return sum(map(lambda x: x.credits, filter(lambda x: x.grade > 0, attempts)))


def average(attempts):
    # valid_attempts = list(filter(lambda x: x.grade > 0, attempts))
    # if not valid_attempts:
    #     return 0  # Avoid division by zero
    # total_grade = sum(map(lambda x: x.grade, valid_attempts))
    # return total_grade / len(valid_attempts)

    passed_courses = list(filter(lambda x: x.grade > 0, attempts))
    if not passed_courses:
        return 0  # Avoid division by zero
    total_credits = reduce(
        lambda total, course: total + course.grade, passed_courses, 0
    )
    return total_credits / len(passed_courses)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
