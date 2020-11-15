#### 1.1 Airflow安装
```shell script
pip3 install apache-airflow -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

#### 1.2 Airflow配置 

在 /etc/profile 文件添加内容   
```
export AIRFLOW_HOME=/home/airflow
```

使前述各项配置立即生效
```
source /etc/profile
```

#### 2 初始化
#### 2.1 配置sqlite
直接运行 airflow initdb , airflow会在 /home/airflow 下生成 airflow.db
#### 2.2 配置MySQL

设置 /home/airflow/airflow.cfg 的两个属性
```
# executor = SequentialExecutor
executor = LocalExecutor

sql_alchemy_conn = mysql+pymysql://username:password@host/dbname
```
检查目标库设置
``` SQL
show global variables like '%timestamp%';
set global explicit_defaults_for_timestamp =1;
```
运行 airflow initdb , airflow会完成建表