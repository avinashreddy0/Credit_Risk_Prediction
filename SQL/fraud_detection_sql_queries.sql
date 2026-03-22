create database fraud
use fraud

select * from fraud

-- task 1
-- What is the overall fraud rate in the transaction dataset?

select count(*) as total_rows,sum(fraud) as total_fraud,
round(sum(fraud) * 100.0 / count(*),2) as fraud_rate
from fraud

-- taks 2
-- Which locations have the highest fraud rate, and how does it compare to the overall fraud rate?

select count(*) as total_rows,sum(fraud) as fraud ,location,
round(sum(fraud)*100.0/count(*),2) as total_fraud_rate
from fraud
group by location
order by total_fraud_rate desc
limit 1

-- take 3
-- Which device types are most frequently used in fraudulent transactions?

select count(*) as total_rows,sum(fraud) as total_fraud,device_type,
round(sum(fraud)*100.0/count(*),2) as total_fraud_rate
from fraud
group by device_type
order by total_fraud_rate desc
limit 1

-- take 4
-- What is the average transaction amount for fraud vs non-fraud transactions, and how large is the difference?

select fraud,avg(amount) as total_amount
from fraud
group by fraud

-- task 5
-- Which accounts have the highest number of fraudulent transactions?

select customer_id,count(*) as fraud_transactions
from fraud
where fraud = 1
group by customer_id
order by fraud_transactions desc
limit 5

-- task 6
-- What transaction amount ranges (low, medium, high) show the highest fraud probability?

select 
case
 when amount <= 10000 then 'low'
 when amount <= 20000 then 'medium'
else 'high'
 end as amount_transtation,
 count(*) as total_rows,
 sum(fraud) as total_fraud
 from fraud
 group by amount_transtation
 order by total_fraud desc

-- task 7
-- Which combination of location and device type has the highest fraud occurrence?

select sum(fraud) as total_fraud,location,device_type
from fraud
group by location,device_type
order by total_fraud desc
limit 3

-- task 8
-- How does the number of previous failed login attempts affect fraud probability?

select previous_failed_logins,sum(fraud) as total_fraud,count(*) as total_rows,
round(sum(fraud)*100.0 / count(*),2) as fraud_rate
from fraud
group by previous_failed_logins
order by fraud_rate desc
limit 3

-- task 9 
-- Identify suspicious transactions where the amount is much higher than the user’s average transaction amount.

select customer_id,amount
from fraud as f
where amount > (select avg(amount) from fraud where customer_id = f.customer_id)

-- task 10
-- -- Which users show repeated fraudulent activity within a short period of time, indicating potential account takeover?

select * from fraud

select customer_id,count(*) as total_fraud
from fraud
where fraud = 1 
group by customer_id
having count(*) > 2
order by total_fraud desc

