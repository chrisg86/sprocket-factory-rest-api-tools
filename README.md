# Sprocket Factory REST API Tools

This repo serves as a collection of tools used to bring json example data into the right format to be imported into the MySQL database used in the main repository [https://github.com/chrisg86/sprocket-factory-rest-api](https://github.com/chrisg86/sprocket-factory-rest-api)

## Usage

I used Python 3.9 to convert the files. In total there is one file for each example data json.

- `src/factory_data_to_sql.py` to convert aggregated factory data into single entities.
- `src/sprocket_data_to_sql.py` to translate json sprockets into sql.

Both scripts will pull the correct file from the `data/` folder and will print the sql statements to stdout, so you can just redirect the output to whatever file you'd like.

Example usage:

factory_data_to_sql

```
python3.9 src/factory_data_to_sql.py > data/seed_factory_data.sql
```

sprocket_data_to_sql

```
python3.9 src/sprocket_data_to_sql.py > data/seed_sprocket_types.sql
```
