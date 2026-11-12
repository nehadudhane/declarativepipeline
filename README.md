# Databricks Declarative Pipelines | Bronze–Silver–Gold Data Engineering

A Databricks data engineering project demonstrating **declarative pipelines**, **streaming tables**, **data quality expectations**, **Auto CDC**, **slowly changing dimensions (SCD)**, and **sales analytics** using a medallion architecture.

This repository contains the original Databricks-exported source code and SQL notebooks. The working Python transformations and notebooks are preserved as supplied.

## Architecture

```text
Source tables (dltneha.source)
  ├── customers
  ├── products
  ├── sales_east
  └── sales_west
           │
           ▼
BRONZE — streaming ingestion
  ├── customers_stg       [data quality rules]
  ├── products_stg        [data quality rules]
  └── append_sales        [East + West append flows]
           │
           ▼
SILVER — enrichment + Auto CDC (SCD Type 1)
  ├── customers_enr       [uppercase customer names]
  ├── products_enr        [price cast to integer]
  └── sales_enr           [quantity × amount]
           │
           ▼
GOLD — modeled data + analytics
  ├── fact_sales          [Auto CDC, SCD Type 1]
  ├── dim_customers       [Auto CDC, SCD Type 2]
  ├── dim_products        [Auto CDC, SCD Type 2]
  └── business_sales      [sales by region and category]
```

## Technologies

- Databricks Declarative Pipelines / Delta Live Tables Python API (`dlt`)
- PySpark and Spark Structured Streaming
- Databricks SQL
- Change data capture with `dlt.create_auto_cdc_flow`
- SCD Type 1 and Type 2
- Data quality rules with `dlt.expect_all_or_drop`
- Medallion architecture (Bronze, Silver, Gold)

## Source Data

The provided `DWH_source.dbquery.ipynb` notebook defines sample source tables for **customers**, **products**, **sales_east**, and **sales_west**, along with example initial and incremental records. These feed the `dltneha.source` tables referenced by the Python pipeline. A separate `source_orders.dbquery.ipynb` contains an orders example used in tutorial/exploration code.

## Pipeline Implementation

### Bronze: ingestion and quality rules

The pipeline uses `spark.readStream.table(...)` to ingest customer and product datasets. Expectations drop records that fail key rules: customers require non-null IDs and names, while products require non-null IDs and non-negative prices.

Sales data from East and West source tables is combined into the `append_sales` streaming table using two named append flows. Sales records must have a non-null `sales_id`.

### Silver: transformations and change handling

The Silver transformations standardize and enrich the streamed data:

| Output | Transformation | CDC configuration |
|---|---|---|
| `customers_enr` | Uppercase `customer_name` | Customer key, `last_updated`, SCD 1 |
| `products_enr` | Cast `price` to integer | Product key, `last_updated`, SCD 1 |
| `sales_enr` | Calculate `total_amount = quantity × amount` | Sales key, `sale_timestamp`, SCD 1 |

All three are defined with `dlt.create_auto_cdc_flow`.

### Gold: analytical model

The Gold layer creates:

- **`fact_sales`** — sales facts using Auto CDC with SCD Type 1.
- **`dim_customers`** — customer dimension with SCD Type 2 history.
- **`dim_products`** — product dimension with SCD Type 2 history.
- **`business_sales`** — joins sales, customers, and products, then aggregates `total_sales` by region and product category.

## Repository Structure

```text
declarativepipelines/
├── README.md
├── DWH_source.dbquery.ipynb
├── source_orders.dbquery.ipynb
└── DLT_root/
    ├── README.md
    ├── explorations/
    │   └── sample_exploration.py
    ├── utilities/
    │   └── utils.py
    └── transformations_SourceCode/
        ├── tutorial/
        │   ├── 1_CoreComponents.py
        │   └── 2_dependency.py
        ├── bronze/
        │   ├── ingest_customers.py
        │   ├── ingestion_products.py
        │   └── ingestion_sales.py
        ├── silver/
        │   ├── transform_customers.py
        │   ├── Transform_product.py
        │   └── transform_sales.py
        └── gold/
            ├── fact_sales.py
            ├── dim_customers.py
            ├── dim_products.py
            └── business_sales.py
```

The `tutorial/` files contain commented learning examples. The nested `DLT_root/README.md` is the original Databricks-generated README, retained for reference.

## Data Flow Notes

- The source references use `dltneha.source`; when using a different Databricks workspace or catalog, provide equivalent source tables and appropriate access.
- `DWH_source.dbquery.ipynb` includes example update scenarios represented as additional SQL inserts. Its SQL is preserved as exported; whether each statement runs successfully depends on source-table state and constraints.
- The folder contains Python pipeline definitions but not a separate pipeline deployment configuration or execution logs. Runtime success and production readiness are not independently verified by this repository review.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
