# pc 微信二维码登录 关注公共号
appid = =""
appsecret = ""

async def getAccessToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+ appid +'&secret=' + appsecret
    async with aiohttp.ClientSession() as session:
        async with  session.get(url) as resp:
            s = await resp.text()
            try:
                req = json.loads(s)
                return req
            except:
                return None

# 网页二维码
async def getWxCode(token: str ):
    get_img_url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=" + token
    payload = {
        "expire_seconds": 604800, 
        "action_name": "QR_SCENE", 
        "action_info": {
            "scene": {
                "scene_id": '123'
            }
        }
    } 
    payload = json.dumps(payload)
    async with aiohttp.ClientSession() as session:
        async with  session.post(get_img_url, data = payload) as resp:
            s = await resp.text()
            try:
                req = json.loads(s)
                return req
            except:
                return None


# 回调用获取用户信息
async def getWxUserInfo( token: str, openid: str  ):
    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=" + token + "&openid=" + openid + "&lang=zh_CN"
    async with aiohttp.ClientSession() as session:
        async with  session.get( url ) as resp:
            s = await resp.text()
            try:
                req = json.loads(s)
                return req
            except:
                return None