# CSV Faker

## Usage

For example, to generate 100 rows of random data based on `input.csv`'s
contents:

```bash
cat input.csv | docker run --rm --interactive busser/csv-faker --rows 100
```

## Performance

Running this script in a Docker container is significantly slower than running
it directly on the system. This is probably due to the fact that the script
does a lot of I/O.
