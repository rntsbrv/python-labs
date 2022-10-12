run_dict = {
    6: {
        'мужской':{
            3: [10.5, 11.1],
            4: [10.0, 10.4],
            5: [0.0, 9.9]
            },
        'женский':{
            3: [10.7, 11.2],
            4: [10.4, 10.6],
            5: [0.0, 10.3]
        }},
    7: {
        'мужской':{
            3: [10.3, 11.0],
            4: [9.5, 10.2],
            5: [0.0, 9.4]
        },
        'женский':{
            3: [10.7, 11.4],
            4: [9.9, 10.6],
            5: [0.0, 9.8]
        }
    }
}

if __name__ == "__main__":
    file_in = open("run_of_60_m.txt", "r", encoding="utf-8")
    file_out = open("run_of_60_mark.txt", "w", encoding="utf-8")
    lines = file_in.readlines()
    best_res = {
        'мужской': {
            'name': "",
            'grade': 0,
            'time': 1000.0
        },
        'женский': {
            'name': "",
            'grade': 0,
            'time': 1000.0
        }
    }
    for line in lines:
        params = line.split()
        name = params[0]
        sex = params[1].lower()
        grade = int(params[2])
        time = float(params[3])

        if time < best_res.get(sex).get('time'):
            best_res[sex]['name'] = name
            best_res[sex]['grade'] = grade
            best_res[sex]['time'] = time

        for marks in run_dict.get(grade).get(sex).items():
            if time >= marks[1][0] and time <= marks[1][1]:
                file_out.write(f"{name} {sex} {str(grade)} {str(time)} {str(marks[0])}\n")
                break
    file_in.close()
    file_out.close()
    print(f"Лучший школьник: {best_res.get('мужской').get('name')} {best_res.get('мужской').get('grade')} класс {best_res.get('мужской').get('time')} сек")
    print(f"Лучшая школьница: {best_res.get('женский').get('name')} {best_res.get('женский').get('grade')} класс {best_res.get('женский').get('time')} сек")