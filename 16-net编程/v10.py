from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello wold",  "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字符
header_from = Header("从图灵学院邮箱发出去的<TuLingXueYuan@qq.cn>", "utf-8")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("去王晓静的地方<wangxiaojing@sina.com>", 'utf-8')
msg['To'] = header_to

header_sub = Header("这是图灵学院的主题", 'utf-8')
msg['Subject'] = header_sub



# 发送email地址，此处地址直接使用我的qq有偶像，密码一般需要临时输入，此处偷懒
from_addr = "290241262@qq.com"

# 此处密码是经过申请设置后的授权码，不是不是不是你的qq邮箱密码
from_pwd = "nkxkncllwbntbgeh"
# 收件人信息
# 此处使用qq邮箱，我给自己发送
to_addr = "cnishop@126.com"



smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)