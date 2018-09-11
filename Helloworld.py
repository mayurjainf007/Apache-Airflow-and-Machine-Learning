from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta
from oss import rsakey,dirlis,install,faceid,vidcap
from twitterstream import maintts,fetchsample
from fetch import read,top_10
from exit import end
from pathlib import Path

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'mayurjain',
    'depends_on_past': False,
    'start_date': datetime(2018, 7, 21),
    'email': ['mayurjain333@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Helloworld', default_args=default_args)


t1 = PythonOperator(task_id='Installation', python_callable=install, dag=dag)

t2 = PythonOperator(task_id='Twitter_Authorisation', python_callable=maintts, dag=dag)
t3 = PythonOperator(task_id='Fetching_Data', python_callable=fetchsamples, dag=dag)

t4 = PythonOperator(task_id='RSA_Key_256SHA', python_callable=rsakey, dag=dag)
t5 = PythonOperator(task_id='Directory_List', python_callable=dirlis, dag=dag)

t6 = PythonOperator(task_id='Face_Detection', python_callable=faceid, dag=dag)
t7 = PythonOperator(task_id='Video_Capture', python_callable=vidcap, dag=dag)

t8 = PythonOperator(task_id='Read_Validate_Json', python_callable=read, dag=dag)
t9 = PythonOperator(task_id='TOP_10_Places', python_callable=top_10, dag=dag)

tf = PythonOperator(task_id='End_Point', python_callable=end, dag=dag)


t2.set_upstream(t1)
t4.set_upstream(t1)
t3.set_upstream(t2)
t5.set_upstream(t4)
t8.set_upstream(t3)
t9.set_upstream(t8)
t6.set_upstream(t5)
t7.set_upstream(t6)
tf.set_upstream(t7,t9)
