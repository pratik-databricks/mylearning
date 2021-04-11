# Databricks notebook source
# MAGIC %sh
# MAGIC #!/bin/bash
# MAGIC /dbfs/databricks/scripts/postgresql-install.sh

# COMMAND ----------

dbutils.fs.put("/databricks/scripts/python-lib-install.sh","""
#!/bin/bash
set -ex
/databricks/python/bin/python -V
. /databricks/conda/etc/profile.d/conda.sh
conda activate /databricks/python
conda install -y astropy""", True)

# COMMAND ----------

# MAGIC %sh
# MAGIC #!/bin/bash
# MAGIC /dbfs/databricks/scripts/python-lib-install.sh

# COMMAND ----------

# MAGIC 
# MAGIC %conda install mkl