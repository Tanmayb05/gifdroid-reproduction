"""Session state management for the multi-turn automation loop."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

import numpy as np


@dataclass
class ConversationTurn:
    step_index: int
    screenshot: np.ndarray  # HxWxC uint8 array
    action_taken: Any | None  # ExecutableAction or None for initial state


class AutomationSession:
    """Tracks history and step count for an automation loop."""

    def __init__(self, max_steps: int, history_window: int = 3) -> None:
        self.max_steps = max_steps
        self.history_window = history_window
        self._turns: list[ConversationTurn] = []

    def add_turn(self, turn: ConversationTurn) -> None:
        self._turns.append(turn)

    def get_history(self) -> list[ConversationTurn]:
        """Return the most recent `history_window` turns."""
        return self._turns[-self.history_window :]

    @property
    def step_count(self) -> int:
        return len(self._turns)

    def is_at_limit(self) -> bool:
        return self.step_count >= self.max_steps
