;
var account_index_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        var that = this; // 更换作用域
        //查询账户操作
        $(".wrap_search .search").click(function () {
            $(".wrap_search").submit();
        });
        $(".remove").click(function () {
            that.ops("remove",$(this).attr('data')); // 获取data得值
        });

        $(".recover").click(function () {
            that.ops("recover",$(this).attr('data'));
        });
    },
    ops:function (act,id) {
        var callback = {
            'ok':function () {
                $.ajax({
                url:common_ops.buildUrl("/account/ops"),
                type:'POST',
                data:{'act':act,'id':id},
                dataType:'json',
                success:function (res) {
                    var callBack = null;
                    if(res.code == 200){
                        callBack = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert(res.msg,callBack);
                }
            });
            },
            'cancel':null
        };
        common_ops.confirm((act=='remove'?'确定删除吗?':'确定恢复吗?'),callback);
    }
};

$(document).ready(function () {
    account_index_ops.init();
})