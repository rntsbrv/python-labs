foot_dict = {
'Россия': 'A',
'Португалия': 'B',
'Франция': 'C',
'Дания': 'C',
'Египет': 'A'
}

if __name__ == "__main__":
    foot_dict['Турция'] = 'B'

    team_group = input()
    for team in foot_dict.items():
        if team[1] == team_group:
            print(team[0])

    group_dict = {'A': 0, 'B': 0, 'C': 0}
    for team in foot_dict.values():
        group_dict[team] += 1
    for group in group_dict.items():
        print(f'{group[0]}: {group[1]}')