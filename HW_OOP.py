class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'\nИмя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка за домашнее задание: {self.average_grades()}\n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def average_grades(self):
        grades = []
        for x in list(self.grades.values()):
            grades.extend(x)
        return round(sum(grades) / len(grades), 1)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grades() < other.average_grades()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'\nИмя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.average_grades()}\n'
        return res

    def average_grades(self):
        grades = []
        for x in list(self.grades.values()):
            grades.extend(x)
        return round(sum(grades) / len(grades), 1)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades() < other.average_grades()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'


def student_average_rating(student, courses):
    rating = []
    for el in range(len(student)):
        if list(student[el].grades.keys()) == [courses]:
            for n in student[el].grades.values():
                rating.extend(n)
    return round(sum(rating) / len(rating), 1)


def lecturer_average_rating(lecturer, courses):
    rating = []
    for el in range(len(lecturer)):
        if list(lecturer[el].grades.keys()) == [courses]:
            for n in lecturer[el].grades.values():
                rating.extend(n)
    return round(sum(rating) / len(rating), 1)


student_1 = Student('Name_1', 'Surname_1', 'Gender_1')
student_2 = Student('Name_2', 'Surname_2', 'Gender_2')
study = [student_1, student_2]
student_1.courses_in_progress = ['Python', 'C++']
student_2.courses_in_progress = ['Python', 'Java']
student_1.finished_courses = ['Введение в программирование']
student_2.finished_courses = ['Введение в программирование']

mentor_1 = Mentor('Name_1', 'Surname_1')
mentor_2 = Mentor('Name_2', 'Surname_2')
mentor_1.courses_attached = ['Python', 'Java', 'C++']
mentor_2.courses_attached = ['Python', 'C#', 'JavaScript']

lecturer_1 = Lecturer('Name_1', 'Surname_1')
lecturer_2 = Lecturer('Name_2', 'Surname_2')
lecturer_1.courses_attached = ['Python', 'C++', 'Perl']
lecturer_2.courses_attached = ['Python', 'Java', 'Ruby']

reviewer_1 = Reviewer('Name_1', 'Surname_1')
reviewer_2 = Reviewer('Name_2', 'Surname_2')
reviewer_1.courses_attached = ['Python', 'C++', 'PHP']
reviewer_2.courses_attached = ['Python', 'Java', 'JavaScript']

student_1.rate_lecturer(lecturer_1, 'C++', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Ruby', 8)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'PHP', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 5)

print('Оценки студентов:', student_1.grades, student_2.grades)
print('Оценки лекторов:', lecturer_1.grades, lecturer_2.grades)

print(f'Средние оценки студентов: {student_1.average_grades()}, {student_2.average_grades()}')
print(f'Средние оценки лекторов: {lecturer_1.average_grades()}, {lecturer_2.average_grades()}')

print('Средние оценки всех студентов по курсу:', student_average_rating(study, 'Python'))

print('Сравнение оценок студентов:', student_1 > student_2)
print('Сравнение оценок лекторов:', lecturer_1 < lecturer_2)
print('Неверное сравнение:', student_1 > lecturer_2)

print(student_1, student_2, lecturer_1, lecturer_2)
