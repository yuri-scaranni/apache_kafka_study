README

projeto kafka

ideias:
- criar imagem do kafka com mais comandos de shell como 'clear' por exemplo.
- criar o kafka server com producer/consumer e criar python produce/consumer pra utilizar esse conteúdo docker.
- colocar esses pythons em dags.

comandos:
docker-compose ps -->> listar itens do compose
docker exec -it apache_kafka-kafka-1-1 bash -->> entra na máquina
kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 3 --partitions 3 --topic meutopico -->> criar tópico
kafka-topics --list --bootstrap-server localhost:29092 -->> listar tópicos
kafka-console-producer --broker-list localhost:29092 --topic meutopico -->> abre escrita no tópico.
kafka-console-consumer --bootstrap-server localhost:29092 --topic meutopico -->> abre leitura do tópico.
kafka-console-consumer --bootstrap-server localhost:29092 --topic meutopico --from-beginning -->> abre leitura do tópico desde início.
kafka-console-consumer --bootstrap-server localhost:29092 --topic meutopico --from-beginning --group a -->> '' c/ grupo.


docker exec -it 6a491e1c20f5 bash

kafka-topics --create --bootstrap-server localhost:29092 --replication-factor 1 --partitions 3 --topic projetoxicotopic3
kafka-console-consumer --bootstrap-server localhost:29092 --topic projetoxicotopic3 --from-beginning --group pjtx_1

--delete groups
kafka-consumer-groups --bootstrap-server localhost:29092 --delete --group 'console-consumer-35771'

--delete topicos
kafka-topics --bootstrap-server localhost:29092 --topic projetoxicotopic2 --delete

--list groups
kafka-consumer-groups --offset --bootstrap-server localhost:29092


kafka-consumer-groups --bootstrap-server localhost:29092 --describe --group console-consumer-35771 --state
