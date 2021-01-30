
export function wxapp_login() {
    const appid = 'xxxx';
    const redirectUri = encodeURIComponent("http://") // url 要与配置网页授权域名相同
    const url = `https://open.weixin.qq.com/connect/oauth2/authorize?appid=${ appid }&redirect_uri=${ redirectUri }&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect`;
    window.location.href  = url;
}