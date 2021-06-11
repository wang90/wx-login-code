# 微信登录调用汇总

-------
## 扫码登录
#### [扫码从微信公共号登录pc](./扫码从微信公共号登录pc)
- 打开微信公共号 （https://mp.weixin.qq.com/）
- 获取appid 与 appsecret
- 在公共号内设置白名单
- 获取access_token
- 获取wx qrcode
- 公共号内回调
[官方文档](https://developers.weixin.qq.com/doc/offiaccount/Account_Management/Generating_a_Parametric_QR_Code.html)

#### [扫码直接登录](./扫码直接登录)
- 打开开放平台网站(https://open.weixin.qq.com)
- 获取appid和appsecret
- 授权回调域配置
- 本地请求code
- 通过 code 获取appid和appsecret
- 通过 access_token 获取用户基本数据。
[官方文档](https://developers.weixin.qq.com/doc/oplatform/Website_App/WeChat_Login/Wechat_Login.html)

-------

## 进入登录
#### [微信直接H5登录](./微信直接H5登录)

- 打开微信公共号（https://mp.weixin.qq.com/）
- 获取appid 与 appsecret
- 在公共号内设置白名单
- 配置网页授权域名
- 调用https://open.weixin.qq.com/connect/oauth2/authorize?appid=${ appId }&redirect_uri=${ redirectUri }&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect
- 获取回掉的code
- 获取access_token,openid
- 获取用户信息
[官方文档](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html)
