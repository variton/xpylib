import re

from metric.observer import measure

def test_measure_returns_result_and_prints_timing(capsys):
    @measure
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr().out.strip()
    # Example: "add executed in 0.000001 seconds"
    assert re.match(r"^add executed in \d+\.\d{6} seconds$", captured)
