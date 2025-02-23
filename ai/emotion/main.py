from kafka import KafkaConsumer
from json import loads
from s3_reader import s3_image_reader
from emotion import emotion

# 카프카 서버
bootstrap_servers = ["kafka:9092"]

# 카프카 토픽
str_topic_name = 'FEELINGS'

# 카프카 소비자 group1 생성
str_group_name = 'group1'
consumer = ''
try:
    print("카프카 소비자 생성 시작", flush=True)
    consumer = KafkaConsumer(str_topic_name, bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest', # 가장 처음부터 소비
                             enable_auto_commit=True,
                             group_id=str_group_name,
                             value_deserializer=lambda x: loads(x.decode('utf-8'))
                            )
    print("카프카 소비자 생성", flush=True)
except Exception as e:
    print("카프카 소비자 생성 실패:", e, flush=True)

for message in consumer:
    try:
        print("감정 분석 요청", message, flush=True)
        image_data = s3_image_reader(message.value['imageKey'])
        emotion(image_data, message.value['imageKey'], message.value['memberId'], message.value['quizId'], message.value['correctAnswer'] )
    except Exception as e:
        print("물체 분석 실패:", e, flush=True)