import dlt
#sales expectations
sales_rules={
    "rule_1":"sales_id is NOT NULL"
}


#empty streaming table
dlt.create_streaming_table(
    name="append_sales",
    expect_all_or_drop=sales_rules
)

#creating east sales flow
@dlt.append_flow(target='append_sales')
def east_sales():
    df=spark.readStream.table("dltneha.source.sales_east")
    return df

#creating west sales flow
@dlt.append_flow(target='append_sales')
def west_sales():
    df=spark.readStream.table("dltneha.source.sales_west")
    return df
    