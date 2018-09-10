$(function () {
    $(".add").click(function () {
        var $current_btn = $(this);
        var c_id = $(this).parents("li").attr("c_id");
        $.ajax({
            url:"/axf/api/v1/cart_item",
            data:{
                'c_id': c_id,
                'operate_type': 'add'
            },
            method:"post",
            success:function (res) {
                console.log(res);
                if (res.code == 1) {
                    var current_num = res.data.current_num;
                    var money = res.data.money;
                    //修改显示的数量
                    $current_btn.prev().html(current_num);
                    // 修改 总价
                    $("#money_id").html(money);
                } else if (res.code == 3){
                    window.open(url=res.data, target="_self")
                } else {
                    alert(res.msg);
                }


            }
        });
    });
    $(".sub").click(function () {
        var $current_btn = $(this);
        var c_id = $(this).parents("li").attr("c_id");
        $.ajax({
            url:"/axf/api/v1/cart_item",
            data:{
                'c_id': c_id,
                'operate_type': 'sub'
            },
            method:"post",
            success:function (res) {
                console.log(res);
                if (res.code == 1) {
                    var current_num = res.data.current_num;
                    var money = res.data.money;
                    if (current_num <= 0 ){
                        //如果减到0了 删除对应li
                        $current_btn.parents("li").remove();
                    } else {
                        //修改显示的数量
                        $current_btn.next().html(current_num);
                    }

                    // 修改 总价
                    $("#money_id").html(money);
                } else if (res.code == 3){
                    window.open(url=res.data, target="_self")
                } else {
                    alert(res.msg);
                }


            }
        });
    });

    // 给选中按钮添加点击事件
    $('.confirm').click(function () {
        var  c_id = $(this).parent('li').attr('c_id');
        $.ajax({
            url: '/axf/api/v1/cart_item_status',
            data:{
                'c_id':c_id
            },
            method:'put',
            success:function (res) {
                console.log(res);
            }
        })
    })
})