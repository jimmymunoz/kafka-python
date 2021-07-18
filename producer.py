import time
from kafka import KafkaProducer
from faker import Faker

faker = Faker()

producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'])
for _ in range(100):
  name = faker.name().encode('utf-8')
  producer.send('names', name)
  print(name)
time.sleep(20)