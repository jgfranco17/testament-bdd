import logging

import click
import colorama

from testament.command.run import run_tests
from testament.core.internal.handler import TestamentCliHandler
from testament.core.internal.output import ColorHandler

from . import __version__

colorama.init(autoreset=True)


def __get_log_level(verbosity: int) -> int:
    levels = {0: logging.WARN, 1: logging.INFO, 2: logging.DEBUG}
    return levels.get(verbosity, logging.DEBUG)


def __set_logger(level: int):
    logger = logging.getLogger(__package__)
    log_level = __get_log_level(level)
    logger.setLevel(log_level)
    handler = ColorHandler()
    handler.setLevel(log_level)
    formatter = logging.Formatter(
        fmt="[%(asctime)s][%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


@click.group(cls=TestamentCliHandler)
@click.pass_context
@click.version_option(version=__version__)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase verbosity. Use multiple times for more detail (e.g., -vv for debug).",
)
def cli(context: click.Context, verbose: int):
    """Testament: Building and executing BDD tests."""
    __set_logger(verbose)
    context.ensure_object(dict)


cli.add_command(run_tests)
