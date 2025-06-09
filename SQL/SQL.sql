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
SELECT
    ROUND(AVG(price), 2)
FROM
    products;

2611
SELECT
    m.id,
    m.name
FROM
    movies AS m
JOIN
    genres AS g ON m.id_genres = g.id
WHERE
    g.description = 'Action';

2613
SELECT
    m.id,
    m.name
FROM
    movies AS m
JOIN
    prices AS p ON m.id_prices = p.id
WHERE
    p.value < 2

2614
SELECT
    c.name,
    r.rentals_date
FROM
    customers AS c
JOIN
    rentals AS r ON c.id = r.id_customers
WHERE
    r.rentals_date BETWEEN '2016-09-01' AND '2016-09-30';

2615
SELECT
    city
FROM
    customers
GROUP BY
    city

2616
SELECT
    c.id,
    c.name
FROM
    customers AS c
LEFT JOIN
    locations AS l ON c.id = l.id_customers
WHERE
    l.id_customers IS NULL;

2617
SELECT
    p.name,
    pr.name
FROM
    products AS p
JOIN
    providers AS pr ON p.id_providers = pr.id
WHERE
    pr.name = 'Ajax SA';

2618
SELECT
    p.name,
    pr.name,
    c.name
FROM
    products AS p
JOIN 
    providers AS pr ON p.id_providers = pr.id
JOIN
    categories AS c ON p.id_categories = c.id
WHERE
    pr.name = 'Sansul SA' AND c.name = 'Imported'

2619
SELECT
    p.name,
    pr.name,
    p.price
FROM
    products AS p
JOIN 
    providers AS pr ON p.id_providers = pr.id
JOIN
    categories AS c ON p.id_categories = c.id
WHERE
    p.price > 1000 AND c.name = 'Super Luxury'

2620
SELECT
    c.name,
    o.id
FROM
    customers AS c
JOIN 
    orders AS o ON c.id = o.id_customers
WHERE
    o.orders_date BETWEEN '2016-01-01' AND '2016-06-30'

2621
SELECT
    p.name
FROM
    products AS p
JOIN 
    providers AS pr ON p.id_providers = pr.id
WHERE
    p.amount BETWEEN 10 AND 20 AND pr.name LIKE 'P%';

2622
SELECT
    c.name
FROM
    customers AS c
JOIN 
    legal_person AS l ON c.id = l.id_customers

2623
SELECT
    p.name,
    c.name
FROM
    products AS p
JOIN
    categories AS c ON p.id_categories = c.id
WHERE
    p.amount > 100 AND c.id IN (1, 2, 3, 6, 9)
ORDER BY
    c.id;

2624
SELECT 
    COUNT(DISTINCT city)
FROM 
    customers;

2625 -- terminar
SELECT 
    n.cpf
FROM 
    natural_person AS n
WHERE 
    cpf ~ '^\d{3}\.\d{3}\.\d{3}-\d{2}$';


