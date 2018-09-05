# CSV Faker

## Usage

For example, to generate 100 rows of random data based on `input.csv`'s
contents:

```bash
cat input.csv | docker run --rm --interactive busser/csv-faker --rows 100
```
