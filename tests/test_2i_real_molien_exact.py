from scripts.audit_2i_real_molien_exact import audit


def test_exact_2i_group_and_real_molien_through_degree_60():
    result = audit(60)
    assert result["group_order"] == 120
    assert result["closure_products_checked"] == 14400
    assert result["unit_norms_checked"] == 120
    assert result["left_matrices_checked"] == 120
    assert result["determinants_checked"] == 120
    assert result["degrees_checked"] == 61

    coefficients = result["coefficients"]
    assert coefficients[:13] == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 14]
    assert coefficients[20] == 35
    assert coefficients[24] == 60
    assert coefficients[30] == 91
    assert coefficients[60] == 677


def test_scalar_part_class_multiplicities_sum_to_120():
    result = audit(0)
    assert sum(result["scalar_part_multiplicities"].values()) == 120
