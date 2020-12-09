"""
    To use this you must run it next to a file 'config.json' which contains
    an entry
        "ELEMENT_DIR": (...)
    which contains a path to a directory containing:
        * element_cli
        * A directory "ElementPackages" which contains all required libraries
"""

import os
import json
import subprocess


CONFIG_FPATH = 'config.json'

ELEMENT_CLI_COMMAND = "./element_cli"


class ElementException(BaseException):
    def __init__(self, messages):
        self._messages = messages
    def __str__(self):
        return 'Messages from Element:\n\n' + '\n\n'.join([str(m) for m in self._messages[:-1]])


def run(element_expression):
    expression = 'evaluate --expression "'
    expression += element_expression
    expression += '" --logjson --packages ChristmasLibrary ExtendedLibrary'

    with open(CONFIG_FPATH) as fp:
        element_dir = json.load(fp)['ELEMENT_DIR']

    cli_cmd = ELEMENT_CLI_COMMAND
    cw_dir = os.path.expanduser(element_dir)

    process_command = cli_cmd + ' ' + expression
    proc = subprocess.Popen(process_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cw_dir, shell=True)
    returned, errors = proc.communicate()

    returned_str = str(returned, 'utf-8')
    errors_str = str(errors, 'utf-8')
    msgs = returned_str.strip().split('\n')

    loaded_msgs = [json.loads(m) for m in msgs]

    """
    for msg in loaded_msgs:
        if 'MessageLevel' in msg:
            if msg['MessageLevel'] == 3:
                raise ElementException(loaded_msgs)
    """
    result_msg = loaded_msgs[-1]
    result = result_msg['Context'].strip().split(' ')
    
    print(errors_str)

    try:
        result_data = [float(x) for x in result]
    except:
        raise ElementException(msgs)
    return result_data


def main():
    result = run("DayEight.run")
    print(result)

if __name__ == '__main__':
    main()
