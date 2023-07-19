# Runs out of Memory, Gets killed by OOM

1. 
```
SELECT "trace_id", MAX("time") AS t FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" ORDER BY t DESC LIMIT 20;
```

2. 
```
SELECT "trace_id" FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) GROUP BY "trace_id" LIMIT 20;
```

### Logical Plan

```bash
Limit: skip=0, fetch=20   
    Aggregate: groupBy=[[spans.trace_id]], aggr=[[]]
        Projection: spans.trace_id
            TableScan: spans projection=[service.name, time, trace_id], full_filters=[spans.service.name = Dictionary(Int32, Utf8("frontend")), spans.time >= TimestampNanosecond(1688713200000000000, None), spans.time <= TimestampNanosecond(1689000240000000000, None)]
```

### Physical Plan

```bash
GlobalLimitExec: skip=0, fetch=20
    CoalescePartitionsExec
        AggregateExec: mode=FinalPartitioned, gby=[trace_id@0 as trace_id], aggr=[]
            CoalesceBatchesExec: target_batch_size=8192
                RepartitionExec: partitioning=Hash([trace_id@0], 10), input_partitions=10
                    AggregateExec: mode=Partial, gby=[trace_id@0 as trace_id], aggr=[]
                        RepartitionExec: partitioning=RoundRobinBatch(10), input_partitions=3
                            UnionExec
                                ProjectionExec: expr=[trace_id@2 as trace_id]   
                                    CoalesceBatchesExec: target_batch_size=8192
                                        FilterExec: service.name@0 = frontend AND time@1 >= 1688713200000000000 AND time@1 <= 1689000240000000000
                                            ParquetExec: file_groups={2 groups: [[1/3/43a5cfe042906bdb21727b26e30883262ec8ff4f7b30d59eb3906cfcb828cd91/02a04d8e-e31c-4a14-a287-a77dc1820df7.parquet], [1/3/43a5cfe042906bdb21727b26e30883262ec8ff4f7b30d59eb3906cfcb828cd91/d0f8798c-ca80-433e-8d29-be3c7492f7fd.parquet]]}, projection=[service.name, time, trace_id], output_ordering=[service.name@0 ASC], predicate=service.name@5 = frontend AND time@9 >= 1688713200000000000 AND time@9 <= 1689000240000000000, pruning_predicate=service.name_min@0 <= frontend AND frontend <= service.name_max@1 AND time_max@2 >= 1688713200000000000 AND time_min@3 <= 1689000240000000000
                                                ProjectionExec: expr=[trace_id@4 as trace_id]
                                                    DeduplicateExec: [service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC]
                                                        SortPreservingMergeExec: [service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC,__chunk_order@0 ASC]
                                                            SortExec: expr=[service.name@1 ASC,trace_id@4 ASC,span_id@2 ASC,time@3 ASC,__chunk_order@0 ASC]
                                                                CoalesceBatchesExec: target_batch_size=8192
                                                                    FilterExec: service.name@1 = frontend AND time@3 >= 1688713200000000000 AND time@3 <= 1689000240000000000
                                                                        ParquetExec: file_groups={10 groups: [[1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/169e5e5c-dcb6-4089-8f9f-d39bce4ab6bc.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/5c05e20f-69dd-40bc-a828-688456940c24.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/d9113bee-6244-41f2-84a9-03b104b246b4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/f532bc39-d052-49cb-aef4-145014e1b7e4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/0b28d0e1-2d12-4819-a660-cb844655e15e.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/ba01c02c-b38d-4adb-8f20-a68c993874ba.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3b4326c3-d16b-436f-b5ab-cd6681aeb3bf.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/56c04fd7-c5cb-4d4b-be4f-888140c0ec9f.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/f370107b-b7b1-47db-9198-4dbfada7e2fb.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/6fa26594-a9c0-4bae-82bd-696f97571158.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/6e330dd5-6856-4134-8cc4-f4e2bf96fd2b.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/fc5daa2e-3007-472c-ab9d-a64ba834cd0e.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3107d952-b4ef-4f4c-8b13-a4dc8236c66a.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/63ca1a54-0a28-4938-9f26-2323cbe318ad.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/80ab19f8-e0b9-4659-8b63-be98406083af.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/b6a5c8cd-4253-402b-bdc4-8cb829fad874.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3b696809-6f86-46d3-8497-cfe2aee1907f.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/e547e24a-f3a3-4cf0-b019-c5f934b4c539.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/9313f401-e15f-45f9-9ff6-52f660230ab4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/badfed4f-2065-41b4-8754-02147cd15feb.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/64ce5a05-e9e8-46a8-8389-09914564177e.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/e0c8cba1-978b-48a9-81a5-dc8f745117a3.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/84ee9663-6114-4e7b-8171-d9b7a466ef45.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/4b41cb50-8e42-4dd4-aa75-65c0b4730730.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/145ea4bc-9d39-474c-8281-e966606efc3b.parquet, ...], ...]}, projection=[__chunk_order, service.name, span_id, time, trace_id], predicate=service.name@5 = frontend AND time@9 >= 1688713200000000000 AND time@9 <= 1689000240000000000, pruning_predicate=service.name_min@0 <= frontend AND frontend <= service.name_max@1 AND time_max@2 >= 1688713200000000000 AND time_min@3 <= 1689000240000000000
```

# Does not run out of memory

3. 
```
SELECT "trace_id" FROM 'spans' WHERE "service.name" = 'frontend' AND "time" >= to_timestamp(1688713200000000000) AND "time" <= to_timestamp(1689000240000000000) LIMIT 20;
```

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
                                                    ParquetExec: file_groups={10 groups: [[1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/169e5e5c-dcb6-4089-8f9f-d39bce4ab6bc.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/5c05e20f-69dd-40bc-a828-688456940c24.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/d9113bee-6244-41f2-84a9-03b104b246b4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/f532bc39-d052-49cb-aef4-145014e1b7e4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/0b28d0e1-2d12-4819-a660-cb844655e15e.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/ba01c02c-b38d-4adb-8f20-a68c993874ba.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3b4326c3-d16b-436f-b5ab-cd6681aeb3bf.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/56c04fd7-c5cb-4d4b-be4f-888140c0ec9f.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/f370107b-b7b1-47db-9198-4dbfada7e2fb.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/6fa26594-a9c0-4bae-82bd-696f97571158.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/6e330dd5-6856-4134-8cc4-f4e2bf96fd2b.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/fc5daa2e-3007-472c-ab9d-a64ba834cd0e.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3107d952-b4ef-4f4c-8b13-a4dc8236c66a.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/63ca1a54-0a28-4938-9f26-2323cbe318ad.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/80ab19f8-e0b9-4659-8b63-be98406083af.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/b6a5c8cd-4253-402b-bdc4-8cb829fad874.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/3b696809-6f86-46d3-8497-cfe2aee1907f.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/e547e24a-f3a3-4cf0-b019-c5f934b4c539.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/9313f401-e15f-45f9-9ff6-52f660230ab4.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/badfed4f-2065-41b4-8754-02147cd15feb.parquet, ...], [1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/64ce5a05-e9e8-46a8-8389-09914564177e.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/e0c8cba1-978b-48a9-81a5-dc8f745117a3.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/84ee9663-6114-4e7b-8171-d9b7a466ef45.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/4b41cb50-8e42-4dd4-aa75-65c0b4730730.parquet, 1/3/25a784d7942535df9ef4d026e24922682e3fb22583d4329da020367fed84efe8/145ea4bc-9d39-474c-8281-e966606efc3b.parquet, ...], ...]}, projection=[__chunk_order, service.name, span_id, time, trace_id], predicate=service.name@5 = frontend AND time@9 >= 1688713200000000000 AND time@9 <= 1689000240000000000, pruning_predicate=service.name_min@0 <= frontend AND frontend <= service.name_max@1 AND time_max@2 >= 1688713200000000000 AND time_min@3 <= 1689000240000000000
```

4. Select all the spans for a particular trace Id.
```
SELECT * FROM 'spans' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');
```



5. Select all the logs for a particular trace Id.
```
SELECT * FROM 'logs' WHERE "trace_id" IN ('00000000000000000000267cc6e91edb');
```
