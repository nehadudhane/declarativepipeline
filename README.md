# Databricks Declarative Pipelines — Bronze, Silver & Gold

A Databricks data engineering project demonstrating declarative pipeline definitions, PySpark transformations, streaming ingestion, data-quality expectations, Auto CDC, slowly changing dimensions, and sales analytics using a medallion architecture.

## Project architecture

```text
Customers, Products, Sales East & Sales West
                      |
                      v
Bronze: streaming ingestion + data quality
                      |
                      v
Silver: transformations + Auto CDC (SCD Type 1)
                      |
                      v
Gold: fact_sales, dim_customers, dim_products, business_sales
```

## Technology stack

- Databricks declarative pipelines (Delta Live Tables / `dlt` API)
- Python and PySpark
- Structured Streaming
- Auto CDC, SCD Type 1 and SCD Type 2
- Databricks SQL
- Bronze–Silver–Gold medallion architecture

## Source assets

The project includes source SQL notebooks and pipeline transformations under `DLT_root/transformations_SourceCode/`, grouped by Bronze, Silver, and Gold processing layers.

### Bronze
Streaming ingestion of customers and products with validation expectations, plus append flows combining sales from East and West sources.

### Silver
Data standardization and derived fields, with Auto CDC for customer, product, and sales records using SCD Type 1.

### Gold
Sales fact modeling, SCD Type 2 dimensions for customers and products, and an aggregated business sales dataset by region and category.

## Repository organization

```text
├── README.md
├── DWH_source.dbquery.ipynb
├── source_orders.dbquery.ipynb
└── DLT_root/
    ├── README.md
    ├── explorations/
    ├── utilities/
    └── transformations_SourceCode/
        ├── bronze/
        ├── silver/
        ├── gold/
        └── tutorial/
```

## Notes

The existing pipeline and notebook files are preserved as provided. This README describes the committed project artifacts, not a verified deployment or performance benchmark.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
