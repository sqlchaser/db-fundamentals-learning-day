# Databricks notebook source
# MAGIC %md
# MAGIC # Learning Day Notebook #
# MAGIC
# MAGIC Code is easy to notate when you can leverage Markdown!
# MAGIC Simple Notebook that will install the mlops-end2end Demo in your Databricks Workspace

# COMMAND ----------

# DBTITLE 1,Install dbDemos
pip install dbdemos

# COMMAND ----------

# DBTITLE 1,List Demos Available - Many!
import dbdemos
dbdemos.list_demos()

# COMMAND ----------

# MAGIC %md
# MAGIC _We're going to Install the mlops-end2end demo for use in our Learning Day_

# COMMAND ----------

# DBTITLE 1,Install mlops-end2end
import dbdemos
dbdemos.install('mlops-end2end')

# COMMAND ----------

# MAGIC %md
# MAGIC **Note: You may see errors in the demo pipeline that is generated - these are OK for the sake of this demo**