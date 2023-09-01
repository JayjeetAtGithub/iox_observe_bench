## Benchmarking Row conversion on low and high cardinality dicts W/ dict preserving

```bash
convert_columns row_conv_low_card_preserve
                        time:   [74.488 µs 75.092 µs 75.683 µs]
                        change: [-2.9368% -2.0388% -1.1049%] (p = 0.00 < 0.05)
                        Performance has improved.
Found 2 outliers among 100 measurements (2.00%)
  2 (2.00%) high mild

convert_columns row_conv_low_card_no_preserve
                        time:   [98.062 µs 100.62 µs 103.11 µs]
                        change: [+6.9081% +8.6130% +10.458%] (p = 0.00 < 0.05)
                        Performance has regressed.
Found 6 outliers among 100 measurements (6.00%)
  6 (6.00%) high mild

Benchmarking convert_columns row_conv_high_card_preserve: Warming up for 3.0000 s
Warning: Unable to complete 100 samples in 5.0s. You may wish to increase target time to 8.9s, enable flat sampling, or reduce sample count to 50.
convert_columns row_conv_high_card_preserve
                        time:   [1.6723 ms 1.6792 ms 1.6868 ms]
                        change: [+1.4646% +2.6848% +3.9482%] (p = 0.00 < 0.05)
                        Performance has regressed.
Found 7 outliers among 100 measurements (7.00%)
  6 (6.00%) high mild
  1 (1.00%) high severe

convert_columns row_conv_high_card_no_preserve
                        time:   [291.13 µs 293.96 µs 296.85 µs]
                        change: [+7.0485% +8.3143% +9.6703%] (p = 0.00 < 0.05)
                        Performance has regressed.
Found 9 outliers among 100 measurements (9.00%)
  3 (3.00%) low severe
  4 (4.00%) low mild
  2 (2.00%) high mild
```

**Observation:** For low cardinality, preserving dict is beneficial, but for high cardinality, preserving is highly damaging.
