SELECT A.FLAVOR
FROM FIRST_HALF A
INNER JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
    AND TOTAL_ORDER >= 3000
    AND INGREDIENT_TYPE LIKE "fruit%"
