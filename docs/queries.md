# Runs out of Memory, Gets killed by OOM

1. SELECT "trace_id", MAX("time") AS t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;

2. SELECT "trace_id" FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" LIMIT 20;

# Does not run out of memory

3. SELECT "trace_id" FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) LIMIT 20;

### Logical Plan

```bash
Projection: spans.trace_id

    Limit: skip=0, fetch=20

        TableScan: spans projection=[service.name, time, trace_id], full_filters=[spans.service.name = Dictionary(Int32, Utf8("frontend")), spans.time >= TimestampNanosecond(1688713200000000000, None), spans.time <= TimestampNanosecond(1689000240000000000, None)], fetch=20
```

### Physical Plan

```bash
ProjectionExec: expr=[trace_id@2 as trace_id]
    GlobalLimitExec: skip=0, fetch=20
        CoalescePartitionsExec
            UnionExec
                CoalesceBatchesExec: target_batch_size=8192
                    FilterExec: service.name@0 = frontend AND time@1 >= 1688713200000000000 AND time@1 <= 1689000240000000000
                        ParquetExec: file_groups={2 groups: [[1/3/43a5cfe042906bdb21727b26e30883262ec8ff4f7b30d59eb3906cfcb828cd91/02a04d8e-e31c-4a14-a287-a77dc1820df7.parquet], [1/3/43a5cfe042906bdb21727b26e30883262ec8ff4f7b30d59eb3906cfcb828cd91/d0f8798c-ca80-433e-8d29-be3c7492f7fd.parquet]]}, projection=[service.name, time, trace_id], output_ordering=[service.name@0 ASC], predicate=service.name@5 = frontend AND time@9 >= 1688713200000000000 AND time@9 <= 1689000240000000000, pruning_predicate=service.name_min@0 <= frontend AND frontend <= service.name_max@1 AND time_max@2 >= 1688713200000000000 AND time_min@3 <= 1689000240000000000
                            ProjectionExec: expr=[service.name@1 as service.name, time@3 as time, trace_id@4 as trace_id]
                                DeduplicateExec: [service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC]
                                    SortPreservingMergeExec: [service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC,__chunk_order@0 ASC]
                                        SortExec: expr=[service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC,__chunk_order@0 ASC]
                                            CoalesceBatchesExec: target_batch_size=8192
                                                FilterExec: service.name@1 = frontend AND time@3 >= 1688713200000000000 AND time@3 <= 1689000240000000000
                                                    ParquetExec

```

4. SELECT * FROM 'spans' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');

5. SELECT * FROM 'logs' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');

6. SELECT * FROM 'span-links' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');
