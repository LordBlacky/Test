import pytest
from src import Calculator

class TestCalculator:

    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator: Calculator) -> None:
        result = calculator.add(3, 4)
        assert result == 7

    def test_subtract(self, calculator: Calculator) -> None:
        result = calculator.subtract(10, 5)
        assert result == 5

    def test_multiply(self, calculator: Calculator) -> None:
        result = calculator.multiply(3, 3)
        assert result == 9

    def test_divide(self, calculator: Calculator) -> None:
        result = calculator.divide(10, 2)
        assert result == 5.0

    def test_divide_by_zero(self, calculator: Calculator) -> None:
        with pytest.raises(ValueError):
            calculator.divide(10, 0)
