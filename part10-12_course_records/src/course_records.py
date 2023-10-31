# tee ratkaisusi tänne


class StudyTracker:
    def __init__(self):
        self.courses = {}

    def add_course(self, course, grade, credits):
        if course not in self.courses:
            self.courses[course] = {
                "grade": grade,
                "credits": credits,
            }  # course作为key 字典里面套另外一个字典。
        else:
            if grade > self.courses[course]["grade"]:
                self.courses[course]["grade"] = grade
            if credits > self.courses[course]["credits"]:
                self.courses[course]["credits"] = credits

    def get_course_data(self, course):
        if course in self.courses:
            data = self.courses[course]  # values 是字典
            print(f"{course} ({data['credits']} cr) grade {data['grade']}")
        else:
            print(f"no entry for this course")

    def statistics(self):
        total_credits = 0
        total_score = 0
        grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

        for course, data in self.courses.items():
            total_credits += data["credits"]
            total_score += data["grade"]
            grade = data["grade"]

            if grade in grade_distribution:
                grade_distribution[grade] += 1
            else:
                grade_distribution[grade] = 1

        completed_courses = len(self.courses)  # key-value pair
        mean_grade = total_score / completed_courses if completed_courses > 0 else 0

        print(
            f"{completed_courses} completed courses, a total of {total_credits} credits"
        )
        print(f"mean {mean_grade:.1f}")

        print("grade distribution")
        for grade in sorted(grade_distribution.keys(), reverse=True):
            count = grade_distribution[grade]
            stars = "x" * count
            print(f"{grade}: {stars}")

    def help(self):
        print("1 add course\n2 get course data\n3 statistics\n0 exit")

    def run(self):
        self.help()

        while True:
            command = input("command: ")

            if command == "1":
                course = input("course: ")
                grade = int(input("grade: "))
                credits = int(input("credits: "))
                self.add_course(course, grade, credits)
            elif command == "2":
                course = input("course: ")
                self.get_course_data(course)
            elif command == "3":
                self.statistics()
            elif command == "0":
                break
            else:
                self.help()


tracker = StudyTracker()
tracker.run()
