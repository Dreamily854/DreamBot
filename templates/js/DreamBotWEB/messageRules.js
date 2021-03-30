

var el = document.getElementById('items');
var sortable = Sortable.create(el, {
    animation: 200,
    forceFallback: false,
    onUpdate: function (/**Event*/evt) {
        // 与onEnd相同的属性

        console.info("old {" + evt.oldIndex + "} -> new {" + evt.newIndex + "}")
        mdui.snackbar({
            message: '更新成功',
            timeout: 1250,
        });
    },

});
$("#items").append(test);
function addruleui(data){
    
}
var test = "<div class='list-group-item mdui-panel-item mdui-p-r-1 mdui-p-l-1 mdui-m-b-2 mdui-m-t-2 fade-in-right'><div class='mdui-panel-item-header'><div class='mdui-panel-item-title'>#2 DreamBotManager</div><div class='mdui-panel-item-summary mdui-text-color-red'>包含错误</div><i class='mdui-panel-item-arrow mdui-icon material-icons'>keyboard_arrow_down</i></div><div class='mdui-panel-item-body'><div class='mdui-typo'><p>按前缀 <kbd>/</kbd> 匹配消息</p><p>模式: 插件直通处理模式</p><p>插件: com.dreambot.manager</p><p>生效范围: 全部私聊</p><p>停止处理其它规则</p></div><div class='mdui-panel-item-actions'><button class='mdui-btn mdui-ripple'>EDIT</button></div></div></div>"

