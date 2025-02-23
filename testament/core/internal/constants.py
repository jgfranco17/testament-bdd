from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class StepExecutionStatus:
    """Constants for execution statuses."""

    COMPLETED: Final[str] = "COMPLETED"
    EXCLUDED: Final[str] = "EXCLUDED"
    FAILED: Final[str] = "FAILED"
    SKIPPED: Final[str] = "SKIPPED"
    NOT_EXECUTED: Final[str] = "NOT EXECUTED"


@dataclass(frozen=True)
class ConsoleIcons:
    """Icons for the shell prints."""

    CHECK: Final[str] = "\u2713"
    CROSS: Final[str] = "\u2715"
