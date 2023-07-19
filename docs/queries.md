# Runs out of Memory, Gets killed by OOM

1. SELECT "trace_id", MAX("time") AS t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;

2. SELECT "trace_id" FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" LIMIT 20;

# Does not run out of memory

3. SELECT "trace_id" as t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) LIMIT 20;

4. SELECT * FROM 'spans' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');

5. SELECT * FROM 'logs' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');

6. SELECT * FROM 'span-links' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');
