def calculate_bonus(years_worked, sick_days, annual_income):
    bonus = 0

    if years_worked > 3:
        bonus = 0.3 * annual_income
    elif years_worked >= 1.5:
        bonus = 0.25 * annual_income
    elif years_worked >= 0.25:
        bonus = 0.15 * annual_income

    if years_worked > 0 and sick_days == 0:
        bonus += 0.03 * annual_income

    return bonus


# автотесты
def test_calculate_bonus():
    assert calculate_bonus(10, 0, 100000) == 30000
    assert calculate_bonus(2, 0, 100000) == 25000
    assert calculate_bonus(1, 0, 100000) == 15000
    assert calculate_bonus(0.5, 0, 100000) == 15000
    assert calculate_bonus(0.25, 0, 100000) == 15000
    assert calculate_bonus(0.25, 0, 50000) == 7500
    assert calculate_bonus(0, 0, 100000) == 0
    assert calculate_bonus(10, 10, 100000) == 30000
    assert calculate_bonus(3, 0, 100000) == 30000
    assert calculate_bonus(1.5, 0, 100000) == 25000
    print("Все тесты пройдены успешно!")


test_calculate_bonus()
