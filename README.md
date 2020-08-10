# discord-webhook-sender

DiscordのWebhookを送信するやつです。    
なんと、ただそれだけ。

## 使い方

```
$ pipenv install // install dependencies

$ python main.py

ようこそDiscord Webhook Senderへ
まずは送信先のWebhook URLを入力してください。
>>> // input webhook url

送信先: 
次に送信メッセージを入力してください。
>>> // input your message

送信先: url
メッセージ: messageで送信しました。
```

## 継続モード

```python
sendMode = True
```

main.pyのsendModeをTrueにすると継続して送信できます。

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A81VPXD)