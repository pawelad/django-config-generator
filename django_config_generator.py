#!/usr/bin/env python3
import os

from project_info import PROJECT_INFO


def run():
    # Set environment variables
    for key, value in PROJECT_INFO.items():
        os.environ[key] = value

    jobs = {
        'Gunicorn': {
            'out_file': 'gunicorn',
            'config_file': 'configs/gunicorn-config',
            'make_executable': True,
            'final_dir': '{}/bin/{}'.format(
                PROJECT_INFO['PROJECT_PATH'],
                PROJECT_INFO['PROJECT_NAME']
            )
        },
        'Supervisor': {
            'out_file': 'supervisor',
            'config_file': 'configs/supervisor-config',
            'make_executable': False,
            'final_dir': '/etc/supervisor/conf.d/{}.conf'.format(
                PROJECT_INFO['PROJECT_NAME']
            )
        },
        'Nginx': {
            'out_file': 'nginx',
            'config_file': 'configs/nginx-config',
            'make_executable': False,
            'final_dir': '/etc/nginx/sites-enabled/{}'.format(
                PROJECT_INFO['PROJECT_NAME']
            )
        }
    }

    for key, value in jobs.items():
        expandvars_and_copy(value['config_file'], value['out_file'])
        if value['make_executable']:
            make_executable(value['out_file'])

        print("{} config generated successfully".format(key))
        print("To move it in the right place run "
              "'mv {} {}'".format(value['out_file'], value['final_dir']))

    # Delete previously set environment variables
    for key in PROJECT_INFO.keys():
        del os.environ[key]

    print("\nAll done!")


def expandvars_and_copy(path_in, path_out):
    """Copy file with expanded environment variables"""
    f_in = open(path_in, 'r')
    f_out = open(path_out, 'w')
    f_out.write(os.path.expandvars(f_in.read()))
    f_in.close()
    f_out.close()


def make_executable(p):
    """
    Make file in given path executable
    Source:
        http://stackoverflow.com/a/33179977/3023841
    """
    st = os.stat(p)
    os.chmod(p, st.st_mode | 0o111)

if __name__ == '__main__':
    run()
