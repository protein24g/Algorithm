SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
CASE WHEN STATUS = "SALE" THEN "판매중"
WHEN STATUS = "RESERVED" THEN "예약중"
ELSE "거래완료"
END STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE LIKE "2022-10-05"
ORDER BY BOARD_ID DESC