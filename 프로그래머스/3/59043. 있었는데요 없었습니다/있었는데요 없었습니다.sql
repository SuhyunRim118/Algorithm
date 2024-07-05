SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I, ANIMAL_OUTS AS O
WHERE I.ANIMAL_ID=O.ANIMAL_ID and I.DATETIME > O.DATETIME
ORDER BY I.DATETIME;