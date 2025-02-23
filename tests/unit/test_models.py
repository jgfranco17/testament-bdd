from typing import Dict

import pytest

from testament import TestCase


def test_initialization() -> None:
    """Tests if the TestCase initializes with a given name."""
    test = TestCase.scenario("Sample Test")
    assert test.name == "Sample Test"


def test_given_with_callable() -> None:
    """Tests if `given` correctly stores callable output."""
    test = TestCase.scenario("Test Given Callable")

    def setup() -> None:
        return {"user": "Alice", "age": 25}

    test.given("a user object", setup)

    assert test._context["given"] == {"user": "Alice", "age": 25}


def test_given_with_dict() -> None:
    """Tests if `given` correctly stores dictionary input."""
    test = TestCase.scenario("Test Given Dict")
    test.given("a user object", {"user": "Bob", "age": 30})

    assert test._context["given"] == {"user": "Bob", "age": 30}


def test_when_modifies_context() -> None:
    """Tests if `when` updates context correctly."""
    test = TestCase.scenario("Test When")

    def setup() -> None:
        return {"user": "Alice", "age": 25}

    def modify(data: Dict):
        return {**data, "age": 30}

    test.given("a user object", setup).when("updating age", modify)

    assert test._context["when"]["age"] == 30


def test_then_passes() -> None:
    """Tests if `then` passes when assertion is correct."""
    test = TestCase.scenario("Test Then Pass")

    def setup() -> None:
        return {"count": 5}

    def increment(data: Dict) -> Dict:
        return {**data, "count": data["count"] + 1}

    test.given("a counter", setup).when("incrementing", increment).then(
        "count should be 6", lambda data: data["count"] == 6
    )


def test_then_fails() -> None:
    """Tests if `then` fails when assertion is incorrect."""
    test = TestCase.scenario("Test Then Fail")

    def setup() -> None:
        return {"count": 5}

    def increment(data: Dict):
        return {**data, "count": data["count"] + 1}

    test.given("a counter", setup).when("incrementing", increment)

    with pytest.raises(AssertionError, match="THEN failed: count should be 10"):
        test.then("count should be 10", lambda data: data["count"] == 10)


def test_but_passes() -> None:
    """Tests if `but` assertion works correctly."""
    test = TestCase.scenario("Test But Pass")

    def setup() -> None:
        return {"status": "active"}

    test.given("an active user", setup).but(
        "status should not be inactive", lambda data: data["status"] != "inactive"
    )


def test_but_fails() -> None:
    """Tests if `but` fails when assertion is incorrect."""
    test = TestCase.scenario("Test But Fail")

    def setup() -> None:
        return {"status": "inactive"}

    test.given("a user", setup)

    with pytest.raises(AssertionError, match="BUT failed: status should be active"):
        test.but("status should be active", lambda data: data["status"] == "active")
