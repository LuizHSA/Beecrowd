/*
2602
SELECT name
FROM customers
WHERE state = 'RS'


2603
SELECT name, street
FROM customers
WHERE city = 'Porto Alegre'

2604
SELECT id, name
FROM products
WHERE price < 10 OR price > 100;

2605
SELECT
  p.name,
  pr.name
FROM
  products AS p
JOIN
  providers AS pr ON p.id_providers = pr.id
JOIN
  categories AS c ON p.id_categories = c.id
WHERE
  c.name = 'executive';

2606
SELECT
  p.id,
  p.name
FROM
  products AS p
JOIN 
  categories AS c ON p.id_categories = c.id
WHERE
  c.name LIKE 'super%;

2607
SELECT city
FROM providers
ORDER BY city

2608
SELECT
  MAX(price),
  MIN(price)
FROM products 

2609
SELECT
  c.name,
  SUM(p.amount) AS sum
FROM
  categories AS c
JOIN
  products AS p ON c.id = p.id_categories
GROUP BY
  c.name
ORDER BY
  c.name

2610
