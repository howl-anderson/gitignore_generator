# -*- coding: utf-8 -*-

"""Console script for gitignore_generator."""
import subprocess
from pathlib import Path

import click

GITIGNORE_GIT_REPO_ADDRESS = "https://github.com/github/gitignore.git"
GITINGORE_FILE = ".gitignore"


home_dir = Path.home()
workspace_dir = home_dir / ".gitignore_generator"
workspace_dir.mkdir(exist_ok=True)

data_source_dir = workspace_dir / "data_source"


@click.group()
def cli():
    """Init create or pull github ignore source"""
    pass


@cli.command()
def init():
    """Init project: clone gitignore from github"""
    home_dir = Path.home()
    workspace_dir = home_dir / ".gitignore_generator"
    workspace_dir.mkdir(exist_ok=True)

    data_source_dir = workspace_dir / "data_source"

    git_clone_cmd = " ".join(["git", "clone",
                             GITIGNORE_GIT_REPO_ADDRESS,
                             data_source_dir.as_posix()])

    subprocess.run(git_clone_cmd, shell=True, check=True)


# TODO: not finished
def validate_template(ctx, param, value):
    try:
        rolls, dice = map(int, value.split('d', 2))
        return (dice, rolls)
    except ValueError:
        raise click.BadParameter('rolls need to be in format NdM')


@cli.command()
@click.option('--template', '-t', multiple=True, default=[])
def create(templates):
    """create .gitignore from scratch"""
    current_working_dir = Path.cwd()

    gitignore_file = current_working_dir / GITINGORE_FILE

    with gitignore_file.open('wt') as fd:
        for t in templates:
            template_file = data_source_dir / t
            t_content = template_file.read_text()

            fd.write()
            fd.write(t_content)
            fd.write()


main = click.CommandCollection(sources=[cli])

if __name__ == "__main__":
    main()
