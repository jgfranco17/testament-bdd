from typing import Any, Callable, Dict, Union


class TestCase:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__context = {}

    @property
    def name(self) -> str:
        """Returns the name of the test case."""
        return self.__name

    @classmethod
    def scenario(cls, name: str) -> "TestCase":
        """Define a testcase with given name."""
        return cls(name)

    def _resolve(self, value: Union[Callable[..., Any], Dict[Any, Any]]) -> Any:
        """Executes callable inputs, returns dictionary inputs as-is."""
        return value() if callable(value) else value

    def given(
        self, description: str, setup: Union[Callable[..., Any], Dict[Any, Any]]
    ) -> "TestCase":
        """Sets up initial context for the test."""
        self.__context["given"] = self._resolve(setup)
        print(f"GIVEN: {description} -> {self.__context['given']}")
        return self

    def when(
        self, description: str, action: Union[Callable[..., Any], Dict[Any, Any]]
    ) -> "TestCase":
        """Performs an action based on the setup."""
        self.__context["when"] = self._resolve(action)
        print(f"WHEN: {description} -> {self.__context['when']}")
        return self

    def then(self, description: str, assertion: Callable[..., bool]) -> "TestCase":
        """Verifies expected results."""
        assert assertion(self.__context.get("when")), f"THEN failed: {description}"
        print(f"THEN: {description} ✅")
        return self

    def but(self, description: str, assertion: Callable[..., bool]) -> "TestCase":
        """Checks an alternative condition."""
        assert assertion(self.__context.get("when")), f"BUT failed: {description}"
        print(f"BUT: {description} ✅")
        return self
