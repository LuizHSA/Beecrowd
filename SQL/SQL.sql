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
