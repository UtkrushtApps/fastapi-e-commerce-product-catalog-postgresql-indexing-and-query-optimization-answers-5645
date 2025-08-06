# Solution Steps

1. Analyze the current product filtering queries and determine that simultaneous filtering by category and brand is slow due to lack of efficient indexes.

2. Design and implement a composite index in the PostgreSQL schema (preferably via Alembic migration) to cover both category_id and brand_id columns in the products table, so the database can efficiently filter by both properties.

3. (Optional) Check if there are unnecessary/duplicated indexes to clean up, reducing write overhead and bloat.

4. In the app's database access layer, ensure that queries are written to take advantage of the indexes. Use SQLAlchemy's async interface to keep queries non-blocking and efficient.

5. Change the query logic in the product filter endpoint to use SQLAlchemy's async Session and build dynamic filter conditions using the 'and_' operator for composability.

6. Ensure pagination is in place with offset/limit for scalability.

7. Test query speed with filtering: verify that results are returned in under 500ms and SQL 'EXPLAIN ANALYZE' uses the new composite index.

