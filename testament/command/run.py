import logging
from pathlib import Path
from typing import Optional, Tuple

import click

from testament.core.internal.constants import ProjectFiles
from testament.core.internal.errors import TestamentInputError

logger = logging.getLogger(__name__)


@click.command("run")
@click.argument(
    "directory",
    type=click.Path(exists=True, dir_okay=False),
)
def run_tests(directory: Path) -> None:
    """Run BDD testcases."""
    print("Hello, world!")
