var LoginProcessDialog = new mdui.Dialog('#Login_Process_Dialog');


$$('#dbot_login-button').on('click', function (e) {
    LoginProcessDialog.open();
    $("#LoginProcessDialogStat").html("正在连接服务器...");
    $("#LoginProcessDialogStat").html("正在登录....");
    $("#LoginProcessDialogStat").html("登录成功! 欢迎Dream");
    LoginProcessDialog.close();

});

function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return encodeURI(r[2]); return null; //返回参数值
}

if (getUrlParam("errcode") == "1") {
    mdui.dialog({
        title: '认证失败',
        content: '您没有登录！',
        buttons: [
            {
                text: '确定'
            }
        ]
    });
}
else if (getUrlParam("errcode") == "2") {
    mdui.dialog({
        title: '认证失败',
        content: '登录失效！',
        buttons: [
            {
                text: '确定'
            }
        ]
    });
}
