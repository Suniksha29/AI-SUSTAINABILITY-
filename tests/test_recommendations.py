from backend.model import RECOMMENDATIONS


def test_recommendations_have_all_classes():
    expected = {"plastic", "paper", "metal", "glass", "organic", "cardboard"}
    assert expected.issubset(set(RECOMMENDATIONS.keys()))
