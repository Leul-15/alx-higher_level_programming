-- displays the average temperature
-- by city ordered by descending temperature
SELECT city, avg(value) AS avg_temp FROM temperatures GROUP BY city
ORDER BY avg_temp DESC
