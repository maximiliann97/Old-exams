fn = 'default_config.ini'
fn2 = 'user_overrides.ini'
writingfile = 'game_options.ini'
# Part A

def read_ini(filename):
    options = dict()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('#') and len(line) > 0:
                if line.startswith('['):
                    line = line.strip('\n')
                    config = line.replace('[', '').replace(']', '')
                    options[config] = dict()
                elif not line.startswith(' '):
                    line = line.strip('\n')
                    if line == '':
                        continue
                    setting, value = line.split('=')
                    options[config][setting] = value
    return options


def write_ini(filename, game_options):
    with open(filename, mode='w') as file:
        for config, option in game_options.items():
            file.write('['+str(config)+']' + '\n')
            counter = 0
            for setting, value in game_options[config].items():
                file.write(str(setting)+'='+str(value)+'\n')
                counter += 1
                if counter == len(game_options[config]):
                    file.write('\n')


def apply_overrides(default, user):
    for config, option in user.items():
        if config not in default:
            print(f'Section "{config}" not found in config. Skipping.')
        else:
            for setting, value in user[config].items():
                if setting not in default[config]:
                    print('Parameter "{}" not found under section "{}".'.format(setting, config))
                else:
                    for def_set, def_value in default[config].items():
                        default[config][setting] = value
    print(default)










config = read_ini(fn)
user = read_ini(fn2)
apply_overrides(config, user)
write_ini(writingfile, config)
