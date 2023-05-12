
def get_information_about_courses(choice, courses):
    for i in courses:
        if i['course'] == choice:
            print(f'{i["course"]}: {i["audience"]}, {i["teacher"]}, {i["time"]}')

courses = [{"course": "CS101", "audience": "3004", "teacher": "Хайнс", "time": "8:00"},
           {"course": "CS102", "audience": "4501", "teacher": "Альварадо", "time": "9:00"},
           {"course": "CS103", "audience": "6755", "teacher": "Рич", "time": "10:00"},
           {"course": "NT110", "audience": "1244", "teacher": "Берк", "time": "11:00"},
           {"course": "CM241", "audience": "1411", "teacher": "Ли", "time": "13:00"}]

choice = input()

get_information_about_courses(choice, courses)