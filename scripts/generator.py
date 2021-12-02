"""
Generates stubs files for solving problem
"""

import os
import pathlib

import fire
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIRECTORY = pathlib.Path(__file__).parent.joinpath('templates')
SOLUTIONS_FOLDER = pathlib.Path(__file__).parent.joinpath('../solutions')


def generate(year: int, day: int):
    problem_folder = SOLUTIONS_FOLDER.joinpath(str(year), str(day))
    problem_folder.mkdir(parents=True)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIRECTORY)))
    template = env.get_template('problem.template')
    template_output = template.render(year=year, day=day)
    with problem_folder.joinpath('problem.py').open(mode='w') as template_file:
        template_file.write(template_output)

    os.system(f'aoc download --file {problem_folder}/input --year {year} --day {day}')


def generate_all(year: int):
    for day in range(1, 26):
        generate(year, day)


if __name__ == '__main__':
  fire.Fire()

