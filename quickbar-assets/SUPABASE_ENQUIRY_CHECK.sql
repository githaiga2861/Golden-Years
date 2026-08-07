-- The quick modal saves into your EXISTING 'enquiries' table — no new
-- table needed. This just confirms the table and its policies exist.
select table_name from information_schema.tables where table_name = 'enquiries';
select policyname from pg_policies where tablename = 'enquiries';
