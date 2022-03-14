from collections import defaultdict
fn = 'passwd.txt'
fn2 = 'group.txt'


def read_users(filename):
    users = {}
    with open(filename, mode='r') as file:
        for line in file:
            line = line.strip()
            line = line.split(':')
            if int(line[2]) >= 500:
                name = line[4]
                user = line[0]
                users[name] = user
    return users


def read_groups(filename):
    groups = defaultdict(list)
    with open(filename, mode='r') as file:
        for line in file:
            line = line.strip()
            line = line.split(':')
            group = line[0]
            users = line[len(line)-1]
            users = users.split(',')
            for user in users:
                groups[user].append(group)
    return groups


def print_user_table(names, groups):
    max_name = max([len(name) for name in names.keys()])
    max_user = max([len(user) for user in names.values()])
    header = 'User' + ' '*(max_user-4) + '|' + ' Name' + ' '*(max_name-4) + '|' + ' Groups'
    split_line = '-'*len(header)
    print(header)
    print(split_line)
    for name, user in sorted(names.items()):
            print('{:9s}| {:17s}| {}'.format(user, name, groups[user]))








user_dict = read_users(fn)
group_dict = read_groups(fn2)
print_user_table(user_dict, group_dict)
