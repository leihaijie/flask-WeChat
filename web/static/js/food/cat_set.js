;
var cat_edit_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $(".wrap_cat_set .save").click(function () {
            var btn_target = $(this);
            if(btn_target.hasClass("disabled")){
                common_ops.alert("正在处理!!请不要重复提交~");
                return;
            }
            var catname_target = $(".wrap_cat_set input[name=name]");
            var catname = catname_target.val();

            var catweight_target = $(".wrap_cat_set input[name=weight]");
            var catweight = catweight_target.val();

            if(!catname){
                common_ops.tip("请输入分类名称~",catname_target);
                return false;
            }
            if(!catweight){
                common_ops.tip("请输入分类权重~",catweight_target);
                return false;
            }

            btn_target.addClass("disabled");
            var data = {
                'name':catname,
                'weight':catweight,
                'id':$(".wrap_cat_set input[name=id]").val()
            };
            $.ajax({
                url:common_ops.buildUrl("/food/cat-set"),
                type:"POST",
                data:data,
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callBack = null;
                    if(res.code == 200){
                        callBack = function () {
                            window.location.href = common_ops.buildUrl("/food/cat");
                        }
                    }
                    common_ops.alert(res.msg,callBack);
                }
            });
        });
    }
};

$(document).ready(function () {
    cat_edit_ops.init();
})