import pika
import sys



def main():
    params = pika.ConnectionParameters(
            host='krtkskrabbitmq-dev.krthomolog.com.br',
            port='5672',
            credentials=pika.PlainCredentials('backbone', '12345'))
    
    connection = pika.BlockingConnection(params)
    
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f"Mensagem: {body}")

    channel.basic_consume(queue='queue.captacao.ofertas.preco.backbone',
                          on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrompendo")
        sys.exit(0)
