// DreamBot WEBUI 
// Ver 1.0
var $$ = mdui.$;

function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return encodeURI(r[2]); return null; //返回参数值
}



/**
 *     ____                            ____        __ 
 *    / __ \________  ____ _____ ___  / __ )____  / /_
 *   / / / / ___/ _ \/ __ `/ __ `__ \/ __  / __ \/ __/
 *  / /_/ / /  /  __/ /_/ / / / / / / /_/ / /_/ / /_  
 * /_____/_/   \___/\__,_/_/ /_/ /_/_____/\____/\__/  
 * DreamBot Control API  
 * 
 * API :
 * 1.Get Rules List (/dreambot/getruleslist) (POST)
 * [token = ??]
 * 
 * 2.Add rule (/dreambot/addrule) (POST)
 * [token = ??,ruledata = {json}]
 * 
 
*/