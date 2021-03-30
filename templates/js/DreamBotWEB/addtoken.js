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


function BindRuleChange() {
    var BindEvent_INFO = Get_BindEvent_INFO()
    ChangeBind_Event_info(BindEvent_INFO);
    //console.log(BindEvent_INFO);


    
}



