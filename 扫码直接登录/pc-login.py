
appid = ""
appsecret = ""
# pc code -> access_token
async def fromCodeGetAccessToken( code : str ):
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=APPID&secret=SECRET&code=CODE&grant_type=authorization_code"
    async with aiohttp.ClientSession() as session:
        async with  session.get(url) as resp:
            s = await resp.text()
            try:
                req = json.loads(s)
                return req
            except:
                return None


# 获取用户信息
async def getWxUserInfo( token: str, openid: str  ):
    url = " https://api.weixin.qq.com/sns/userinfo?access_token=" + token +  "&openid=" + openid +  "&lang=zh_CN"
    async with aiohttp.ClientSession() as session:
        async with  session.get( url ) as resp:
            s = await resp.text()
            try:
                req = json.loads(s)
                return req
            except:
                return None
