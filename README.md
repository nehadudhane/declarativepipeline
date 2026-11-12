# Databricks Declarative Pipelines | Bronze–Silver–Gold

A Databricks data engineering project demonstrating **streaming ingestion**, **data quality expectations**, **Auto CDC**, **SCD Type 1 and Type 2**, and sales analytics using a medallion architecture.

The original Python and SQL notebook contents are preserved; files are grouped by purpose to make this repository easier to navigate.

## Architecture

```text
Customer, product and regional sales source tables
                        |
                        v
              BRONZE / Ingestion
     Streaming reads, expectations, append flows
                        |
                        v
             SILVER / Enrichment
         Transformations, Auto CDC (SCD 1)
                        |
                        v
              GOLD / Analytics
  fact_sales | dim_customers | dim_products
               business_sales
```

## Technology stack

**Databricks Declarative Pipelines (DLT API)** · **PySpark** · **Spark Structured Streaming** · **Databricks SQL** · **Auto CDC** · **Medallion Architecture**

## Project structure

```text
declarativepipeline/
├── README.md
├── notebooks/
│   ├── DWH_source.dbquery.ipynb
│   └── source_orders.dbquery.ipynb
├── pipelines/
│   ├── bronze/
│   │   ├── ingest_customers.py
│   │   ├── ingestion_products.py
│   │   └── ingestion_sales.py
│   ├── silver/
│   │   ├── transform_customers.py
│   │   ├── Transform_product.py
│   │   └── transform_sales.py
│   └── gold/
│       ├── fact_sales.py
│       ├── dim_customers.py
│       ├── dim_products.py
│       └── business_sales.py
├── utilities/
│   └── utils.py
└── examples/
    ├── 1_CoreComponents.py
    ├── 2_dependency.py
    └── sample_exploration.py
```

## Data layers

### Bronze — raw streaming ingestion

[`pipelines/bronze/`](pipelines/bronze/) contains customer and product ingestion scripts, plus sales ingestion with append flows for East and West sales records. Data-quality expectations are defined as part of the ingestion logic.

### Silver — curated data and CDC

[`pipelines/silver/`](pipelines/silver/) contains customer, product and sales transformations and Auto CDC definitions. The source code demonstrates SCD Type 1 change handling and derivation of analytical fields such as sales totals.

### Gold — analytical model

[`pipelines/gold/`](pipelines/gold/) contains a sales fact definition, customer and product dimensions (including SCD Type 2 logic), and aggregated business sales by region and product category.

### SQL notebooks and supporting material

- [`notebooks/`](notebooks/) provides the source-table SQL notebooks and sample records.
- [`utilities/`](utilities/) contains a PySpark email-validation utility.
- [`examples/`](examples/) retains exploratory and tutorial examples.

## Scope and usage

The project uses environment-specific source table references and Databricks pipeline definitions. To use it in a different workspace, configure source tables, permissions and pipeline resources for that environment. This README documents the checked-in artifacts; it does not assert independently verified deployment or run results.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
