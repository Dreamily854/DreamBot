var $$ = mdui.$;
function Get_BindEvent_INFO() {

    var Get_BindEvent_INFO_data = {
        FriendPrivateMessageEvent: $('#CheckBox_Bind_FriendPrivateMessageEvent').is(':checked'),
        GroupPrivateMessageEvent: $('#CheckBox_Bind_GroupPrivateMessageEvent').is(':checked'),
        OtherPrivateMessageEvent: $('#CheckBox_Bind_OtherPrivateMessageEvent').is(':checked'),
        NormalGroupMessageEvent: $('#CheckBox_Bind_NormalGroupMessageEvent').is(':checked'),
        AnonymousGroupMessageEvent: $('#CheckBox_Bind_AnonymousGroupMessageEvent').is(':checked'),
        NoticeGroupMessageEvent: $('#CheckBox_Bind_NoticeGroupMessageEvent').is(':checked'),

        FriendRequestEvent: $('#CheckBox_Bind_FriendRequestEvent').is(':checked'),
        AddGroupRequestEvent: $('#CheckBox_Bind_AddGroupRequestEvent').is(':checked'),
        InviteGroupRequestEvent: $('#CheckBox_Bind_InviteGroupRequestEvent').is(':checked'),

        GroupUploadNoticeEvent: $('#CheckBox_Bind_GroupUploadNoticeEvent').is(':checked'),
        GroupAdminNoticeEvent: $('#CheckBox_Bind_GroupAdminNoticeEvent').is(':checked'),
        GroupDecreaseNoticeEvent: $('#CheckBox_Bind_GroupDecreaseNoticeEvent').is(':checked'),
        GroupIncreaseNoticeEvent: $('#CheckBox_Bind_GroupIncreaseNoticeEvent').is(':checked'),
        GroupBanNoticeEvent: $('#CheckBox_Bind_GroupBanNoticeEvent').is(':checked'),
        FriendAddNoticeEvent: $('#CheckBox_Bind_FriendAddNoticeEvent').is(':checked'),
        FriendRecallNoticeEvent: $('#CheckBox_Bind_FriendRecallNoticeEvent').is(':checked'),
        GroupRecallNoticeEvent: $('#CheckBox_Bind_GroupRecallNoticeEvent').is(':checked'),
        PokeNotifyNoticeEvent: $('#CheckBox_Bind_PokeNotifyNoticeEvent').is(':checked'),
        LuckyKingNotifyNoticeEvent: $('#CheckBox_Bind_LuckyKingNotifyNoticeEvent').is(':checked'),
        HonorNotifyNoticeEvent: $('#CheckBox_Bind_HonorNotifyNoticeEvent').is(':checked'),

        LifeCycleMetaEvent: $('#CheckBox_Bind_LifeCycleMetaEvent').is(':checked'),
        HeartBeatMetaEvent: $('#CheckBox_Bind_HeartBeatMetaEvent').is(':checked'),
    };
    return Get_BindEvent_INFO_data;
}
function ChangeBind_Event_info(data) {
    var Count_Message = 0;
    var Count_Notice = 0;
    var Count_Request = 0;
    var Count_Meta = 0;
    if (data.FriendPrivateMessageEvent == true) { Count_Message = Count_Message + 1 }
    if (data.GroupPrivateMessageEvent == true) { Count_Message = Count_Message + 1 }
    if (data.OtherPrivateMessageEvent == true) { Count_Message = Count_Message + 1 }
    if (data.NormalGroupMessageEvent == true) { Count_Message = Count_Message + 1 }
    if (data.AnonymousGroupMessageEvent == true) { Count_Message = Count_Message + 1 }
    if (data.NoticeGroupMessageEvent == true) { Count_Message = Count_Message + 1 }

    if (data.GroupUploadNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.GroupAdminNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.GroupDecreaseNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.GroupIncreaseNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.GroupBanNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.FriendAddNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.FriendRecallNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.GroupRecallNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.PokeNotifyNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.LuckyKingNotifyNoticeEvent == true) { Count_Notice = Count_Notice + 1 }
    if (data.HonorNotifyNoticeEvent == true) { Count_Notice = Count_Notice + 1 }

    if (data.FriendRequestEvent == true) { Count_Request = Count_Request + 1 }
    if (data.AddGroupRequestEvent == true) { Count_Request = Count_Request + 1 }
    if (data.InviteGroupRequestEvent == true) { Count_Request = Count_Request + 1 }

    if (data.LifeCycleMetaEvent == true) { Count_Meta = Count_Meta + 1 }
    if (data.HeartBeatMetaEvent == true) { Count_Meta = Count_Meta + 1 }

    $('#Bind_Event_info-message').text(Count_Message + "/6")
    $('#Bind_Event_info-notice').text(Count_Notice + "/11")
    $('#Bind_Event_info-request').text(Count_Request + "/3")
    $('#Bind_Event_info-meta').text(Count_Meta + "/2 (暂不提供支持)")

}
function quick_check_all() {
    $('#CheckBox_Bind_FriendPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_OtherPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_NormalGroupMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_AnonymousGroupMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_NoticeGroupMessageEvent').prop("checked", true)

    $('#CheckBox_Bind_FriendRequestEvent').prop("checked", true)
    $('#CheckBox_Bind_AddGroupRequestEvent').prop("checked", true)
    $('#CheckBox_Bind_InviteGroupRequestEvent').prop("checked", true)

    $('#CheckBox_Bind_GroupUploadNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupAdminNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupDecreaseNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupIncreaseNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupBanNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_FriendAddNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_FriendRecallNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupRecallNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_PokeNotifyNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_LuckyKingNotifyNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_HonorNotifyNoticeEvent').prop("checked", true)

    // $('#CheckBox_Bind_LifeCycleMetaEvent').prop("checked", true)
    // $('#CheckBox_Bind_HeartBeatMetaEvent').prop("checked", true)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}
function quick_check_message_all() {
    $('#CheckBox_Bind_FriendPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_OtherPrivateMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_NormalGroupMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_AnonymousGroupMessageEvent').prop("checked", true)
    $('#CheckBox_Bind_NoticeGroupMessageEvent').prop("checked", true)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}
function quick_check_meta_all() {
    $('#CheckBox_Bind_LifeCycleMetaEvent').prop("checked", true)
    $('#CheckBox_Bind_HeartBeatMetaEvent').prop("checked", true)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}
function quick_check_notice_all() {
    $('#CheckBox_Bind_GroupUploadNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupAdminNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupDecreaseNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupIncreaseNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupBanNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_FriendAddNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_FriendRecallNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_GroupRecallNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_PokeNotifyNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_LuckyKingNotifyNoticeEvent').prop("checked", true)
    $('#CheckBox_Bind_HonorNotifyNoticeEvent').prop("checked", true)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}
function quick_check_request_all() {
    $('#CheckBox_Bind_FriendRequestEvent').prop("checked", true)
    $('#CheckBox_Bind_AddGroupRequestEvent').prop("checked", true)
    $('#CheckBox_Bind_InviteGroupRequestEvent').prop("checked", true)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}
function quick_uncheck_all() {
    $('#CheckBox_Bind_FriendPrivateMessageEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupPrivateMessageEvent').prop("checked", false)
    $('#CheckBox_Bind_OtherPrivateMessageEvent').prop("checked", false)
    $('#CheckBox_Bind_NormalGroupMessageEvent').prop("checked", false)
    $('#CheckBox_Bind_AnonymousGroupMessageEvent').prop("checked", false)
    $('#CheckBox_Bind_NoticeGroupMessageEvent').prop("checked", false)

    $('#CheckBox_Bind_FriendRequestEvent').prop("checked", false)
    $('#CheckBox_Bind_AddGroupRequestEvent').prop("checked", false)
    $('#CheckBox_Bind_InviteGroupRequestEvent').prop("checked", false)

    $('#CheckBox_Bind_GroupUploadNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupAdminNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupDecreaseNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupIncreaseNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupBanNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_FriendAddNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_FriendRecallNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_GroupRecallNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_PokeNotifyNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_LuckyKingNotifyNoticeEvent').prop("checked", false)
    $('#CheckBox_Bind_HonorNotifyNoticeEvent').prop("checked", false)

    // $('#CheckBox_Bind_LifeCycleMetaEvent').prop("checked", false)
    // $('#CheckBox_Bind_HeartBeatMetaEvent').prop("checked", false)
    ChangeBind_Event_info(Get_BindEvent_INFO());
}

// 
/**
 * CheckBox_Bind_FriendPrivateMessageEvent
 * CheckBox_Bind_GroupPrivateMessageEvent
 * CheckBox_Bind_OtherPrivateMessageEvent
 * CheckBox_Bind_NormalGroupMessageEvent
 * CheckBox_Bind_AnonymousGroupMessageEvent
 * CheckBox_Bind_NoticeGroupMessageEvent
 * 
 * CheckBox_Bind_FriendRequestEvent
 * CheckBox_Bind_AddGroupRequestEvent
 * CheckBox_Bind_InviteGroupRequestEvent
 * 
 * CheckBox_Bind_GroupUploadNoticeEvent
 * CheckBox_Bind_GroupAdminNoticeEvent
 * CheckBox_Bind_GroupDecreaseNoticeEvent
 * CheckBox_Bind_GroupIncreaseNoticeEvent
 * CheckBox_Bind_GroupBanNoticeEvent
 * CheckBox_Bind_FriendAddNoticeEvent
 * CheckBox_Bind_FriendRecallNoticeEvent
 * CheckBox_Bind_GroupRecallNoticeEvent
 * CheckBox_Bind_PokeNotifyNoticeEvent
 * CheckBox_Bind_LuckyKingNotifyNoticeEvent
 * CheckBox_Bind_HonorNotifyNoticeEvent
 * 
 * CheckBox_Bind_LifeCycleMetaEvent
 * CheckBox_Bind_HeartBeatMetaEvent
 */
var DirectModeForm =
    "<div class='fade-in-left'>" +
    "   <div class='mdui-text-center mdui-card-primary-title mdui-m-t-1 mdui-m-b-1'>直通模式设置</div>" +
    "   <div class='mdui-container'>" +
    "       <p>选择一个插件以生效</p>" +
    "       <select class='mdui-select mdui-p-t-2' id='Direct_Plugin_Select' mdui-select>" +
    "       </select>" +
    "   </div>" +
    "</div>";

var CommandModeForm =
    "<div class='fade-in-left'>" +
    "    <div class='mdui-text-center mdui-card-primary-title mdui-m-t-1 mdui-m-b-1'>命令模式设置</div>" +
    "    <div class='mdui-container'>" +
    "        <form class='mdui-m-t-1'>" +
    "            <ul class='mdui-list'>" +
    "                <li class='mdui-list-item mdui-ripple'>" +
    "                    <div class='mdui-list-item-content'>匹配前缀</div>" +
    "                    <label class='mdui-radio'>" +
    "                        <input type='radio' value='prefix' name='group2' />" +
    "                        <i class='mdui-radio-icon'></i>" +
    "                    </label>" +
    "                </li>" +
    "                <li class='mdui-list-item mdui-ripple'>" +
    "                    <div class='mdui-list-item-content'>匹配后缀</div>" +
    "                    <label class='mdui-radio'>" +
    "                        <input type='radio' value='postfix' name='group2' />" +
    "                        <i class='mdui-radio-icon'></i>" +
    "                    </label>" +
    "                </li>" +
    "            </ul>" +
    "            <div class='mdui-textfield mdui-textfield-floating-label'>" +
    "                <label class='mdui-textfield-label'>前缀/后缀</label>" +
    "                <input class='mdui-textfield-input' type='text' />" +
    "            </div>" +
    "        </form>" +
    "    </div>" +
    "</div>";

var ProxyModeForm =
    "<div class='fade-in-left'>" +
    "    <div class='mdui-text-center mdui-card-primary-title mdui-m-t-1 mdui-m-b-1'>转发模式设置</div>" +
    "    <div class='mdui-container'>" +
    "        <p>选择服务器:</p>" +
    "        <select class='mdui-select mdui-p-t-2' id='Proxy_server_select' mdui-select>" +
    "            <option>None(添加一个?)</option>" +
    "        </select>" +
    "    </div>" +
    "</div>";

function BindRuleChange() {
    var BindEvent_INFO = Get_BindEvent_INFO()
    ChangeBind_Event_info(BindEvent_INFO);
    //console.log(BindEvent_INFO);


    if (
        (
            (BindEvent_INFO.FriendPrivateMessageEvent == true) ||
            (BindEvent_INFO.GroupPrivateMessageEvent == true) ||
            (BindEvent_INFO.OtherPrivateMessageEvent == true) ||
            (BindEvent_INFO.NormalGroupMessageEvent == true) ||
            (BindEvent_INFO.AnonymousGroupMessageEvent == true)
        ) &&
        (
            (BindEvent_INFO.NoticeGroupMessageEvent == false) &&
            (BindEvent_INFO.GroupUploadNoticeEvent == false) &&
            (BindEvent_INFO.GroupAdminNoticeEvent == false) &&
            (BindEvent_INFO.GroupDecreaseNoticeEvent == false) &&
            (BindEvent_INFO.GroupIncreaseNoticeEvent == false) &&
            (BindEvent_INFO.GroupBanNoticeEvent == false) &&
            (BindEvent_INFO.FriendAddNoticeEvent == false) &&
            (BindEvent_INFO.FriendRecallNoticeEvent == false) &&
            (BindEvent_INFO.GroupRecallNoticeEvent == false) &&
            (BindEvent_INFO.PokeNotifyNoticeEvent == false) &&
            (BindEvent_INFO.LuckyKingNotifyNoticeEvent == false) &&
            (BindEvent_INFO.HonorNotifyNoticeEvent == false) &&
            (BindEvent_INFO.FriendRequestEvent == false) &&
            (BindEvent_INFO.AddGroupRequestEvent == false) &&
            (BindEvent_INFO.InviteGroupRequestEvent == false) &&
            (BindEvent_INFO.LifeCycleMetaEvent == false) &&
            (BindEvent_INFO.HeartBeatMetaEvent == false)
        )

    ) {
        $('#Message_HandleCommand_INFO').text("命令模式")
        $('#Message_HandleCommand').prop("disabled", false)

    }
    else {
        $('#Message_HandleCommand_INFO').text("命令模式(当前无法使用)")
        $('#Message_HandleCommand').prop("disabled", true)
        $('#Message_HandleCommand').prop("checked", false)
    }
}
function MessageUpdateMode() {
    var Mode = $('input[name="message_processmode"]:checked').val()
    console.log(Mode)
    if (Mode == "Proxy") {
        $('#MessageModeAdv').empty()
        $('#MessageModeAdv').append(ProxyModeForm)
    } 
    else if(Mode == "Command") {
        $('#MessageModeAdv').empty()
        $('#MessageModeAdv').append(CommandModeForm)
    }
    else if(Mode == "Direct") {
        $('#MessageModeAdv').empty()
        $('#MessageModeAdv').append(DirectModeForm)
    }

}


