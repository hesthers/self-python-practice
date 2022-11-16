-- Hackerrank question -> 'Challenges'

SELECT H.HACKER_ID AS ID, H.NAME AS N, COUNT(*) AS CNT
FROM CHALLENGES AS C
    JOIN HACKERS AS H
    ON H.HACKER_ID = C.HACKER_ID
GROUP BY C.HACKER_ID, H.NAME
HAVING CNT IN (       
                                    SELECT CH.CNT
                                    FROM (
                                            SELECT HACKER_ID, COUNT(*) AS CNT
                                            FROM CHALLENGES
                                            GROUP BY HACKER_ID
                                          ) AS CH
                                    GROUP BY CH.CNT
                                    HAVING COUNT(*) = 1
                                 )
    OR CNT = (
                                SELECT MAX(CH2.CNT) 
                                FROM (
                                        SELECT HACKER_ID, COUNT(*) AS CNT
                                        FROM CHALLENGES
                                        GROUP BY HACKER_ID
                                     ) AS CH2
                             )        
ORDER BY COUNT(C.HACKER_ID) DESC, H.HACKER_ID
