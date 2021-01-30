// 微信公共号后台回答服务

app.use(
    "/wechat",
    wechat(nonce, function(req, res, next) {
        var message = req.weixin;
        if (message.MsgType === "event") {
            if (message.Event === "subscribe" || message.Event === "SCAN") {
                // 请求自己服务器api,
                // 携带参数 
                // 「  message.Event,
                //     message.FromUserName,  // openid
                //     message.Ticket, 
                //     message.EventKey 」
            }
        }
    })
)