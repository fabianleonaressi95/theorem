import pytest

from monte_carlo import METRICS, monte_carlo, write_summary


def test_monte_carlo_is_reproducible_and_complete():
    first = monte_carlo(replicates=3, seed=123, steps=4)
    second = monte_carlo(replicates=3, seed=123, steps=4)
    assert first == second
    assert len(first) == 3 * len(METRICS)
    assert {row["architecture"] for row in first} == {
        "hierarchical", "matrix", "practices_like"
    }
    assert all(row["replicates"] == 3 for row in first)
    assert all(row["ci95_normal_lower"] <= row["mean"] <= row["ci95_normal_upper"]
               for row in first)


def test_monte_carlo_requires_two_replicates():
    with pytest.raises(ValueError):
        monte_carlo(replicates=1)


def test_write_summary_creates_json_and_csv(tmp_path):
    rows = monte_carlo(replicates=2, seed=5, steps=2)
    write_summary(rows, tmp_path)
    assert (tmp_path / "monte_carlo.json").is_file()
    assert (tmp_path / "monte_carlo.csv").is_file()
