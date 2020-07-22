/*
*
* 工具类
*
*/

var host = "http://127.0.0.1:10010";  //域名

//http请求方法封装（ajax）
function http(url, data, method, success, fail) {
    var data = method == 'GET' ? data : JSON.stringify(data);
    $.ajax({
        type: method,
        contentType: "application/json; charset=utf-8",
        data: data,  //请求参数
        url: url,
        dataType: 'json',
        success: success,  //成功回调
        fail: fail  //失败回调
    });
}
