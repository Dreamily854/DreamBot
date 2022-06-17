function UI_Login() {

    $.ajax({
        url: "/login.html",
        async:false,
        success: function (result) {
            $("#ui_body").html(result);
            mdui.mutation();
            
            //事件监听要放进回调函数中
            console.log($("#ui_login_button_login").click(
                function () {
                // code ...
                console.log("login_btn");
            }));
        }
    });

}
function HeadToolBar() {

    $.ajax({
        url: "/headToolBar.html",
        async:false,
        success: function (result) {
            $("#ui_body").html(result);
            mdui.mutation();
            
        }
    });

}
function UI_Main() {

    $.ajax({
        url: "/main.html",
        async:false,
        success: function (result) {
            $("#ui_main_page").html(result);
            mdui.mutation();
            
        }
    });

}
// $("#ui_login_input_username").val();
// $("#ui_login_input_password").val();




