
import findspark
findspark.init()

from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .appName("DeviceIoTData") \
    .getOrCreate()

from dataclasses import dataclass

class DeviceIoTData:
    battery_level: int
    c02_level: int
    cca2: str
    cca3: str
    cn: str
    device_id: int
    device_name: str
    humidity: int
    ip: str
    latitude: float
    lcd: str
    longitude: float
    scale: str
    temp: int
    timestamp: int

df = spark.read.json("/Users/sunghoon/Desktop/file/iot_devices-2.json") #본인 파일 경로


df.show(5, truncate=False)

filterTempDF = df.filter((df.temp > 30) & (df.humidity > 70))

filterTempDF = filterTempDF.drop('scale', 'timestamp') #혹시나 겹치는 부분이 있다면 제거 (안해도 됨)

filterTempDF.show(5, truncate = False)

from pyspark.sql.functions import col #지정을 위해서 Col 가져옴

class DeviceTempByCountry:
    temp: int
    device_name: str
    device_id:int
    cca3: str
# temp가 25 이상인 데이터 필터링
dfTemp = df.filter(col('temp') > 25) \
           .select(
               col('temp'),
               col('device_name'),
               col('device_id'),
               col('cca3')
           )

# 결과 확인
dfTemp.show(5, truncate=False)

#데이터 세트 첫 열 

device = dfTemp.columns[0]

device_c = df.select(device)

device_c.show(5, truncate = False)

#데이터 세트 첫 행

device_r = dfTemp.first()

print(device_r)

#where 을 활용한 방법

dfTemp2 = (df.select(col("temp"), col("device_name"), col("device_id"), col("cca3"))
             .where(df.temp > 25 ))

dfTemp2.show(5, truncate = False)







# %%



