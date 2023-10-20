SELECT MCDP_CD "진료과코드", COUNT(MCDP_CD) "5월예약건수"
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD), MCDP_CD