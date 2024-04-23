"""
Pub Sub Low Level Design:
1. Publisher publishes messages to Topics
    a. topics: list[Topic]
    - publish(Topic t, Message m) 
        - Create topic if does not exist
    - addTopic(topic t)
    - removeTopic(topic t)
2. Message m consists of schema:
    m: {id, body}
3. Subscriber can subscribe to certain topics
    a. subscribed_topics: list[Topic]
    - subscribe(Topic t, Callable callback)
4. PubSubService class
    - addToQueue(Message m, Topic t)
    - createQueueForTopic(Topic t)
    - clearQueueForTopic(Topic t)
"""