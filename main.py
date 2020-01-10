import requests

sendMode = True

def send_data(webhookUrl, message, mode=sendMode):
    sendContent = {
        "content": message
    }
    requests.post(webhookUrl,sendContent)
    print('\n送信先: {}\nメッセージ: {}で送信しました。'.format(webhookUrl,
                                                        message))

    if mode:
        print('\n継続モードのため、続けて送信を行います。')
        input_send_data(webhookUrl)
    

def input_send_data(webhookUrl=None):
    if webhookUrl == None:
        print('ようこそDiscord Webhook Senderへ\n'
            +'まずは送信先のWebhook URLを入力してください。')

        webhookUrl = input('>>> ')

    print('\n送信先: {}\n'.format(webhookUrl)
        +'次に送信メッセージを入力してください。')

    message = input('>>> ')

    send_data(webhookUrl, message)

if __name__ == "__main__":
    input_send_data()