
export function wxapp_login() {
    const appid = 'xxxx';
    const redirectUri = encodeURIComponent("http://") // url 要复合授权回调域
    const url = `https://open.weixin.qq.com/connect/qrconnect?appid=${ appid }&redirect_uri=${ redirectUri }&response_type=code&scope=SCOPE&state=STATE#wechat_redirect`;
    window.location.href  = url;
}

// 或
// 引入 http://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js
// 通过调用二维码
var obj = new WxLogin({
    self_redirect:true,
    id:"login_container", 
    appid: "", 
    scope: "", 
    redirect_uri: "",
     state: "",
    style: "",
    href: ""
});