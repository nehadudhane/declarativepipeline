# #creating an end-to-end basic pipeline

# import dlt


# #Staging Area

# @dlt.table(
#     name="staging_orders"
#     )
# def staging_orders():
#   df=spark.readStream.table("dltneha.source.orders")
#   return df

# #creating transformed area

# @dlt.view(
#     name="transformed_orders"
# )

# def  transformed_orders():
#     df = spark.readStream.table("staging_orders")
#     return df