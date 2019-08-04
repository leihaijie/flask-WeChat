;
var user_resetpwd_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $("#save").click(function () {
            var btn_target = $(this);
            if(btn_target.hasClass("disabled")){
                common_ops.alert("正在处理!!请不要重复提交~");
                return;
            }
            var oldpwd_target = $("#old_password");
            var oldpwd = oldpwd_target.val();

            var newpwd_target = $("#new_password");
            var newpwd = newpwd_target.val();

            if(!oldpwd || oldpwd.length<2){
                common_ops.tip("请输入原始密码~",oldpwd_target);
                return false;
            }
            if(!newpwd || newpwd.length<6){
                common_ops.tip("请输入不小于6位的新密码~",newpwd_target);
                return false;
            }
            btn_target.addClass("disabled");
            var data = {
                'old_password':oldpwd,
                'new_password':newpwd
            }
            $.ajax({
                url:common_ops.buildUrl("/user/reset-pwd"),
                type:"POST",
                data:data,
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callBack = null;
                    if(res.code == 200){
                        callBack = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert(res.msg,callBack);
                }
            });
        });
    }
};

$(document).ready(function () {
    user_resetpwd_ops.init();
})